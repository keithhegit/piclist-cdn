#!/usr/bin/env python3
"""
Notion Sync - 子页面版
Markdown报告同步到Notion（主页面+子页面）

用法:
    python3 notion_sync_subpages.py <文件>
    python3 notion_sync_subpages.py /path/to/report.md
"""

import os, re, requests
from datetime import datetime

# ============= 配置 =============
NOTION_KEY = os.environ.get("NOTION_KEY", "[REDACTED][REDACTED]026236eWN3zCq0z3WXMfnqvioA8wYyAXLOvhc3Hs")
DATABASE_ID = os.environ.get("NOTION_DATABASE_ID", "[REDACTED]b6a57f8348a9d0014c0fd0f7c4")
GITHUB_OWNER = os.environ.get("GITHUB_OWNER", "keithhegit")
GITHUB_REPO = os.environ.get("GITHUB_REPO", "piclist-cdn")

HEADERS = {
    "Authorization": f"Bearer {NOTION_KEY}",
    "Notion-Version": "2025-09-03",
    "Content-Type": "application/json"
}

# ============= 工具函数 =============

def normalize_title(title):
    """标准化标题"""
    return title.replace('.md', '').replace('.MD', '').strip()

def check_exists(filename):
    """检查是否已存在"""
    url = "https://api.notion.com/v1/search"
    data = {
        "query": normalize_title(filename),
        "filter": {"property": "object", "value": "page"},
        "page_size": 10
    }
    
    r = requests.post(url, headers=HEADERS, json=data)
    if r.status_code == 200:
        for item in r.json().get('results', []):
            t = item.get('properties', {}).get('Recurso', {}).get('title', [])
            if t:
                if normalize_title(t[0].get('plain_text', '')) == normalize_title(filename):
                    return True, item.get('id')
    return False, None

def markdown_to_blocks(text):
    """Markdown转Notion blocks"""
    lines = text.strip().split('\n')
    blocks = []
    
    for line in lines:
        s = line.strip()
        if not s: continue
        
        # 标题
        m = re.match(r'^(#{1,6})\s+(.+)$', s)
        if m:
            lvl = min(len(m.group(1)), 3)
            blocks.append({
                "object": "block",
                "type": f"heading_{lvl}",
                f"heading_{lvl}": {"rich_text": [{"type": "text", "text": {"content": m.group(2).strip()}}]}
            })
            continue
        
        # 无序列表
        if s.startswith('- '):
            blocks.append({
                "object": "block", "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": s[2:]}}]}
            })
            continue
        
        # 有序列表
        m = re.match(r'^\d+\.\s+(.+)$', s)
        if m:
            blocks.append({
                "object": "block", "type": "numbered_list_item",
                "numbered_list_item": {"rich_text": [{"type": "text", "text": {"content": m.group(1)}}]}
            })
            continue
        
        # 段落
        blocks.append({
            "object": "block", "type": "paragraph",
            "paragraph": {"rich_text": [{"type": "text", "text": {"content": s}}]}
        })
    
    return blocks

def create_page(title, content_blocks, parent_id=None, db_id=None):
    """创建Notion页面"""
    parent = {"page_id": parent_id} if parent_id else {"database_id": db_id}
    
    data = {
        "parent": parent,
        "properties": {"title": [{"text": {"content": title}}]},
        "children": content_blocks[:85]  # 限制85个blocks
    }
    
    r = requests.post("https://api.notion.com/v1/pages", headers=HEADERS, json=data)
    return r.status_code == 200, r.json()

def cdn_url(filename):
    """生成CDN URL"""
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"https://cdn.jsdelivr.net/gh/{GITHUB_OWNER}/{GITHUB_REPO}/images/{ts}_{filename}"

# ============= 主函数 =============

def sync_file(filepath):
    """同步单个文件"""
    filename = os.path.basename(filepath)
    exists, page_id = check_exists(filename)
    
    if exists:
        print(f"⏭️ 跳过: {filename} (已存在)")
        return False
    
    print(f"📤 处理: {filename}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 解析章节
    chapters = re.split(r'\n## ', content)
    
    # 主页面
    main_blocks = [{
        "object": "block", "type": "paragraph",
        "paragraph": {"rich_text": [{"type": "text", "text": {"content": f"📑 共{len(chapters)}章节"}}]}
    }]
    
    ok, result = create_page(f"🦞 {filename}", main_blocks, db_id=DATABASE_ID)
    
    if not ok:
        print(f"  ❌ 主页面失败: {result.get('message', 'Unknown')}")
        return False
    
    main_id = result.get('id')
    print(f"  ✅ 主页面创建")
    
    # 子页面 (最多4个)
    names = ["SCQA与概述", "公司概况", "核心产品", "市场定位", 
             "客户案例", "技术架构", "商业模式", "竞争分析",
             "行业趋势", "结论建议", "附录"]
    
    max_subs = min(4, len(chapters))
    per_section = (len(chapters) - 1) // max_subs + 1
    
    for i in range(max_subs):
        start = i * per_section + 1
        end = min((i + 1) * per_section + 1, len(chapters))
        
        section_content = "## " + "## ".join(chapters[start:end])
        blocks = markdown_to_blocks(section_content)
        
        sub_name = names[i] if i < len(names) else f"第{start}-{end}章"
        ok2, _ = create_page(f"第{start}-{end}章: {sub_name}", blocks, parent_id=main_id)
        
        if ok2:
            print(f"    ✅ 子页面 {i+1}: {sub_name} ({len(blocks)} blocks)")
        else:
            print(f"    ❌ 子页面 {i+1} 失败")
    
    return True

def main():
    if len(sys.argv) < 2:
        print("""
📤 Notion Sync - 子页面版

用法:
    python3 notion_sync_subpages.py <文件>
    python3 notion_sync_subpages.py report.md

说明:
    - 创建主页面 + 最多4个子页面
    - 每个子页面最多85个blocks
    - 自动跳过已存在的文件
""")
        sys.exit(0)
    
    filepath = sys.argv[1]
    
    if not os.path.exists(filepath):
        print(f"❌ 文件不存在: {filepath}")
        sys.exit(1)
    
    print(f"\n{'='*50}")
    print(f"📤 同步到 Notion")
    print(f"{'='*50}\n")
    
    sync_file(filepath)
    
    print(f"\n{'='*50}\n")

if __name__ == "__main__":
    main()
