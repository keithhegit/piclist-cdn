# Grok Bot 云电脑搭 Claude Code＋Orca＋Tailscale

> 来源：Asa（@app_sail）X Article，2026-10-09｜原标题「把这篇文章丢给 Grok Bot：给你注册 Claude，搭配 Orca + Tailscale，打造 7×24 在线的 Claude Code 云主机」｜https://x.com/app_sail/status/2108523630900748335
> 依据：帖内 Article 全文（一手源），非转述。文中 IP、主机名、日期都是作者机器上的例子，别照抄。

## 一句话定位

把 Grok Bot 自带的美国云电脑（8 核 / 16 GB，无 systemd，会自动更新换实例）当成一台 7×24 在线的 Claude Code 服务器：用 Tailscale 组网，用 Orca 的 Remote Server 把会话同步到 MacBook 和手机，再让 Grok Bot 用 orca CLI 替你派活。重点不在“装上”，而在于 **Grok Bot 自动更新后还能自己恢复**。

## 上手顺序

**先做三件事（需要人）**
1. 设置 → General → Timezone 改成云电脑出口所在的美国时区（作者是 America/New_York）。时区是所有 Bot 共用的，已在跑的程序要重启才会生效。
2. 保持“云电脑流量走本机代理”的开关**关闭**，出口要用它自己的美国出口。
3. 添加 Bot「SSH to Grok via Tailscale」：https://x.ai/bot/BrViAOWzDSiAjBLqUnBgA →「Add to Grok Bot」。

**四步搭建**（让 Grok Bot 每做完一步就停下汇报）
1. **Tailscale**：由上面那个 Bot 自动装。节点名固定为 `grok-bot`，带看门狗、每 5 分钟一次的「Auto-restore Tailscale」，以及密钥过期提醒。需要人：点授权链接，把 ACL 贴到 Tailscale 后台。
2. **Claude**：在云电脑浏览器里注册 → 用官方脚本装 Claude Code → 订阅 Pro/Max（免费号不能用 Claude Code）→ `claude auth login`。注册、填卡、点 Subscribe、登录都由人接管电脑完成。
3. **Orca**：下载 AppImage，放好附录 A 的 `orca-serve.sh`，建「Auto-start Orca」（每 10 分钟一次），再放好附录 B 的自检脚本，跑到全 ✅ 为止。
4. **连设备（需要人）**：MacBook 在 Orca 的 Settings → Remote Orca Servers → + Add Server 里粘贴配对链接；手机装 Tailscale 和 Orca App，选 Pair 后扫码。

**第五步，日常指挥**：在 Grok Bot 对话框里让它用 `orca` CLI 查看、派活、等结果、读输出，再给你汇总。

## 能力表

| 环节 | 需要人 | Grok Bot 可做 |
|---|---|---|
| 时区 / 代理开关 / 添加 Tailscale Bot | ✅ | — |
| 安装 Tailscale、看门狗、恢复任务 | 点授权、贴 ACL、删掉旧的 grok-bot 节点 | ✅（Tailscale Bot 完成） |
| 注册 Claude | 填邮箱、验证码、密码（接管“打开电脑”） | 打开登录页 |
| 安装 Claude Code | — | ✅ 官方脚本，检查 PATH |
| 订阅 Pro / Max | 输卡号、点 Subscribe | 提前把账单地址存进 Chrome，让表单自动填 |
| `claude auth login` | 浏览器授权，把授权码贴回终端 | 运行命令、打开链接 |
| Orca 下载、启动脚本、防火墙、定时任务、自检 | — | ✅ |
| MacBook 配对 / 手机扫码 / 最终验收 | ✅ | 给出链接和二维码 |
| 日常派活、催进度、汇总、每日账号巡检 | 定规矩（发送/发布/花钱/改生产必须问人） | ✅ |

## 可复制 Prompt 与关键命令

**总指令**
```
按这篇文章一步一步执行，每做完一步停下来向我汇报。
```

**注册**
```
注册一个 Claude 账号
```

**装 Claude Code**
```
用官方脚本安装 Claude Code，命令是 curl -fsSL https://claude.ai/install.sh | bash。确认 ~/.local/bin 在 PATH 里（~/.profile 和 ~/.bashrc 都要有），告诉我版本号。
```
用官方脚本，不要用 `npm i -g`：前者装在 home 里，更新后还在；npm 全局目录在 home 外，更新一次就没了。

**登录**
```
在终端里运行 claude auth login，把它给出的授权链接在这台电脑的浏览器里打开，然后把电脑交给我，我自己登录和授权。
```
验收命令：`bash -lc 'command -v claude'` 应指向 `~/.local/bin/claude`；`claude auth status` 显示用 claude.ai 订阅登录（不是 API key），订阅类型为 Pro 或 Max。

**装 Orca（四行）**
```bash
mkdir -p ~/.orca ~/orca-setup
case "$(uname -m)" in aarch64|arm64) a=orca-linux-arm64.AppImage ;; *) a=orca-linux.AppImage ;; esac
curl -fL -o ~/.orca/orca-linux.AppImage https://github.com/stablyai/orca/releases/latest/download/$a
chmod +x ~/.orca/orca-linux.AppImage
```
```
把附录 A 原样存成 ~/.orca/orca-serve.sh，加可执行权限后运行，把输出发给我。再建一个每 10 分钟运行它一次的定时任务 "Auto-start Orca"，没出错就不用通知我。
```
（两个脚本全文见 transcript.md 的「附录脚本」。）

`orca-serve.sh` 的参数：不带参数＝没在跑就启动；`--restart`＝重启并打印电脑端配对链接（换了新 AppImage 后也用它）；`--mobile`＝打印手机配对码；`--desktop-link`＝不重启，从日志里取电脑端链接；`--version`＝查版本。

**自检**
```
把本文附录 B 的自检脚本原样保存为 ~/check-after-update.sh，加可执行权限，运行它，把结果发给我。再写一份 ~/after-update.md，记下更新之后要运行的三条命令：sudo ~/.tailscale/bootstrap-tailscale.sh、~/.orca/orca-serve.sh、~/check-after-update.sh。
```

**更新后的恢复清单**（每条都可以重复跑，没有先后顺序）
```bash
sudo ~/.tailscale/bootstrap-tailscale.sh   # 重装 Tailscale，还原登录状态和 SSH host key
~/.orca/orca-serve.sh                      # 补防火墙规则，拉起 orca serve
~/check-after-update.sh                    # 只读检查，逐项打印 ✅ / ❌
```

**连设备**
```
Mac 和 iPhone 怎么链接上 Orca Remote Server
```

**让 orca CLI 派活（第五步示例）**
```
先运行 orca agent-context，读懂这台机器上 orca CLI 的用法。以后我让你查看或指挥 Claude Code，都通过 orca CLI 来做。用 orca worktree ps 看一下现在各个项目里 Claude Code 的状态，哪些在跑、哪些在等我。
```
```
先用 orca worktree ps 找到【项目名】对应的 Claude Code 终端，让它跑一遍测试。等它空闲后把终端输出读回来，给我一个三行以内的总结。
```
```
在【项目名】新开一个工作区和一个 Claude Code 会话，让它修 issue #12，改完后不要提交，把 diff 摘要发给我。
```
常用命令：`orca worktree ps`、`orca terminal list / read / send`、`orca terminal wait --for tui-idle`（`--for` 必填）、`orca worktree create --name <名字> --agent claude`、`orca orchestration …`、`orca search <关键词>`。

**作者建议的四个进阶用法**：① 把“发指令 → 等空闲 → 读输出”存成一个 skill；② 多个 Bot 时只留一个负责分派和汇总；③ 写进长期指令：发送、发布、花钱、改生产环境必须先问人；④ 每天自动查一次 `claude auth status`，再随机给 Claude Code 发一句 hello，记到 `~/.claude-hello/hello.log`，出现异常就通知。

## 坑

- **自动更新会清空环境**：Grok Bot 更新相当于换一台新实例。apt 装的包、/opt、/usr/local/bin、/var/lib/tailscale，以及 start-sand-box 的改动全部清空。home 会从快照还原，但只有 root 能读的文件回不来。原则：home 外的东西都在 home 里留安装包和恢复脚本；代码及时推到 git；项目最好放在 /workspace。
- **千万别 `pkill -f orca`**：一个 orca 进程管着所有 Claude Code 会话，会一起被杀掉。重启只能用 `~/.orca/orca-serve.sh --restart` 或 `--mobile`，而且要先说明原因、征得同意。
- **手机码和电脑链接不能混用**：电脑端用完整权限的链接，手机端要用 `--mobile` 打印的码。拿电脑链接生成二维码给手机扫，会提示权限不足。用 `--mobile` 启动后，日志里只有手机链接；要电脑链接，先试 `--desktop-link`，不行再 `--restart`。
- **6768 端口的防火墙**：端口只能在本机和 tailnet 内可达。iptables 是跟着 Tailscale 装上的，10/9 一次更新后，Orca 比 Tailscale 先恢复，端口约 7 分钟没有防护。新脚本缺 iptables 会自己用 apt 装，规则设不好就不启动。
- **Tailscale IP 会变**：重新登录等于新节点，IP 会换。所以配对要用主机名 `grok-bot`，不要用 100.x 的 IP。重新登录前先在后台删掉旧节点，否则新节点会变成 `grok-bot-1`，这时要改脚本里 `ADDR=` 那一行（脚本唯一允许改的地方）。
- **Orca 里又让你登录**：账号没掉，是命令行登录跳过了首次设置向导。备份 `~/.claude.json` 后，把 `hasCompletedOnboarding` 设为 true 即可。
- **看门狗起不来（flock）**：被拉起的子进程继承了锁的文件描述符，旧看门狗死后锁仍被占着，新看门狗就静默退出。解法：每个子进程加 `9>&-` 把锁的 fd 关掉。
- 其他：直接运行 AppImage 会在 /tmp 留下失效挂载（看版本用 `orca-serve.sh --version`）；`pgrep -f` 会把自己执行的那条命令也算进去；改正在运行的脚本要先写临时文件再 `mv -f`；没有 D-Bus 所以 Orca 的密钥是明文存的；serve.log 涨得快，要定期清；Tailscale 每天会掉线几次，看门狗除了查进程在不在，还要查控制面认不认为节点在线；作者的连接目前走新加坡中继，延迟偏高。

## 适合谁 / 风险声明

- **适合**：想要一个与本机网络无关、7×24 在线的 Claude Code 环境，经常在电脑和手机之间切换，愿意折腾的人；已经在用 Grok Bot、想让它当总管指挥编码 agent 的人。
- **不适合**：想要“稳定不折腾”的人。作者的建议是直接买 VPS（有 systemd，不会被换实例），三层搭法不变。
- **风险**：**这不是防封教程**。有人这样用了一个多月正常，也有人在 Grok Bot 上登录后没用就被封。Anthropic 有地区条款，出口是 Cloudflare 共享出口（访问 API 时 IP 稳定，访问 claude.ai 时会变），不是独占的原生 IP。使用 Anthropic 服务的风险自负。
- **安全**：机器上的 Claude Code 以 `--dangerously-skip-permissions` 运行，Grok Bot 又能直接给它下指令，中间没有闸门，所以：Tailscale ACL 不能省；6768 不能暴露到公网；配对码、状态文件、密钥不要贴进聊天；发送、发布、花钱、改生产必须问人。

## 章节导航（原文）

1. 开头：一句话说明、怎么用、需要你确认的事项
2. 为什么折腾这个（封号潮、真实环境 > 伪装）
3. 先做三件事（需要人）
4. 整体架构 + 四步总览
5. 给 Grok Bot 的执行说明（10 条执行规矩）
6. 第一步 Tailscale → 第二步 Claude 注册/订阅/登录 → 第三步 Orca → 第四步 MacBook/手机配对
7. 第五步：让 Grok Bot 指挥 Claude Code（orca CLI + 四个进阶用法）
8. 踩过的坑（IP 变化、自动更新、看门狗、掉线、重复登录、6768 防火墙、pkill 等）
9. 常见问题（出口 IP、VPS、要不要 Tailscale、杀后台进程、SSH vs Orca、凭证、代码同步、预览、付款）
10. 更新之后的恢复清单 / 升级 Orca / 日志位置
11. 附录 A `orca-serve.sh`、附录 B `check-after-update.sh`

## 关键外链

- SSH to Grok via Tailscale（Bot）：https://x.ai/bot/BrViAOWzDSiAjBLqUnBgA
- 作者整理的 VPS 精选：https://vps.appsail.dev/
- Orca 发布页：https://github.com/stablyai/orca/releases（AppImage：`/releases/latest/download/orca-linux.AppImage`，arm64 用 `orca-linux-arm64.AppImage`）
- Claude Code 官方安装：`curl -fsSL https://claude.ai/install.sh | bash`
- FAQ 来源讨论帖：https://x.com/app_sail/status/2106003366749126914
