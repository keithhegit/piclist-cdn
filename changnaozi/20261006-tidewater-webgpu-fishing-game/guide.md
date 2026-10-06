# Tidewater：AI（Opus 5.5）生成的纯 WebGPU + WGSL 浏览器海岛钓鱼游戏，开源可二开

> **元信息**
> - 来源：微信公众号「柳杉前端」｜作者署名：柳杉前端
> - 原标题：Claude Opus 5.5 + WebGPU 做出来的海岛钓鱼游戏，已经开始像一款真正的游戏了
> - 原文：https://mp.weixin.qq.com/s/OioiV0lB-DZqmW-WQivR-Q
> - 发布：2026-09-24 19:04（北京时间）｜字数：约 3,900 字（不含代码块）
> - 主题仓库：https://github.com/dgreenheck/tidewater（MIT，1,119 ⭐ / 247 forks，2026-10-06 查询）
> - 在线版：https://dgreenheck.github.io/tidewater/（HTTP 200，无需登录）
> - 类型：开源项目解读 / 浏览器 3D 游戏 / WebGPU 图形学 / AI 编程能力案例
> - 整理：2026-10-06，全文见同目录 `transcript.md`

---

## 一句话定位

一个据仓库描述"用 Opus 5.5 打造"的浏览器海岛钓鱼游戏，没用 Three.js 等框架，直接基于 WebGPU + WGSL 自研小型渲染引擎（FFT 海洋、体积云、大气散射、空间音频、钓鱼状态机、经济/装备成长全都有），MIT 开源，`npm install && npm run dev` 就能本地跑起来，适合拿来做 WebGPU 游戏的二开底座。

---

## 仓库与在线版本（二开用）

### A. 文章中出现的全部链接（原样照录）

| # | 链接（原文原样） | 在文中位置 / 形式 | 验证状态（2026-10-06） |
|---|---|---|---|
| 1 | `@dgreenheck/tidewater` | 开头第一句，纯文本（非链接），指 GitHub 用户/仓库名 | 对应 #3，仓库存在 |
| 2 | https://dgreenheck.github.io/tidewater/ | 「一、游戏核心逻辑」开头 + 文末「在线体验：」，纯文本 | ✅ HTTP 200，GitHub Pages 静态站，页面 `<title>Tidewater</title>` |
| 3 | https://github.com/dgreenheck/tidewater | 文末「项目地址：」，纯文本 | ✅ HTTP 200 |
| 4 | https://github.com/dgreenheck/tidewater.git | 「八、如何在本地运行」代码块里的 `git clone` | ✅ 可 clone（200，重定向到 #3）；已实测 `git clone` 成功 |
| — | 视频号嵌入视频（"先预览视频来体验一下海景视觉和音效"） | 文内嵌入，无可复制的外链 URL | 不适用 |
| — | 13 张截图（mmbiz.qpic.cn 微信图床） | 图片无图注，图中没有出现额外 URL | 已人工查看，未发现图内链接 |

- 文章中**没有**出现：GitHub 登录 / OAuth 说明、文档站、一键部署按钮（Vercel/Netlify 等）、Demo 以外的托管版本。
- 文章提到"每次向 main 分支提交代码后，GitHub Actions 会自动构建并部署到 GitHub Pages"，但没给出 workflow 链接。

### B. 是否需要 GitHub 登录

- **在线版不需要任何登录**：纯静态 GitHub Pages 页面，进度存在浏览器本地（README："Progress is saved in the browser"）；源码 `src/` 里没有 login / OAuth 相关代码（已 grep 确认）。
- 只有在 **fork / 提 PR / 用自己仓库部署 Pages** 时才需要你自己的 GitHub 账号。

### C. 仓库事实（来自 GitHub API + 实际 clone，2026-10-06 查询）

| 项 | 值 |
|---|---|
| full name | `dgreenheck/tidewater`（作者 Daniel Greenheck；LICENSE 版权方 DRG Software Solutions LLC） |
| description | Coastal town built with Opus 5.5 |
| homepage | https://dgreenheck.github.io/tidewater/ |
| stars / forks / open issues | 1,119 / 247 / 13 |
| license | MIT（代码）；第三方素材各自保留许可，见 `CREDITS.md` |
| default branch | `main`（另有分支 `perf-and-reflections`，与 main 指向同一 commit `4811ba4`） |
| 创建时间 | 2026-09-24 05:40（北京时间）/ 2026-09-23 14:40 PT |
| last push | 2026-09-25 12:02（北京时间）/ 2026-09-24 21:02 PT |
| 最近 commit | `4811ba4` "Backwash: no ruled line at the draining sheet's edge"（共 48 个 commit） |
| 主语言 | JavaScript（约 3.39 MB）；另有 CSS 61 KB、HTML 10 KB、Python 9 KB、Shell 3 KB |
| 技术栈 | 原生 WebGPU + WGSL（着色器以字符串形式写在 JS 里，没有单独的 .wgsl 文件），Vite 8 构建，无运行时依赖；devDependencies 只有 `vite ^8.3.0`、`webgpu ^0.6.1`（Node 端无头测试用） |
| 规模 | `src/` 下 209 个 JS 文件，约 8.1 万行；`public/` 素材约 53 MB；`test/` 下约 50 个测试/调试脚本 |
| CI/CD | `.github/workflows/deploy.yml`：push 到 `main` 或手动触发 → Node 22 → `npm ci` → `npm run build` → 上传 `dist` → `actions/deploy-pages@v4` |
| 文章提到的文件 | `src/game/Game.js`、`Bites.js`、`CatchMinigame.js`、`FishingRod.js`、`src/engine/Engine.js`、`src/sky/Clouds.js`（1,621 行）、`src/App.js`、`src/main.js`：全部存在 ✅ |

### D. 本地运行 / 部署（README 原文要点）

**环境要求（README）**
- 支持 WebGPU 的浏览器：较新的 Chrome、Edge 或 Safari。
- 性能够用的 GPU：目标是 Apple M5 Pro 上 2560×1267 跑 60 fps，较慢机器靠动态分辨率降渲染。
- 首次加载要编译几百个着色器，可能要一分钟以上，之后浏览器会缓存。

**命令（README "Running locally"，原样）**

```sh
npm install
npm run dev      # http://127.0.0.1:5189
npm run build    # static build in dist/
```

**补充命令（package.json / 文章）**

```bash
git clone https://github.com/dgreenheck/tidewater.git
cd tidewater
npm install
npm run dev
npm test              # node test/game-logic.mjs && node test/engine-smoke.mjs
npm run build
npm run preview
```

**部署（README）**：Every push to `main` deploys to GitHub Pages through `.github/workflows/deploy.yml`。`vite.config.js` 里 `base: './'`，所以构建产物可以放在任何子路径下运行。

**二开时我补充的注意点（我自己的判断，README 和文章都没写）**
- fork 之后，fork 仓库默认不启用 Actions，要手动打开；还要在 Settings → Pages 里把 Source 设成 "GitHub Actions"，deploy.yml 才能发布到 `https://<你的用户名>.github.io/tidewater/`。
- `vite.config.js` 里 server 端口是 `5188`（`strictPort: true`），但 `npm run dev` 的命令行参数 `--port 5189` 会覆盖它，所以实际端口以 5189 为准。
- CI 用的是 Node 22，本地建议也用 Node 22+（Vite 8）。

**URL 调试参数（README，原样）**：在 URL 后加，例如 `?fly&noAudio`

| Option | Effect |
|---|---|
| `fly` | Start in the free camera |
| `noAudio` | Disable sound |
| `noClouds` | Skip the volumetric clouds |
| `noHaze` | Skip the haze and sun shafts |
| `noCaustics` | Skip caustics |
| `noVeg` | Skip vegetation |
| `noSim` | Skip the swash (shallow-water) simulation |

### E. 文章观点 vs README 事实（分开看）

| 文章怎么说（作者观点 / 解读） | README / 仓库实际情况 |
|---|---|
| 展示了 "Opus 5.5 在复杂项目规划、代码生成、图形学实现和系统整合上的能力" | 只有仓库 description 写了 "Coastal town built with Opus 5.5"；README、CREDITS 都没写 AI 具体参与了多少、用什么流程 |
| "整个项目没有使用成熟的三维游戏框架" | README："runs directly on WebGPU and WGSL with its own small rendering engine, no framework"。另外 `docs/PORTING.md` 显示它是从 three.js/TSL 版本移植到原生 WebGPU 的（移植时的工作分支叫 `webgpu-native`），引擎 API 也故意做成了和 three 兼容的风格 |
| 42 段来自 Freesound 的 CC0 实地录音 | CREDITS.md 证实：42 field recordings，CC0 1.0 |
| 目标是 M5 Pro 上 2560×1267 + 动态分辨率 | README 原话："targets 60 fps at 2560×1267 on an Apple M5 Pro" |
| 鱼种由水域 / 水深 / 时间决定 | README：18 种加勒比鱼类，按 shallows / pier / reef / bay / deep water、水深和时段决定 |
| （截图里是中英双语 UI） | 仓库源码 UI 只有英文，没有 i18n；截图里的中文像是浏览器自动翻译出来的（比如把 "Interact" 翻成了"相互影响"） |

---

## 上手顺序

1. **先玩在线版**：用 Chrome/Edge 打开 https://dgreenheck.github.io/tidewater/ ，等着色器编译完，按 F1 看全部按键。
2. **本地跑起来**：`git clone` → `npm install` → `npm run dev` → 打开 http://127.0.0.1:5189 。
3. **用 URL 参数做减法定位性能**：`?noClouds&noVeg&noSim` 等逐项关闭，找出自己机器上的性能瓶颈。
4. **按文章的阅读路线看代码**：`src/main.js` → `src/App.js`（`init` / `_frame`）→ `src/engine/Engine.js` → `src/game/Game.js`（钓鱼状态机）→ `src/sky/Clouds.js`。
5. **读 `docs/PORTING.md`**：它是自研引擎 API 和 three.js 概念的对照表，二开前必读。
6. **跑测试**：`npm test`；`test/` 下还有 ocean / sky / world 等模块的无头测试和调试页。
7. **fork 并部署自己的 Pages**：打开 Actions，Pages 的 Source 选 GitHub Actions。

---

## 能力表

| 模块 | 能力（文章 + README） | 关键文件 / 目录 |
|---|---|---|
| 钓鱼玩法 | 蓄力抛竿 → 浮标试探（nibble）→ 真咬钩（take）→ 鱼线张力搏鱼 → 冷藏箱；18 种鱼、记录本 | `src/game/Game.js`、`Bites.js`、`CatchMinigame.js`、`FishingRod.js` |
| 经济 / 成长 | Joe 收鱼、Marta 杂货铺卖鱼线 / 渔轮 / 鱼竿 / 更大鱼舱 / 油箱 / 发动机 / 鱼探 / 甲板灯；船耗柴油；进度存浏览器 | `src/game/` |
| 海洋 | 四级级联 FFT（Tessendorf 谱）、白沫、破碎浪、浅水冲刷模拟、尾流、船头飞沫、焦散、折射、水线分屏、镜头水滴 | `src/ocean/` |
| 天空 | Hillaire 2020 物理大气、日月星、体积积云 + 卷云、云影、空气透视、God rays、镜头光晕 | `src/sky/`（`Clouds.js` 1,621 行） |
| 世界 | 地形、渔村、码头、珊瑚礁鱼群、热带植被（impostor + 抖动 LOD）、鸟 / 蟹 / 海洋雪、座头鲸 | `src/world/` |
| 光照 / 后处理 | 级联阴影、接触阴影、GTAO、TAAU 时间上采样、Bloom、自动曝光、运动模糊、夜间灯光 / 手电 | `src/materials/`、`src/post/` |
| 音频 | 42 段 CC0 实地录音，空间化，随水下 / 离岸距离 / 船转速变化 | `src/audio/` |
| 引擎 | 自研 WebGPU 引擎：GPU 单例、UniformBlock、ComputeKernel、ShaderModule、Material、GLB 加载、GPU 蒙皮 | `src/engine/`、`docs/PORTING.md` |
| 性能 | 管线后台编译 + 加载期预热、动态渲染分辨率（0.5–1）、云层 4×4 分摊 + 重投影 | `App.precompile`、`setRenderScale` |
| 工程 | Vite、GitHub Actions → Pages、无头测试 | `vite.config.js`、`.github/workflows/deploy.yml`、`test/` |

---

## 可复制的命令与代码（原文原样）

**本地运行（文章）**
```bash
git clone https://github.com/dgreenheck/tidewater.git
cd tidewater

npm install
npm run dev
```

**测试**
```bash
npm test
```

**构建生产版本**
```bash
npm run build
npm run preview
```

**package.json（文章引用）**
```json
{
"name":"tidewater",
"version":"1.0.0",
"scripts":{
"dev":"vite --host 127.0.0.1 --port 5189",
"build":"vite build",
"preview":"vite preview",
"test":"node test/game-logic.mjs && node test/engine-smoke.mjs"
},
"devDependencies":{
"vite":"^8.3.0",
"webgpu":"^0.6.1"
},
"license":"MIT",
"private":true,
"type":"module"
}
```

**钓鱼输入状态机（文章引用 Game.js 片段，同一个左键在不同状态下含义不同）**
```javascript
if ( rod.equipped && ! panelOpen ) {
if ( rod.state === 'idle' && lDown ) rod.startWindup();
else if ( rod.state === 'windup' && lUp ) rod.release();
else if ( rod.state === 'floating' ) {
if ( lDown ) this.strike();
else if ( rDown ) {
			rod.retrieve();
this.bite = null;
		}
	} else if ( rod.state === 'flying' && rDown ) rod.retrieve();
}
```

**动态分辨率（文章引用）**
```javascript
setRenderScale( v ) {
const scale = MathUtils.clamp( Math.round( v * 20 ) / 20, 0.5, 1 );
this.settings.renderScale = scale;
this.post.setScale( scale );
if ( this.clouds ) this.clouds.resolutionScale = scale;
}
```

> 其余代码片段（`App` 构造与 `init`、`main.js` 入口、`Engine.init`、`App._frame` 主循环、`updateBite`、Clouds.js 头部注释、`resize`、`audio.update` 参数）都在 `transcript.md` 里。原文这些代码丢了关键字空格，已在 transcript 里恢复。
> 文章里没有 AI 提示词（prompt），也没有讲作者是怎么用 Opus 5.5 生成这些代码的。

---

## 坑

- **WebGPU 兼容性**：需要较新的 Chrome / Edge / Safari；老浏览器、部分 Linux 和移动端可能直接报错（加载界面会显示 "Something went wrong: …"）。
- **首次加载慢**：要编译几百个着色器，可能要 1 分钟以上（README）。不要以为是卡死了。
- **吃 GPU**：目标硬件是 M5 Pro 级别；核显机器先用 `?noClouds&noVeg&noSim` 降负载。
- **体积大**：`public/` 素材约 53 MB；二开时如果换 CDN 或做小游戏平台适配，要考虑首包体积。
- **素材许可不全是 MIT**：代码是 MIT，但音频（Freesound CC0）、扫描模型（Poly Haven CC0）、角色（Microsoft Rocketbox，MIT，需保留 `LICENSE-Rocketbox.md`）、字体（OFL / Apache）各自有许可，商用二开要保留 `CREDITS.md` 和对应 LICENSE 文件。
- **没有中文 / i18n**：UI 是硬编码英文，文章截图里的中文是浏览器翻译的效果；要做中文版需要自己抽文案。
- **自研引擎，学习成本高**：没有 Three.js 生态可用，要先读 `docs/PORTING.md` 了解引擎 API；WGSL 以字符串形式散落在 JS 里。
- **项目很新**：仓库 2026-09-23 才创建，48 个 commit，已有 13 个 open issue，API 可能还会变；二开前先锁定一个 commit（比如 `4811ba4`）。
- **fork 后 Pages 不会自动发布**：需要手动启用 Actions，并把 Pages 来源设为 GitHub Actions（我的补充）。
- **"Opus 5.5 生成"无法核实**：只有仓库 description 这么写，AI 具体参与程度无从证实；文章的能力评价属于作者的解读。

---

## 适合谁

- 想 **fork / 二开浏览器 3D 游戏**、但不想被 Unity / Three.js 绑住的独立开发者（比如 Keith 计划做的二开）。
- 想系统学习 **WebGPU / WGSL 实时渲染**（FFT 海洋、体积云、大气散射、TAAU）的前端 / 图形程序员。
- 关注 **AI 编程能力边界**，想看"AI 参与做的大型项目"实际长什么样的人。
- 做休闲钓鱼 / 模拟经营类游戏、需要参考 **状态机 + 环境约束随机** 玩法设计的策划。

---

## 章节导航（对应 transcript.md）

- **开篇**：项目简介（@dgreenheck/tidewater，"Coastal town built with Opus 5.5"），定位为纯 WebGPU 自研引擎的钓鱼游戏 + 视频号预览
- **一、游戏核心逻辑**：在线版链接；9 步核心循环；1. 钓鱼不是随机判定（受水域 / 水深 / 码头 / 珊瑚礁 / 时间影响）；2. 海岛不是背景图（系统驱动的世界）；3. 海洋是技术核心（FFT、Tessendorf、四级级联等 11 项效果）
- **二、为什么能体现 Opus 5.5 的能力**：涉及 15 个技术领域；`App.js` 分阶段组装运行时
- **三、核心代码是如何工作的**：1. Canvas → WebGPU（`main.js`、`Engine.init`、管线后台编译）；2. 主循环 `_frame` 的依赖顺序；3. 钓鱼状态机（idle → windup → flying → floating → retrieving → fighting → landing）与 `updateBite`；4. 体积云（Worley / Perlin 噪声、光线步进、时间重投影、1/44 像素分摊）
- **四、动态分辨率**：`setRenderScale` / `resize`
- **五、声音参与世界构建**：42 段 CC0 录音，`audio.update` 读取空间状态
- **六、从代码规模看不是 Demo**：`src/` 目录结构，跨子系统一致性
- **七、最让人印象深刻的地方**：13 个打磨细节
- **八、如何在本地运行**：package.json、clone / install / dev / test / build / preview，GitHub Actions 部署
- **最后**：AI 参与软件开发的边界从"补全函数"走向"共同完成作品"；项目地址与在线体验链接
