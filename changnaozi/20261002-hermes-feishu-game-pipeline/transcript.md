# 校对版摘要：Hermes + 飞书游戏站全自动流水线

| 项目 | 内容 |
|---|---|
| 原标题 | 我用 Hermes + 飞书，做了一个全自动更新的游戏站流水线 |
| 作者 | 七鹿 |
| 链接 | https://mp.weixin.qq.com/s/rFDTj0JY5RzllFjWcpfjmQ |
| 校对 | 2026-10-02 WebFetch；攻略按「举一反三」改写映射到 Roblox Map SEO Ads |
| 说明 | 本地原文件夹曾缺失；本离线稿自 Notion 页导出，供 CDN 弱网副本 |

## 结构摘录

- 核心矛盾：内容不够、新鲜度不足 → 爬虫不来。人手搓页/文案/sitemap/CDN 不可持续。
- **一、自动抓游戏**：Hermes skill 六源；看页面类型（itch embed / unityweb）→ 下载清洗（广告 SDK、跳转、telemetry）→ R2 + HEAD；飞书确认后自动跑。
- **二、SEO 页面自动生成**：overview / howToPlay / features / tips / FAQ(q,a) / comments；硬约束后注入 games.json，模板渲染，git 部署。
- **三、定时**：每日挖词（含 Roblox 长尾 + YouTube）· Actions 同步 Markdown 报告 · 四层过滤批量注入 Trending。
- **四、认知**：Hermes 解决「怎么不用你」——人定方向与标准，执行与校验交给自动化。
- **五、体系**：监测→清洗→上传→生成 SEO→注入→构建→验证→部署；一开始就奔全自动设计。
- 开源：kennyzir/7deer_skills。
