# Hermes+飞书游戏站全自动流水线

> 来源：七鹿 · 微信 · [原文](https://mp.weixin.qq.com/s/rFDTj0JY5RzllFjWcpfjmQ) · 校对 2026-10-02 · 本文件为离线 CDN 副本（从 Notion 攻略摘要导出）

## 一句话定位

原文用 Hermes Skill + 飞书闸门，把「抓游戏→洗包→R2→SEO→注入→部署」做成全自动；**我们要偷的是链路思维与人只拍板**，不是换整套 Hermes/H5 iframe 栈。映射到现有：Researchy 锁源 → 远程控制合包 Upload → 双闸 → 定时补长尾。

## 上手顺序（对我们站）

1. **先定「人只确认一次」的闸门**：等价飞书确认——例如 Researchy 事实 PASS + UI 视觉 PASS 后，才由远程控制 Upload。
2. **把可脚本化步骤写成 Skill / Routine**：挖词、sitemap/GSC 复查、JSON 数据刷新、SEO Checklist。
3. **SEO 内容规范锁进 Skill**：overview 用字符串、FAQ 键名 `q`/`a`、tips 不自带序号。
4. **定时三件套对标**：每日挖词 · 仓库报告同步到站 · 批量注入/加厚内页。
5. **不要照搬**：六源 H5 抓游 / 去广告 SDK / R2 托管可玩包——我们是 codes+guides SEO 站。

## 能力表（原文 → 我们）

| 原文环节 | 原文做法 | 我们映射 |
|---|---|---|
| 监测抓源 | 六聚合平台 + 定时 Skill | Researchy 锁 URL/有字幕 YT；趋势+Reddit+盘词 |
| 人工闸门 | 飞书确认上不上 | 双闸 PASS 后 Upload |
| 清洗上传 | 去广告/跳转 → R2 + HEAD | 合包规范 + live spot；不托管可玩包 |
| SEO 生成 | Skill 生成区块 + 规范校验 → games.json | 指南/工具页 JSON 或 MD 驱动 |
| 部署 | git 推构建 | 远程控制 CF Pages Direct Upload |
| 养鲜 | 挖词 / Actions 同步 / Trending 注入 | Sprint 加厚 + GSC sitemap |

## 金句

- 自动化价值不是单点提速，是**整条链路**提速。
- 人只做一件事：决定要不要上；其余交给流水线。
- 硬规则与分工定了之后，Skill/Routine/远程控制 CLI 才是执行干部。

## 坑

- 半自动心态起步 → AI 方案也会停在半自动
- 未双闸就 Upload、Codes 未核验却标 Working
- 开源仓 kennyzir/7deer_skills 可参考，落地前对齐总案栈

## 适合谁

Roblox Map SEO Ads 房间要迭代「养站自动化 / Skill 化」时读；H5 可玩站另案。

## 章节导航（原文）

一抓游 → 二 SEO 生成 → 三定时养鲜 → 四认知 → 五做成体系
