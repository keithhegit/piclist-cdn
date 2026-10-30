# 用9个Grok Bot搭周循环产品流水线（含REA洁净室）

> 攻略摘要｜源：搞机小帅《如何用人工智能体Bot建造任何东西（完整课程）》（2026-10-23）  
> 源链：https://mp.weixin.qq.com/s/A7vAaxzHmnVQGizgkfCztA  
> 用途提示：可迁移到本助手多 Bot 协作 / Grokbot 应用修炼；**核心是「窄职责 + 文件交接 + 洁净室」**，不是单 Bot 万能聊天。

## 一句话定位

用 **9 个专职 Grok Bot**（侦察→痛点→竞品→可选 REA 行为还原→战略→CEO 杀弱→SPEC→建造→发布视频），按**周循环 + HANDOFF.md 文件交接**做产品流水线；你只拍板，不把所有事塞进一个超级机器人。

## 上手顺序（最小闭环）

1. **建共享目录约定**：`/workspace/loop/week-YYYY-WW/`（ISO 周）+ 根级 `MEMORY.md`、`/workspace/ideas/SCOREBOARD.md`。
2. **创建 9 个 Bot**：可直接 fork 文中 x.ai 公开模板，或把文内英指令粘成各 Bot 系统提示（见下「能力表」）。
3. **统一共享规则**（每个 Bot 开头相同）：只写 loop 目录；读 HANDOFF 再动手；事实带链接、推断要标注；未经你批准不外发/购买/删除。
4. **周一跑 Scout** → `trending.md`；并行 **Pain Miner**（`feedback.csv`+`pain.md`）与 **Competitor Mapper**（`competitors.md`）。
5. **Strategy Lead** 出 `strategy.md`（蓝海 / Zero to One / 7 Powers）；**CEO** 做 GO/HOLD/KILL + 记分板（完整粘贴指令原文缺失，先用模板 Bot + 文内「董事会」提示包）。
6. **（可选）Behavior Reverser**：仅当你**明示授权**的目标在 `target/`；接 REA MCP（`npx -y rea-agents@<钉死版本> mcp`）→ `investigation.md`；**洁净室**：建造侧只读 SPEC，不看反编译。
7. **Spec Writer** → `SPEC.md`；并行 **Builder**（`build/`+测试）与 **Video Director**（`video.md`）；**你批准**才发布。
8. **挂例行**：周一 Scout、每日投诉清扫、每日 REA/工具监视、上线+48h 复盘（文内有可粘贴 routine 提示）。

## 能力表

| 角色 | 产出文件 | 做什么 | 绝不做什么 |
|---|---|---|---|
| Scout | `trending.md`, `raw/sources.csv` | PH / GH Trending / HN / Reddit / 公域 X 扫热门 | 不发明商业模式、不分析痛点 |
| Pain Miner | `feedback.csv`, `pain.md` | 公域评论聚类痛点；频次×强度排序 | 不设计定价；不编造引用 |
| Competitor Mapper | `competitors.md` | 竞品表 + gap 矩阵 | 不登录墙后；价不明写 unknown |
| Behavior Reverser | `investigation.md` | 授权目标上用 REA 追**行为**证据 | 不倾倒专有源码；不绕 DRM/付费墙 |
| Strategy Lead | `strategy.md` | JTBD / 蓝海 ERRC / Thiel 七问 / 7 Powers / go-hold-kill | 不写生产代码 |
| CEO | 刷新 strategy + `SCOREBOARD.md` | 办公时间质询、董事会、7 日实验、杀弱 | 不写生产代码（完整指令原文缺） |
| Spec Writer | `SPEC.md` | 洁净室规格：故事、可观察行为、验收、非目标 | 不抄闭源 UI/资源原文 |
| Builder | `build/`, 测试报告 | 只按 SPEC 原创实现 | 编码时不打开 `target/` / investigation |
| Video Director | `video.md` | 30–60s 脚本/分镜/缩略图文案 | 不拍不发；不用他家 Logo/UI |

## 可复制清单

### 目录骨架

```text
/workspace/loop/week-YYYY-WW/
  HANDOFF.md
  trending.md
  feedback.csv
  pain.md
  competitors.md
  investigation.md   # 可选
  strategy.md
  SPEC.md
  build/
  video.md
/workspace/loop/MEMORY.md
/workspace/ideas/SCOREBOARD.md
```

### 交接行格式

```text
[timestamp IST] [bot] DONE -> [file] -> next: [bot]
# 卡住：
[timestamp IST] [bot] BLOCKED -> reason...
```

### 公开模板（文中原链）

| Bot | URL |
|---|---|
| Scout | https://x.ai/bot/stEZpy6WQFTBOWaOOSWAM |
| Pain Miner | https://x.ai/bot/0uLHAD8JUmBEEzIulNpju |
| Competitor Mapper | https://x.ai/bot/9FdrISzxvOd2kTaE36eon |
| Behavior Reverser | https://x.ai/bot/d1omyX9etZuAdtVMFgjUD |
| Strategy Lead | https://x.ai/bot/5enFHSkSHV9UpbFX8Ky6a |
| CEO | https://x.ai/bot/I1m1EtRVJrCwXhlEljoBH |
| Spec Writer | https://x.ai/bot/yH0hoOX2FcXhdXe8b1Huj |
| Builder | https://x.ai/bot/iCKWgIWPwg2dZe0GUlsgI |
| Video Director | https://x.ai/bot/yPkcpwD13HI-ka3PuPODS |

### 提示包（原文短触发）

```text
# 周一开球
run week [YYYY-WW]. Scout first at /workspace/loop/week-[YYYY-WW]/.
everyone else wait for HANDOFF.md.

# 授权 REA（必须先有授权目标）
Behavior Reverser: I own / am authorized to inspect the software at /workspace/loop/week-[YYYY-WW]/target.
feature: [feature]. produce investigation.md. behavior only. no proprietary code dumps.

# CEO 董事会
CEO: board-meeting mode on the top idea in strategy.md.
live research on. cite sources. end with GO/HOLD/KILL and a 7-day pass/fail experiment.

# 洁净室建造
Builder: you only get SPEC.md. do not open target/ or investigation.md.
build under build/. tests for every acceptance item.
```

### REA 在 Grok Bot 上（原文要点）

- 项目：https://github.com/morluto/rea （MIT，@morluto）；npm：`rea-agents`
- Grok Bot：**setup 不会自动注册** → 在云电脑上加自定义 MCP，名建议 `rea`：  
  `npx -y rea-agents@<你钉死测过的版本> mcp`
- 练习包：https://rea.tools/examples/notes-example.zip（追导出按钮）
- 合法轨道：只分析你拥有/被授权的软件；描述行为与证据路径；禁 DRM/许可绕过、禁凭据爆破、禁服务端入侵

## 坑与边界

- **单 Bot 塞所有事**会被搞混——本文主张窄职责 + 书面交接，这是主论点。
- **Scout 指令在原文截断**（止于 `note it under`）；落地需自行补全「Gaps」段落或改用公开 Scout 模板。
- **CEO 完整粘贴指令原文没有**——只有 gstack 理念（github.com/garrytan/gstack）与差异点；请用 x.ai 模板 Bot，勿假装文内有全量 system prompt。
- **8 个可选插件「即将推出」**：正文未给名单，不要当已交付。
- **逆向 ≠ 复制**：洁净室（调查 → 新上下文写 SPEC → Builder 永不看反编译）；不抄专有代码/资源/商标/逐字 UI；尊重各站 ToS；外联草稿等你批准。
- **REA 看不见纯服务端逻辑**；原生二进制还要合法 Ghidra/Hopper/IDA；星标≠好重建。
- **分销仍靠你**；战略/CEO 可能错，最终 GO/KILL 是人的决策。
- 文中时间混用 IST / EST 表述，挂 routine 时自己统一时区。
- 中文叙述机翻腔明显；**可执行部分以英文指令块为准**。

## 适合谁

- 已在用（或准备用）Grok Bot / 多 Agent，想把「找题→杀弱→规格→上线」流程化的人。
- 愿意维护共享文件夹与 HANDOFF 纪律、接受「人只做决策门」的人。
- 对竞品行为做**授权范围内**洁净室规格、而非 clone 抄袭的人。

不适合：想要一个万能单 Bot、或指望本文直接给出可商用抄袭竞品路径的人——原文明确反对复制专有资产。

## 章节导航（对应原文）

1. 简介：为何小队 > 超级机器人；REA 热度背景  
2. 第一部分：交接目录、周循环图、合法轨道与洁净室  
3. 第二部分：9 个公开模板链接  
4. 第三–四部分：Scout / Pain Miner / Competitor Mapper / Behavior Reverser（含 REA）  
5. 第五部分：Strategy Lead + CEO 理念（CEO 指令缺）  
6. 第六部分：Spec Writer / Builder / Video Director  
7. 第七部分：可调度例行（周一扫、日监视、日投诉、+48h 复盘）  
8. 第八部分：交接协议、限制、提示包  

完整英指令与中文叙述见同目录 `transcript.md`。
