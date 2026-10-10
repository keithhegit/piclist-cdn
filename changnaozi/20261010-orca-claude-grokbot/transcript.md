# Grok Bot 云电脑搭 Claude Code＋Orca＋Tailscale

> **作者**：Asa（@app_sail）· **平台**：X Article · **发布**：2026-10-09 19:43 北京时间（2026-10-09 04:43 PT）
> **源链接**：https://x.com/app_sail/status/2108523630900748335
> **原文标题**：把这篇文章丢给 Grok Bot：给你注册 Claude，搭配 Orca + Tailscale，打造 7×24 在线的 Claude Code 云主机
> **篇幅**：正文约 16600 字（不含脚本），附 2 个 bash 脚本
> **校对说明**：一手源 = 帖内 X Article 全文（API plain_text），非 ASR、非二次剪辑；正文逐字保留，仅按原文小节补 Markdown 标题、把命令放进代码块。原文配图 8 张未收录。附录两个脚本取自 Article 内代码块原文，未改动。

---

一句话说清楚：在 Grok Bot 上注册 Claude，并在自带的那台美国云电脑（16 GB 内存）上装好 Orca，把它当成一台远程服务器；你的 MacBook 和手机上的 Orca 通过 Tailscale 接入，直接控制跑在 Grok Bot 上的 Claude Code，7×24 小时在线，太爽啦。

怎么用这篇文章：把全文（或链接）发给 Grok Bot，对它说“按这篇文章一步一步执行，每做完一步停下来向我汇报”。你一边读，它一边做。也可以逐步复制文中的 Prompt 自己发。

需要你确认的：确认两个设置、添加一个现成的 Bot（见第一步）、点一次 Tailscale 授权、注册并订阅 Claude、登录一次、在 MacBook 上配对一次、手机上扫一次码。其余全部交给 Grok Bot。

这篇和别的教程不一样的地方：除了注册 Claude、安装 Orca、Tailscale、各种配置全流程以外，更重要的是 Grok Bot 更新之后还能正常使用。这台云电脑没有 systemd，而且 Grok Bot 会自动更新，每更新一次，装在 home 目录以外的软件和改动就全没了——这两件事才是真正的坑。整个流程我已经反复测过多次：Tailscale 那部分打包成了一个现成的 Bot 直接可以安装，Orca 那部分用官方 AppImage，再加一个启动脚本和一个定时任务。

## 为什么折腾这个

2026 年国庆前后，Claude Code 又迎来一波严重的封号。Claude 本来就难注册，手机号、Gmail 邮箱、支付方式、网络环境，每一关都能卡住人。Anthropic 封得越来越狠，大家想出来的办法也越来越野，给人的感觉现在是两边都有点魔怔了😂。

我不想再把精力花在跟风控斗智斗勇上，只想要一个一直在线、和我本机网络无关的环境：系统在美国，出口在美国，时区在美国，不经过我本机的任何代理。

我的看法是：任何伪装、任何想跟 Anthropic 斗智斗勇的策略长期来说都没有意义。它有那么强的 AI，装出来的环境迟早会露馅。与其伪装，不如让环境本身名副其实：一台真的在美国的机器，美国的出口，美国的时区，从注册到日常使用都在这台机器上完成，不混进中国的网络和代理。

Grok Bot 正好送了一台这样的机器。它背后是一台完整的 Linux 云电脑，8 核、16 GB 内存，只拿来聊天太浪费了。本文的玩法也是这个思路：直接让它在自己的电脑上装好 Claude Code 的命令行，登录一次，之后它就能把活派过去。

先说清楚：这不是防封教程，我也不能保证这样就不会被封。𝕏 上有人说这样用了一个多月账号正常，也有人说在 Grok Bot 上登录之后一次没用就收到了封号邮件。Anthropic 对可用地区有自己的条款，风险自己评估。这篇只讲怎么把环境搭稳。整个过程也有点折腾，适合爱折腾的小伙伴们。

## 先做三件事（需要人）

动手之前，先做下面三件事。前两件在 Grok Bot 的设置里改，它们决定这台机器在外面看起来是不是一台“一直在美国的电脑”；第三件是添加一个 Bot，为第一步装 Tailscale 做准备。

时区改成美国时区。 在设置 → General → Timezone 里改。默认跟随你本机的时区，要手动改成云电脑所在地的时区。我这台的出口在美国东部，所以选的是美东时间（America/New_York），让时区和出口对得上。改完在云电脑里跑 date 可以确认。有两点要知道：这台云电脑是你所有 Bot 共用的，改了之后大家看到的时间都会变；已经在跑的程序（比如 Orca 里开着的 Claude Code）要重启之后才会用新时区。不确定该选哪个时区，可以直接问 Grok Bot 这台云电脑的出口在哪儿，再按它的回答来选。

不要让云电脑的流量走本机代理。 设置里有一个让云电脑的网络流量经过你自己设备的开关，保持关闭。它一开，云电脑的出网就绕回你自己的电脑和代理，出口不再是它自己的美国出口，这台机器最大的优点就没了。

### 装好 SSH to Grok via Tailscale 这个 Bot

打开 https://x.ai/bot/BrViAOWzDSiAjBLqUnBgA，点 “Add to Grok Bot”；它会在云电脑上装好 Tailscale、把你的设备组进同一张网，具体见第一步。

## 整体架构

整体分三层（见下图）：你的设备都走 Tailscale 连到云电脑上的 Orca；Claude Code 跑在云端，合上电脑也不停；Tailscale 看门狗管掉线，更新之后由 Tailscale Bot 的恢复任务和 Orca 每 10 分钟一次的定时任务把它们拉回来，通常几分钟内会自动恢复。

搭建只有四步：

在 Grok Bot 的美国云电脑上安装 Tailscale，把自己的所有设备加进同一张网。

在云电脑上注册 Claude，安装 Claude Code 并登录。

在云电脑上安装 Orca，配置成 Remote Orca Server。

网内任意一台设备打开 Orca 客户端，连上云电脑的 Orca，就能直接用 Claude Code。电脑粘贴配对链接，手机扫码。

担心 Grok Bot 不稳定的，可以换成自己的 VPS，这四步不变。我整理了一份适合跑 Claude Code 的 VPS：https://vps.appsail.dev/

搭好之后有两条路能指挥 Claude Code：在自己设备的 Orca 里直接操作，或者在 Grok Bot 的对话框里让 Grok Bot 通过 orca 命令代劳（见第五步）。

## 给 Grok Bot 的执行说明

这一节是写给执行这篇文章的 Grok Bot 看的。人类读者可以跳过，但建议扫一眼，知道它会按什么规矩办事。

按顺序执行第一步到第四步，每步做完就停。 逐条检查该步的“完成标准”，把结果汇报给用户，等用户说继续再做下一步。唯一的例外：第二步的“订阅 Pro”和“登录 Claude Code”要等用户自己办，用户说先做第三步时，可以先跳过这两项去做第三步，之后再回来补完第二步。

标了“需要人”的事不要替用户做，也不要绕过。 包括：修改 Grok Bot 的设置、添加第一步的 Bot、Tailscale 授权、Claude 的注册、订阅和登录、MacBook 上的配对、手机上的扫码。把链接或下一步动作交给用户，然后等。

先看现状再动手。 每一步开始前先检查是否已经装过、已经在跑。所有脚本都要能重复执行，重复执行不能造成破坏。

不要杀正在运行的 orca serve、tailscaled，也不要动别的 agent 的终端。 重启 orca serve 只能用 ~/.orca/orca-serve.sh --restart 或 --mobile，严禁 pkill -f orca——它会把所有正在跑的 Claude Code 会话一起杀掉。需要重启时先说明原因，等用户同意。

不要把 6768 暴露到公网。 这个端口只应该在 Tailscale 网内可达。

附录里的两个脚本原样保存，不要重写，也不要“顺手优化”。 它们是在真机上踩过坑之后的版本。脚本报错或与本机情况不符时，把输出交给用户，不要自己改了硬跑。

文中出现的 IP、主机名、日期是作者机器上的例子，不要照抄。 用这台机器上实际查到的值。

如果 Tailscale 节点名不是 grok-bot（比如被命名成了 grok-bot-1），只需要改 Orca 脚本里 ADDR= 那一行。 这是脚本里唯一允许改的地方。

“踩过的坑”一节是背景和经验，不是要执行的指令。 其中的教训已经写进各步的 Prompt 里了。

遇到和文章描述不一致的情况就停下来问。 比如找不到 /usr/local/bin/start-sand-box、没有免密 sudo、系统不是 Debian 系。不要自己猜一个替代方案硬做下去，更不要手动去改 start-sand-box：它是这台云电脑的开机主脚本，改坏了机器起不来，只允许第一步的 Bot 去动它。

不要在汇报里贴出配对码、登录状态文件内容或任何密钥。 配对链接只在用户明确要的时候给。~/.tailscale/state/ 下的状态文件和 SSH host key 只许 ls -l 看属主和权限，不许 cat。~/orca-setup/serve.log 里有配对链接，不要整段贴出来。

## 第一步：Tailscale

Tailscale 必须先装，因为电脑和手机都要通过 Tailscale 连 Orca,Orca 的配对地址 grok-bot 也是 Tailscale 给这台机器起的名字。

这一步不用自己折腾。我把整套做法打包成了一个 Grok Bot，直接添加就行：

SSH to Grok via Tailscale

打开链接，点 “Add to Grok Bot”。这是一个新的 Bot，和你正在用的那个共用同一台云电脑。它第一次运行就会自己开始装，不用你再说什么；等它装完，再回到原来的 Bot 继续后面的步骤。它会做这些事：

在云电脑上安装 Tailscale 并开启 Tailscale SSH，节点名固定为 grok-bot，装完你可以直接 ssh box@grok-bot 连进去；

在 ~/.tailscale/ 里建一套恢复工具：节点名配置、看门狗 tailscaled-autostart、可重复执行的 bootstrap-tailscale.sh；

把看门狗挂进开机脚本，并把登录状态和 SSH host key 备份到 ~/.tailscale/state/；

建一个每 5 分钟跑一次的定时任务：发现 Tailscale 不见了（通常是云电脑刚更新完）就自动跑恢复脚本，通常几分钟内同一个节点、同一个 IP 就会回来，不用重新登录；没恢复就手动跑 sudo ~/.tailscale/bootstrap-tailscale.sh；

建一个每周检查的提醒：节点密钥还剩 21 天以内过期时通知你；

给你一段 ACL 配置，把 SSH 锁定到只有你自己的设备能连、不能直接用 root。这一段要你自己贴到 Tailscale 后台，因为改错了会把自己锁在外面。

需要人：点开它发来的 Tailscale 登录链接，授权；把它给的 ACL 贴到 Tailscale 后台。如果你的 tailnet 里已经有一个叫 grok-bot 的旧节点，先去后台删掉，否则新节点会被命名成 grok-bot-1；真变成了 grok-bot-1，第三步脚本里的 ADDR= 要跟着改。

完成标准：

在云电脑里 tailscale ip -4 返回一个 100.x.x.x 地址；

在你自己的电脑上 ssh box@grok-bot 能连上；

Mac 上 ping grok-bot 能通（说明 MagicDNS 已经开着），手机的 Tailscale App 里能看到 grok-bot；

~/.tailscale/bootstrap-tailscale.sh 存在，ls -l ~/.tailscale/state/tailscaled.state 显示属主是 box；

Grok Bot 的定时任务里有 “Auto-restore Tailscale”。

这台机器上跑着跳过权限确认的 agent，所以那条 ACL 不要省。原则是别让 agent 顶着你本人的身份、在你的 tailnet 里到处走。

## 第二步：注册、订阅、登录 Claude（需要人）

网络通了，先把 Claude 账号和 Claude Code 准备好，后面装 Orca 时它就能直接用。这一步的每个环节都要你本人来做，Grok Bot 只负责打开页面、敲命令、把控制权交给你。全程在云电脑上完成，不要拿到自己本机的浏览器里去做。

### 1. 注册账号

对 Grok Bot 说：

注册一个 Claude 账号

它会在云电脑的浏览器里打开 Claude 的登录页。Claude 没有单独的注册入口：填一个新邮箱点 Continue，它会往邮箱发验证码，验证通过就直接建号；也可以点 Google 登录，用 Google 账号直接注册。

到了填邮箱、密码、验证码的地方，Grok Bot 会停下来，聊天里出现一个“打开电脑”的按钮。点开它，自己在云电脑的浏览器里填完，再把控制权交还。

两条规矩：

密码和验证码不要发到聊天里，只在云电脑的浏览器里填。Grok Bot 看不到你填的内容。

用 Google 登录的话，Google 可能会发一封“有新设备登录”的提醒邮件，这是正常的，登录的就是这台云电脑。

### 2. 安装 Claude Code

发给 Grok Bot：

用官方脚本安装 Claude Code，命令是 curl -fsSL https://claude.ai/install.sh | bash。确认 ~/.local/bin 在 PATH 里（~/.profile 和 ~/.bashrc 都要有），告诉我版本号。

这里特意用官方安装脚本而不是 npm i -g。官方脚本把程序装在 ~/.local/share/claude/，在 home 目录里，更新云电脑之后还在。npm 全局安装的位置在 home 之外，更新一次就没了。

### 3. 订阅 Pro

免费账号用不了 Claude Code。拿免费账号去连，授权页会直接告诉你需要 Max 或 Pro 订阅。

所以至少要订 Pro。订阅之前先做一件准备：把账单地址提前存进云电脑上 Chrome 的 profile 里。可以在 Chrome 里登录自己的 Google 账号并打开同步，存在 Google 里的地址会同步过来；也可以在 Chrome 设置的“地址”里手动加一条。这样到了 Claude 的付款页，姓名和地址点一下就能自动填好，不用手敲。

卡号和最后点 Subscribe 这两步自己来，不要交给 Grok Bot，也不要把卡号发到聊天里。我用的是 Mercury 的借记卡付的订阅。Mercury 是一家美国金融科技公司，它的银行账户和卡由合作银行提供。

没有 Mercury 的，其他几种支付方式可以参考：

其他美国银行卡。 成本最高，但最长期、最干净，和 Mercury 是同一类。

Google Pay. 在付款页直接选 Google Pay，前提是你的 Google 账号里已经绑了能用的卡。

走美区 Apple 账号。 在 iPhone 上用美区 Apple ID 登录，从 Claude 的 App 里订阅，扣的是 Apple 账号的钱。Apple 账号本身可以用美区礼品卡充值余额（成功率最高），也可以绑 Apple Pay 或美区 PayPal。

虚拟卡、其他海外卡。 部分能用，但不稳定，被风控拦下的概率大。

这几种的细节，可以先看我之前写的这条关于美国支付方式的帖子，它是以美区 Apple 账号为例讲的，思路通用。

我最近会整理一版更详细的美国支付方式，到时候单独发出来，敬请期待。

在那之前不用急着订阅：可以先拿免费账号用两天 Claude，养养号，再来订阅。这两天不用干等，下面的“登录 Claude Code”要订阅之后才能做，但第三步装 Orca 不受影响，可以跟 Grok Bot 说“先做第三步“。

### 4. 登录 Claude Code

发给 Grok Bot：

在终端里运行 claude auth login，把它给出的授权链接在这台电脑的浏览器里打开，然后把电脑交给我，我自己登录和授权。

点“打开电脑”接管之后：

在浏览器里登录刚才注册的 Claude 账号，中间可能要过一次人机验证，自己点完。

点授权，页面上会显示一串授权码。

把授权码粘回终端里等着的 claude auth login，登录完成，再把电脑交还给 Grok Bot。

登录状态存在 ~/.claude/ 里，在 home 目录下，更新云电脑之后不用重新登录。

完成标准：

bash -lc 'command -v claude' 指向 ~/.local/bin/claude，claude --version 有输出；

claude auth status 显示已登录，登录方式是 claude.ai 账号的订阅登录（不是 Console 的 API key），订阅类型是 Pro 或 Max。

## 第三步：Orca

Orca 在这台机器上不开窗口，只跑 orca serve，监听 6768，等电脑和手机来配对。

Orca 连远程机器有两种方式：一是让本地 Orca 通过 SSH 去连；二是在远程机器上跑一个 Remote Orca Server 再配对。开发全在远程机器上的话，官方建议用后一种：电脑和手机接的是同一个会话，换设备能接着干，网络偶尔断开也没关系，重新连上之前的任务都还在。本文用的就是后一种。

这里用官方的 AppImage，不用 .deb。AppImage 就是一个文件，放在 home 目录里，云电脑更新后还在，不用重装。需要我们自己补的只有一件事：这台机器没有 systemd，重启或更新之后得有人把 orca serve 再拉起来。办法是附录 A 的启动脚本，加一个每 10 分钟跑一次的定时任务。

发给 Grok Bot：

运行下面四行，下载 Orca 的 AppImage：

```bash
mkdir -p ~/.orca ~/orca-setup
case "$(uname -m)" in aarch64|arm64) a=orca-linux-arm64.AppImage ;; *) a=orca-linux.AppImage ;; esac
curl -fL -o ~/.orca/orca-linux.AppImage https://github.com/stablyai/orca/releases/latest/download/$a
chmod +x ~/.orca/orca-linux.AppImage
```

把附录 A 原样存成 ~/.orca/orca-serve.sh，加可执行权限后运行，把输出发给我。再建一个每 10 分钟运行它一次的定时任务 “Auto-start Orca”，没出错就不用通知我。

脚本做三件事：

6768 只放行本机和 tailnet（缺 iptables 会自己用 apt 装；

有免密 sudo 却设不好规则时，不启动 orca serve，报错退出）；

orca serve 没在跑就用 AppImage 解包出来的程序启动；已经在跑就什么都不做。

所以它可以反复执行，交给定时任务去跑也没问题。配对地址用的是 Tailscale 名字 grok-bot，不是 100.x 的 IP，以后 IP 变了也不用重新配对。如果你的节点名不是 grok-bot（比如被命名成了 grok-bot-1），先把脚本里 ADDR= 那一行改成实际的节点名，这是唯一允许改的地方；附录 B 的自检脚本会从这一行读取节点名，不用另外改。客户端设备要开着 Tailscale 的 MagicDNS（默认就是开的），才能解析这个名字。

完成标准：

~/.orca/orca-serve.sh --version 打印出 Orca 版本；

ss -ltn | grep ':6768 ' 有监听；

再运行一次 ~/.orca/orca-serve.sh，它马上退出，cat ~/.orca/serve.pid 里的数字没变；

sudo -n iptables -S INPUT 2>/dev/null | head -4 和 sudo -n ip6tables -S INPUT 2>/dev/null | head -4：第 1 到 3 条规则依次是 6768 的 lo 放行、tailscale0 放行、DROP；

grep "Advertised endpoint" ~/orca-setup/serve.log | tail -1 显示 ws://<ADDR>:6768，其中 <ADDR> 是脚本里 ADDR= 那一行的值（默认 grok-bot）；

Grok Bot 的定时任务里有 “Auto-start Orca”，间隔 10 分钟。

Orca 会自动接管和 Claude Code 的集成。它在 ~/.orca/agent-hooks/ 放了 hook 脚本并写进 ~/.claude/settings.json，这样界面上能看到每个 agent 是在干活还是在等人。

最后装上自检脚本，以后每次出问题先跑它。它只读不改，逐项打印 ✅ 或 ❌，失败项后面带修复命令：

把本文附录 B 的自检脚本原样保存为 ~/check-after-update.sh，加可执行权限，运行它，把结果发给我。再写一份 ~/after-update.md，记下更新之后要运行的三条命令（都可以重复执行，没有先后顺序）：sudo ~/.tailscale/bootstrap-tailscale.sh、~/.orca/orca-serve.sh、~/check-after-update.sh。

自检脚本全部为 ✅，这一步才算完成。

## 第四步：从 MacBook 和手机连上来（需要人）

服务器搭好了，最后把自己的设备接上去。电脑粘贴配对链接，手机扫码。直接给 Grok bot 发消息：

Mac 和 iPhone 怎么链接上 Orca Remote Server

### MacBook：粘贴配对链接

确认 MacBook 上的 Tailscale 开着，和云电脑在同一个账号下（第一步已经装过）,MagicDNS 也开着。

在 MacBook 的 Orca 里添加这台云电脑：打开 Settings → Remote Orca Servers，选 Connect to a host，点右边的 + Add Server，起个名字（比如 Grok Bot），粘贴配对链接。列表里出现这台机器并显示绿色的 Connected，就连上了。

配对成功后，云电脑上你的项目目录（作者放在 ~/orca/projects/，也可以按 Grok Bot 官方文档的建议放进 /workspace）里的项目会出现在 Orca 里。选一个项目，新建 Claude Code 会话，随便发一句话，能正常回复就全部搭完了。

如果这时候它又弹出登录，别慌，账号没掉。第二步是用命令行登录的，Claude Code 的“首次设置向导”还没走完，交互界面会把向导从头走一遍。把 ~/.claude.json 里的 hasCompletedOnboarding 设为 true（改之前先备份）就不会再问了，详见“踩过的坑”。

顺带一提，在我这里的 Orca 里新开 Claude Code 会话，实际执行的是 claude --dangerously-skip-permissions。这个参数跳过所有权限确认，放在这种隔离的云电脑上才合适，别在自己的主力机上这么用。

### 手机：扫码

手机装好 Tailscale，登录同一个账号，MagicDNS 开着（默认就是开的）。

装上 Orca 的手机 App，打开后选 Pair。

扫 Grok Bot 发来的二维码，就连上了。

连上之后，电脑上开着的那些 Claude Code 会话在手机上都能看到：谁在干活、谁在等你，点进去能看终端输出，也能直接回复。

电脑端的配对链接和手机端的二维码不是同一种凭据，不能混用：电脑用的是带完整权限的链接，手机用的是手机专用的码，拿错了会提示权限不足。

### 完成标准

只能由人确认，Grok Bot 交出链接和二维码之后就停：

MacBook 的 Orca 里能看到云电脑上的项目，状态是 Connected；

Claude Code 会话能正常回话；

合上 MacBook 再打开，会话还在；

手机 App 里能看到同样的项目和会话。

## 第五步：让 Grok Bot 指挥 Claude Code

前四步做完，环境就搭好了。这一步不是安装，而是日常用法，也是把环境装在 Grok Bot 云电脑上最大的好处：Grok Bot 自己就坐在这台机器里，可以直接调用 orca 命令。

它能用到的命令主要是这几组。参数以这台机器上的 orca <命令> --help 为准；orca agent-context 会打印一份给 agent 看的完整命令说明，让 Grok Bot 第一次用之前先读它：

看所有项目里 agent 的概况：orca worktree ps

列出、读取终端输出：orca terminal list、orca terminal read

给某个终端里的 agent 发指令：orca terminal send

等 agent 干完：orca terminal wait --for tui-idle（--for 必填，可选 exit 或 tui-idle）

新开一个终端或工作区：orca terminal create、orca worktree create --name <名字> --agent claude（--name 必填；权限参数由 Orca 自己加）

多 agent 派活和收消息：orca orchestration ...

搜索所有 agent 的历史会话：orca search <关键词>

于是你可以在 Grok Bot 的对话框里这样说：

先运行 orca agent-context，读懂这台机器上 orca CLI 的用法。以后我让你查看或指挥 Claude Code，都通过 orca CLI 来做。用 orca worktree ps 看一下现在各个项目里 Claude Code 的状态，哪些在跑、哪些在等我。先用 orca worktree ps 找到【你的项目名】对应的 Claude Code 终端，让它跑一遍测试。等它空闲后把终端输出读回来，给我一个三行以内的总结。在【你的项目名】新开一个工作区和一个 Claude Code 会话，让它修 issue #12，改完后不要提交，把 diff 摘要发给我。

人在外面、手边只有手机的时候，这条路比手机上盯终端好用得多：只跟 Grok Bot 说话，让它去看、去催、去汇总。

用顺手之后，有四件事值得做。

把“派活”存成一个 skill。 每次都解释一遍“先找终端、再发指令、等它空闲、读回输出”很啰嗦。有人给 Grok Bot 写了一个 skill，只要说一句“让 Grok Build 做某某事”，Bot 就知道去开终端、启动 CLI、把话转过去。这里同理：让 Grok Bot 把上面那套 orca terminal send 加 orca terminal wait 的流程存成 skill，以后说“让 Claude Code 做某某事”就够了。

只留一个总管。 如果你有好几个 Bot，让其中一个专门负责分派和汇总，所有任务都从它那儿走，其他的只管干活。Orca 这边也一样，自带的 orchestration 可以让一个 agent 当协调者，把同一个任务分给几个不同模型的 agent 各做一遍，再汇总比较，有人就这么搭了一个多模型的设计评审团。

事先讲好哪些事要回来问你。 这台机器上的 Claude Code 跳过了所有权限确认，Grok Bot 又能替你给它下指令，中间没有任何一道闸。一条被反复引用的规矩是：调研、起草、测试、整理文件可以让 agent 自己跑完；发送、发布、花钱、改生产环境，必须回到人手里。把这条写进给 Grok Bot 的长期指令里。同样的道理，API key 之类的密钥存进 Bot 的安全字段或密码管理器，不要贴在对话里。

让 Grok Bot 每天替你看一眼账号。 账号出了问题最怕的是过了几天才发现。我让 Grok Bot 设了一个每天自动跑的检查：早上查一次 claude auth status，确认账号和订阅没变；再在上午随机挑一个时间给 Claude Code 发一句 hello，结果记到 ~/.claude-hello/hello.log。一旦出现账号警告、被登出、权限或地区报错，或者频繁要求重新验证，就马上通知我；一切正常就不打扰。

这四条只是把环境用顺手的开始。后续我会再写一篇文章，专门分享如何真正用好 Grok Bot、让它替你跑 Claude Code 干活。

## 踩过的坑

### Mac 突然连不上：Tailscale IP 变了

现象是 MacBook 的 Orca 一直连不上，云电脑上 orca serve 明明在跑，6768 也在监听。

一开始以为是 Orca 挂了，重启也没用。后来翻 serve.log 才发现，配对地址前后出现过两个：早先是 100.85.x.x，后来变成了 100.111.x.x。

原因是 Tailscale 重新登录过一次，新登录等于一个新节点，IP 换了。MacBook 里保存的还是旧地址。

解法是重新配对。现在改成用主机名 grok-bot 配对，IP 变了也不用重新配对；更彻底的办法是保住登录状态，让节点根本不变，这就是下一个坑。

### Grok Bot 自动更新之后全没了

9 月 30 日下午，我什么都没点，Grok Bot 自己更新了一次。回来一看，Tailscale、Orca 全部消失，orca 命令都找不到。

查下来才明白，Grok Bot 的自动更新不是原地升级，而是把云电脑换成一个全新的实例，事先没有任何提示。/home/box 会从平台的快照里还原回来，但 apt 装的包、/opt、/usr/local/bin、/var/lib/tailscale，以及对开机脚本 start-sand-box 的修改，统统清空。home 也不是百分之百保险：只有 root 能读的文件不会回来，快照之后才写的东西也可能赶不上。

更糟的是那一次 ~/.tailscale 整个目录也没了，登录状态的备份跟着丢失，只能重新登录，这才有了上面的 IP 变动。后来发现更新在复制 home 目录时会跳过只有 root 能读的文件，于是把备份改成 box 所有、权限 600。

更新还会直接打断正在干活的 agent，跑到一半的任务就停在那儿。自动更新拦不住，也不知道下一次是什么时候，所以只能假设它随时会来。现在的原则有两条：凡是装在 home 之外的东西，home 里都要有一份安装包和一个恢复脚本；重要的代码及时推到 git，不要只放在云电脑上。发现环境没了，让 Grok Bot 照“更新之后的恢复清单”跑一遍就行。

如果又需要重新登录 Tailscale，先去后台把旧的离线 grok-bot 节点删掉，否则新节点的名字可能被加上后缀。

顺带一提，Grok Bot 的官方文档建议把工作文件放在 /workspace。我的项目一直放在 ~/orca/projects/，目前没丢过，但如果你从头开始，按 Grok Bot 官方的建议来更稳妥，也就是把项目放到 /workspace 下面。

### 看门狗死了，新的看门狗起不来

现象是当时 Orca 用的看门狗 orca-autostart 进程没了，手动再启动一个，它一声不吭就退出。

看门狗用 flock 锁文件保证只跑一个实例。问题在于它拉起的 orca serve 继承了那个锁的文件描述符。看门狗死后，锁还被 orca serve 拿着，新看门狗抢不到锁，按设计静默退出。

解法是看门狗里每个子进程都加 9>&-，把锁的 fd 关掉再启动。现在 Tailscale 的看门狗就是这么做的；Orca 改用了定时任务，附录 A 的脚本仍然用 flock 防止同时跑两份，但启动 orca serve 等子进程时同样加了 9>&-，不会再出现这个问题。

### Tailscale 一天掉线好几次

现象是用着用着突然断开，过几分钟又自己好了。

看门狗的日志显示，控制面每天都会有几次报告节点离线。10 月 6 日一天就记录了 8 次，其中 4 次持续超过 3 分钟、触发了自动重启 tailscaled，其余 4 次自己恢复了。

这大概是沙箱网络本身的特性，没法根治。所以看门狗里除了“进程在不在”，还要检查“控制面认不认为我在线”。只查进程是查不出这种掉线的。

### Orca 里又让我登录一次

现象是命令行里明明已经登录，claude auth status 也正常，但第一次在 Orca 里打开 Claude Code 的交互界面，它又弹出了登录。

第一反应是账号掉了，其实没有。之前一直是用命令行登录和测试，Claude Code 的“首次设置向导”从来没走完过，所以交互界面会把向导从头走一遍，里面就包括选登录方式那一步。

解法是把 ~/.claude.json 里的 hasCompletedOnboarding 设为 true，改之前先备份。之后再打开就不会要求登录，只会问一句是否信任这个文件夹。

### 更新后 6768 没有防火墙保护：iptables 是跟着 Tailscale 来的

10 月 9 日早上又一次更新后，“Auto-start Orca” 比 Tailscale 先恢复，把 orca serve 拉了起来。但这台机器上的 iptables 是装 Tailscale 时一起装上的，更新后它跟着 Tailscale 一起没了。当时的脚本补不上防火墙规则，只打了一句警告就照常启动，6768 有大约 7 分钟没有防火墙保护，直到 Tailscale 重装、iptables 回来。

现在已经修好：附录 A 的脚本缺 iptables 会自己用 apt 装；有免密 sudo 却设不好规则时，干脆不启动 orca serve，退出码 1 让定时任务报出来；已经在跑的 serve 不会被停掉，只报错。

### pkill -f orca 会杀掉所有会话

这台机器上一个 orca 进程管着所有 Claude Code 会话，pkill -f orca 会把它们一起杀掉，正在跑的任务就没了。要重启 orca serve，只用 ~/.orca/orca-serve.sh --restart。

### orca serve 会改写 ~/.local/bin/orca

orca serve 启动时，会把 ~/.local/bin/orca 写成一个转发到当前版本的小脚本（那里已经有一个不是 Orca 写的同名文件时会跳过）；不用手动去建软链，也别指望它固定指向某个路径。

### 直接运行 AppImage 看版本，会在 /tmp 留下失效挂载

这台机器没有 /etc/mtab，直接跑 ~/.orca/orca-linux.AppImage 每次都会在 /tmp 留一个收不掉的挂载点。看版本要用 ~/.orca/orca-serve.sh --version，或者解包后的 ~/.orca/app/resources/bin/orca-ide --version。

### 带 --mobile 启动时，日志里只有手机链接

--mobile 那次启动，serve.log 里只会打印手机配对链接，没有电脑端的。要电脑端链接，先用 --desktop-link 从日志里取更早打印的那条（它不重启）；取不到再 --restart（不带 --mobile）。

### 用电脑端链接生成的二维码，手机扫了配不上

电脑端链接和手机端二维码不是同一种凭据。拿电脑端链接去生成二维码给手机扫，会提示权限不足，必须用 --mobile 打印的手机链接。

### 其他零碎的

改脚本要原子替换。 bash 是边读边执行的，原地改写一个正在运行的看门狗脚本，它会读到半新半旧的内容。先写临时文件再 mv -f。

serve.log 里满屏 dbus 报错。 沙箱没有系统 D-Bus，不影响使用。但这也意味着没有系统密钥环，Orca 的密钥是明文存的；日志涨得也快，记得定时清理。

pgrep -f 会把自己数进去。 让 agent 检查“看门狗是不是只有一个”，它得到的是 2：多出来的那个是它自己执行命令的 shell，命令行里正好含有要找的字符串。不说清楚的话，agent 会去杀“多余”的进程。

开机钩子不能加在文件末尾（这条现在只跟 Tailscale 有关）。 start-sand-box 最后会 exec 或 wait，后面的内容永远不会执行。钩子要插在这之前。

连接走了中继。 我的 MacBook 到 grok-bot 目前走的是 Tailscale 新加坡中继而不是直连，延迟偏高，还没解决。

## 常见问题

这些问题来自 𝕏 上讨论这套玩法的评论区。

https://x.com/app_sail/status/2106003366749126914

### 出口 IP 是固定的吗？

要分两路看。我实测下来，访问 api.anthropic.com 和 console.anthropic.com 时，出口连续几天都是同一个美国 IP，是 Cloudflare 在弗吉尼亚一带机房的共享出口；访问 claude.ai 和其他网站时，走的是每次都会变的地址。Claude Code 主要连的是 API 那一路，所以它看到的出口是稳定的，地区也一直是美国。

但这是共享出口，不是你独占的“原生 IP”。评论区有人说用它注册会被秒封、地址池已经被标记，我自己没遇到，也没法替别人验证。我的看法是，IP 变动本身不是主要风险，更大的风险是出口落在不支持的地区、短时间内在差别很大的国家之间来回跳、多人共用账号，以及付款信息可疑。想要一个完全属于自己的固定出口，只能自己买 VPS。

### 那直接用 VPS 行不行？

行，而且更简单。VPS 有 systemd，不会被平台定期换成新实例，Tailscale 的看门狗和 Orca 的定时任务都可以换成 systemd 服务。Orca + Tailscale + Claude Code 这三层的搭法不变。英文圈里常见的就是这种：一台 Hetzner 服务器，笔记本、手机、服务器三端都装 Orca，用 Tailscale 连起来，在家开的项目路上接着做；服务器上的 orca serve 直接注册成一个 systemd 服务。

我把自己挑 VPS 时做的功课整理成了一个页面：VPS Picks · 精选 Claude Code VPS。

它只收适合跑 Claude Code 的机器，思路是“主力机 + 代理机（可选）”：8 GB 内存的主力机放在 Claude 支持的地区，用来跑 Orca 和 Claude Code；再配一台同城、带回国优化线路（CN2 GIA、9929、CMIN2 等）的最低配小机器做代理，国内经它连主力机，延迟低。日本、新加坡这类离国内近、Claude 也支持的地区，一台主力机就够。每个套餐都标了月价、线路、测试 IP、三网延迟、是否在 Claude 支持地区和退款政策，可以按自己的网络、机房地区和月价上限筛选，价格是人工核实的。

### 有 VPS 的话还需要 Tailscale 吗？

可以不用，但那样 6768 要自己做 TLS 和访问控制。用 Tailscale 的话，这个端口根本不出现在公网上。

### Grok Bot 的云电脑会杀后台进程吗？

评论区有人反馈任务多了后台会被杀。我这边 tailscaled 和 orca serve 都挂过，所以才要 Tailscale 看门狗，加上 Orca 每 10 分钟一次的定时任务。这台机器 16 GB 内存，我日常开三四个项目的 Claude Code 会话，已经用到 12 GB 左右，再多就要小心了。

### 云电脑会不会哪天被换掉、东西全没了？

会，Grok Bot 自动更新时就会换一台新的。这正是本文要解决的问题，见“Grok Bot 自动更新之后全没了”。

### 已经能 SSH 了，为什么还要 Orca？

SSH 加 tmux 也能做到“断线不丢会话”，喜欢终端的人完全可以这么用。Orca 多出来的是：一眼看到所有项目里每个 agent 在干活还是在等人、电脑和手机看到同一个会话、以及 Grok Bot 能通过 orca CLI 指挥这些会话。

### Orca 托管的是会话还是账号凭证？

是会话。Claude 的登录状态在云电脑的 ~/.claude/ 里，MacBook 上不存 Claude 的凭证，只存 Orca 的配对信息。多个设备连上来看到的是同一个终端，同时打字会互相干扰，轮流用就没问题。

### 代码都在云电脑上，怎么拿回本地？

最省事的是 git：让 Claude Code 在云上提交、推送，本地拉取。想要实时同步文件，可以在 tailnet 里跑 Syncthing，我自己就是这么同步笔记的。

### 起的网页服务怎么预览？

让服务监听在 Tailscale 网卡上，MacBook 浏览器打开 http://grok-bot:<端口>。localhost 指的是云电脑自己。

### 订阅 Claude 怎么付款？

见第二步的“订阅 Pro”：提前把账单地址存进云电脑 Chrome 的 profile，付款页自动填充，卡号自己输。我用的是 Mercury 的卡。

## 更新之后的恢复清单

```bash
sudo ~/.tailscale/bootstrap-tailscale.sh   # 重装 Tailscale，还原登录状态和 SSH host key
~/.orca/orca-serve.sh                      # 补防火墙规则，拉起 orca serve
~/check-after-update.sh                    # 只读检查，逐项打印 ✅ / ❌
```

三条都可以重复执行，正常情况下一条都不用手动跑：第一步那个 Bot 的定时任务通常几分钟内会把 Tailscale 自动恢复，没恢复就手动跑第一条命令；“Auto-start Orca” 每 10 分钟检查一次，会把 orca serve 拉起来。Orca 的程序、配置和配对记录都在 home 里，不用重装。正常情况下两者没有先后顺序要求：配对地址用的是 grok-bot 这个名字，serve 启动时不需要 Tailscale 已经就绪。更新把 iptables 也清掉了也没关系：orca-serve.sh 会自己用 apt 把 iptables 装回来；防火墙规则设不好时，它不会启动 orca serve，而是报错退出，等下一次运行再试。

升级 Orca：重新执行第三步的下载命令覆盖 ~/.orca/orca-linux.AppImage，再运行 ~/.orca/orca-serve.sh --restart。脚本会解包到新的 ~/.orca/app-<版本>-<时间>，把 ~/.orca/app 链接切过去，旧目录先保留；后台终端守护进程会继续用旧版本，直到它自己重启，所以升级挑没有任务在跑的时候做。

日志位置：~/orca-setup/serve.log、/var/log/tailscaled-autostart.log。

## 附录：脚本全文

附录 A 就是我这台机器上正在用的版本，原样贴出；附录 B 是从我自用的自检脚本里精简出来的通用版，去掉了时区、个人项目这些只跟我有关的检查。它们假设用户名是 box、home 是 /home/box，这是 Grok Bot 云电脑的现状；平台以后改了，脚本也要跟着改。

两个脚本都以 box 身份运行，都不碰开机脚本 start-sand-box。附录 A 只在补防火墙规则（以及缺 iptables 时用 apt 安装）时用 sudo -n；没有免密 sudo 就跳过这一步，打印警告后照常启动；有免密 sudo 但规则设不好时，不启动 orca serve；附录 B 读防火墙规则时也用 sudo -n（只读），没有免密 sudo 时这两项会报 ❌。使用前请自己读一遍。

Tailscale 那部分的脚本不在这里，由第一步的 Bot 负责生成和维护。

### 附录 A：~/.orca/orca-serve.sh

> （脚本全文见文末「附录脚本」A）

Orca 的启动脚本：补防火墙规则（缺 iptables 就先装），规则设不好不启动；orca serve 没在跑就拉起来，已经在跑就什么都不做。第三步保存它，“Auto-start Orca” 定时任务每 10 分钟运行一次。

### 附录 B：~/check-after-update.sh

只读自检脚本。Orca 的配对地址从附录 A 的 ADDR= 那一行读取，serve 是否在跑按 ~/.orca/serve.pid 判断。

> （原文此处内嵌附录 B 脚本全文，见文末「附录脚本」B）

---

## 附录脚本

### A. `~/.orca/orca-serve.sh`（Orca 启动脚本，"Auto-start Orca" 每 10 分钟运行）

```bash
#!/usr/bin/env bash
# ~/.orca/orca-serve.sh — orca serve 没在跑就拉起来；已经在跑就什么都不做。可以反复执行，交给定时任务跑。
#
#   ~/.orca/orca-serve.sh                没在跑就启动（日志里打印电脑端配对链接）
#   ~/.orca/orca-serve.sh --mobile       重启一次，日志里打印手机二维码/链接（已配对的设备和会话不受影响）
#   ~/.orca/orca-serve.sh --restart      重启一次，日志里重新打印电脑端链接；换了新 AppImage 后也用它
#   ~/.orca/orca-serve.sh --desktop-link 不重启，从日志里找最新的电脑端配对链接
#   ~/.orca/orca-serve.sh --version      打印已解包的 Orca 版本
#
# 注意：用 --mobile 启动之后，不带参数的运行看到 6768 在监听就直接退出，serve 会一直保持 mobile 模式，
# 日志里最新的只有手机链接。要电脑端链接：先试 --desktop-link（更早打印的链接只要没用过就仍然有效），
# 不行再 --restart。
#
# AppImage 只在解包（--appimage-extract）时执行一次；serve 和 --version 都从解包目录运行。
# 直接运行 AppImage 会走 FUSE 挂载，这台机器没有 /etc/mtab，退出后会留下失效的 /tmp/.mount_orca-*。
set -u
ORCA_DIR="$HOME/.orca"
APPIMAGE="$ORCA_DIR/orca-linux.AppImage"   # arm64 机器下载 orca-linux-arm64.AppImage，但同样保存成这个文件名
APPDIR="$ORCA_DIR/app"                     # 指向 app-<版本>-<时间> 的符号链接（老安装可能是普通目录）
PORT=6768
ADDR=grok-bot                              # Tailscale MagicDNS 名字；节点名不同就只改这一行
LOG="$HOME/orca-setup/serve.log"
PIDF="$ORCA_DIR/serve.pid"
LOCK="$ORCA_DIR/orca-serve.lock"

listening() { ss -ltn "sport = :$PORT" | grep -q LISTEN; }
cli() { echo "$APPDIR/resources/bin/orca-ide"; }

download_hint() {
  local asset=orca-linux.AppImage
  case "$(uname -m)" in aarch64|arm64) asset=orca-linux-arm64.AppImage ;; x86_64|amd64) ;; *) echo "不支持的架构 $(uname -m)" >&2 ;; esac
  echo "下载：curl -fL -o $APPIMAGE https://github.com/stablyai/orca/releases/latest/download/$asset && chmod +x $APPIMAGE" >&2
}

case "${1:-}" in
  --version)
    if [ -x "$(cli)" ]; then
      echo "Orca $("$(cli)" --version 2>/dev/null | tail -1)（$(readlink -f "$APPDIR")）"
      [ "$APPIMAGE" -nt "$APPDIR/" ] && echo "提示：$APPIMAGE 比解包目录新，--restart 后生效"
    else echo "还没解包；运行一次 $0" >&2; exit 1; fi
    exit 0 ;;
  --desktop-link)
    python3 - "$LOG" "$HOME/.config/orca/orca-devices.json" <<'PY'
import base64, json, re, sys
log, devf = sys.argv[1], sys.argv[2]
s = open(log, errors="ignore").read()
def scope(u):
    c = u.split("code=", 1)[1]
    try: return json.loads(base64.urlsafe_b64decode(c + "=" * (-len(c) % 4)))
    except Exception: return {}
links = [(m.start(), m.group(0)) for m in re.finditer(r"orca://pair\?code=[A-Za-z0-9_-]+", s)]
starts = [m.start() for m in re.finditer(r"^=== .* start orca serve.*===$", s, re.M)]
last_start = starts[-1] if starts else 0
desk = [(p, u) for p, u in links if scope(u).get("scope") == "runtime"]
if not desk: sys.exit("日志里没有电脑端配对链接；运行 ~/.orca/orca-serve.sh --restart")
p, u = desk[-1]; d = scope(u)
if p < last_start:
    print("注意：最近一次启动是 --mobile，下面这条是更早一次启动打印的电脑端链接。", file=sys.stderr)
try: ids = {x.get("deviceId") for x in json.load(open(devf))}
except Exception: ids = set()
print(("授权仍在，可以用。" if d.get("pairedDeviceId") in ids else "这条链接的授权已经不在了，请运行 --restart。") + f" 地址 {d.get('endpoint')}", file=sys.stderr)
print(u)
PY
    exit $? ;;
  ""|--mobile|--restart) ;;
  *) sed -n '2,13p' "$0"; exit 2 ;;
esac

mkdir -p "$HOME/orca-setup"
exec 9>"$LOCK"
flock -n 9 || exit 0                       # 同一时间只跑一个

# 6768 只放行本机和 tailnet：三条规则放在 INPUT 链的第 1、2、3 条（排在 Tailscale 的 -j ts-input 前面）。
# 更新后规则会丢，所以每次都检查；已经是这三条且顺序对就什么都不做。
# iptables 平时随 Tailscale 的安装包一起装上；更新后它可能还没回来，这里缺了就自己用 apt 装。
# 有免密 sudo 时“失败即不启动”：IPv4 规则必须设好；IPv6 只有在 ip6tables 连 INPUT 链都读不到
# （内核没有 IPv6 netfilter）时才只警告，读得到却设不好同样算失败。规则设不好时不启动、不重启 serve，
# 退出码 1 让定时任务报出来；已经在跑的 serve 不会被停掉。没有免密 sudo 时没法设防火墙，只警告，照常启动。
R1="-i lo -p tcp -m tcp --dport $PORT -j ACCEPT"
R2="-i tailscale0 -p tcp -m tcp --dport $PORT -j ACCEPT"
R3="-p tcp -m tcp --dport $PORT -j DROP"
apt_iptables() { sudo -n env DEBIAN_FRONTEND=noninteractive apt-get "$@" >/dev/null 2>&1 9>&-; }
fw_ensure() {                              # $1 = iptables / ip6tables；返回 0 = 规则就位
  local fw=$1 rules
  rules="$(sudo -n $fw -S INPUT 2>/dev/null | sed -n 's/^-A INPUT //p')"
  if [ "$(head -3 <<<"$rules")" = "$(printf '%s\n%s\n%s' "$R1" "$R2" "$R3")" ] &&
     [ "$(grep -c -- "--dport $PORT " <<<"$rules")" = 3 ]; then return 0; fi
  for r in "$R1" "$R2" "$R3"; do while sudo -n $fw -D INPUT $r 2>/dev/null; do :; done; done
  if sudo -n $fw -I INPUT 1 $R3 && sudo -n $fw -I INPUT 1 $R2 && sudo -n $fw -I INPUT 1 $R1; then
    echo "已重设 $fw 的 $PORT 规则"; return 0
  fi
  echo "错误：$fw 的 $PORT 规则没有设好" >&2; return 1
}
FW=nosudo                                  # nosudo / ok / fail
if sudo -n true 2>/dev/null; then
  if ! sudo -n iptables -S INPUT >/dev/null 2>&1 || ! sudo -n sh -c 'command -v ip6tables' >/dev/null 2>&1; then
    echo "没有可用的 iptables，用 apt 安装……"
    apt_iptables install -y -qq iptables || { apt_iptables update -qq && apt_iptables install -y -qq iptables; } ||
      echo "错误：apt 安装 iptables 失败（apt 可能正被别的任务占用，下次运行会再试）" >&2
  fi
  FW=ok
  fw_ensure iptables || FW=fail
  if sudo -n ip6tables -S INPUT >/dev/null 2>&1; then fw_ensure ip6tables || FW=fail
  elif ! listening; then echo "警告：ip6tables 读不到 INPUT 链（这台机器可能没有 IPv6 netfilter），只靠 IPv4 规则" >&2; fi
fi
if [ "$FW" = fail ]; then
  if listening; then
    echo "错误：$PORT 的防火墙规则设不好，orca serve 还在跑但没有保护；不会停掉或重启它，请手动检查" >&2
  else
    echo "错误：$PORT 的防火墙规则设不好，为了不把端口裸露出去，不启动 orca serve" >&2
  fi
  exit 1
fi

case "${1:-}" in
  --mobile|--restart)
    # 只停自己上次启动的那一组进程（setsid 让它们在同一个会话里）。不要 pkill -f orca：
    # 那会连终端守护进程和正在跑的 Claude Code 一起杀掉。守护进程在别的会话里，这里碰不到它。
    [ -s "$PIDF" ] && pkill -s "$(cat "$PIDF")" 2>/dev/null
    for _ in $(seq 30); do listening || break; sleep 1; done ;;
esac

listening && exit 0
[ "$FW" = nosudo ] && echo "警告：没有免密 sudo，设不了 $PORT 的防火墙规则；照常启动 orca serve，请确认这台机器的 $PORT 不在公网上" >&2

# 第一次运行，或者换了新的 AppImage：解包到新的 app-<版本>-<时间> 目录，再原子地切换 app 链接。
# 旧目录不删（后台守护进程可能还在用），只清理比上一个更老的、且没有进程在用的目录。
if [ ! -x "$(cli)" ] || [ "$APPIMAGE" -nt "$APPDIR/" ]; then
  [ -x "$APPIMAGE" ] || { echo "找不到 $APPIMAGE" >&2; download_hint; exit 1; }
  ts=$(date +%Y%m%d%H%M%S); tmp="$ORCA_DIR/.extract-$ts"
  rm -rf "$tmp"; mkdir -p "$tmp"
  ( cd "$tmp" && "$APPIMAGE" --appimage-extract >/dev/null 2>&1 ) 9>&- && [ -x "$tmp/squashfs-root/resources/bin/orca-ide" ] \
    || { rm -rf "$tmp"; echo "解包失败（AppImage 损坏，或架构不对）" >&2; download_hint; exit 1; }
  ver=$("$tmp/squashfs-root/resources/bin/orca-ide" --version 2>/dev/null 9>&- | tail -1 | tr -cd '0-9A-Za-z.-')
  new="$ORCA_DIR/app-${ver:-unknown}-$ts"
  mv "$tmp/squashfs-root" "$new" && rmdir "$tmp" && touch "$new"
  prev=""
  if [ -L "$APPDIR" ]; then prev="$(readlink -f "$APPDIR")"
  elif [ -d "$APPDIR" ]; then                # 老安装：app 是普通目录，第一次升级时改名保留
    prev="$ORCA_DIR/app-legacy-$ts"; mv "$APPDIR" "$prev"
    echo "警告：旧的 $APPDIR 已改名为 $prev；从旧路径启动的后台进程之后再按路径加载文件时，会读到新版本" >&2
  fi
  ln -sfn "$(basename "$new")" "$ORCA_DIR/.app.tmp" && mv -Tf "$ORCA_DIR/.app.tmp" "$APPDIR"
  echo "已切换到 $(basename "$new")"
  [ -n "$prev" ] && echo "警告：后台终端守护进程会一直用旧版本，直到它自己退出或重启；旧目录 $(basename "$prev") 保留" >&2
  for d in "$ORCA_DIR"/app-*; do              # 只留当前和上一个
    [ -d "$d" ] && [ ! -L "$d" ] || continue
    [ "$d" = "$new" ] || [ "$d" = "$prev" ] && continue
    if grep -qsF "$d/" /proc/[0-9]*/cmdline 2>/dev/null || ls -l /proc/[0-9]*/exe 2>/dev/null | grep -qF "$d/"; then echo "保留 $(basename "$d")：还有进程在用" >&2; else rm -rf "$d"; fi
  done
fi

REAL="$(readlink -f "$APPDIR")"            # 用真实路径启动，以后切换链接不会影响已经在跑的进程
echo "=== $(date '+%F %T') start orca serve ${1:-} ($(basename "$REAL")) ===" >>"$LOG"
setsid nohup "$REAL/resources/bin/orca-ide" serve --port $PORT --pairing-address $ADDR \
  $([ "${1:-}" = "--mobile" ] && echo --mobile-pairing) >>"$LOG" 2>&1 </dev/null 9>&- &
echo $! >"$PIDF"

for _ in $(seq 60); do
  if listening; then
    echo "orca serve 已在 $PORT 监听（Orca $("$REAL/resources/bin/orca-ide" --version 2>/dev/null 9>&- | tail -1)）"
    [ "${1:-}" = "--mobile" ] && echo "现在是手机配对模式；要电脑端链接用 --desktop-link，或者 --restart"
    exit 0
  fi
  sleep 1
done
echo "60 秒内没等到 $PORT 监听，看 $LOG" >&2; exit 1
```

### B. `~/check-after-update.sh`（更新后只读自检）

```bash
#!/usr/bin/env bash
# Update 后的一键检查：只读，不改任何东西
export PATH="$HOME/.local/bin:$PATH"
FIX="~/.orca/orca-serve.sh"
PORT=6768
ADDR=$(sed -n 's/^ADDR=\([^ #]*\).*/\1/p' ~/.orca/orca-serve.sh 2>/dev/null | head -1)   # 配对地址以 orca-serve.sh 为准
ok=0; bad=0
pass(){ echo "  ✅ $1"; ok=$((ok+1)); }
fail(){ echo "  ❌ $1"; [ -n "$2" ] && echo "     → $2"; bad=$((bad+1)); }
echo "== Tailscale =="
if command -v tailscale >/dev/null; then
  ip=$(tailscale ip -4 2>/dev/null | head -1)
  [ -n "$ip" ] && pass "已连接 tailnet，IP $ip" || fail "tailscale 已装但未连接" "sudo ~/.tailscale/bootstrap-tailscale.sh"
else fail "tailscale 未安装" "sudo ~/.tailscale/bootstrap-tailscale.sh"; fi
pgrep -f "tailscaled-autostart --watch" >/dev/null && pass "tailscale 看门狗在运行" || fail "tailscale 看门狗未运行" "sudo ~/.tailscale/bootstrap-tailscale.sh"
echo "== Orca =="
[ -x ~/.orca/orca-linux.AppImage ] && pass "AppImage 在 ~/.orca/" || fail "~/.orca/orca-linux.AppImage 不见了" "按第三步重新下载"
v=$(orca --version 2>/dev/null | tail -1); [ -n "$v" ] && pass "orca 命令可用（$v）" || fail "orca 命令不可用" "$FIX"
spid=$(cat ~/.orca/serve.pid 2>/dev/null)   # orca-serve.sh 记下的 serve 进程号；app 目录可能带版本号
[ -n "$spid" ] && kill -0 "$spid" 2>/dev/null && tr '\0' ' ' <"/proc/$spid/cmdline" 2>/dev/null | grep -qE '/\.orca/app[^/]*/orca-ide .*serve' \
  && pass "orca serve 在运行（pid $spid）" || fail "orca serve 未运行" "$FIX"
ss -ltn 2>/dev/null | grep -q ":$PORT " && pass "端口 $PORT 在监听" || fail "端口 $PORT 没有监听" "$FIX"
if [ -z "$ADDR" ]; then fail "从 ~/.orca/orca-serve.sh 读不到 ADDR=" "$FIX"
else grep -a "Advertised endpoint" ~/orca-setup/serve.log 2>/dev/null | tail -1 | grep -qF "ws://$ADDR:$PORT" && pass "配对地址是 $ADDR" || fail "配对地址不是 $ADDR" "~/.orca/orca-serve.sh --restart"; fi
echo "== Claude Code =="
if v=$(claude --version 2>/dev/null); then pass "claude 可运行：$v"
else fail "claude 无法运行" "curl -fsSL https://claude.ai/install.sh | bash"; fi
echo "== 防火墙 =="
want=$(printf '%s\n' "-i lo -p tcp -m tcp --dport $PORT -j ACCEPT" "-i tailscale0 -p tcp -m tcp --dport $PORT -j ACCEPT" "-p tcp -m tcp --dport $PORT -j DROP")
for fw in iptables ip6tables; do
  if ! rules=$(sudo -n $fw -S INPUT 2>/dev/null); then fail "$fw：读不到 INPUT 链" "需要免密 sudo；有的话运行 $FIX"; continue; fi
  rules=$(sed -n 's/^-A INPUT //p' <<<"$rules")
  [ "$(head -3 <<<"$rules")" = "$want" ] && [ "$(grep -c -- "--dport $PORT " <<<"$rules")" = 3 ] \
    && pass "$fw：$PORT 的三条规则在链首、顺序正确（lo 放行 → tailscale0 放行 → 丢弃）" \
    || fail "$fw：$PORT 的规则缺失、重复或不在链首第 1–3 条" "$FIX"
done
echo; echo "结果：$ok 项正常，$bad 项有问题"
[ "$bad" -eq 0 ]
```
