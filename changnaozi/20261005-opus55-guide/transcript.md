# 用好 Opus 5.5：整包交任务、管住长跑、先读「等你拍板」

---
source_url: https://claude.dev/blog/getting-the-most-out-of-opus-5-5/
original_title: Getting the most out of Opus 5.5 in Claude and Claude Code
publisher: claude.dev Blog (Anthropic)
author: Addy Osmani
published: 2026-09-22
word_count: ~2391 (英文正文；页面标注 9 min / 09m 09s)
note: 下文先附完整英文原文，再附忠实中文翻译/校对稿；文中提示词与代码块保持英文原文 verbatim。
---

## English original（完整原文）

# Getting the most out of Opus 5.5 in Claude and Claude Code

How to prompt Opus 5.5, steer a long run, and check your results in Claude apps and Claude Code.

AUTHOR: Addy Osmani  
PUBLISHED: Sep 22, 2026  
READ TIME: 9 min

Opus 5.5 works well with the way you already use Claude. A few things behave differently, though: it works for longer on its own, it tells you plainly what it did, and it thinks before every reply. This guide covers how to work with Opus 5.5 in Claude apps and Claude Code, including how to prompt the model, steer a long run, and check your results.

## TRY THIS FIRST

Three things to try in your first session with Opus 5.5

1. Hand over the whole task. Say what "done" looks like and when you want it to stop and ask. Then let it work.
2. Delete "think carefully" lines. Opus 5.5 already thinks before every reply.
3. When a long run ends, read what it needs from you first.

### Say what "done" looks like, then let it run

**What to do.** Give the whole task in one message. Name the finish line, like "the tests pass" or "every endpoint is migrated." Then let it cook.

**Why it matters on Opus 5.5.** Opus 5.5 keeps going on long, multi-part work better than Opus 5 did. Compared to prior Opus models, its biggest gains are on multi-step work, like carrying a change through a large repository until the tests pass. Early testers had it run long coding tasks for hours with little oversight. With a clear finish line, it knows when it's done.

**How.** In Claude Code, for example:

```
Migrate the payment endpoints from the old client to the new one.
Done means: every endpoint uses the new client, the old client is deleted, and the test suite passes.
Stop and ask me only if a test fails for a reason you can't explain.
```

FIG A One message: the whole task, the finish line, and when to stop.

### Stop telling it to "think hard"

**What to do.** Remove "think carefully," "think step by step," and similar lines from your prompts and your saved instructions.

**Why it matters on Opus 5.5.** Opus 5.5 always thinks before it replies, and it decides how much. You don't need to ask it to think. In our testing in a chat product, removing a "think carefully" line made replies start sooner, with no clear drop in quality.

**How.** Delete the line. For a quick answer to a simple question, say so: "Answer directly." To change how much it thinks in Claude Code, change effort.

### Add to a running task

**What to do.** If you remember something mid-run, you can type a follow-up while it works.

**Why it matters on Opus 5.5.** Runs are longer now, so a restart costs more.

**How to do it.** In Claude Code, type the message and press Enter while Claude works, for example, "Also keep the old endpoint names as aliases."

### For design work, name the styles you don't want

**What to do.** When you ask for a page, an app, or an artifact, list the design habits you want left out.

**Why it matters on Opus 5.5.** With no design direction, Opus 5.5 falls back on a few default styles. A general instruction like "avoid a generic look" mostly swaps one default for another. A list of specific patterns works much better.

**How.** Name the patterns:

```
Build a personal website with placeholder content.
Don't use a cream or off-white background, italic accent words in headings, numbered "01 / 02 / 03" section labels, monospace labels, or pill-shaped buttons.
```

Then look at what it chose instead. If you don't like that either, add it to the list and ask again.

### Tell it which stops you want

**What to do.** Put a short rule in your CLAUDE.md file about when to stop and ask, and when to keep going.

**Why it matters on Opus 5.5.** Opus 5.5 keeps you posted as it works. On a long task, it sometimes stops to report instead of going on: a summary that names the next step without taking it, an offer to continue, or a list of choices that don't block the work. It follows instructions that name these stops. Name the stops you want, too.

**How.** Add this to CLAUDE.md, and edit it to fit your project:

```
When a step doesn't need my input, keep going. Put status notes in the same message as your next action.
Stop and ask only when you can't continue without me, or before anything destructive: deleting data, force-pushing, or changing anything outside this repository.
```

FIG B The CLAUDE.md rule: when to keep going, and when to stop and ask.

If a run stops with "Want me to continue?" reply "continue." If that happens often, the rule above will help.

A rule to keep going means fewer stops, so keep your own check before anything risky or hard to undo. The last line of the rule above does that. Keep permission prompts on for destructive commands too.

For pair programming, you may want the opposite: a one-line plan before it starts and a short recap at the end. Say that in your CLAUDE.md instead. Opus 5.5 follows either one.

### Ask it to split big work across subagents

**What to do.** For an audit, a migration, or a review across a large codebase, ask Opus 5.5 to split the work across subagents and check each result.

**Why it matters on Opus 5.5.** Early testers had Opus 5.5 coordinate parallel subagents on long audits and migrations, with little oversight.

```
Audit every service in services/ for the retry bug in the linked issue.
Give each service to its own subagent. When a subagent reports back, check its evidence before you accept it.
Finish with one table: service, affected yes or no, and the evidence.
```

FIG C Fan out to subagents, check each one's evidence, then finish with one table.

### Keep the task list in a file

**What to do.** For a run that will take a while, ask Opus 5.5 to keep its task list in a file and update it as it goes. Then read the file, not the scrollback, to see where the run is.

**Why it matters on Opus 5.5.** Runs are longer now. A long run fills the context window, and Claude Code then summarizes older turns. A list in a file survives that, and it shows you at a glance what's done and what's left.

**How.** "Keep a checklist in TASKS.md. Tick each item when it's done, and add anything new you find."

### Read what it needs from you first

**What to do.** When a long run ends, look first for anything Claude is waiting on you for, like a decision it left open or a change it wants you to approve. Then read the rest of Claude's summary.

**Why it matters on Opus 5.5.** Opus 5.5 reports on its work more clearly than Opus 5. Its updates and its final summary say what it did, what it found, and what it needs from you, in plain language.

**How.** To change the summary's format, say so in CLAUDE.md, for example, "End every run with three headings: Blocked on me, Changed, Found."

### Ask it to review the code

**What to do.** Ask Opus 5.5 to review a diff or a pull request before a person does.

**Why it matters on Opus 5.5.** One early tester said Opus 5.5 at its lowest effort caught more bugs than Opus 5 at high effort, with fewer false alarms. It also explains its changes in plain language, so its pull request descriptions are easier to review.

**How.** Feed this prompt to Claude:

```
Review the diff on this branch against main.
List only problems you'd block the merge for. For each one, give the file and line, why it's wrong, and how to show it fails.
```

### Ask it to mark what it couldn't confirm

**What to do.** For research and analysis, ask it to say what it couldn't find or couldn't check.

**Why it matters on Opus 5.5.** "I couldn't find this" is worth reading, and asking for it makes it easy to find.

**How.** Add "Mark anything you couldn't confirm, and say where you looked" to the request. This works in a Claude research report and in Claude Code.

## 4. IN CLAUDE APPS

First, check that the model picker says Opus 5.5.

### Share the chart or screenshot itself

**What to do.** Attach the chart, diagram, screenshot, or slide. Don't retype the numbers.

**Why it matters on Opus 5.5.** Opus 5.5 reads charts, diagrams, and screenshots more accurately than Opus 5, and it needs no extra steps to do it. It's also better at meaning that depends on where things are in the image: which boxes an arrow connects, what changed between two versions of a diagram, or when a meeting starts and ends in a calendar screenshot.

**How.** Attach the image and ask a specific question: "Which of these services call the billing API directly?"

### Ask it to check a long document

**What to do.** Give it a long plan, report, or deck, and ask it to find mistakes.

**Why it matters on Opus 5.5.** Opus 5.5 pays more attention to detail than prior Opus models. In our testing, it caught a date that fell on the wrong weekday in a long planning thread, and a chart that didn't match the numbers in a deck.

**How.** Submit the prompt: "Check this deck for anything that contradicts itself: numbers, dates and names. Quote each problem and say where it is."

### Ask for the finished file

**What to do.** When you want a spreadsheet or a document, ask for the file, not an outline.

**Why it matters on Opus 5.5.** The spreadsheets and documents Opus 5.5 makes need less editing than Opus 5's before you share them.

**How.** "Make this a spreadsheet I can share: one row per vendor, with columns for cost, contract end date and owner."

### In a project, say when answers are settled

**What to do.** If follow-up questions in a long chat feel slow, add an instruction that earlier answers are settled.

**Why it matters on Opus 5.5.** In a long chat, Opus 5.5 sometimes goes back over an earlier answer while it thinks about a short follow-up. That slows the reply.

**How.** Add this to the project's instructions:

```
Once you have answered something, treat that answer as done. Focus on what I'm asking now, and don't go back over an earlier answer unless I ask about it or point out a problem with it.
```

Leave it out of projects for long analysis, where a later step can show a mistake in an earlier one.

## 5. WHEN A MESSAGE IS FLAGGED

Opus 5.5 is the first Opus model to launch with Fable-level bio and cyber safeguards. In Claude apps and Claude Code, most flagged messages move to an older model, and your work goes on there. Finding security vulnerabilities in source code is allowed, and everyday health and educational questions should still work. These safeguards can sometimes flag legitimate work, and we're tuning them to cut down on incorrect flags. If you're switched, here's what you'll see and what to do.

### In Claude apps

**What you see.** A notice that starts with "Switched to" and the name of an older model. Claude answers on that model, and the chat stays on it.

**What to do.**

- To go back to Opus 5.5, choose it in the model picker. If the earlier message is still in the chat, it may be flagged again. Starting a new chat avoids that.
- To be asked first, go to Settings, then Capabilities, and turn off "Switch models when a message is flagged." You'll see a "paused" card with your options.

The check covers everything in the conversation, including files and search results. So a flag can come from earlier content, not only your last message.

### In Claude Code

**What you see.** A notice that names the older model. The session continues on that model.

**What to do.**

- Run /model to switch back.
- Press Esc twice to edit your last message and try again.
- To be asked first, run /config and change "Switch models when a message is flagged."
- Run /feedback if the flag was wrong.

### Don't ask it to show its reasoning in the reply

**What to do.** Remove requests to reproduce its internal reasoning in the reply from your prompts and instructions.

**Why it matters on Opus 5.5.** A request to reproduce its internal reasoning in the reply can be declined. It's one of the flag categories.

**How.** Ask Claude for what you need instead, for example, "Explain why you chose this approach in three sentences."

### Turn on fast mode when you're waiting on each reply

**What to do.** In Claude Code, use fast mode for back-and-forth work, where you read each reply before you send the next message.

**Why it matters on Opus 5.5.** Fast mode is available for Opus 5.5 at launch as a research preview. You get the same model, and the text arrives sooner. It needs extra usage turned on, and it costs more per token than standard mode.

**How.** Type /fast into Claude.

## YOUR OPUS 5.5 CHECKLIST

Run through this before your next long task.

FIG D The checklist at a glance.

**Asking**

- The task says what "done" looks like
- No "think hard" lines in prompts or saved instructions
- Design requests list the styles to leave out
- Charts and screenshots are attached, not retyped

**Long runs in Claude Code**

- CLAUDE.md says when to stop and when to keep going, and to stop before anything destructive
- Permission prompts are still on for destructive commands
- Large audits and migrations are split across subagents
- The task list is kept in a file

**Checking**

- The "needs from you" part of the report is read first
- A review pass runs before a person reviews
- Research answers mark what couldn't be confirmed

**Flags**

- You know how to switch back: the model picker, or /model
- "Switch models when a message is flagged" is set the way you want

Start building with Opus 5.5!

With thanks to Molly Vorwerck for reviewing.

## 中文全文翻译 / 校对稿

Opus 5.5 大体上仍兼容你现有的 Claude 用法。不过有几处不一样：它能更长时间自主推进，会用白话说清自己做了什么，而且每次回复前都会先思考。本指南讲如何在 Claude 应用与 Claude Code 里用好 Opus 5.5：怎么提示模型、怎么引导长跑，以及怎么验收结果。

## 先试这三步

第一次用 Opus 5.5 时，建议先试这三件事：

1. **整包交任务。** 说清「完成」长什么样、什么时候该停下来问你。然后让它干活。
2. **删掉「认真想」类句子。** Opus 5.5 每次回复前本来就会思考。
3. **长跑结束后，先读它需要你做什么。**

### 说清「完成」长什么样，然后让它跑

**怎么做。** 用一条消息给出整项任务。点名终点线，例如「测试通过」或「每个端点都迁完」。然后让它去做。

**为什么对 Opus 5.5 重要。** Opus 5.5 在长、多段工作上比 Opus 5 更能持续推进。相对以前的 Opus，它最大的提升在多步工作上，例如在大型仓库里把一项改动一路做到测试通过。早期测试者让它在几乎无人盯梢的情况下跑数小时的编程任务。有了清晰终点，它就知道何时算完。

**怎么写。** 在 Claude Code 里例如：

```
Migrate the payment endpoints from the old client to the new one.
Done means: every endpoint uses the new client, the old client is deleted, and the test suite passes.
Stop and ask me only if a test fails for a reason you can't explain.
```

图 A 一条消息：整项任务、终点线、以及何时停下来问人。

### 别再催它「用力想」

**怎么做。** 从提示词和已保存指令里删掉 “think carefully”“think step by step” 以及类似句子。

**为什么对 Opus 5.5 重要。** Opus 5.5 每次回复前都会思考，并且自己决定想多少。你不必再要求它思考。在聊天产品测试中，去掉 “think carefully” 后回复更快开始，质量未见明显下降。

**怎么写。** 删掉那一行即可。若只要简单问题的快速回答，直接说：“Answer directly.” 若要改 Claude Code 里的思考量，去改 effort。

### 给正在跑的任务加补充

**怎么做。** 若中途想起什么，可以在它工作时打一条跟进消息。

**为什么对 Opus 5.5 重要。** 现在单次跑得更久，重启代价更高。

**怎么操作。** 在 Claude Code 里一边工作一边输入并回车，例如：“Also keep the old endpoint names as aliases.”

### 做设计时，点名你不想要的风格

**怎么做。** 要页面、应用或 artifact 时，列出你希望排除的设计习惯。

**为什么对 Opus 5.5 重要。** 没有设计方向时，Opus 5.5 会落到几种默认风格。“避免通用感”这类笼统指令多半只是换一套默认。列出具体模式效果好得多。

**怎么写。** 点名模式：

```
Build a personal website with placeholder content.
Don't use a cream or off-white background, italic accent words in headings, numbered "01 / 02 / 03" section labels, monospace labels, or pill-shaped buttons.
```

再看它换了什么。若仍不满意，把新的也加进列表再问一次。

### 告诉它你要哪些停顿

**怎么做。** 在 CLAUDE.md 里写一条短规则：何时停下来问、何时继续。

**为什么对 Opus 5.5 重要。** Opus 5.5 工作时会持续通报进度。长任务中它有时会停下来汇报而不是继续：只点名下一步却不执行的摘要、问要不要继续、或列出并不阻塞工作的选项。它会遵守点名这些停顿的指令。你也要把想要的停顿写清楚。

**怎么写。** 把下面加进 CLAUDE.md，并按项目改写：

```
When a step doesn't need my input, keep going. Put status notes in the same message as your next action.
Stop and ask only when you can't continue without me, or before anything destructive: deleting data, force-pushing, or changing anything outside this repository.
```

图 B CLAUDE.md 规则：何时继续、何时停下来问。

若跑到一半出现 “Want me to continue?”，回复 “continue.” 若经常这样，上面那条规则会有帮助。

「继续推进」规则意味着停顿更少，所以在有风险或难撤销的操作前，仍要保留你自己的把关。上面规则的最后一行就是干这个的。破坏性命令的权限提示也请保持开启。

结对编程时你可能想要反过来：开工前一行计划、结束时短复盘。那就在 CLAUDE.md 里那样写。Opus 5.5 两种都能跟。

### 让它把大活拆给子代理

**怎么做。** 对大代码库的审计、迁移或评审，让 Opus 5.5 拆到多个子代理并核对各结果。

**为什么对 Opus 5.5 重要。** 早期测试者看到 Opus 5.5 能协调并行子代理做长审计与迁移，几乎不用人盯。

```
Audit every service in services/ for the retry bug in the linked issue.
Give each service to its own subagent. When a subagent reports back, check its evidence before you accept it.
Finish with one table: service, affected yes or no, and the evidence.
```

图 C 扇出到子代理，核对各自证据，最后汇总成一张表。

### 把任务清单放进文件

**怎么做。** 对会跑一阵子的任务，让 Opus 5.5 把任务清单写进文件并边做边更新。然后读文件、而不是翻聊天记录，看进度。

**为什么对 Opus 5.5 重要。** 现在跑得更久。长跑会填满上下文窗口，Claude Code 随后会摘要更早的轮次。文件里的清单能熬过摘要，一眼看出完成了什么、还剩什么。

**怎么写。** “Keep a checklist in TASKS.md. Tick each item when it's done, and add anything new you find.”

### 先读它需要你做什么

**怎么做。** 长跑结束时，先找 Claude 在等你的事：留下的决策、希望你批准的改动。再读摘要其余部分。

**为什么对 Opus 5.5 重要。** Opus 5.5 比 Opus 5 更清楚地汇报工作。进度更新与最终摘要会用白话说明做了什么、发现了什么、需要你做什么。

**怎么写。** 若要改摘要格式，在 CLAUDE.md 里写明，例如：“End every run with three headings: Blocked on me, Changed, Found.”

### 先让它审代码

**怎么做。** 在人审之前，先让 Opus 5.5 审 diff 或 PR。

**为什么对 Opus 5.5 重要。** 一位早期测试者说：Opus 5.5 在最低 effort 下抓到的 bug 比 Opus 5 高 effort 还多，误报更少。它也会用白话解释改动，PR 描述更好审。

**怎么写。** 把下面提示喂给 Claude：

```
Review the diff on this branch against main.
List only problems you'd block the merge for. For each one, give the file and line, why it's wrong, and how to show it fails.
```

### 让它标出无法确认的部分

**怎么做。** 做研究与分析时，让它说明找不到或没核对到的内容。

**为什么对 Opus 5.5 重要。** 「我找不到这个」值得读，主动要求它会更容易被看见。

**怎么写。** 在请求里加上 “Mark anything you couldn't confirm, and say where you looked”。这对 Claude 研究报告与 Claude Code 都适用。

## 4. 在 Claude 应用里

先确认模型选择器显示的是 Opus 5.5。

### 直接附上图表或截图

**怎么做。** 附上图表、示意图、截图或幻灯片。不要把数字再打一遍。

**为什么对 Opus 5.5 重要。** Opus 5.5 读图表、示意图和截图比 Opus 5 更准，且无需额外步骤。它也更擅长依赖空间位置的含义：箭头连了哪些框、两版示意图差在哪、日历截图里会议起止时间。

**怎么写。** 附上图片并问具体问题：“Which of these services call the billing API directly?”

### 让它检查长文档

**怎么做。** 给一份长计划、报告或幻灯片，让它找错误。

**为什么对 Opus 5.5 重要。** Opus 5.5 比前代 Opus 更注意细节。测试中它抓到过长规划线程里落在错误星期的日期，以及幻灯片里与数字不符的图表。

**怎么写。** 提交：“Check this deck for anything that contradicts itself: numbers, dates and names. Quote each problem and say where it is.”

### 直接要成品文件

**怎么做。** 想要电子表格或文档时，直接要文件，不要只要大纲。

**为什么对 Opus 5.5 重要。** Opus 5.5 做出的表格与文档，分享前需要改的地方比 Opus 5 更少。

**怎么写。** “Make this a spreadsheet I can share: one row per vendor, with columns for cost, contract end date and owner.”

### 在项目里写明「先前结论已定」

**怎么做。** 若长对话里后续问题变慢，加一条指令：先前答案视为已定。

**为什么对 Opus 5.5 重要。** 在长聊天里，Opus 5.5 有时会在想短跟进时回头翻看更早的答案，拖慢回复。

**怎么写。** 加到项目指令：

```
Once you have answered something, treat that answer as done. Focus on what I'm asking now, and don't go back over an earlier answer unless I ask about it or point out a problem with it.
```

长分析类项目可不用这条——后面步骤有时会暴露前面的错误。

## 5. 消息被标记时

Opus 5.5 是首个以 Fable 级生物与网络安全护栏上线的 Opus。在 Claude 应用与 Claude Code 中，多数被标记的消息会切到更旧的模型，工作在那里继续。在源码中找安全漏洞是允许的，日常健康与教育类问题一般仍可用。这些护栏有时会误伤正当工作，团队也在调优以减少误标。若被切换，你会看到什么、该怎么做如下。

### 在 Claude 应用里

**你会看到。** 以 “Switched to” 开头、并带上旧模型名的提示。Claude 在该模型上回答，且聊天会留在该模型。

**怎么做。**

- 要回到 Opus 5.5，在模型选择器里选它。若先前那条消息仍在聊天里，可能再次被标记。新开聊天可避免。
- 想先被询问：到 Settings → Capabilities，关掉 “Switch models when a message is flagged.” 你会看到带选项的 “paused” 卡片。

检查覆盖整段对话，包括文件与搜索结果。因此标记可能来自更早内容，不只是最后一条消息。

### 在 Claude Code 里

**你会看到。** 点名旧模型的提示。会话在该模型上继续。

**怎么做。**

- 运行 `/model` 切回。
- 按两次 Esc 编辑上一条消息再试。
- 想先被询问：运行 `/config`，改 “Switch models when a message is flagged.”
- 若标记有误，运行 `/feedback`。

### 别要求它在回复里展示内部推理

**怎么做。** 从提示词与指令里去掉「在回复中复现内部推理」一类请求。

**为什么对 Opus 5.5 重要。** 要求在回复里复现内部推理可能被拒绝，这是标记类别之一。

**怎么写。** 改问你真正需要的，例如：“Explain why you chose this approach in three sentences.”

### 来回等回复时打开 fast mode

**怎么做。** 在 Claude Code 里，对「每条都要读完再发下一条」的来回工作使用 fast mode。

**为什么对 Opus 5.5 重要。** Opus 5.5 上线即提供 fast mode（研究预览）。同一模型，文本更快到达。需要打开额外用量，且按 token 比标准模式更贵。

**怎么操作。** 在 Claude 里输入 `/fast`。

## 你的 Opus 5.5 清单

下次长任务前过一遍。

图 D 清单一览。

**提问**

- 任务写清了「完成」长什么样
- 提示词与已保存指令里没有 “think hard” 类句子
- 设计请求列出了要排除的风格
- 图表与截图是附上的，不是重打的

**Claude Code 长跑**

- CLAUDE.md 写明何时停、何时继续，以及破坏性操作前要停
- 破坏性命令的权限提示仍开启
- 大型审计与迁移拆到子代理
- 任务清单保存在文件里

**验收**

- 先读报告里「需要你」的部分
- 人审之前先跑一轮评审
- 研究类回答标出无法确认之处

**标记**

- 知道如何切回：模型选择器，或 `/model`
- “Switch models when a message is flagged” 按你想要的方式设置

开始用 Opus 5.5 构建吧！

感谢 Molly Vorwerck 审阅。
