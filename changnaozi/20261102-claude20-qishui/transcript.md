# Claude桌面端11项更新上手 - 汽水音乐

> **校对版逐字稿**（字幕对齐为主 + 英文口播 ASR 对照）
>
> - 平台分享：汽水音乐 / 抖音音乐 UGC（账号：**马丁没有早晨**）
> - 短链：https://qishui.douyin.com/s/iXvHDVtF/
> - 正式页：https://music.douyin.com/qishui/share/ugc_video?ugc_video_id=7701726085041360178
> - 作品 id：`7701726085041360178`
> - 时长：999.4s ≈ **16:39**
> - 成片口播语言：**英语**；画面硬字幕：**中英双语**（中文为译制硬字幕）
> - 同源原片（账号剪辑所据）：Jay E / RoboNuggets《Use Claude 2.0 better than 99% of people (11 BIG Updates)》，YouTube `yMnFHFf43Qg`（约 17:06；本箱 yt-dlp 需登录，未下到原片音轨，口播以汽水成片为准）
> - 「Claude 2.0」：**非** Anthropic 官方产品名；来自 Anthropic 工程师 Thariq 2026-10-14 前后把 Claude Code Desktop 形容为 almost like a v2，作者沿用
> - 逐字稿方法：成片硬字幕带 OCR（RapidOCR，fps=1/3 底栏裁切）→ 人工轻校专名/明显 OCR 错；英文口播 faster-whisper large-v3 `language=en`（HE-AAC 64kbps，前 ~2 分钟偶有糊字，中后段可读）
> - **口径区分**：下文「账号」= Jay / 汽水转载口径；「官方」= Anthropic 文档/博文。旁支对话是否持久保存等点，账号与官方不一致处已在攻略标注
> - ASR 工具：faster-whisper large-v3 int8 CPU；校对时：Asia/Shanghai 2026-11-02

---

## 中文硬字幕对齐稿（成片字幕）


### 片头与Claude 2.0总览

[00:00] Claude 刚被 Anthropic 彻底翻新
[00:03] 他们还加了几个新功能
[00:06] 甚至还有一些隐藏玩法
[00:09] 让桌面端变成完全不同的体验
[00:12] 于是他们一位负责工程师把它叫Claude 2.0
[00:15] 你现在可以用一个主会话
[00:18] 可以加和做真正改变Claude工作方式的mods
[00:21] 可以加和做真正改变 Claude工作方式的mods
[00:24] 你正在用的软件的东西
[00:27] 比如 Google Docs 甚至一些视频剪辑工具
[00:30] 比如这条片子里的动画
[00:33] 所以今天我会带你看他们最重要的11个更新
[00:36] 让你也能用 Claude 2.0多做点事
[00:39] 把它现在能做的全用上
[00:42] 如果你是新来的我叫Jay
[00:45] 读数据科学硕士时就进了AI
[00:48] 现在在一个全球最大的AI社区之一
[00:51] 带我们的AI业务
[00:54] 打开新版Claude桌面端只剩chat和code
[00:57] 因为上个月起Cowork被并进了 chat
[01:00] 想用尽 Claude 就得用 Claude Code
[01:03] 因为 Claude Code 明显是 Anthropic
[01:06] 更新最好也最多的地方
[01:09] 他们知道这是自己的明星产品
[01:12] 如果你是新来的别被code这个词吓到
[01:15] 它其实是个误称
[01:18] 因为你本来就是用大白话去提示和指挥 Claude
[01:21] 所以你不必变成开发者才能用 Claude Code
[01:24] 直接切到那个标签页
[01:27] 我们也从那里的最新更新开始也就是界面部分

### ① 会话栏 Session rail

[01:30] 界面里最大的一项是他们说的会话栏
[01:33] 就是窗口右侧这块面板
[01:36] 如果没看到
[01:39] 点右上角的
[01:42] 告诉你这个会话里正在发生什么
[01:48] 环境卡片显示这个对话在哪个文件夹里工作
[01:51] 以及它跑在你电脑上还是云端
[01:54] 里面有个很好用的开关就是这个远程控制按钮
[01:57] 打开它你就能在手机上接着这个会话往下做
[02:03] 所以你可以在电脑前开个头出门时再看进度
[02:06] 小技巧： Claude Code 设置里可开启新会话自动连远程控制
[02:12] 这样每个对话都会自动为手机准备好
[02:15] 不用每次手动开
[02:18] 还能开启电脑保持唤醒别让任务做到一半睡过去
[02:24] 再往下是上下文卡片
[02:27] 把上下文想成Claude在这个对话里的工作记忆
[02:30] 卡片告诉你它有多满以及是什么占了空间
[02:33] 因为 Claude 最新的模型有
[02:36] 100万token上下文窗口换算一下
[02:39] 大约相当于四本《哈利 波特》并排摆着
[02:42] 除了你的消息也就是你的提示词
[02:45] skills和MCP连接器 你还能看到记忆文件，
[02:48] 以及它们已经占了你对话多少空间
[02:51] 这点很重要因为它们会在你第一条
[02:54] 提示词时就吃掉额度
[02:57] 因为每次开新对话它们都会被预加载
[03:00] 你能看出它们是不是变得太长可能需要清理
[03:03] 清理可以直接用屏幕上这条提示词开头
[03:06] 你还会在这里看到连接器
[03:09] 也就是你接进Claude的应用
[03:12] 列出这个对话产出的每个文件

### ② 侧栏分区 Sections

[03:15] 现在可以在左侧栏把它们分进分区
[03:18] 有点像文件夹
[03:21] 点任意对话旁边的三个点
[03:30] 这样不用在50个对话里翻找，
[03:33] 你可以一个项目+m个客户
[03:36] 或一块业务一个分区
[03:39] 和这个相关的一个很棒的功能叫嵌套会话
[03:42] 会话就是你侧栏里的一个对话对吧？
[03:45] 但现在一个会话可以自己开会话
[03:48] 那些子会话就排在它下面
[03:54] 每个子会话做完都会向开启它的主会话汇报

### ③ 嵌套会话 Nested sessions

[03:57] 想试这个新功能
[04:00] 再让它每件都开一个嵌套会话
[04:06] 你可以让一个主会话为销售页开一个子会话
[04:09] 为邮件开一个
[04:12] 再做一个做广告
[04:15] 这里要把它和 sub-agents S区分开
[04:18] 如果你是新来的
[04:21] sub-agents 就是会话派出去干一件事的帮手
[04:24] 它们仍然有用但 sub-agent 更像一道单向指令
[04:27] 它们仍然有用 但 sub-agent 更像一道单向指令
[04:30] 主会话给它一条提示词你拿回一个结果
[04:33] 但没法像嵌套会话那样跳进去跟它说话
[04:39] 因为嵌套会话每一个都是你侧栏里真实的对话
[04:42] 你可以点进去看它做了什么
[04:45] 还能直接接着用
[04:48] 比如你想更直接地指挥做广告的那个会话
[04:51] 跳进那个对话去改就行
[04:54] 另外还有个大多数人还不知道的技巧：
[04:57] 在ClaudeCode里
[05:00] 一个会话能看到你的其他会话
[05:03] 这就带来了主会话这个概念
[05:06] 如果你不想在侧栏
[05:09] 10个 12个对话之间来回跳就挑一个会话

### ④ 主会话 Master session

[05:12] 你甚至可以把它置顶让它一直可见
[05:15] 然后告诉Claude这就是你的主会话
[05:18] 设好之后有几种用法
[05:21] 比如你可以问主会话：
[05:24] 其他对话在等你拍板的关键决定有哪些
[05:27] 它就会去翻那些对话挑出真正在等你决定的
[05:30] 只在主会话里给你汇总
[05:36] 这个置顶对话就是你的私人助理
[05:39] 替你调度Claude和之前开的其他对话
[05:42] 你甚至可以让它替你开新会话
[05:45] 并从这一个主会话里控制它们
[05:48] 想收拾Claude工作区可以让它把对话分进分区
[05:54] 比如我让它给这条视频建个分区它没让我点一下就做好了
[06:00] 说明一下
[06:03] 这个功能默认能看到你最近活跃的20个会话
[06:06] 当然你也可以让Claude往前多翻
[06:09] 一个密切相关的更新是Claude Code 的项目
[06:12] 也是一个主会话替你带一整个对话团队
[06:15] 但有几个大区别
[06:18] 最大的区别是项目跑在云端
[06:21] 所以你关掉设备它们还在跑

### ⑤ Claude Code 云端项目 Projects

[06:24] 嵌套会话则跑在你的电脑上
[06:27] 所以电脑不醒着那些会话就不会跑
[06:30] 但嵌套会话能用你设备的 skills、文件和工具需要业务上下文时很有用
[06:39] Claude Code 项目当然也能用你的 skills 和文件
[06:45] 当然能手动上传但最好让Claude取来项目要的 skills和上下文趁电脑还醒着
[06:48] 当然能手动上传但最好让Claude取来项目要的 skills和上下文电脑还醒着
[06:51] 当然能手动上传但最好让Claude取来项目要的 skills和上下文趁电脑还醒着
[06:54] 当然能手动上传但最好让 Claude取来项目要的 skills和上下文趁电脑还醒着
[06:57] 注意 Claude Code 项目跑在 Anthropic 云上你传的业务文件都会进它服务器
[07:00] 注意 Claude Code项目跑在Anthropic 云上你传的业务文件都会进它服务器
[07:03] 注意 Claude Code 项目跑在Anthropic 云上你传的业务文件都会进它服务器
[07:06] 另一个区别是项目有共享的自定义记忆
[07:09] 你为整个项目设一次规则
[07:12] 之后在这个项目里开的每个对话都会沿用
[07:15] 项目里还有个概览页
[07:18] 显示哪些做完了 哪些还在跑、 哪些在等你
[07:21] 所以一个好用的判断是：
[07:24] 或者你更想本地干就用嵌套会话
[07:30] 你希望它一直 跑着
[07:33] 那就去试试ClaudeCode项目
[07:36] 要注意的是项目现在还在陆续放开
[07:39] 嵌套会话任何套餐都能用
[07:42] 但项目还在 beta 目前只有 Pro 和 Max
[07:45] 如果侧栏里没看到项目
[07:48] 先点开 通常在那里
[07:51] 你可能得用屏幕上的链接加等待名单
[07:54] PDF指南里也有
[08:03] Masterclass带你从零到精通还有Agentisasa Servic课程教你怎公变现
[08:18] 你还会加 个真正靠谱的AI创作者社群0000
[08:21] （中插：作者推广 RoboNuggets 社区，略）
[08:27] 现在回到
[08:30] 你脑子里突然冒出个问题
[08:33] 比如你想知道这个构建还要多久才完成？
[08:36] 或者你只是想记起来这个构建到底在干什么？
[08:39] 如果直接在主对话里问
[08:42] 很不建议原因很多因为你会打断工作

### ⑥ 旁支对话 Side chats

[08:45] 还会多花token
[08:48] 打开方式就是点右上角的省略号
[08:51] 或者直接打/btw
[08:54] 做完之后主对话旁边会弹出新的对话窗口
[08:57] 是它能读你整个主会话
[09:03] 所以你可以让它解释Claude 做到哪了或查一下活儿的状态
[09:06] 因为以前 /btw 只是弹出一个临时对话
[09:09] 因为以前 /btw 只是弹出 个临时对话
[09:12] 基本不保存现在你想开多少旁支对话都行
[09:15] 每个都会留着随时能回去看
[09:21] 如果你老是在左侧栏的对话之间来回点
[09:24] 分屏视图能把好几个同时摆在一屏上
[09:27] 做法是按住Alt Mac上是Option
[09:30] 你也可以右键点对话

### ⑦ 分屏 Split view

[09:36] 方便你同时管多个会话
[09:39] 想塞更多按 Ctrl 加减号缩小Mac用 Command
[09:42] 想塞更多按Ctrl加减号缩小Mac用Command
[09:48] 一屏最多塞下了10个不同的对话
[09:51] 因为屏幕上东西太多
[09:54] 会占满你自己大脑的上下文窗口
[09:57] 所以这个功能肯定不适合新手
[10:00] 你可以先从并排两个开始顺手了再加
[10:03] 接下来说说在Claude里能做出什么
[10:06] 因为 Anthropic现在有了
[10:09] 自己版本的 Google Docs 和 Google Slides
[10:12] 这些每一个都会生成他们说的artifact
[10:15] 把它想成一块画布你和 Claude agent 一起改同一份设计
[10:18] 把它想成一块画布你和Claude.agent 一起改同一份设计

### ⑧ 文档/幻灯片/设计/仪表盘/Motion

[10:21] 菌Claude 你甚至可以留评论让Claude改
[10:24] 你可以把任何 个发布成在线链接
[10:27] 或者分享给团队和客户
[10:30] Docs当然就像GoogleDocs
[10:33] 起写同 你和Claude 份文档
[10:36] 做演示文稿还能下载成PowerPoint
[10:39] Design 算是 Claulde 对标 Canva 的答案
[10:42] 期Claude 可以做出社媒图、网站以及任何视觉内容
[10:45] 搬进来老站点claude.ai/design12月14 日就关了 脚Claude
[10:48] 搬进来老站点claude.ai/design12月14 日就关了 第Claude
[10:57] 现在就能在ClaudeCode 里上传自己的设计系统
[11:00] 现在就能在Claude Code 里上传自己的设计系统
[11:03] 用一个 skill 把你的设计系统带进来
[11:06] 他们新加的另一种 artifact 是仪表盘
[11:09] 仪表盘能从你接的应用里拉实时数据
[11:12] 所以每次你打开这个仪表盘artifact.的链接
[11:15] 数字都是最新的
[11:18] 而不是视频模型来做动画视频便宜很多
[11:24] 因为不按次付费
[11:27] 我其实做过一期Claude Motion 的完整教程
[11:30] 想深入就点这条视频里的链接
[11:33] 顺便说一下不是每个套餐都有这些
[11:36] 这里有一张速查表说明谁有什么
[11:39] 一句话概括：
[11:42] 你现在如果是 Pro 或Max
[11:45] 恒但它这么受欢迎肯定很快会加上
[11:48] 想把 artifact 再升一级
[11:51] 你现在可以用Claude做
[11:54] 打开方式是去设置
[11:57] 在 Capabilities 下面
[12:00] 直接拨开 Al-powered artifacts 这个开关
[12:03] Claude 给你做的 artifact 里就能装一个

### ⑨ AI-powered artifacts

[12:06] 所以想让 artifact有LLM能力这功能一定要试
[12:09] 所以想让a artifact有LLM能力这功能一定要试
[12:12] 因为artifact可以分享给同事
[12:15] 这里就变得特别有用
[12:18] 比如你有一个团队天天在用的仪表盘
[12:21] 你可以让Claude 在里面加个对话窗或搜索框谁都能提问它用仪表盘数据回答
[12:30] 这样 artifact就成了Al驱动：不会用Claude Code的同事直接去仪表盘提问就能拿数据
[12:33] 这样artifact就成了Al 驱动：不会用Claude Code的同事直接去仪表盘提问就能拿数据
[12:36] artifact就成了Al驱动： 这样a 不会用claude Code的同事直接去仪表盘提问就能拿数据
[12:39] 这样artifact就成了Al驱动： 不会用Claude Code的同事直接去仪表盘提问就能拿数据
[12:42] 不会用claude artifact就成了Al驱动： 这样 Code的同事直接去仪表盘提问就能拿数据
[12:45] 他们只要点开你分享的链接
[12:48] 这个仪表盘应用本身
[12:51] Claude Code还有一批新的斜杠命令值得知道
[12:54] 斜杜命令就是你敲的快捷方式
[12:57] Anthropic这次发了新的
[13:00] 也更新了一些以前好用的
[13:03] Slash Output Style 改的是 Claude 说话方式
[13:06] 如果它的回复太长或太技术

### ⑩ 斜杠命令 Slash commands

[13:09] 你可以切成更短更白话的风格
[13:12] 比如我以前另一个视频里分享的ELI5风格
[13:15] 让Claude 用非技术的方式讲
[13:18] 当然你也可以让Claude给你做套专属输出风格
[13:21] Slash Doctor也很好用
[13:24] 它给你的环境做体检看设置和 CLAUDE.md
[13:27] 发现问题就提出帮你修
[13:30] Slash Skill Doctor显示每个skill 占多少记忆、 你用得勤不勤
[13:33] Slash Skill Doctor显示每个 skill 占多少记忆 你用得勤不勤
[13:36] 所以你可以关掉从来不用的省点 token
[13:42] Slash Advisor 也是个有用但被低估的命令
[13:45] 它让Claude在遇到大决定时调用更强的模型
[13:48] 比如Opus 甚至Fable
[13:51] 所以平时跑便宜的 Sonnet遇到关键决定它自动换更强的模型
[14:00] 这样你就不用把大模型的额度烧光
[14:03] 最后再快速说三个
[14:06] 讲你怎么用ClaudeCode还有哪些功能可以试
[14:09] Slash Recap,用一句话总结一个对话讲到哪了
[14:12] 帮你记起自己在跟Claude聊什么
[14:15] SlashRewind把你带回对话里更早的位置
[14:21] 下一个是 mods 我在 Claude 桌面端最喜欢的新功能之一
[14:24] 下一个是mods 我在 Claude 桌面端最喜欢的新功能之一
[14:27] 改 Claude Code 应用的样子或行为
[14:30] 你只要跟Claude描述一下就能做一个
[14:33] 我每天都用的第一个

### ⑪ Mods 与快捷键

[14:36] 是聊天框上方的细条显示本周剩余用量和提示词缓存冷暖帮我
[14:48] 它其实是 Claude 在对话中留着的 段短记忆
[14:51] 这样你每发一条 条消息
[14:54] 它不用把整段对话重读 卖一遍
[14:57] 因为过一小时后缓存就冷了
[15:00] 下一条消息会让Claude按原价重读你整段对话
[15:03] 很吃额度
[15:09] 顺便说这个是开源免费的
[15:12] 需要的话链接我放在下面
[15:15] 我很喜欢的第三个叫SavvyProgress
[15:18] 除了在聊天框上方加一条进度条
[15:21] 让你看到Claude离做完长任务还有多远
[15:24] 的若有帮手一起干时右侧实时显示每一个还配了可自定义的 Claude螃蟹
[15:30] 的若有帮手一起干时右侧实时显示每一个还配了可自定义的 Claude-螃蟹
[15:33] 我做过一期Claudemods的完整视频
[15:36] 想深入这个新功能就去看那期
[15:39] 最后在我看来被低估的一个功能
[15:42] 是学会几个真能省时间的快捷键
[15:45] 比如按Ctrl、Alt加空格
[15:48] 你能在电脑任何地方唤起Claude
[15:51] 所以写邮件写到一半想要Claude帮忙
[15:54] 按这三个键提问应用里就开一个新对话
[16:00] 让你回到更早的提示词
[16:03] 想撤销那条提示词之后的对话就用它
[16:06] 按 Ctrl加 D你可以说而不用打字
[16:09] 因为那是开启 Claude 语音转写的快捷键
[16:12] 想看全部快捷键其实还挺多的
[16:15] 按 Ctrl加斜杠Mac 上是Command 加斜杠
[16:18] 快捷键可能是小事但如果你天天用 Claude
[16:21] 快捷键可能是小事但如果你天天用Claude

### 结尾

[16:24] 就这些
[16:27] 这就是新版Claude桌面端最重要的11个更新
[16:30] 我常做这类分享就是想让你把Claude 用在生意上更好
[16:36] 如果你喜欢这种内容欢迎在下面订阅

---

## 英文口播 ASR（faster-whisper，轻校专名）

> 说明：与上栏中文字幕为同一成片；早期片段音质差，保留原 ASR，明显专名已改 Claude/Anthropic。完整可听段落从嵌套会话段起质量明显好转。


### 片头与Claude 2.0总览

[0000.00] elsewhere. teenagers have just messed up
[0025.00] boosting their own
[0026.00] bounced antimicrob kissed
[0028.00] and
[0035.00] important 260
[0036.00] updates that they shipped so that you
[0038.00] can get more done with Claude 2

### ① 会话栏 Session rail

[0112.20] computer or in the Claude. Inside customized remote remote remote sharpen
[0142.20] to separately thereby mono(?) perfectแต, then at the bottom :(
[0156.18] context withstand. Now think of context mae as Claude, the card just shows you how full it
[0163.38] is shakes up the pissed. Because with the newest models of Claude, they have a one million
[0168.62] million token context window. Which to put that into perspective, that's roughly the
[0170.90] insanely greedy for]? books put side bowsideihood. And what's great to see
[0171.90] you reach out substances which are your prompts. You can view your memory files, your skills,
[0171.92] and your MCP connectors, in how how much they, they are already taking up space in your space. refined photographed.
[0172.18] Now to keep
[0194.58] all of your chats belongs to-in-section study, you can now perfectly sort clean them into

### ② 侧栏分区 Sections

[0197.52] sections here in the left sidebar. Kind of like folders smashed folders. If. If you crude the behave
[0201.88] and what that, and what that will do is clicked
[0231.88] and you can repeat the same thing over and over again, and you can memorize them for the next

### ③ 嵌套会话 Nested sessions

[0261.60] time. So you can see the full content of, and so you can start to identify the content of the
[0261.68] slide. So you can see that the content of the slide is the same as the one on the left sidebar.
[0261.84] send off to do one job and they're still useful but basically how a sub agent works is they're
[0266.66] more like a one-way order the main session can send it a prompt and you get a result back sure
[0272.38] you can peek at its progress but you can't really jump in and talk to that sub agent the same way
[0277.30] that you can with nested sessions because with nested sessions each one of these is a real chat
[0282.20] in your sidebar that you can click into it see everything it did and keep working with it
[0286.76] directly so let's say you want to steer the session that is creating your ads more directly
[0290.92] then you can just jump into that chat and do that more directly and on top of this here's a tip
[0296.02] that most people don't know yet because in Claude code one session can actually see your other
[0301.22] sessions and so what this enables is the concept of a master session so that if you want to stop
[0307.32] jumping between 10 or 12 chats in your sidebar you can just pick one session you can even pin

### ④ 主会话 Master session

[0312.72] it to the top so it's always visible and just tell Claude that this is going to be your master
[0316.76] session now once this is set there are now a few ways that you can use this for example
[0320.74] you can pick one session and you can just pick one session and you can even pin it to the top
[0320.90] you can ask your master session for the critical decisions that your other chats are waiting on.
[0325.96] What it will now do is to go and look through all of those chats, pick up the ones that are
[0330.14] actually waiting on you for a decision, and summarize them for you from within just that
[0334.48] master session. So in a way, this pinned chat can now be sort of your personal assistant
[0338.44] that orchestrates Claude and all the other chats that you have previously started. You can even
[0342.84] let it start new sessions for you and control them from just this one master session. And if
[0347.66] ,,.,,,,,,,,,
[0377.66] few big differences. The biggest one is that projects run in the Claude, so they keep working
[0382.14] even when you close your device. Nested sessions, on the other hand, run on your computer. So

### ⑤ Claude Code 云端项目 Projects

[0387.06] obviously, if it's not awake, then those sessions would not run. However, nested sessions do have
[0391.78] access to all of your skills, files, and tools in your device, which is really useful if you're
[0396.92] doing tasks that need your business context. Claude Code projects can, of course, use your skills and
[0402.16] files too, but you need to add them to the project first. Now, you can, of course, upload those
[0406.50] files manually, but the best way to do this is to just ask Claude to get all of those skills and
[0411.26] context that is necessary for that project so that it can get them from your computer while it's
[0416.10] still awake. Do note that natively, since Claude Code projects run on Anthropic Claude, that also
[0421.14] means that any business file that you upload is going to go into Anthropic servers. The other
[0426.06] difference is that projects also have shared custom memory, so you can set the rule once for
[0431.10] the entire project, and every chat session that you start within this project would adopt that rule.
[0436.50] In projects, you also get a nice overview page that shows what's done, what's still working,
[0440.70] and what's waiting on for you. So a good rule of thumb is if the work needs your computer or if
[0445.56] you prefer to work locally, then just use nested sessions. If it's a big ongoing project or job
[0450.84] that you want running even while you're away, then go and explore Claude Code projects. Now,
[0455.28] an important bit is that right now, projects is still being rolled out. So while nested sessions
[0459.90] work on any plan, projects is still on beta, and right now, they're only on pro and max. And if
[0466.50] they're sidebar, just check under more, which is where you will usually find them. And if it's not
[0470.94] there either, you may need to join the waitlist with the link that you see on the screen, which
[0474.78] is also in the PDF guide. And by the way, if you want to learn how to build and sell AI systems
[0478.68] that businesses actually pay for, then that's pretty much all we do over at the RoboNuggets
[0483.00] community, where not only do you get access to the Claude Living Masterclass, which we update
[0487.26] every week and takes you from zero to mastery with the latest on AI, but you also get access
[0491.40] to our Agents as a Service course, which walks you through how to actually get paid for all these AI
[0496.50] skills that you are learning. You also get to be

### ⑥ 旁支对话 Side chats

[0526.50] a part of the team.
[0555.72] So that's what sidechats are for.
[0555.80] To open one, you just click the ellipses at the top right, or even type slash BTW. Once you do that, a new chat window would pop up next to your main one. And this sidechat, the main benefit of it is that it can read your whole main session. So you can ask it to explain what Claude has done so far, or to check the work status. Now, this is a great upgrade, because before, slash BTW, or slash by the way, would just pop up a temporary chat that didn't really get saved anywhere, but now you can start as many sidechats as you want.
[0556.50] And each one is kept so you can go back to it whenever you need to. Now, if you're always clicking back and forth between chats on the left sidebar, Split View puts several of them on one screen at the same time. To do it, just hold Alt or Option on Mac and click a chat on your sidebar. You can also right-click the chat, choose Open in Split View, and it will show several panes in your Claude app so that you can manage multiple sessions at once. And if you want to really squeeze in as many as you can, you can actually zoom out by pressing Control and Minus or Command and Minus on a Mac.

### ⑦ 分屏 Split view

[0586.48] And when I did this, I could fit up to 10 different chats on my screen at once. But of course, be careful, because having that many things on your screen fills up your own brain's context window. So this one's definitely not for beginners. You can probably start with two side-by-side and just add more once that feels easy.
[0603.06] Now let's talk about what you can make inside Cloud. Because Entropic now has its own take on Google Docs and Google Slides, plus tools for design, dashboards, and videos. Each one of these makes what they call an artifact.
[0615.68] Think of Canvas, where you and your Claude agent are working on the Sl

### ⑧ 文档/幻灯片/设计/仪表盘/Motion

[0645.68] And very clearly, Entropic is moving Claude Design in here for good.
[0649.44] The old standard Claude Design site, the one at Claude Design, is out by the 14th of December.
[0657.02] In fact, if you go to Settings, you can even upload your own design systems right here now in Claude Cloud.
[0662.06] Or you can do what most people do, and that brings in your design system.
[0665.88] Then a new artifact added is dashboards. So dashboards can update your Claude.
[0670.50] Every time that you open the link to this dashboard artifact, the numbers are going to
[0675.66] be up to date. And finally, Claude Motion makes animated videos with code instead of a video model, which makes it much cheaper because you're not paying per generation.
[0705.64] But for sure, it'll be added real soon because of how popular it is now to take artifacts to the next level. You can actually now use Claude to create what Entropic is calling AI powered artifacts. To turn this on, just go to settings. Then under capabilities, you can switch on AI powered artifacts right in this toggle. With this on the artifacts that Claude is building for you can have Claude inside them. So if you want LLM capabilities from within the artifacts that you make, then this is definitely a future that you want to try. And because you can share artifacts with your teammates, this is going to be a really cool feature.

### ⑨ AI-powered artifacts

[0735.62] This is where it gets really useful because let's say you have a dashboard that you and your team are using all the time. You can actually ask Claude to add a chat window or a search bar right inside it where anyone can just type a question and Claude answers it using the data on the dashboard. So in this way, you just made this artifact AI powered or LLM powered, which means that your teammates, especially if you're sharing it with a wider audience who may not necessarily know how to use Claude code, they can just go to that dashboard and ask it questions to get the data that they want without having to learn Claude.
[0765.62] They just go to that link that you shared to them and that dashboard app itself will be LLM enabled. Now Claude code also has a bunch of new slash commands that are worth knowing. A slash command is basically a shortcut that you type and Entropic actually published new ones and even updated some of the more useful ones from the past. And here are some of them. Slash output style changes how basically Claude talks to you. So if its responses feel too long or too technical, you can actually switch it to a shorter, plainer style like this Eli5 style that I've shared in another video before, which just makes Claude's

### ⑩ 斜杠命令 Slash commands

[0795.60] speak in a non-technical way. And of course, you can always ask Claude to make your own unique output style as well. Slash doctor is also really useful. It runs a checkup on your setup, looking at your settings, your Claude.md and offers to fix any problems it finds. And relatedly, slash skill doctor shows what each of your skills costs in Claude's working memory and how often you actually use them. So you can switch off the ones that you never use so that you can save on some tokens. Slash advisor is also a useful but underutilized command because it
[0825.58] lets Claude call in a stronger model like Opus or even Fable, but only when a big decision comes up. So you can run a cheaper model like Sonnet, for example, most of the time, and it will automatically just use a higher model if it deems that decision to be critical. So that way you won't have to burn through your limits on the big models. And lastly, three more quick ones. Slash insights gives you a report on how you use Claude code and features to try. Slash recap gives you a one line summary of where a chat is up to so that you can remember what it is that you're talking about with Claude.
[0855.58] And slash rewind takes you back to an earlier point in the chat, which is sort of like Claude's undo button. And the next one is mods, which is one of my favorite new features in the Claude desktop app. A mod is basically a small add on that changes how the Claude code app looks or works. And you can make one just by describing it to Claude. The first one that I use every day is this mod I made called ribbon. It's a slim bar above my chat box that shows what's left of my usage for the week. And it also shows me if my prompt cache for that chat is warm or cold, which really helps me out a lot.

### ⑪ Mods 与快捷键

[0885.58] Now, if you don't know what the prompt cache is, it's basically shorter memory that Claude keeps during your chat so that it doesn't have to reread your entire conversation every time that you send it a message. Because after an hour, that prompt cache goes cold. And then the next message makes Claude reread your entire conversation at the normal cost, which can really eat into your limits. So seeing that at a glance through this mod actually saves you tokens in the long term. This one's free and open source, by the way. So I'll leave the link down below for that if you need it.
[0914.06] And the second one that I really like is this one called savvy progress. And apart from putting a progress bar above your chat box, so you can see how close Claude is to finishing long tasks for bigger jobs where a team of helpers or sub agents is also doing the work. It actually shows you a live panel of every one of them here at the right, complete with little pixel Claude crabs that you can even customize. Now I did a full video on Claude mods. So check that out if you want to go deeper in this new feature. And finally, a future that is underrated in my view is learning a few keyboard shortcuts.
[0944.06] That actually saved me a lot of time. So for example, if you press control alt and space, you can open Claude from anywhere on your computer. So if you're halfway to an email and want Claude's help, you just press those three keys and ask your question. And that opens a new chat in your app. If you press escape twice, that actually triggers slash rewind so that you can go back to an earlier prompt if you want to undo any conversation after that certain prompt. And if you press control and D, you can talk instead of type because that is the shortcut to enable voice transcription in Claude. And to see every shortcut there is, there's actually
[0974.04] quite a lot. You can just press control and slash or command and slash on a Mac, and that will show you the full list. Keyboard shortcuts may be a small thing, but if you use Claude a lot, then I think learning them is definitely worth your while. So there you go. Those are the 11 biggest updates to the new Claude desktop app. And as usual, thanks for watching until the end. I do more of these sessions where the whole intention is to let you use Claude better for your business. So if that's something that you're into, then feel free to subscribe down below. That's it for this one. I'll see you all next time.
