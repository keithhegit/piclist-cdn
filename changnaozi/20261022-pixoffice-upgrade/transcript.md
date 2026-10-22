# PixOffice 10/19 重大升级：多团队 2D 智能体办公室与 HTTP 接入协议 - 抖音

> **元信息**
> - 作者：赛文同学(AI版)（抖音）
> - 平台：抖音
> - 正式链接：https://www.douyin.com/video/7698114904053534015 （分享短链 https://v.douyin.com/Izy8u3aVCTc/）
> - 分享标题：PixOffice 重大升级更新！ PixOffi...（分享文案被截断，全文未取得）
> - 时长：未知（成片未得）
> - 发布时间（推断）：作品 ID 高 32 位换算为 **2026-10-19 04:57（北京时间）**，紧跟仓库 10/19 01:42 的 `feat: finalize office integration and multi-team experience`。这是按 ID 推算，页面没有核实。分享文案里的「08/14」看起来不是发布日期，时间线**有不确定**。
> - **校对说明：抖音成片未得；依据源仓库/源文。**
>   - `yt-dlp` 返回 `HTTP 403 / Fresh cookies are needed`；iesdouyin 分享页 SSR 没有 `videoInfoRes`，web/api 返回空；PC 页没有视频数据。箱内**没有口播 ASR**，下文**不是视频口播逐字稿**，是视频所讲升级对应的**一手源原话**（README、commit、官方接入文档）。
>   - 视频里实际说了哪些点、画面上展示了什么，都没有核实；用「账号剪辑口径」引用时请以原视频为准。
> - 一手源（以此为准）：
>   1. GitHub `workbzw/pixoffice`（MIT，创建于 2026-09-30，约 64★，最近推送 2026-10-22 09:52 北京时间）README.md / README.en.md
>   2. `integration/README.md` 与 `integration/docs/office-integration.md`、`chat-integration.md`、`dashboard-integration.md`、`message-relay.md`
>   3. `docs/plugin-runtime.md`（场景命令协议 2.0）
>   4. 10/19–10/22 commit 记录
>   5. 演示站 https://pixoffice.online/
>   6. 姊妹项目 `workbzw/ai-office-react` README：「免费商用开源版请使用 PixOffice 项目」；该项目只能自用（Spine 许可）
> - 第三方解读（**不是源文档，时间更早，已过时**）：blog.mushroom.cv《PixOffice：给 AI 多智能体加一层 2D 办公室可视化，三种接入方式详解》（2026-10-05）。文中的 `/scene/commands`、`/actions`、`VITE_PIXOFFICE_CHAT_URL` 属于 10/05 的旧网关（仓库当时有 `scripts/scene-gateway.mjs`、`action-gateway.mjs`），**10/19 起主分支已换成 Fastify `POST /api/pixoffice/messages`**。
> - 搜索「赛文同学 PixOffice」「PixOffice 重大升级」，没有找到同题的公众号、B 站稿或文字稿。

---

## 一、源原话：README（当前主分支，摘录）

> PixOffice 是基于 Vite + React + PixiJS 的二维互动场景项目。内置六个人物的帧动画，支持多办公室、任务白板、聊天、限时决策菜单和网格布局编辑；办公室、教室、农场可独立装配。

> 使用 Node.js 24，最低支持 Node.js 22.13。
> ```bash
> npm ci
> npm run dev:vite
> ```
> 打开终端显示的地址，进入 `/office/` 即可体验本地演示，无需业务后端。聊天默认为交互预览，不调用模型。
> 接入外部系统时使用 `npm run dev` 启动前端与 Fastify，再按对接指南初始化办公室。
> `npm run build` 生成 `dist/`，可用于 Vercel 静态演示；服务器与 Docker 对接部署见部署文档。

> 场景包与素材包在仓库内开发，尚未发布 npm。2:1 轴测入口仍为架构验证，骨骼动画引擎尚未实现。
> 软件许可见 LICENSE 与第三方声明；图片素材的使用授权需另行确认。

10/19 版 README（`00eb967`，后来被精简）原话：

> 当前办公室动画区域实录（2026-10-19，6秒循环、25帧/秒）：墙面任务白板、电脑旁任务气泡、人物走动与工位交流。
> 内置六个人物的帧动画、坐姿和办公室素材，支持多办公室切换、工位拜访、多人会议、持续专注、固定格式任务白板、限时确认与选项菜单、插件启停和网格拖放布局。
> 项目使用 npm workspaces，共十一个包。五个通用包：`protocol` 对接协议、`contracts` 表现与动画契约、`runtime` 核心运行时、`renderer-pixi` 渲染宿主、`animation-frame` 帧播放器。三个现有场景分别由 `scene-office` / `assets-office`、`scene-classroom` / `assets-classroom`、`scene-farm` / `assets-farm` 组成，场景之间不互相依赖。
> 本地预览点击"开始演示"后，约 15 秒弹出当前办公室的一条确认问题，约 30 秒在另一个办公室显示一条侧边选择卡。
> 办公室右上角网格按钮进入全屏「布置办公室」；左上角按钮打开团队空间总览。……外部 AI 可通过同一套 `map.edit` 协议修改共享草稿，不需要模拟鼠标。

## 二、源原话：升级时间线（commit，北京时间）

| 时间 | commit | 原文 |
|---|---|---|
| 10/05 | 1072f05 / eac5a79 | refactor: split PixOffice into packages and office examples / feat: add bilingual website and language-aware READMEs |
| 10/07 | ee2d11e 等 | feat: add isolated classroom scene and homepage preview（教室场景） |
| 10/10 | 72c4411 | Add independent farm scene with crops and roaming chickens（农场场景） |
| **10/19 01:42** | **d43eef2** | **feat: finalize office integration and multi-team experience** — "Add the Fastify relay, strict protocol contracts, recovery and integration tests. Separate scene controllers and UI shells, update whiteboard activity progress and typography, and clean up retired code and assets."（752 个文件，+18985/−12456） |
| 10/19 02:43 | 86337f7 | feat: handle background decisions directly and refresh office previews — "Add team-scoped quick decision cards with countdowns and mobile layouts. Slow whiteboard activity progress…" |
| 10/19 04:21 | 00eb967 | fix: refine demo decisions and suspension recovery |
| 10/19 05:39 | 156ba5f | refactor: consolidate integration guides and test tooling |
| 10/19 13:04 | efbdaf0 / 1f9baee | feat: refine office work effects and rendering performance / docs: simplify bilingual READMEs and add project support |
| 10/21 09:38 | 32a406f | fix: restore 60 FPS office walking |
| 10/21 09:40 | c6b9854 | feat: render office chat replies as Markdown |
| 10/21 13:51 | 683ac63 | feat: configure chat services during office initialization |
| 10/22 09:52 | 782cf72 | feat: add multi-conversation chat history and recovery |

> 推断：视频约在 10/19 04:57 发布，讲的「重大升级」最可能是 d43eef2–00eb967 这一批（Fastify 中转、多团队、决策卡、白板）。10/21–10/22 的 Markdown 回复、60FPS 行走修复、多会话聊天发生在视频**之后**，视频里大概率没有。

## 三、源原话：对接指南 `integration/docs/office-integration.md`（关键段落）

**通信参与方**

> 外部业务后端调用 PixOffice 服务端。PixOffice 服务端通过 SSE 向浏览器页面发送消息……
> ```text
> 外部业务后端 -- POST /api/pixoffice/messages --> PixOffice 服务端
> PixOffice 服务端 -- SSE 消息 --> PixOffice 浏览器页面
> 外部业务后端 <-- 同一次 HTTP 请求的响应 -- PixOffice 服务端
> ```

**地址与认证**

> 所有办公室业务操作和场景指令都发送到同一个地址：
> ```http
> POST <PixOffice 服务地址>/api/pixoffice/messages
> Authorization: Bearer <PIXOFFICE_API_KEY>
> Content-Type: application/json
> ```
> 默认服务地址为 `http://127.0.0.1:8765`，默认密钥为公开演示值 `pixoffice-demo-key`。

**操作与返回时机**

| 请求内容 | 返回时机 |
| --- | --- |
| `offices.initialize` | 取得浏览器逻辑初始化结果后返回 `200`；已缓存但未等待浏览器确认时返回 `202` |
| `office.snapshot` | 取得浏览器应用结果后返回 `200` 和 `applied`；已缓存但未等待浏览器确认时返回 `202` 和 `cached`；较旧状态返回 `200` 和 `ignored` |
| `office.read` | 返回办公室目录，或等待在线页面返回指定办公室的状态 |
| `office.capabilities` | 服务端立即返回人物、物品、行为及 UI 的 JSON Schema，初始化前也可查询 |
| `ui.next` | 领取一个用户操作；等待时间内没有操作则返回 `data.actions: []` |
| `ui.respond` | 服务端接收指定用户操作的展示结果后返回 |
| `decision.request` | 等待用户选择后返回；到期返回 `408` |
| `{teamId, command}` | 指令发送到在线页面连接后返回 `200`；播放由浏览器随后执行 |

> 初始化、状态更新和状态查询等待浏览器处理的默认时限为 10 秒。菜单等待时限默认 60 秒，`timeoutMs` 可设为 1000–300000 毫秒。外部业务后端和反向代理的 HTTP 超时应大于相应等待时限，例如为最长菜单配置 310 秒。

**通用数据规则（原话节选）**

> - 请求和响应的任何层级都禁止 `null`。
> - 办公室、场景人物、命令和交互 ID 使用 1–100 个字符，允许英文字母、数字、`_`、`.`、`:`、`-`。
> - 时间使用包含时区的 ISO 8601 格式。
> - 办公室业务和场景指令的单次请求体最大 64 KiB；聊天请求使用独立接口，上限为 512 KiB。

**1. 初始化办公室（原样 JSON）**

```json
{
  "type": "offices.initialize",
  "chat": { "url": "https://your-host.example/chat" },
  "offices": [
    {
      "schemaVersion": "1.0",
      "seq": 1,
      "workspace": { "id": "team-a", "name": "研发办公室" },
      "conversations": [
        {
          "id": "main",
          "title": "登录模块开发",
          "employees": [
            { "id": "coding", "sceneActorId": "office-lead", "name": "代码开发", "online": true },
            { "id": "testing", "sceneActorId": "office-lead", "name": "自动化测试", "online": true }
          ],
          "tasks": [
            {
              "id": "task-1", "title": "登录模块开发", "assigneeId": "coding",
              "status": "running", "summary": "实现登录与权限校验。",
              "updatedAt": "2026-10-18T10:00:00Z"
            }
          ],
          "events": [],
          "whiteboard": { "template": "task-board-v1", "title": "", "status": "queued", "steps": [] }
        }
      ]
    }
  ]
}
```

> 一个办公室对应一个工作区，`conversations` 列出工作区中的会话。每个会话独立提供成员绑定、任务、动态和当前目标白板。

**2. 更新任务（`office.snapshot`）**

> `snapshot` 表示该办公室在此版本下的完整业务状态……外部业务后端负责汇总该办公室的完整数据，并为每次更新生成更大的 `seq`。PixOffice 根据 `seq` 选择最新状态，因此 HTTP 请求可以乱序到达。
> 电脑旁的进度条是活动展示：进行中最多显示 99%，收到 `completed` 后显示 100%。

**3. 请求用户确认（原样 JSON）**

```json
{
  "type": "decision.request",
  "teamId": "team-a",
  "timeoutMs": 60000,
  "decision": {
    "id": "decision-1",
    "actorId": "office-lead",
    "kind": "confirmation",
    "title": "是否提交登录模块？",
    "description": "请检查实现结果后决定。",
    "confirmLabel": "确认提交",
    "rejectLabel": "暂不提交"
  },
  "conversationId": "main"
}
```

> 多选项菜单（`kind: "choice"`）允许 2–8 个选项。`conversationId` 必填……否则返回 `404 CONVERSATION_NOT_FOUND`。

**6. 处理用户操作**

```json
{ "type": "ui.next", "timeoutMs": 30000 }
```

```json
{
  "type": "ui.respond", "interactionId": "action-1",
  "presentation": {
    "target": "dialog",
    "content": { "template": "detail-v1", "title": "王明的任务", "description": "正在开发登录模块。", "fields": [{ "label": "进度", "value": "66%" }], "actions": [{ "id": "review", "label": "提交审核" }] }
  }
}
```

> `action` 类型：`actor.inspect`、`employee.inspect`、`task.start` / `task.block` / `task.complete`、`task.assign`、`dialog.action`、`conversation.delete`。
> 用户操作最多保留并等待处理 60 秒，超时后……`ui.respond` 返回 `410 UI_REQUEST_EXPIRED`。

**7. 发送场景指令（原样 JSON）**

```json
{
  "teamId": "team-a",
  "command": {
    "protocolVersion": "2.0", "sceneId": "team-a", "commandId": "say-1",
    "type": "activity.start", "capability": "scene.say",
    "participants": [{ "entityId": "office-lead", "role": "actor" }],
    "params": { "text": "开始处理任务。", "durationMs": 2000 }
  }
}
```

> `teamId` 与命令的 `sceneId` 必须一致。……指令也可按顺序或并行组成最多 32 条的批次。
> HTTP `200` 表示指令已发送到至少一个在线页面连接。……本接口不返回动画开始或完成通知。无在线页面返回 `409`。
> 对已初始化办公室的墙面白板发送 `object.state.set` 会返回 `400 SNAPSHOT_REQUIRED`，应改用 `office.snapshot`。

**内置能力（`docs/plugin-runtime.md` 原表）**

> `scene.primitives`：`scene.move`、`scene.say`（不依赖工位的通用移动与发言）
> `office.visits`：`office.visit`（逐个拜访、每个对象独立消息与回应）
> `office.meetings`：`office.meeting`（2–4 人集合、到齐后讨论、返回各自工位）
> `office.personal`：`office.focus`、`office.emote`（持续专注；挥手、思考、惊讶）

## 四、源原话：聊天接入 `chat-integration.md`（10/21–10/22 新增，视频后）

> 浏览器固定调用同源 `POST /api/pixoffice/chat`，PixOffice 服务端将请求转发至注册的地址。……外部聊天服务无需为 PixOffice 浏览器配置 CORS。模型 API Key 由外部聊天服务保管。

| `type` | 用途 | 成功响应 |
| --- | --- | --- |
| `send` | 提交一轮消息并接收回复 | NDJSON |
| `history` | 分页读取已有记录及生成状态 | JSON |
| `resume` | 继续接收指定轮次的回复 | NDJSON，首条为完整 `snapshot` |
| `cancel` | 明确停止指定轮次的生成 | JSON |

> 所有操作包含 `version: "1.0"`、`teamId`、`conversationId`。……切换会话或办公室不会停止其他会话的回复生成。

## 五、源原话：部署 `message-relay.md`

```bash
npm install
npm run dev                    # Vite + Fastify，POST 默认 http://127.0.0.1:8765/api/pixoffice/messages
npm run integration-example    # 模拟业务后端：建两个办公室、更新任务、等用户确认
npm run integration-ui-example # 领取点击人物/任务按钮的操作
PIXOFFICE_URL=http://127.0.0.1:3000 PIXOFFICE_API_KEY=your-private-key npm run integration-example
CHAT_SERVICE_URL=http://your-backend:8000/chat npm run integration-example

docker build -t pixoffice .
docker run --rm -p 3000:3000 -e PIXOFFICE_API_KEY=replace-with-private-key pixoffice
# 打开 http://localhost:3000/office/
```

> Docker 默认一个容器、一个 Node 进程，同源提供页面、POST 和 SSE。状态与连接保存于该进程内存，多实例部署需要额外的状态共享和消息广播服务。
> `.env.example` 只是配置模板，启动器不自动加载 `.env`。

---

## 附：第三方解读（mushroom.cv，2026-10-05，旧协议，仅作对照）

> 这一节是第三方写的，不是作者原话，记录的是 10/05 前后的旧接入方式，**现在主分支已不适用**。

- 旧端口：前端 `5173`；Action Gateway `8765`。
- 旧路径 1：`POST /scene/commands`（Scene Commands v2.0）+ `GET /scene/commands/{commandId}` 轮询、`GET /scene/state`、`GET /scene/capabilities`。
- 旧路径 2：Legacy `POST /actions`（`desk_visit` / `move` / `say` / `set_state`）。
- 旧路径 3：`VITE_PIXOFFICE_CHAT_URL` 或 `OfficeApp chatSource` 注入。
- 新旧对照：命令体（`protocolVersion: "2.0"`、`activity.start`、`capability`、`participants`、`params`）**还在用**，但现在要包在 `{teamId, command}` 里，发到 `/api/pixoffice/messages`，并带 Bearer 鉴权；没有轮询，只返回「已转发」。聊天地址从前端构建变量改成了 `offices.initialize.chat.url` 服务端注册。
