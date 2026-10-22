# PixOffice 10/19 重大升级：多团队 2D 智能体办公室与 HTTP 接入协议 - 抖音

> 来源：抖音 @赛文同学(AI版) https://www.douyin.com/video/7698114904053534015 （推断发布于 2026-10-19 04:57 北京时间）
> **抖音成片未得；依据源仓库/源文。** 下面的能力、命令都出自 `workbzw/pixoffice` 主分支（截至 2026-10-22 09:52 北京时间）。视频具体讲了哪几点没有核实。

## 一句话定位

PixOffice 是开源（MIT）的 2D 像素办公室前端：你的智能体或业务后端发 HTTP 消息，它就把「谁在做什么任务、白板进度、要不要人确认」画成人物走动、工位拜访、会议、白板和弹出决策卡。10/19 这次升级把它从「场景演示」改成了**可对接的多团队服务**：Fastify 中转 + SSE + 严格协议 + 多会话。

## 这次升级到底改了什么（源文档口径）

| 方面 | 升级前（~10/05，第三方博客也记录的旧版） | 升级后（10/19 起主分支） |
|---|---|---|
| 接入入口 | `/scene/commands`、`/actions` 旧网关，无鉴权 | 统一 `POST /api/pixoffice/messages` + `Authorization: Bearer` |
| 服务端 | 开发脚本网关 | **Fastify 中转**，SSE 推给浏览器，可 Docker 单容器部署 |
| 数据模型 | 单场景 + 前端变量接 dashboard | `offices.initialize` 多办公室（多团队），每个办公室下多 `conversations` |
| 任务/白板 | 前端数据源 | `office.snapshot` 全量快照 + 递增 `seq`（允许乱序），固定模板 `task-board-v1` |
| 人工确认 | 无 | `decision.request`：确认 / 2–8 选项菜单，带倒计时，超时 408；后台团队弹侧边卡 |
| 用户点击 | 无回传 | `ui.next` / `ui.respond` 领取式：点人物、任务按钮，后端返回详情卡 |
| 聊天 | `VITE_PIXOFFICE_CHAT_URL` 前端构建变量 | 初始化时注册 `chat.url`，服务端转发；10/21 起支持 Markdown 回复，10/22 起支持多会话历史、断线续传（resume）、停止（cancel） |
| 场景 | 办公室 | 办公室 + 教室 + 农场独立装配，共 11 个 workspace 包 |
| 测试 | 少量 | 协议 Schema、端到端（HTTP 客户端 + 真浏览器 + 临时 Docker）验收 |

> 账号剪辑 vs 源原话：视频标题只写了「重大升级更新」，具体卖点（比如「多团队」「决策卡」「接入智能体」）是我对着 commit 推断的；转述时请写「据仓库更新日志」，不要写成视频原话。

## 上手顺序

1. **先看效果（零配置）**：打开 https://pixoffice.online/office/ ，或在本地运行：
   ```bash
   git clone https://github.com/workbzw/pixoffice.git && cd pixoffice
   npm ci          # Node 24（最低 22.13）
   npm run dev:vite   # 打开终端地址 + /office/，纯本地演示，聊天不调模型
   ```
2. **起服务端模式**：`npm run dev`（Vite + Fastify，默认 `http://127.0.0.1:8765`，演示密钥 `pixoffice-demo-key`）。
3. **跑官方示例客户端**（模拟你的业务后端）：
   ```bash
   npm run integration-example      # 建两个办公室、更新任务、弹确认
   npm run integration-ui-example   # 再开一个终端：处理页面点击
   ```
4. **换成自己的智能体**：按「查能力 → 初始化 → 推快照 → 发动画 / 请求确认 → 领用户操作」接入（见下方命令）。
5. **接聊天（可选）**：自己实现一个 NDJSON 聊天服务，初始化时带上 `chat.url`。
6. **部署**：Docker 单容器，务必换掉私有密钥，并给页面加访问控制。

## 能力表

| 能力 | 协议 `type` / capability | 说明 |
|---|---|---|
| 查人物/行为/Schema | `office.capabilities` | 初始化前也能查，拿到机器可读的 JSON Schema |
| 建办公室 | `offices.initialize` | 多办公室 + 多会话 + 成员绑定人物（`sceneActorId`） |
| 更新任务/白板 | `office.snapshot` | 全量快照，`seq` 必须递增 |
| 查状态 | `office.read` | 列办公室目录，或读单个办公室 |
| 人工确认 | `decision.request` | confirmation / choice，`timeoutMs` 1000–300000 |
| 用户点击 | `ui.next` → `ui.respond` | 返回详情卡 `dialog` / 白板 `whiteboard` / 结果 `result` |
| 人物动画 | `{teamId, command}` | `scene.move`、`scene.say`、`office.visit`、`office.meeting`（2–4 人）、`office.focus`、`office.emote`；最多 32 条一批 |
| 聊天 | `POST /api/pixoffice/chat` | `send` / `history` / `resume` / `cancel`，NDJSON |
| 地图编辑 | `map.edit` | 外部 AI 可以直接改布局草稿 |

## 可复制命令

```bash
URL=http://127.0.0.1:8765/api/pixoffice/messages
KEY=pixoffice-demo-key
H=(-H "Authorization: Bearer $KEY" -H 'Content-Type: application/json')

# 1) 查能力
curl -s "${H[@]}" -X POST $URL -d '{"type":"office.capabilities"}'

# 2) 初始化一个办公室
curl -s "${H[@]}" -X POST $URL -d '{
 "type":"offices.initialize",
 "offices":[{"schemaVersion":"1.0","seq":1,
  "workspace":{"id":"team-a","name":"研发办公室"},
  "conversations":[{"id":"main","title":"登录模块开发",
   "employees":[{"id":"coding","sceneActorId":"office-lead","name":"代码开发","online":true}],
   "tasks":[{"id":"task-1","title":"登录模块开发","assigneeId":"coding","status":"running","summary":"实现登录与权限校验。","updatedAt":"2026-10-18T10:00:00Z"}],
   "events":[],
   "whiteboard":{"template":"task-board-v1","title":"","status":"queued","steps":[]}}]}]}'

# 3) 让人物说话
curl -s "${H[@]}" -X POST $URL -d '{"teamId":"team-a","command":{
 "protocolVersion":"2.0","sceneId":"team-a","commandId":"say-1",
 "type":"activity.start","capability":"scene.say",
 "participants":[{"entityId":"office-lead","role":"actor"}],
 "params":{"text":"开始处理任务。","durationMs":2000}}}'

# 4) 请求人工确认（会一直挂起等用户点，最长 timeoutMs）
curl -s --max-time 70 "${H[@]}" -X POST $URL -d '{
 "type":"decision.request","teamId":"team-a","timeoutMs":60000,"conversationId":"main",
 "decision":{"id":"decision-1","actorId":"office-lead","kind":"confirmation",
  "title":"是否提交登录模块？","description":"请检查实现结果后决定。",
  "confirmLabel":"确认提交","rejectLabel":"暂不提交"}}'

# 5) 领取用户点击
curl -s "${H[@]}" -X POST $URL -d '{"type":"ui.next","timeoutMs":30000}'
```

Docker：
```bash
docker build -t pixoffice .
docker run --rm -p 3000:3000 -e PIXOFFICE_API_KEY=replace-with-private-key pixoffice
# http://localhost:3000/office/
```

给 Cursor / 编码智能体的接入提示词（我拟的，不是源文）：
> 读 `integration/docs/office-integration.md`，给我的多智能体系统写一个 PixOffice 适配器：启动时用 `office.capabilities` 取人物 ID，再 `offices.initialize`；每个 Agent 状态变化时推全量 `office.snapshot`（`seq` 单调递增）；交接任务发 `office.visit`；需要人工审批时调 `decision.request`；后台循环 `ui.next` 处理点击。端点和密钥集中放在一个配置模块里。

## 坑

- **别照第三方博客接**：mushroom.cv（10/05）写的 `/scene/commands` 轮询、`/actions`、`VITE_PIXOFFICE_CHAT_URL` 都是旧版。现在只有 `/api/pixoffice/messages`，动画请求只回「已转发」，不回「已完成」。
- **任何层级都不能有 `null`**；业务请求出现未声明字段就返回 400。
- `seq` 必须递增；`snapshot` 是**全量**，漏掉的会话会被当成删除。
- 白板只能用 `office.snapshot` 改，发 `object.state.set` 会返回 `400 SNAPSHOT_REQUIRED`。
- 没有在线页面时，动画返回 `409`；初始化或快照返回 `202`，表示只缓存了、浏览器还没确认。
- **服务端重启后，状态和聊天地址都要重新初始化**（全在进程内存里）；多实例部署需要自己做状态共享。
- `decision.request` 是长挂起请求，反向代理超时要大于菜单时限（官方建议 310 秒）。
- `pixoffice-demo-key` 是公开密钥；上公网必须换私有密钥并加页面访问控制。`.env` 不会自动加载。
- 包没发到 npm，只能从源码用；**图片素材授权要另外确认**（MIT 只覆盖代码）；`ai-office-react` 只能自用（Spine 许可）。
- 项目很新（09/30 创建），协议改得很快，接入层要包一层适配。

## 适合谁

- 在跑多智能体或任务流水线、想给老板或用户一个「看得见」的进度界面的人。
- 做 AI 产品演示、直播、短视频素材，想要像素风办公室画面的人。
- 想学「领取式交互 + SSE + 快照版本号」这类前后端协议设计的人。
- 不适合：要生产级多实例高可用，或要商用美术素材却还没确认授权的人。

## 章节导航（逐字稿）

1. README 原话（定位、快速开始、11 个包）
2. 升级时间线（10/05 → 10/19 重大升级 → 10/21–22 聊天增强）
3. 对接指南：地址鉴权、操作表、初始化 / 快照 / 决策 / 用户操作 / 场景指令 JSON 原样
4. 聊天接入（send / history / resume / cancel）
5. 部署命令
6. 附：第三方博客旧协议对照
