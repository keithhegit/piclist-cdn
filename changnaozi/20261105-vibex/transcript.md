# VibeX 开源 ADE 多智能体开发环境 - 抖音

> meta · 图文+OCR（非口播 ASR）  
> 正式 URL：https://www.douyin.com/note/7703832681612940623  
> 短链：https://v.douyin.com/fzE8ndi2yS0/  
> 作者：Xforever（分享文案；站内 social_author_id≈77250753216）  
> 作品 id：7703832681612940623 · 形态：抖音图文 note（非视频）  
> 发布时间（分享页 meta）：2026-11-05（Asia/Shanghai 日历日）  
> 分享文案角标：11/11（暗示约 11 张图）  
>  
> **抖音原图拉取状态：BLOCKED**  
> 箱外 + 国内 Win/Mac 出口均只能拿到 iesdouyin 空壳 SSR（`_SSR_DATA.data={}`），iteminfo/detail API 空或 Argus 拦截；无 og:image、无 image_list。  
> 下列「官方文案」来自用户分享串 + 同源作者侧公开口径；「图序 OCR」来自 **同源回退**（非抖音 CDN 原图）：  
> 1）GitHub `Xircth/VibeX` README 产品截图 8 张；  
> 2）作者关联账号 `@xiricth`（XingX）X 帖附图（同讲 ADE/VibeX，文案高度同构）；  
> 3）官网 `vibex.xforever.xin` product-stack 截图。  
> **禁止把本稿误认为抖音成片逐张原图 OCR。** 用户若导出抖音图文原图/长截图，可再覆盖校对。

---

## 一、官方 / 分享文案（可核验部分）

### 1.1 用户分享串（抖音客户端复制）

```
5.35 复制打开抖音，看看【Xforever的图文作品】这么好的ADE产品居然没一个人提？最近发现一个超级...
https://v.douyin.com/fzE8ndi2yS0/
… 11/11
```

可还原标题/导语片段：

> 这么好的ADE产品居然没一个人提？最近发现一个超级…

（后半在分享串中被截断；「超级」与下方同源 X 文案「超级无敌好用的多Agent开发ADE工具：VibeX」同构。）

### 1.2 分享页残缺 meta（iesdouyin）

> 于20261105发布在抖音，已经收获了0个喜欢，来抖音，记录美好生活！

（无正文、无图床 URL。）

### 1.3 同源作者公开口径（X · @xiricth / XingX · 2026-11-02，非抖音原文）

帖文 https://x.com/xiricth/status/2117164677264515295 ：

```
发现了一个超级无敌好用的多Agent开发ADE工具：VibeX ，在我用了大半个月之后，我只能说无敌！ @Khazix0918

你之前不是说GrokBot不能在本地用你的Agent吗，这项目的bot功能真的好用，你可以试试。
https://github.com/Xircth/VibeX
```

同账号后续补枪（协作口径）：

```
用用我的vibex，所有Agent都可以是bot，和Grokbot一样自然的协作
https://vibex.xforever.xin
```

```
用下VibeX试试，它的协作空间我觉得和Grokbot一样好用，还可以自选Agent和模型
```

### 1.4 产品自述（GitHub README.zh-CN · 一手）

> **集成智能体开发环境（IADE · Integrated Agent Development Environment）**  
> 把 Claude Code、Codex、DeepSeek、Gemini CLI、Antigravity、Cursor、Kimi Code、OpenClaw 等主流 Coding Agent 装进同一个全插件化研发工作台。  
> 支持无限画布看板调度、Git Worktree 并行隔离、多 Bot 群聊协作、内置浏览器 DOM 拾取与实时 Diff 审查。

官网同义：**ADE / IADE = Integrated Agent Development Environment**；产品名 **VibeX**；域名 `vibex.xforever.xin`；仓库 `github.com/Xircth/VibeX`；当时 Release 约 **v0.4.2（2026-11-05）**。

---

## 二、图序 OCR / 界面审视（同源截图；按产品能力序，非抖音 1…11 原序）

> 说明：抖音「11/11」原序未知。下列按 README 产品图 + X 宣传附图归纳；OCR 为 tesseract + 读图校对混合，专名以界面可见英文/中文为准。

### 图 A · 协作空间 / VibeX-Bot 多角色群聊（X 同源附图 + README `VibeX-Bot.png`）

界面要点（校对）：

- 顶栏可见「协作空间」；左侧会话/成员列表角色名：产品宣传大使、Builder、文档专员、导演、Skill专员、终检审计员、剪辑师等。
- 中央为群聊时间线；示例群名「VibeX宣传片制作组」。
- 导演回报：v2 极简纯白重做版「阶段 7 独立终检审计」**0 BLOCK / 0 WARN**；成片规格文案可见 `1920x1080 @ 30fps`、时长约 `36.0s`；本机路径形态 `C:\Users\…\.vibex\spaces\…`。
- BOSS 反馈浮层三点（可见要点）：① 时长太短，希望至少 2 分钟；② 页面仍是前端 Mock，未用真实前端 UI 转 HTML 做动效；③ 视频里 VibeX LOGO 不正确。
- 右侧「群组详情」：成员旁标注 **Google Antigravity**、模型如 `gemini-4-argon`，以及大额 Token 计数与百分比；底部有 Google AI Ultra / Claude·GPT 周额度条。
- 底栏多工作区标签：`vibex`、`vibex-site`、插件名等 + **VIBEX** 品牌。

### 图 B · 无限画布看板（README `无限画布看板视图.png`）

- 顶栏 Tab：**看板 / 工作区 / 协作空间**。
- 左侧任务/会话列表（含 Fix remote tunnel、WebView 内存保活等条目）。
- 主区：可缩放无限画布，多张会话卡 + 虚线连线；卡片内可见 IDE vs **ADE（Agent Development Environment）** 讨论、多 Agent 协作、验收证据要求等。
- 卡片上常见「47 CHANGES」、Agent Notice、worktree/master 标签。

### 图 C · 默认四栏看板（README `默认看板视图.png`）

- 侧栏状态桶：草稿 / 进行中 / 待检查 / 已完成。
- 主区多色任务卡：含设置外观「浮动设置菜单」合入 master、无限画布会话卡优化、多级菜单闪烁修复、工作区文件重命名/Markdown 预览等。
- 卡内可见 commit hash、测试通过数、用时（如 Worked for 0h 4m / 1h 0m）、模型调用区。

### 图 D · 工作区三栏（文件树 + Agent 对话 + 编辑器）（README `工作区页面.png` / X 同源）

- 左：项目树（`crates`/`frontend`/`src-tauri`/`AGENTS.md` 等）。
- 中：Agent 会话；可见 Token 用量与计时（例：千万级 Token、数十分钟）。
- 右：打开 `AGENTS.md` ——「VibeX is a local-first Tauri desktop app」；要求先读 `CONTEXT.md`、相关 ADR、maiden-skill 等。
- 底栏输入可见模型名（截图版本写 Grok 系列）、「Merge」类应用改动按钮。

### 图 E · 工作区 + 内置浏览器（README `工作区+浏览器.png`）

- 右栏内置浏览器；URL 示例指向 GitHub；可见「拾取/预览」类工作流语境。
- 中栏记录文件树 UI 修复：根行 padding 2px→12px、标题栏高度/半透明 blur、chevron 间距、gitignored 斜体改半透明等；「47 CHANGES / Merge」。

### 图 F · 执行进程 + Git Diff（README `执行进程+Git面板.png`）

- 左：Source Control Diff（数十文件变更，例 47）。
- 中：打开 `SPACE-RULES.md`（人 vs Bot 发言规则、三种回合等）。
- 右：**执行进程**时间线（用户/模型/工具）；工具调用可见 ListDir / GrepSearch / ReadFile 等；任务例「Merge B/D docks into VS Code split tabs」；总时长与 Token 计数可见。
- Diff 列表中出现 `TurnActivity.superagent.test.tsx` 等文件名（界面文件名，不等于产品叫 SuperAgent）。

### 图 G · 会话列表 + 会话详情（README `会话列表+会话详情.png`）

- 左长列表：ACP/gemini、Frontend performance audit、session naming 等。
- 中：`AGENTS.md` 仓库指南。
- 右：计划任务 checklist（policy/shelf/placement/menu/verify 全勾）；用量概览大 Token + 高缓存命中率示意。

### 图 H · 设置 · Agent 鉴权（README `设置页.png`）

侧栏结构（校对）：

- For Human：常规 / 外观 / 快捷指令 / 交互 / 版本管理 / 工作树  
- For SI：**Agent** / Skill / MCP / 消息渠道 / 自动化  
- For System：插件 / 远程连接 / 运行日志 / 系统  
- For Plugin：电脑控制 / 浏览器  

主区示例（选中 **Google Antigravity**）：

- 文案：Google's AI coding agent (first-party ACP server)  
- 状态：已通过账号登录 · 启用开  
- 鉴权管理：官方订阅 / 官方 API / 供应商  
- 预检查可用：运行入口 1.4.5、ACP 适配器 1.4.5、归档解压工具、鉴权 oauth-personal  

### 图 I · 官网 product-stack 工作台（`vibex.xforever.xin/images/product-stack-2.png`）

- Tab：Kanban / Workspace  
- 双栏编辑 +「推理强度」超高滑条；会话模型示意；`/:skill` 类输入提示。

---

## 三、BLOCKED 声明（抖音原图）

```
BLOCKED：抖音 note 7703832681612940623 原图/完整官方长文未能从站外 API 取得。
本 transcript 交付形态 = 分享串文案片段 + 同源产品截图 OCR/读图校对。
非口播 ASR；非抖音 CDN 逐张原图。
```
