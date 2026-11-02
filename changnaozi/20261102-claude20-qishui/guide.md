# Claude桌面端11项更新上手 - 汽水音乐

## 一句话定位

第三方创作者 Jay（RoboNuggets）把 2026-10 前后 Claude Desktop / Claude Code 桌面大改版非正式叫成「Claude 2.0」，用 ~17 分钟演示 **11 个可马上上手的界面与工作流更新**；汽水账号「马丁没有早晨」转载并加中英硬字幕。**不是** 2023 年那个 Claude 2 模型发布。

## 上手顺序（建议）

1. **更新桌面端** → 确认只剩 Chat / Code（Cowork 已并进 Chat）→ **切到 Code 标签**（作者主张：最好更新都先落在这里；用大白话即可，不必写代码）。
2. **打开会话栏（右侧）** → Environment 开 Remote Control；Settings → Claude Code 勾「新会话自动连远程控制」「工作中保持电脑唤醒」。
3. **看 Context 卡** → 跑清理提示词 + `/doctor` + `/skill-doctor`，先砍预加载垃圾。
4. **侧栏分区** 按项目/客户建 section。
5. **嵌套会话** 试一句「同时做多件事，每件开嵌套会话」；需要总控再 **钉住主会话**。
6. 长任务中途提问用 **`/btw` 旁支**；多会话对照用 **Alt/Option+点击分屏**（先 2 路）。
7. 产物走 **Docs / Slides / Design / Dashboard / Motion**；共享看板再开 **AI-powered artifacts**。
8. 斜杠命令按需：`/output-style`、`/doctor`、`/advisor`、`/insights`、`/recap`、`/rewind`。
9. 有余力再装 **mods**（`/plugin`）和记 4 个快捷键。

## 能力表（11 项）

| # | 更新 | 做什么 | 账号口径要点 | 官方/需核对 |
|---|---|---|---|---|
| 1 | 会话栏 Session rail | 右侧 Environment / Context / Connectors / Outputs | Remote Control、上下文预加载吃额度 | 官方 Desktop 文档确有 session details / Context 卡、Remote Control |
| 2 | 侧栏分区 Sections | 对话进「文件夹」 | 三点菜单 Move to section | 官方：Organize sessions（Group） |
| 3 | 嵌套会话 Nested sessions | 父会话拉起子会话并回收结果 | 不同于 one-way 的 sub-agent；子会话是真侧栏对话 | 官方跨会话编排/并行会话能力存在；「嵌套」叙事偏账号演示 |
| 4 | 主会话 Master session | 置顶会话统筹其他会话 | 默认看最近 20 个活跃会话 | 官方：Claude 可读/发消息到其他 Desktop 会话（约 20 个最近） |
| 5 | Claude Code 云端项目 | 云上线程团队+共享记忆 | Pro/Max beta；文件上云 | 以 claude.com / 帮助中心当前套餐为准，滚动发布 |
| 6 | 旁支对话 Side chats | `/btw` 或菜单；读主会话不打断 | **账号称现已可保存多个** | **官方文档写明：关应用后不落盘、无法回去** → 以官方为准 |
| 7 | 分屏 Split view | Alt/Option+点会话；可缩放到约 10 路 | 新手先 2 路 | 官方：Split view / Open in |
| 8 | Docs·Slides·Design·Dashboard·Motion | 应用内 artifact | Design 独立站将关；Motion 偏 Team/Enterprise | 见 Anthropic「Cowork and chat are one Claude」与定价页 |
| 9 | AI-powered artifacts | Settings→Capabilities 开关；共享物内嵌问答 | 适合给不会用 Code 的同事 | 官方有 AI 能力开关类设置，细节随版本变 |
| 10 | 斜杠命令 | `/output-style` `/doctor` `/skill-doctor` `/advisor` `/insights` `/recap` `/rewind` | ELI5 自定义风格；advisor 省旗舰额度 | 命令以 `code.claude.com/docs/en/commands` 为准（名称会增减） |
| 11 | Mods + 快捷键 | `/plugin` 装 mod；Ctrl+Alt+Space 等 | Ribbon 看额度与 prompt cache 冷热；EscEsc=/rewind | 官方 mods 文：TypeScript、与 CLI 同权、**勿装不信任源** |

## 可复制提示词 / 指令（成片出现）

```text
# 设主会话
You're my master session. Keep track of my other sessions from here.

# 主会话催决策
Which of my chats are waiting on me for a decision?

# 主会话代开会话（示例）
Start two new sessions: Saltmarsh captions and a Tidewell FAQ page.

# 嵌套会话示例
Get this week's client reports ready. Start a session for each client.

# 嵌套会话（营销拆分）
（主会话 Saltmarsh Swim launch）分别为销售页 / 邮件 / 广告开嵌套会话

# 舵子会话
Make them more playful, and lead with the free first lesson.

# 上下文清理（作者屏幕提示大意）
先跑 /context；列出每条消息前已加载的内容及大致体积；建议缩短/合并/关闭哪些；在我确认前不要改任何东西。

# 云项目补上下文
Get the skills and context this project needs.

# 项目记忆示例
Write everything in Australian English.

# 旁支
/btw
What has Claude done so far?

# 产出物
Add a search bar where anyone can ask about this dashboard
What was our busiest day?

# 风格
/output-style
（或）short, warm, no jargon.
```

## 坑与口径差

1. **「Claude 2.0」是创作者/工程师口癖，不是商店里的产品版本号。**
2. **旁支对话持久化：账号说「现在会保存」；Anthropic Desktop 文档写「不落盘」。交付与预期以官方为准。**
3. **Projects 套餐/放量随时变**；侧栏没有就查 More 或 waitlist，不要硬解读成「你没资格用 Code」。
4. **云项目 = 文件上 Anthropic 服务器**；敏感业务优先本地嵌套会话。
5. **Mods 与 Claude Code 同权限、非沙箱**；只装信任源；企业有 `sec-default`。
6. **Prompt cache 冷了会按「重读全文」计费**（作者举 $0.08→$3.36 例）；Ribbon 类 mod 只是观测，不是官方计费面板。
7. **分屏塞 10 路会爆你自己的注意力**，不是模型限制。
8. 汽水链路是 **转载+中文字幕**；作者自我介绍与社区 CTA 属账号内容，不是 Anthropic 公告。

## 适合谁

- 已付费用 Claude Desktop / Claude Code，想把多会话、远程续跑、产物和 slash 收成工作台的人。
- 非开发者也适用（作者明确 code 是误称）。
- 需要对比「博主演示 vs 官方文档」再落自己工作流的人（本条攻略为此而写）。

## 章节导航（成片顶栏 ≈）

1. Claude 2.0 总览（Chat/Code，Cowork 并入）
2. 会话栏
3. 分区与嵌套会话
4. 主会话
5. 云端项目
6. 旁支对话与分屏
7. 文档与幻灯片等 artifact
8. 斜杠命令
9. Mods 与快捷键
10. （能力表里 AI-powered artifacts、斜杠细项等拆在讲解中，与「11 更新」计数对齐见上表）

## 一手源（事实核对，不替代口播）

- https://claude.com/resources/articles/cowork-is-now-claude
- https://claude.com/blog/claude-code-desktop-redesign
- https://claude.com/resources/articles/claude-code-mods
- https://code.claude.com/docs/en/desktop
- https://code.claude.com/docs/en/commands
- 原片（若可访问）：https://www.youtube.com/watch?v=yMnFHFf43Qg
