# VibeX 开源 ADE 多智能体开发环境 - 抖音

## 一句话定位

抖音账号 **Xforever** 的图文在安利开源 **ADE/IADE（Integrated Agent Development Environment）** 产品 **VibeX**：把 Claude Code / Codex / DeepSeek / Gemini CLI / Antigravity / Cursor 等 Coding Agent 装进同一本地优先工作台，强调人↔Agent、Agent↔Agent 的原生协作（看板 / 无限画布 / 协作空间 Bot 群聊），而不是再开一堆终端窗口。

源：https://www.douyin.com/note/7703832681612940623 （短链 `v.douyin.com/fzE8ndi2yS0/`）  
一手产品：https://vibex.xforever.xin · https://github.com/Xircth/VibeX（Apache-2.0；本稿处理日 Release 约 v0.4.2）

## Keith 备注 · 定位对照（非账号原文）

> 以下为 Keith 当条补充口径，**不是**抖音正文，入库/引用时请标明「Keith 备注」。

- **SuperAgent**（此处对照卡兹克开源 [Agent-Autoloop](https://github.com/KKKKhazix/agent-autoloop) 那一类）：本质是**基于事件驱动的自动 Agent 任务分发与调配系统**，重心在**事件驱动 + 流程化**（规则/Webhook/流水线把任务起点从人身上挪开）。
- **VibeX**：重心是**人与 Agent、Agent 与 Agent 的原生协作范式**（同一工作台里的会话、看板、协作空间、权限与 worktree）；二者定位不同。
- VibeX **后续也会支持事件触发器**（与 Autoloop 式中台不是同一产品形态，但触发能力会补）。

对照表（便于选型，勿混为一谈）：

| | SuperAgent ≈ Autoloop 类 | VibeX（本条 ADE） |
|---|---|---|
| 主问题 | 谁在什么事件下自动开工、怎么调度 | 人怎么和多 Agent 同屏协作、审 Diff、并行不打架 |
| 主交互 | 规则 / Webhook / 流水线 / 少打扰审批 | 看板·画布·群聊 Bot·工作区·权限审批 |
| 典型画面 | 事件→派工→执行→回传 | 多会话卡、协作空间角色群、Git worktree |
| 重叠点 | 未来 VibeX 也可挂事件触发器 | Autoloop 类也可接 IM 卡片；仍非同一层抽象 |

> 另：圈内还有 **DeepSeek Harness Super-agent**（`dsh-superagent` 研究原型）等同名概念；Keith 本条明确锚定的是 **Autoloop 式事件驱动分发**，不要自动等同 DeepSeek 论文原型。

## 上手顺序（可照做）

1. 打开官网下载页或 GitHub Releases，装 macOS / Windows / Linux 桌面端（或 `npx @omnione/vibex` / 自建 `vibex-server`）。
2. 首次启动让它探测本机 Agent 运行时；在 **设置 → Agent** 里启用你要的 Agent，完成各自登录/API Key（截图示例：Google Antigravity 走 OAuth + ACP 适配器预检查）。
3. 打开或创建 **Git 管理的项目**；并行任务给独立 **Worktree/分支**。
4. 在 **看板 / 无限画布** 起会话卡，或在 **协作空间** 拉多角色 Bot 群；需要时在工作区开 **内置浏览器** 做 DOM 拾取与预览。
5. Agent 改代码后走 **Diff / 执行进程** 审查，再提交；高危操作可走 IM 渠道审批（飞书/企微/QQ/Telegram 等，见官方 docs/chat-channels）。

## 能力表（来自界面审视 + README，勿臆造抖音未展示能力）

| 能力 | 图上/文档可见证据 | 备注 |
|---|---|---|
| ADE/IADE 定位 | README 标题；画布卡内 IDE vs ADE 文案 | ADE = Agent Development Environment |
| 多 Agent 聚合 | 设置页多 Agent 图标；内置 Claude Code/Codex/… 列表 | ACP 统一管道 |
| 协作空间 Bot 群聊 | 宣传片制作组：导演/剪辑/终检/Skill 等同群 | 人↔Agent、Agent↔Agent |
| 无限画布 + 四栏看板 | README 两张看板大图 | 并发任务可视化 |
| Git Worktree 并行 | 卡上 branch/worktree；Diff 面板 | 防多 Agent 互踩 |
| 内置浏览器 + DOM | 工作区右栏浏览器；README 卖点 | 预览/拾取 |
| 执行进程 / 工具轨迹 | 右栏 ListDir/Grep/ReadFile 时间线 | 可审计 |
| 插件 / Skill / MCP | 设置 For SI：Skill·MCP；For Plugin：电脑控制·浏览器 | Everything-is-a-Plugin |
| 消息渠道 | 设置「消息渠道」；docs：飞书/企微/QQ/Telegram | 远程盯进度与审批 |
| 本地优先 | README：无 VibeX 云账号；数据在本机/自托管 | 下载≠SaaS 注册 |

## 图片审视结论（抖音原图未拿到时的同源结论）

- **抖音原图：BLOCKED**（站外空壳 SSR）。分享串 `11/11` 暗示约 11 张；具体原序未知。
- **同源截图实际在秀的产品能力**：本地 Tauri ADE 工作台；多角色协作空间；看板/无限画布；工作区三栏（树·对话·编辑器）；内置浏览器；Git Diff + 执行进程；Agent 级鉴权与环境预检查。
- **文案同构**：作者侧 X 帖「超级…多Agent开发**ADE**工具：**VibeX**」与抖音分享导语「这么好的**ADE**…最近发现一个**超级**…」高度同构，产品指向一致。
- Diff 列表出现 `superagent.test.tsx` 仅是仓库测试文件名，**不能**据此把 VibeX 等同 Keith 说的 SuperAgent/Autoloop。

## 可复制要点 / 金句

- 「Agents needed a new IDE so VibeX exists」——官网定位句。
- ADE ≠ 传统 IDE 插件聊窗；是为 Agent 原生协作搭的工作台。
- 「所有 Agent 都可以是 bot，和 Grokbot 一样自然的协作」（作者 X 口径）。
- 选型口令：**要事件流水线 → Autoloop 类；要同屏多 Agent 协作 → VibeX；以后 VibeX 也会加触发器，仍先认清主问题。**

## 坑

- 抖音正文/原图站外难抓；引用界面细节请优先 GitHub README / 官网 / 自行导出。
- 仍在测试期；各 Agent 需自备订阅或 Key，费用在模型侧。
- 多 Agent 并行务必 worktree，否则 Diff 会糊。
- 名称碰撞：DeepSeek Super-agent、第三方 Superagent.computer、仓库测试文件名 —— 与 Keith 的 Autoloop 对照不是同一对象。
- macOS 未签名安装包可能要在系统设置里放行（官网说明）。

## 适合谁

- 已经在用 Claude Code / Codex / 多 CLI Agent，苦于窗口与权限碎片化的开发者。
- 想要「群聊式」多角色 Agent 协作、又要看 Diff/浏览器的人。
- 在对比 Grok Bot / Autoloop / 自建中台时，需要一张「协作层 vs 事件调度层」地图的人（见 Keith 对照）。

## 章节导航

1. 定位与 Keith 对照  
2. 安装与启用 Agent  
3. 看板 / 画布 / 协作空间  
4. 工作区 · 浏览器 · Diff · 执行进程  
5. 设置：Skill / MCP / 渠道 / 插件  
6. 与 Autoloop 类 SuperAgent 怎么选  

## 推荐入库属性（待你确认；本回合不写 Notion / 不传 CDN）

- **建议 Recurso**：`VibeX 开源 ADE 多智能体开发环境 - 抖音`  
  （勿照搬「这么好的ADE产品居然没一个人提…」）
- **类型**：`第三方来源` + `Git或代码` + `AIGC`  
  （理由：抖音安利帖 + 开源仓库/官网一手；主题为 Agent 工作台）
- **标签**：`常用工具` + `开发日志`  
  （可选再加 `AIGC教程`；勿默认 ClawBot产出）
- **Areas**：`学习` + `工作`
- **Projects**：`Grokbot应用修炼`  
  （作者口径主动对标 Grok Bot 协作；且与 Autoloop/多 Agent 编排修炼相关。若你只想当课外阅读，可改挂 `自我提升-课外阅读`）
