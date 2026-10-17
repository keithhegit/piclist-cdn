# 网页游戏站开源模板选型白皮书 v1.0（getnexa 首选）

> **来源**：Grillme深挖问题与 Keith 选型对话 2026-10-17 CST  
> **状态**：项目暂不启动，仅存档  
> **主仓**：https://github.com/3000Studios/getnexa  
> **Demo**：https://getnexa.space

## 目标

可套用开源网页游戏站模板，需同时满足：

- 注册登录
- Terms / Privacy 法律页
- 排行榜
- 攻略（SEO）
- 广告位（Adsterra Native Banner 等）
- 游戏为**纯前端 JS**，换新游戏尽量只换游戏代码

## Grill 校准（硬约束）

1. **壳**：倾向 Next，但与 D1 冲突时以 **CF D1 为硬约束**
2. **账号 / 排行榜**：可用 BaaS，实际偏好 **CF D1**
3. **游戏**：纯前端；壳内要广告 code
4. **攻略**：要，且 SEO
5. **标准**：**少改动优先**

结论：已放弃「Next 第一优先」。

## 候选对照

| 维度 | getnexa（首选） | macvg-next | TomeWiki |
|---|---|---|---|
| 技术栈 | Workers + Hono + D1 + 原生 JS SPA | Next + Mongo + 门户 UI | 攻略 / Wiki 向（MDX） |
| 登录 | 有 | 有 | 无 Auth / DB |
| 排行榜 | 有 | 有 | 无 |
| 法律页 | 有 | 视实现 | 有 |
| 攻略 SEO | 一般 | 一般 | **强** |
| 广告位 | AdSense 槽 + ads.txt / robots / sitemap | 视实现 | 视实现 |
| D1 适配 | **原生 D1** | 迁 D1 成本高 | 不适用（无 DB） |
| 结论 | **首选，少改动落地** | 备选；非最少改动 | 仅作攻略 SEO 增强参考 |

## 候选说明

### 首选：getnexa

- 仓库：https://github.com/3000Studios/getnexa
- Demo：https://getnexa.space
- 能力：登录 / 排行榜 / 法律页 / `games` 目录 / AdSense 槽 / `ads.txt` · `robots` · `sitemap`
- 缺口：非 Next；攻略 SEO 一般
- 风险：星少，**必须自测**

### 备选：macvg-next

- 仓库：https://github.com/Mac-Web/macvg-next
- Demo：https://macvg.macweb.app
- 说明：Next + Mongo + 门户 UI；迁 D1 贵，不符合「少改动优先」

### 增强参考：TomeWiki

- 仓库：https://github.com/tiankonglan/TomeWiki
- 示例：https://fortunemill.xyz/
- 说明：攻略 SEO 强、有法律页；无 Auth / DB / 排行榜，只作增强参考

## 链接

| 用途 | URL |
|---|---|
| getnexa 仓库 | https://github.com/3000Studios/getnexa |
| getnexa Demo | https://getnexa.space |
| macvg-next 仓库 | https://github.com/Mac-Web/macvg-next |
| macvg-next Demo | https://macvg.macweb.app |
| TomeWiki 仓库 | https://github.com/tiankonglan/TomeWiki |
| TomeWiki 示例 | https://fortunemill.xyz/ |

## 落地清单（存档用 checklist，非 Notion Tasks）

- [ ] Fork getnexa
- [ ] D1 初始化
- [ ] 本地 test / build 验证
- [ ] 换 `public/games`，接入自有游戏 JS
- [ ] `ads.js` 改为 Adsterra（Native Banner 等）
- [ ] 法律页文案与域名对齐
- [ ] 确认 `ads.txt` / `robots` / `sitemap`
- [ ] （可选）按 TomeWiki 补 MDX 攻略 SEO
- [ ] 上线与 Google Search Console

## 风险与决策记录

1. **为何弃 Next-first**：CF D1 是硬约束；macvg-next 迁 D1 成本高，违反「少改动优先」。
2. **getnexa 星少**：社区验证不足，上线前必须本地自测登录、排行榜、广告槽与构建。
3. **攻略 SEO 缺口**：壳内攻略一般；需要时按 TomeWiki 模式增强，不替换主壳。
4. **项目状态（2026-10-17）**：Keith 决定**暂时不启动项目**；本页仅作选型存档，未建 Project / Tasks，未通知 Projects Manager。
