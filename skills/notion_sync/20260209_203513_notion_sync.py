#!/usr/bin/env python3
"""
Notion Sync - Simple Version
文件同步到Notion + GitHub CDN

用法:
    python3 notion_sync.py <文件> [--notion] [--category X]
"""

import os, sys, base64, requests, json
from datetime import datetime

# ============= 配置 =============
NOTION_KEY = os.environ.get("NOTION_KEY", "[REDACTED][REDACTED]026236eWN3zCq0z3WXMfnqvioA8wYyAXLOvhc3Hs")
NOTION_DB_ID = os.environ.get("NOTION_DATABASE_ID", "[REDACTED]b6a57f8348a9d0014c0fd0f7c4")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "[REDACTED]0086BjmP8EvgAma0veh1FLwWv3xLyd3COjOg")
GITHUB_OWNER = os.environ.get("GITHUB_OWNER", "keithhegit")
GITHUB_REPO = os.environ.get("GITHUB_REPO", "piclist-cdn")

HEADERS = {
    "Authorization": f"Bearer {NOTION_KEY}",
    "Notion-Version": "2025-09-03",
    "Content-Type": "application/json"
}

# ============= 核心函数 =============

def upload_github(path, folder="images"):
    """上传到GitHub，返回CDN URL"""
    name = os.path.basename(path)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    github_path = f"{folder}/{ts}_{name}"
    
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{github_path}"
    payload = {
        "message": f"Upload {name}",
        "content": base64.b64encode(open(path, "rb").read()).decode(),
        "branch": "master"
    }
    
    r = requests.put(url, headers={"Authorization": f"token {GITHUB_TOKEN}"}, json=payload)
    if r.status_code == 201:
        cdn = f"https://cdn.jsdelivr.net/gh/{GITHUB_OWNER}/{GITHUB_REPO}/{github_path}"
        return {"success": True, "cdn": cdn}
    return {"success": False, "error": r.text}

def sync_notion(path, category="Research"):
    """同步到Notion (单文件版)"""
    # 1. 上传GitHub
    result = upload_github(path, category)
    if not result["success"]:
        return result
    
    # 2. 获取文件信息
    name = os.path.basename(path)
    ext = path.split('.')[-1].upper() if '.' in path else "File"
    
    # 3. 创建Notion页面
    data = {
        "parent": {"database_id": NOTION_DB_ID},
        "properties": {
            "Recurso": {"title": [{"text": {"content": name}}]},
            "URL": {"url": result["cdn"]},
            "类型": {"multi_select": [{"name": ext}]},
            "标签": {"multi_select": [{"name": "Auto-Sync"}]}
        }
    }
    
    r = requests.post("https://api.notion.com/v1/pages", headers=HEADERS, json=data)
    
    if r.status_code == 200:
        return {"success": True, "notion": r.json().get("url"), **result}
    return {"success": False, "error": r.text, **result}

def check_exists(title):
    """检查页面是否已存在"""
    url = "https://api.notion.com/v1/search"
    data = {
        "query": title.replace('.md', '').strip(),
        "filter": {"property": "object", "value": "page"},
        "page_size": 5
    }
    
    r = requests.post(url, headers=HEADERS, json=data)
    if r.status_code == 200:
        for item in r.json().get('results', []):
            t = item.get('properties', {}).get('Recurso', {}).get('title', [])
            if t and t[0].get('plain_text', '').replace('.md', '').strip() == title.replace('.md', '').strip():
                return True, item.get('id')
    return False, None

# ============= 主程序 =============

def main():
    if len(sys.argv) < 2:
        print("""
📤 Notion Sync - 简单版

用法:
    python3 notion_sync.py <文件> [--notion]
    python3 notion_sync.py report.md --notion --category "Research"
    python3 notion_sync.py image.png --notion --category "Images"

环境变量:
    NOTION_KEY, NOTION_DATABASE_ID, GITHUB_TOKEN, GITHUB_OWNER, GITHUB_REPO
""")
        sys.exit(0)
    
    path = sys.argv[1]
    sync_notion_flag = "--notion" in sys.argv
    category = "Research"
    
    for i, a in enumerate(sys.argv):
        if a == "--category" and i+1 < len(sys.argv):
            category = sys.argv[i+1]
    
    if not os.path.exists(path):
        print(f"❌ 文件不存在: {path}")
        sys.exit(1)
    
    print(f"\n{'='*50}")
    print(f"📤 {os.path.basename(path)}")
    print(f"{'='*50}\n")
    
    result = sync_notion(path, category) if sync_notion_flag else upload_github(path, category)
    
    if result["success"]:
        print(f"✅ GitHub: {result.get('github', 'N/A')}")
        print(f"🌐 CDN: {result['cdn']}")
        if "notion" in result:
            print(f"📒 Notion: {result['notion']}")
        print(f"\n{'='*50}\n")
    else:
        print(f"❌ 失败: {result.get('error', 'Unknown')}\n")

if __name__ == "__main__":
    main()
