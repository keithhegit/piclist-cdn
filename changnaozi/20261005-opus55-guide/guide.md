# 用好 Opus 5.5：整包交任务、管住长跑、先读「等你拍板」

## 一句话定位

官方上手指南：用「整包任务 + 清晰终点 + CLAUDE.md 停顿规则」发挥 Opus 5.5 的长跑与白话汇报能力，并避开「催思考 / 误伤护栏 / 忽略待你拍板」等坑。

## 上手顺序

1. 模型选择器确认 **Opus 5.5**。
2. 第一条消息写清：**整项任务 + Done means… + 何时停下来问你**；然后放手让它跑。
3. 清掉提示词 / 已保存指令里的 **“think carefully / think step by step”**；要快答就说 “Answer directly.”；要改思考量就改 **effort**。
4. 在 **CLAUDE.md** 写停顿规则：能继续就继续；只在缺你输入或破坏性操作前停；**破坏性权限提示保持开**。
5. 长跑：任务清单写进 **TASKS.md**；大审计/迁移 **扇出子代理并核对证据**；中途可直接打跟进消息，不必重启。
6. 跑完先读 **Blocked on me / 等你拍板**，再读 Changed / Found；人审前先让它审 diff。
7. 被护栏切到旧模型时：应用里用选择器或新开聊；Code 里 `/model` / Esc×2 / `/config` / `/feedback`。来回对话可 `/fast`（更贵）。

## 能力 / 设置表

| 项 | 建议 |
|---|---|
| 默认用法变化 | 更长自主、白话汇报、每次先思考 |
| 提示词 | 整包任务 + 终点；删「用力想」；设计列黑名单风格 |
| effort | 用 effort 调思考量，勿靠 “think hard” |
| CLAUDE.md 停顿 | 无输入则继续；破坏性操作前必问 |
| 权限提示 | 破坏性命令保持开启 |
| 长跑状态 | `TASKS.md` 清单，抗上下文摘要 |
| 大范围活 | 子代理并行 + 主代理核对证据 + 汇总表 |
| 验收 | 先读「需要你」；可要求 Blocked on me / Changed / Found |
| 代码审 | 人审前先让 Opus 5.5 审；可低 effort 仍很强 |
| 研究 | 要求 mark 无法确认 + 查了哪里 |
| Claude Apps | 直接附图；要成品文件；长项目可「先前结论已定」 |
| 护栏 | Fable 级 bio/cyber；误标可切回；勿要「展示内部推理」 |
| Fast mode | `/fast`，研究预览，同模型更快、更贵 |

## 可复制提示词 / 配置（verbatim）

**整包迁移任务**

```
Migrate the payment endpoints from the old client to the new one.
Done means: every endpoint uses the new client, the old client is deleted, and the test suite passes.
Stop and ask me only if a test fails for a reason you can't explain.
```

**设计黑名单**

```
Build a personal website with placeholder content.
Don't use a cream or off-white background, italic accent words in headings, numbered "01 / 02 / 03" section labels, monospace labels, or pill-shaped buttons.
```

**CLAUDE.md 停顿规则**

```
When a step doesn't need my input, keep going. Put status notes in the same message as your next action.
Stop and ask only when you can't continue without me, or before anything destructive: deleting data, force-pushing, or changing anything outside this repository.
```

**子代理审计**

```
Audit every service in services/ for the retry bug in the linked issue.
Give each service to its own subagent. When a subagent reports back, check its evidence before you accept it.
Finish with one table: service, affected yes or no, and the evidence.
```

**任务清单**

```
Keep a checklist in TASKS.md. Tick each item when it's done, and add anything new you find.
```

**摘要格式（示例）**

```
End every run with three headings: Blocked on me, Changed, Found.
```

**合并前审 diff**

```
Review the diff on this branch against main.
List only problems you'd block the merge for. For each one, give the file and line, why it's wrong, and how to show it fails.
```

**研究不确定项**

```
Mark anything you couldn't confirm, and say where you looked
```

**长文档自检**

```
Check this deck for anything that contradicts itself: numbers, dates and names. Quote each problem and say where it is.
```

**要成品表**

```
Make this a spreadsheet I can share: one row per vendor, with columns for cost, contract end date and owner.
```

**项目指令：先前结论已定**

```
Once you have answered something, treat that answer as done. Focus on what I'm asking now, and don't go back over an earlier answer unless I ask about it or point out a problem with it.
```

**解释做法（代替「展示内部推理」）**

```
Explain why you chose this approach in three sentences.
```

## 坑

- 仍写 “think carefully / think step by step” → 拖慢开答，无益质量。
- 只说「别太通用」做设计 → 换一套默认风；要列具体反模式。
- 没写停顿规则 → 常问 “Want me to continue?”；写了「继续」却关破坏性权限提示 → 风险。
- 只靠滚动聊天看长跑进度 → 上下文被摘要后丢失；用 `TASKS.md`。
- 跑完先读长摘要、漏掉「等你拍板」→ 卡住的决策被淹没。
- 要求在回复里复现内部推理 → 可能触发护栏/被拒。
- 被切到旧模型后不切回 / 同会话重试旧触发内容 → 反复标记；新开聊或 `/model`。
- 长分析项目误加「先前结论已定」→ 可能掩盖前面错误。
- `/fast` 当默认 → 更贵；适合逐条等回复的来回，不适合纯成本敏感长跑。

## 适合谁

- 用 Claude Code 做仓库级迁移、审计、多小时自主编程的人。
- 想用 CLAUDE.md / 子代理 / 任务文件管长跑的团队。
- 在 Claude 应用里做图表阅读、长文档校对、要可分享成品文件的知识工作者。
- 需要在 Fable 级护栏下知道如何切回、反馈误标的用户。

## 章节导航

| 区块 | 内容 |
|---|---|
| TRY THIS FIRST | 整包任务、删催思考、先读待办 |
| 提示与设计 | 中途加指令、设计黑名单 |
| 长跑管控 | CLAUDE.md 停顿、子代理、TASKS.md |
| 验收 | 先读需要你、审 diff、标未确认 |
| IN CLAUDE APPS | 附图、查长文、要文件、结论已定 |
| WHEN FLAGGED | 应用/Code 切回、勿展推理、`/fast` |
| CHECKLIST | Asking / Long runs / Checking / Flags |

来源：https://claude.dev/blog/getting-the-most-out-of-opus-5-5/ （Addy Osmani，2026-09-22，9 min）
