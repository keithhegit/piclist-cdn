# Roblox工具矩阵站0-1（AdSense）

> 来源：七鹿AI · 微信 · [原文](https://mp.weixin.qq.com/s/jiEXRngX3jCSCmBKK__33A) · 校对 2026-10-02 · 本文件为离线 CDN 副本（从 Notion 攻略摘要导出）

## 一句话定位

用「热门新游 + 低竞争 + 工具化」做 Roblox（及类社区游戏）工具矩阵站抢 Google SEO，再走 AdSense；以 Pokopia 为例跑通 0–1。

## 为什么工具站 > 攻略站

1. 用户：服务高阶玩家（计算/查询/规划）而非浅层阅读
2. 行为信号：交互更深 → 停留与排名隐性加分
3. 商业：高净值用户 → 广告单价更高

护城河：计算器、数据库、交互地图，避开短时资讯内卷。

## 上手顺序（11 步压缩）

1. 选游戏：趋势飙升 + 社区活跃 + YouTube 新视频三线向上
2. 浏览器 Gemini 多轮聊方案（玩家搜什么 / 竞品缺口 / 工具 vs 攻略 / 生命周期）
3. 拆板块深度搜索（务必搜 YouTube + Reddit）→ 结构化 JSON 进 `data/`
4. 方案+素材丢 Claude Opus：Next.js SSG + TS + Tailwind/shadcn + Leaflet → CF Pages
5. 趋势词 → Gemini 意图映射 → IDE 硬编码 SEO + 情境内链
6. SEO Checklist skill 逐项核（含 JSON-LD）
7. AdSense 合规页（隐私/关于/联系/ads.txt）；养自然流量再申请；矩阵注意账号风险隔离（原文主张，须自评估）
8. 养站：趋势 / Reddit / YouTube / 更新日志 → 加内页

## 可复用栈

Next.js 14 App Router 静态导出 · JSON 数据驱动 · Gemini 方案/深搜 · Claude 写码 · CF Pages

## 坑

404 扫描 · 外链图失效 · 过度 SEO · 版权免责声明 · 别第一天就申 AdSense

## 合规提示

文中多 AdSense 账号 / 借身份收款等属高风险操作，仅作原文记录，自行合规评估；不当作可执行建议。
