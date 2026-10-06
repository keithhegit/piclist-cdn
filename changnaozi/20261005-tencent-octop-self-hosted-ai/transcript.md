# 腾讯云开源 Octop：本机单进程自托管 AI 助手全家桶

| 项目 | 内容 |
|---|---|
| 公众号 | 掘金GitHub（gh_1b9349100f90） |
| 作者 | 掘金 |
| 发布日期 | 2026-09-30 11:25 北京时间（= 2026-09-29 20:25 PT） |
| 字数 | 正文汉字约 921；去空白约 1898 字符（含英文/标点/代码） |
| 源链接 | https://mp.weixin.qq.com/s/P1t6Z0OHDA07phC7Jkxrgw |
| 原标题 | 腾讯开源版 WorkBuddy，一个进程跑全家桶 |
| 校对说明 | curl（iPhone Safari UA）HTTP 200 拿到完整 HTML；`#js_content` 可解析；并行 WebFetch 正文一致。未遇验证码/「环境异常」。标题借 WorkBuddy 作对照，正文产品名为 **Octop**（腾讯云开源，MIT；文称约 2,728 Star）。图片 2 张无 alt，仅标注位置。安装脚本 URL、Star 数、能力清单均为原文声称，未另行核验 GitHub。正文以下为 js_content 清洗后的全文（保留命令/列表；合并被 HTML 打断的安装代码块）。 |

---

你的 AI 助手，数据存在谁那里？
ChatGPT、Claude、豆包……它们都帮你解决问题，但你的对话、工作区、凭据，全在别人的服务器上。
Octop 给了另一种答案：所有数据留在你自己的机器上，一个进程启动，Web 控制台、CLI、飞书、钉钉、定时任务全部跑起来。
这是腾讯云开源的自托管 AI 助手平台，2,728 Star，MIT 协议。

[图片1：开篇配图（无 alt；疑为产品/架构示意）]

01 不是聊天窗口，是数字生命体
Octop 的定位是「可并行运作的数字生命体」。
核心架构围绕三个概念展开：
用户：每个用户独立的工作区、凭据、记忆。
Agent：每个用户可以有多个 Agent，各自有不同的角色和能力。
专家：Agent 可调用的专业角色库，比如「技术顾问」「文案写手」「数据分析师」，按场景切换。
一个管理员账号，全家共用。
爸妈用「家庭助手」Agent，你自己在另一个终端用「开发者助手」。
所有人的数据物理隔离，但共享同一个 Octop 实例。

[图片2：配图（无 alt；紧接「数字生命体」架构段落后）]

02 十二项核心能力
Octop 的功能可以归纳为四大类：
入口层：Web 控制台、CLI、HTTP/SSE/WebSocket API、飞书、钉钉、QQ、Discord、企业微信。所有入口共享同一套消息处理管线，你在飞书里说的每一句话，和控制台里说的，进入的是同一个 Agent。
智能层：多 Agent 并行、16 种 MBTI 人格模板、专家库、知识库 RAG、可迁移记忆系统（基于 harness-memory）。记忆随工作区迁移，换台机器记忆还在。
执行层：Terminal AI+（浏览器内交互式 Shell）、Browser AI+（无头 Chromium 网页自动化）、远程桌面（跨平台实时看屏和操作）、ACP 双向集成（委派给 Claude Code / OpenCode / Codex）。
扩展层：Connector 体系（OAuth + MCP 网关，一键接入腾讯文档、微博热搜、新闻等）、插件系统、可插拔存储后端（本地目录、Docker 容器、PostgreSQL、COS/S3）。
最亮眼的是 ACP（Agent Client Protocol）双向集成——`octop acp --agent main`：Claude Code 可以使用 Octop；反过来，Octop 也可以在对话中把编码任务委派给 Claude Code。

03 技术栈：Python + FastAPI + React
后端 Python 3.12+，FastAPI + uvicorn。
Agent 运行时基于腾讯自研的 harness-agent，IM 桥接走 harness-gateway，记忆系统用 harness-memory，浏览器自动化基于 harness-browser（CDP 协议）。
前端 React 18 + TypeScript + Vite + Ant Design。
整个系统是一个单进程架构——不依赖外部消息队列或中间件，Web UI、IM 通道、定时任务全部通过进程内的 HarnessProcessor 统一路由。重启后状态从数据库重建，数据全部存在 `~/.octop/` 下。

```
# macOS / Linux 一键安装
curl -fsSL https://finnie-1258344699.cos.ap-guangzhou.myqcloud.com/octop/install.sh | bash

# 安装后启动
octop run
```

一条命令装完，另一条命令跑起来。不用配 Docker，不用装 Python，脚本自动用 uv 起隔离的 Python 3.12 环境。

04 安全设计：数据不出本机
Octop 从设计层面就考虑了隐私问题。
JWT 多用户隔离——每个用户的 Token 独立签发，互不可见。工具审批机制——敏感操作（比如执行 shell 命令）需要用户确认。Shell 命令防护——内置命令白名单和危险操作拦截。敏感信息脱敏——自动识别身份证号、手机号、邮箱等 PII 信息并脱敏。
所有数据默认存在 `~/.octop/octop.db`（SQLite），也可以换 PostgreSQL 或远端存储。凭据、对话记录、工作区文件，全在你自己机器上。

05 适合谁用

- 有自托管需求的个人开发者——不想把对话数据交给第三方
- 小团队/家庭——多人共用一个 AI 平台，权限隔离
- 关注隐私的企业——数据不出本机，符合合规要求
- 想用 AI 辅助运维——终端 AI+ 和远程桌面直接解决日常运维痛点

写在最后
AI 助手赛道很拥挤。
Octop 走的是另一条路——让 AI 跑在你的机器上，为你所用。
腾讯云出品，代码质量有保障。
如果你正在找一个能把 AI 能力内化的平台，Octop 值得一看。
GitHub：https://github.com/TencentCloud/Octop
