# Claude Opus 5.5 + WebGPU 做出来的海岛钓鱼游戏，已经开始像一款真正的游戏了

> **来源**：微信公众号「柳杉前端」
> **作者**：柳杉前端（公众号署名，未单独署个人作者）
> **原文链接**：https://mp.weixin.qq.com/s/OioiV0lB-DZqmW-WQivR-Q
> **原标题**：Claude Opus 5.5 + WebGPU 做出来的海岛钓鱼游戏，已经开始像一款真正的游戏了
> **发布时间**：2026-09-24 19:04:15（北京时间，页面 create_time=1790247855）
> **字数**：约 3,900 字（正文 3,741 汉字 + 133 个英文词，不含代码块；另含 15 段代码块，约 1,200 个英文词元）
> **抓取时间**：2026-10-06（PT），移动端 UA curl 抓取
> **校对说明**：
> - 正文文字按原文保留，仅修正一处漏字（"这个的目录结构" → "这个项目的目录结构"），并将「三、核心代码是如何工作的」下误用的二级标题改为三级标题。
> - 原文代码块因微信语法高亮丢失了关键字后的空格（如 `exportclassApp`、`newEngine`、`elseif`），本稿已恢复为可读代码（`export class App`、`new Engine`、`else if` 等），未改动任何标识符或数值。
> - 图片保留微信 CDN 地址（mmbiz.qpic.cn，可能有防盗链）；文中视频为视频号嵌入，无外链 URL。
> - 截图中的中英双语界面（如「TIDEWATER 潮汐区」「Interact 相互影响」）看起来是浏览器自动翻译效果，仓库源码本身为纯英文界面。

---

最近看到一个很有意思的开源项目：@dgreenheck/tidewater。

它的描述非常直接：

Coastal town built with Opus 5.5

Tidewater不是一个简单的网页动画，也不是把几个三维模型放进Canvas里展示。它是一款可以直接在浏览器中运行的海岛钓鱼游戏：玩家可以从码头、沙滩或自己的小船出发，寻找不同水域里的鱼，完成抛竿、咬钩、遛鱼、收线，再把鱼卖给Joe，换钱之后去Marta的杂货铺升级装备。

![图1](https://mmbiz.qpic.cn/sz_mmbiz_png/IItIPP7oibkRpwiafguBqgwHGJcZW4F6xiby5E5iaOkUOrJtfK7NiaIC8CTgKOheC1wXdsosRaWEmsm7NicN3neiac6GmlaX4SB4qVibBiadQib75M8FE/640?wx_fmt=png&from=appmsg)

更重要的是，整个项目没有使用成熟的三维游戏框架，而是基于WebGPU和WGSL，自己搭建了一套小型渲染引擎。

这也是这个项目最值得关注的地方：它展示了Opus 5.5在复杂项目规划、代码生成、图形学实现和系统整合上的能力。

先预览视频来体验一下海景视觉和音效：

> [视频号嵌入视频：海景视觉与音效预览（文章内嵌，无外链 URL）]

## 一、游戏核心逻辑

打开项目的在线版本，就能进入这座海岛小镇：

https://dgreenheck.github.io/tidewater/

进入游戏之后，玩家可以在岛上自由行走，也可以下水游泳，登上小船，驶向更远的深海。

![图2](https://mmbiz.qpic.cn/sz_mmbiz_png/IItIPP7oibkRq1aS3UV7CRiadspeia6Pccx5Pa9N6w0xqHp8Sh3UicvRIgd4drDx6ok7yuBNHwG1cibsSJrP6jK7VCs0ric7kJwBuAnJepbpoibxVw/640?wx_fmt=png&from=appmsg)

![图3](https://mmbiz.qpic.cn/mmbiz_png/IItIPP7oibkRqrq3n68qE2kibsXfoN9OvFHSlcc6F7Q6ck0R9CZxsc0NNsxDffLcIlCiaN170CSVHaCYggpB0avW5AuKLydUH0lKjCjxjdRJxQ/640?wx_fmt=png&from=appmsg)

![图4](https://mmbiz.qpic.cn/sz_mmbiz_png/IItIPP7oibkRXPibIOgUZZkQmF22WlsOsbq7M9WNe8x7WG8FibB58QUzhJaSlNWMJqibQf6KGbFjZR3H4EibhIFhqib1ficMhQIicgO91jzzbSDUwmc/640?wx_fmt=png&from=appmsg)

游戏的核心循环很清晰：

- 找到合适的水域
- 拿出鱼竿并抛竿
- 等待浮标产生动静
- 在鱼真正咬钩时提竿
- 控制鱼线张力完成搏鱼
- 把鱼放进冷藏箱
- 找Joe卖鱼
- 找Marta购买更好的装备
- 驾船前往更远的海域，寻找更稀有的鱼

这套设计并不复杂，但它把探索、操作、经济系统和装备成长串到了一起。

![图5](https://mmbiz.qpic.cn/sz_mmbiz_png/IItIPP7oibkRqvEYF2Klq90stql8oicL1hKokxxV9ZnI8Aia4SibjrLJnYqXgR88fjEeQwjic9w1POEkJE9sXExPEnYrg1sCzOSIQaYicj50zlolk/640?wx_fmt=png&from=appmsg)

### 1. 钓鱼不是一次随机判定

游戏里并不是点击一下就随机得到一条鱼。

不同鱼类会受到多个条件影响，包括：

- 当前水域
- 水深
- 是否靠近码头
- 是否处于珊瑚礁区域
- 当前时间
- 鱼的稀有度和搏斗强度

项目中，钓鱼逻辑主要由src/game/Game.js、src/game/Bites.js、src/game/CatchMinigame.js和src/game/FishingRod.js协同完成。

抛竿后，浮标会经历等待、轻微试探、真正咬钩几个阶段。玩家如果在鱼只是试探时过早提竿，游戏会提示“还没到时候”；等浮标真正沉下去，才进入搏鱼阶段。

搏鱼也不是单纯地持续按住鼠标。鱼线有张力区间，玩家需要在“收线”和“放松鱼线”之间做判断。鱼突然发力时，如果还在持续收线，鱼线就可能断掉。

这让一个看似简单的钓鱼动作，变成了一个有节奏、有反馈的小游戏。

### 2. 海岛不是背景图片

![图6](https://mmbiz.qpic.cn/mmbiz_png/IItIPP7oibkReD89ia5BTax4rzGUEBVOCyicwicu6RhR3UBZMuuP2q4vpAevYlVkZSiaFogtYYmdmx3EJxpQp6R0oKINFwyfq81vqutDp5Uxo9kQ/640?wx_fmt=png&from=appmsg)

- 沙滩、山丘、海岬和岩石
- 渔村、码头和商店
- 珊瑚礁和成群的鱼
- 椰子树、香蕉树、龟背竹和海滩植被
- 鸟类、螃蟹、海洋雪花
- 一头会喷水、潜水和跃出海面的座头鲸

这些元素并不是静态模型简单堆叠，而是由不同系统共同驱动。

例如：

![图7](https://mmbiz.qpic.cn/mmbiz_png/IItIPP7oibkQ1icq2Ele6AdMw2VjYYg1ZbP5aNicx3NibITJibGu2UTNXFxp8A1BbOwYkv4Mkibt8bMAPkibia17Xczs0JO2kxsBibwXDKMJ8StvibAdI/640?wx_fmt=png&from=appmsg)

![图8](https://mmbiz.qpic.cn/mmbiz_png/IItIPP7oibkSibZHpNQYp5fMyJf5ushxLtc9cNBNEHYpaEfdG4SkIb4d7Wbv7btwoXEhodVlBU9iaZ8PuETFnTBUeG9wBtiawicicYUXSOH1spibC4/640?wx_fmt=png&from=appmsg)

- 船会消耗燃油
- 船移动时会产生尾流和船头飞沫
- 海浪会影响海岸湿润区域
- 云层会产生阴影
- 水面会影响折射、焦散和水下光照
- 时间变化会带来日夜切换
- 夜晚可以打开手电筒和甲板照明

玩家看到的是一个统一的世界，而不是一系列互不相关的演示效果。

### 3. 海洋是项目的技术核心

水面并不是一张带法线贴图的平面。

![图9](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IItIPP7oibkQe49Jr4KPsDAqjVIOy5DjRsKbzkT9S1wC9iauNGGOY1ZZ0RZ20Nt2UC6jR6RAlS8XVS3ZG7NmIhCPwicI3icV6ysu0Oia9VYb4jD4/640?wx_fmt=jpeg&from=appmsg)

![图10](https://mmbiz.qpic.cn/sz_mmbiz_png/IItIPP7oibkQEfvDrRD6qtyrjiarVaEG4xRYEm0ic6iaiaI3l1WacpxHNVgXHqkjrGibHEzvw2E2bbPMB8lmHlf8eBAbDzgDuibsMExqT6oZFqmrDI/640?wx_fmt=png&from=appmsg)

![图11](https://mmbiz.qpic.cn/sz_mmbiz_png/IItIPP7oibkQJgIZicRZX9CR4hqSyuB7vkGTHz7j9gbhnrlq1CGXYoRjY3x9FoFl11DyRibSRyv4icCwBj2jbftxtib1HTM5BXm27QVytIayHHdk/640?wx_fmt=png&from=appmsg)

项目使用了基于FFT的海洋模拟，README中提到使用了Tessendorf海洋谱，并实现了四级频谱级联。画面中还加入了：

- 风浪和涌浪
- 白沫和浪花
- 海岸破碎浪
- 沙滩上的浅水模拟
- 船尾尾流
- 船头喷溅
- 鲸鱼跃出水面时的水花
- 水下焦散
- 水面折射
- 水线处的水上、水下分界
- 出水时附着在镜头上的水滴

这些效果放在一起，才构成了“海”的感觉。

真正的难点不在于做出一片会动的水，而在于让水和岛屿、船、角色、光照、声音以及玩家动作发生联系。

## 二、它为什么能体现Opus 5.5的能力

“用AI写了一个游戏”本身并不稀奇。真正有难度的是，在没有成熟游戏引擎兜底的情况下，把一个复杂的实时三维项目组织起来。

这个项目涉及的内容非常广：

- WebGPU初始化
- GPU资源管理
- 场景图和网格渲染
- WGSL着色器组合
- 海洋FFT模拟
- 大气散射
- 体积云
- 地形和植被
- 角色蒙皮动画
- 阴影和局部光源
- 后处理
- 音频空间化
- 游戏状态和装备系统
- 浏览器存档
- GitHub Pages部署

这不是单个模块的代码生成，而是需要在长期上下文中保持接口一致。

例如App.js并没有把所有代码写在一个文件里，而是负责组装整个运行时：

```javascript
export class App {

constructor() {

this.settings = {
timeOfDay: 16.2,
sunAzimuth: 0, // degrees: turns the sun's daily path about the vertical
timeSpeed: 0, // hours per real second
exposure: 0.55,
renderScale: 1, // internal resolution (the temporal upscaler reconstructs the output), Performance tab
		};
this.qs = new URLSearchParams( location.search );

	}

async init( onProgress = () => {} ) {

const qs = this.qs;
// report a stage, then let the page paint it before the (synchronous) stage work starts
const progress = async  ( p, text, until ) => {

onProgress( p, text, until );
if ( typeof requestAnimationFrame === 'function' ) await new Promise( ( r ) =>requestAnimationFrame( () =>setTimeout( r, 0 ) ) );

		};
await progress( 0.02, 'Starting WebGPU…' );
const engine = this.engine = new Engine( document.getElementById( 'app' ) );
await engine.init();
```

初始化阶段按照天空、岛屿、海洋、后处理、音频和游戏逻辑逐步构建系统，而不是一次性把所有资源塞进启动流程。

这种组织方式很重要，因为大型项目最容易出问题的地方，往往不是某个函数写错，而是不同模块之间的依赖关系失控。

## 三、核心代码是如何工作的

![图12](https://mmbiz.qpic.cn/mmbiz_png/IItIPP7oibkQXmThO96bicsiaaLxCqShxWhNyFQNRmibzHJUJxdYrgiciclWS063o2jtic4hk2Qm3jOMtk3bwXhasK8IHeeYH7hPhynqWOicOicZtOhY/640?wx_fmt=png&from=appmsg)

### 1. 从浏览器Canvas到WebGPU

项目的入口非常简洁：

```javascript
import { App } from './App.js';
import { UI } from './ui/UI.js';
import { AppUI } from './ui/AppUI.js';

const ui = new UI();
const app = new App();
window.__ui = ui;

app.init( ( p, text, until ) => ui.setLoading( p, text, until ) ).then( async  () => {

	app.ui = new AppUI( app, ui );
	ui.setLoading( 1, 'Ready' );
await ui.hideLoader();
	app.start();
	ui.showStartOverlay( () => {

		app.input.requestLock();
if ( app.audio ) app.audio.resume();

	} );

} ).catch( ( e ) => {

console.error( e );
	ui.setLoadingError( 'Something went wrong: ' + e.message );

} );
```

main.js做三件事：

- 创建界面
- 初始化游戏应用
- 初始化完成后启动主循环

真正的底层GPU初始化位于src/engine/Engine.js：

```javascript
async init() {

const canvas = document.createElement( 'canvas' );
	canvas.tabIndex = 0;
this.container.appendChild( canvas );
this.canvas = canvas;
this.domElement = canvas;
await GPU.init( { canvas } );
this.meshRenderer = new MeshRenderer();
this.meshRenderer.syncPipelines = false; // compile in the background (App.precompile waits for them)
this.camera = new PerspectiveCamera( 62, window.innerWidth / window.innerHeight, 0.06, 60000 );
this.scene = new Scene();
window.addEventListener( 'resize', () =>this.resize() );
this.resize();

}
```

这里有两个值得注意的设计。

第一，项目直接调用自己的GPU.init()，没有依赖Three.js这样的成熟渲染框架。

第二，渲染管线不会阻塞在第一次绘制时同步编译，而是设置为后台编译，随后由App.precompile()集中预热。

这正是WebGPU项目必须面对的问题：着色器和渲染管线的首次编译可能需要较长时间。如果让它们在玩家第一次看到对应画面时才编译，就会产生明显卡顿。

它把这个过程放进加载阶段，并在界面中明确告诉玩家：第一次启动需要编译数百个着色器，后续访问会因为浏览器缓存而更快。

### 2. 主循环如何组织整个世界

App._frame()是整个游戏的心跳。

它先更新时间、输入、玩家和船只，再更新海洋、天空、世界对象，最后完成阴影、场景和后处理渲染。

```javascript
_frame( dt ) {

GPU.beginFrame();
FrameUniforms.fields.frameIndex.value = GPU.frame;
const s = this.settings;
this.updateFPS( dt );
	G.dt.value = dt;
	G.time.value += dt;
if ( s.timeSpeed !== 0 ) s.timeOfDay = ( s.timeOfDay + dt * s.timeSpeed + 24 ) % 24;

// ---- player / boat
this.boatCtl.update( dt );
this.boatSpray.update( dt );
this.wake.update( dt );
if ( this.freeCam ) this.fly.update( dt );
else this.player.update( dt );
this.game.update( dt );
this.updateSun();

this.atmosphere.update( dt, this.camera.position.y );
this.applyAtmosphereReadback();
if ( this.clouds ) this.clouds.update( dt, this.camera );

// ---- water simulation
this.fft.update( dt );
this.seaDetail.update( dt );
this.query.setCamera( this.camera.position.x, this.camera.position.z );
this.boatCtl.queueQueries();
this.query.update();

if ( this.caustics ) this.caustics.update();
if ( this.shoreSim ) this.shoreSim.update();
this.underwaterLighting.update( this.camera );
this.breakers.update( this.camera );
this.spray.update();

// ---- world
this.oceanLOD.update( this.camera );
this.terrain.update( this.camera );
this.rocks.update( this.camera );
this.debris.update( this.camera );
this.reef.update( dt, this.camera.position );
this.village.update( dt );
if ( this.vegetation ) this.vegetation.update( dt, this.camera );
if ( this.whale ) this.whale.update( dt, this.camera );
this.boat.update( dt );
this.wildlife.update( dt, this.camera, this.freeCam ? null : this.player );
this.localLights.update( this.camera, dt );

// ---- render
this.post.beginFrame();
this.underwater.updateCamera( this.camera );
this.shadows.render( this.scene, this.engine.meshRenderer, this.shadows.update( this.camera, G.sunDir.value ) );
this.sceneRenderer.render();
this.post.render();
this.post.endFrame();
GPU.submit();

this.updateAudio( dt );
this.input.endFrame();

}
```

这个顺序不是随意排列的。

例如船的物理状态需要先更新，摄像机才能跟随船的新位置；海洋模拟更新后，船尾流、浮标和水下判断才能使用最新的水面数据；场景渲染完成后，后处理才能对画面进行水下合成、雾效、运动模糊和泛光处理。

一个好的实时渲染循环，本质上是在每一帧维护一张“世界状态依赖图”。

### 3. 钓鱼系统是一套状态机

Game.js把钓鱼过程拆成了多个状态：

- idle
- windup
- flying
- floating
- retrieving
- fighting
- landing

抛竿和搏鱼的输入处理，也被明确地写成了状态转换：

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

if ( rod.state === 'floating' ) this.updateBite( dt );
else if ( ! this.fight ) rod.dip = Math.max( 0, rod.dip - dt * 4 );
if ( this.fight ) this.updateFight( dt, lmb && ! panelOpen );

rod.update( dt, { visible: can, fight: this.fight } );
```

这一段代码体现了一个很实用的游戏开发原则：不要让每种输入在任何时候都生效，而是根据当前状态决定输入的含义。

同一个鼠标左键：

- 在idle状态代表开始蓄力
- 在windup状态代表释放并抛竿
- 在floating状态代表提竿
- 在fighting状态代表收线

这让玩家的操作看起来简单，但底层逻辑并不混乱。

咬钩逻辑也有明确阶段：

```javascript
updateBite( dt ) {

const rod = this.rod;
const b = this.bite;
if ( ! b ) return;
	b.t -= dt;

if ( b.phase === 'nibble' ) rod.dip = Math.max( 0, Math.sin( Math.min( 1, ( b.pulse || 0 ) ) * Math.PI ) * 0.45 );
else if ( b.phase === 'take' ) rod.dip += ( 1.4 - rod.dip ) * ( 1 - Math.exp( - dt * 14 ) );
else rod.dip = Math.max( 0, rod.dip - dt * 3 );

if ( b.t > 0 ) return;

if ( b.phase === 'wait' ) {

const h = this.habitat();
const species = pickSpecies( h, this.hour );

if ( ! species ) {

			b.t = 8;
return;

		}

		b.species = species;
		b.kg = rollWeight( species );
		b.phase = 'nibble';
		b.nibbles = 1 + Math.floor( Math.random() * 3 );
		b.t = 0.7 + Math.random() * 0.8;
		b.pulse = 0;

	} else if ( b.phase === 'nibble' ) {

		b.nibbles --;
		b.pulse = 0;

if ( b.nibbles > 0 ) b.t = 0.6 + Math.random() * 1.0;
else {

			b.phase = 'take';
			b.t = 2.4 - FISH[ b.species ].fight * 0.5;

		}

	} else if ( b.phase === 'take' ) {

this.bite = { phase: 'wait', t: biteDelay( this.habitat(), this.hour ) };

	}

}
```

这里的关键并不是随机数，而是随机数受到环境约束。

鱼种由habitat()决定，咬钩时间由栖息地和时间决定，重量由鱼种决定，真正咬钩后的反应窗口还会根据鱼的搏斗强度缩短。

于是，游戏中的“随机”就不再是完全无规律的抽签，而是建立在世界规则上的变化。

### 4. 云层渲染展示了GPU计算的价值

src/sky/Clouds.js是整个项目中最复杂的文件之一。

它没有使用一张云层图片，而是通过WGSL计算着色器生成体积云。代码中包含：

- Worley噪声
- Perlin噪声
- 多层噪声融合
- 云层密度场
- 光线步进
- 自阴影
- 多次散射近似
- 云影贴图
- 时间重投影
- 历史帧累积
- 双三次上采样
- 空间跳跃优化

项目并没有每一帧对每个屏幕像素进行完整的高质量光线步进，而是使用了时间和空间上的分摊。

文件开头已经说明了这种策略：

```javascript
// Volumetric trade-wind cumulus (Schneider/Nubis density model, Hillaire multiple-scattering
// approximation) under a thin cirrus veil.
//   - view: ray marched in screen space, one pixel of every 4x4 block per frame (two while the camera
//     turns), accumulated at 0.6x the render resolution with reprojection (camera motion and wind drift)
//     and upsampled bicubically, like sky-pro-webgpu's High quality (about 1/44 of the display pixels
//     marched per frame). Empty space is skipped with a coverage dependent 3D distance field, so rays
//     only take small (24 m) steps near clouds.
//   - panorama: a cheaper low resolution version of the whole sky dome for water reflections,
//     the environment cube and Snell's window, refreshed progressively (1/32 per frame).
//   - shadow: transmittance of the cloud layer along the sun around the camera (1/4 per frame).
```

简单来说：

- 每帧只计算一部分像素
- 其他像素复用之前帧的结果
- 摄像机移动时，通过重投影把历史结果映射到新位置
- 云层边缘使用当前帧结果进行修正
- 远处没有云的区域直接跳过
- 水面反射只使用低分辨率全景版本

这是一种典型的实时图形学思路：不是无限堆算力，而是把计算放到最值得计算的地方。

它的云层效果之所以有真实感，也不只是因为用了噪声。项目还根据云层高度、太阳方向、视线方向和云内部密度计算光照，并通过多次散射近似处理云体内部的亮暗变化。

因此玩家在不同时间看到的云，不只是换了颜色，而是会随着太阳位置和天气参数产生不同的光照关系。

## 四、动态分辨率：在画质和帧率之间找平衡

README里提到，项目目标是在Apple M5 Pro上以2560×1267分辨率运行，并通过动态渲染分辨率适配较慢的设备。

代码中，内部渲染分辨率由renderScale控制：

```javascript
setRenderScale( v ) {

const scale = MathUtils.clamp( Math.round( v * 20 ) / 20, 0.5, 1 );
this.settings.renderScale = scale;
this.post.setScale( scale );
if ( this.clouds ) this.clouds.resolutionScale = scale;

}
```

而引擎会根据这个比例设置Canvas的实际像素尺寸：

```javascript
resize() {

const w = window.innerWidth, h = window.innerHeight;
const dpr = this.renderScale;
this.canvas.width = Math.max( 1, Math.floor( w * dpr ) );
this.canvas.height = Math.max( 1, Math.floor( h * dpr ) );
this.canvas.style.width = w + 'px';
this.canvas.style.height = h + 'px';
this.camera.aspect = w / h;
this.camera.updateProjectionMatrix();
FrameUniforms.fields.outputResolution.value.set( this.canvas.width, this.canvas.height );
for ( const f of this.onResize ) f( w, h );

}
```

这是一种很实用的优化方式。

用户看到的窗口尺寸不变，但内部渲染可以使用更低分辨率，再通过时间抗锯齿和后处理重建最终画面。对于云、海洋、阴影和体积效果较多的场景来说，这种策略往往比单纯降低模型质量更有效。

## 五、声音也参与了世界构建

它的音效没有停留在背景音乐层面。

项目使用了42段来自Freesound的CC0实地录音，包括：

![图13](https://mmbiz.qpic.cn/sz_mmbiz_png/IItIPP7oibkTIPJ4VB874nMZ9spRT0z849j6siaEopWHDYl9ibOHGQAMv9u0j2OicWQQFVjOV3hQ0wNNCR8EXbjZQVDZLcUzPuicAjoamsNRLzMw/640?wx_fmt=png&from=appmsg)

- 海浪
- 风
- 棕榈树声
- 蟋蟀
- 鸟叫
- 船用柴油机
- 船体拍水
- 沙滩脚步
- 水下环境
- 鲸鱼歌声
- 鱼竿和渔轮
- 鱼线拉紧和断裂
- 鱼跃出水面的声音

代码会根据玩家所在位置、是否在水下、距离海岸的距离、船的转速和速度等信息，更新声音环境。

例如在App.updateAudio()中，音频系统会接收这样的空间状态：

```javascript
this.audio.update( dt, {
listener: { position: p, forward: f.fwd, up: f.up },
underwater: p.y < h ? 1 : 0,
depthBelowSurface: Math.max( 0, h - p.y ),
surfIntensity: Math.min( 1, this.shore.amplitude.value / 0.6 ),
distanceToShore: Math.abs( coast ),
coastDistance: coast,
waveHeight: this.shore.amplitude.value * 2,
windSpeed: G.windSpeed.value,
windDir: G.windDir.value,
daylight: 1 - G.night.value,
nearPier: Math.abs( p.x - WORLD.pier.x ) < 12 && p.z > WORLD.pier.zStart - 5 && p.z < WORLD.pier.zEnd + 8,
boat: {
active: this.boatCtl.driven,
rpm: this.boatCtl.rpm,
throttle: this.boatCtl.throttle,
speed: this.boatCtl.velocity.length(),
position: this.boat.group.position,
listenerInside: this.player.mode === 'boat' && this.player.camMode === 'first',
	},
} );
```

这说明音频并不是独立播放的素材列表，而是场景状态的一部分。

当玩家潜入水下，声音会发生变化；当船提高转速，发动机声音会随之变化；靠近码头时，水拍打船体的声音也会不同。

视觉系统和声音系统共享同一个世界状态，这也是沉浸感的来源之一。

## 六、从代码规模看，Opus 5.5做的不是一个Demo

这个项目的目录结构也很能说明问题：

```text
src/
  audio/       声音环境和混音
  core/        全局状态、输入、场景渲染、调试工具
  engine/      WebGPU渲染引擎、GPU资源、材质、模型加载
  fx/          喷溅、海洋雪花、空气微粒等特效
  game/        钓鱼、鱼类、装备、商店、HUD和游戏状态
  materials/   阴影、局部光源、接触阴影和共享材质逻辑
  ocean/       FFT海洋、海岸波浪、尾流、焦散和水下光照
  player/      行走、游泳、船只和自由摄像机
  post/        水下合成、雾效、TAAU、运动模糊、Bloom和镜头效果
  sky/         大气、天空、云层和环境光
  ui/          加载界面、设置面板和HUD
  util/        通用工具
  world/       地形、渔村、珊瑚礁、植被、野生动物和鲸鱼
```

这不是“生成一个页面”的工作量。

它要求代码在多个层面保持一致：

- 游戏逻辑要知道玩家位于什么水域
- 水面系统要知道船在哪里
- 船只系统要能产生尾流和喷溅
- 渲染系统要能处理水上和水下的不同光照
- 云层要参与天空、反射和地面阴影
- 后处理要知道水线和摄像机运动
- 音频要读取场景中的空间状态
- UI要把这些状态转换成玩家能理解的提示

从最终效果来看，Opus 5.5的价值并不只是写出了某一个漂亮的着色器，而是能够在多个子系统之间维持一种可运行的整体结构。

## 七、它最让人印象深刻的地方

如果只看某一张截图，它可能会被当作一个画面不错的WebGPU实验。

但真正玩起来之后，会发现它的完成度来自很多小地方：

- 第一次加载时会显示真实的编译进度
- 浮标不是直接跳动，而是先有几次试探
- 鱼线张力会影响搏鱼结果
- 不同水域和时间会影响鱼种
- 鱼有重量和价格
- 冷藏箱容量有限
- 船会消耗燃油
- 装备升级会改变实际能力
- 夜间捕鱼需要甲板灯
- 鱼探测器会显示水深和鱼群情况
- 游戏进度会保存在浏览器中
- 船可以在海上漂流，玩家能够走到甲板和驾驶室
- 水下和水上的光照、音效、雾效都不同

这些细节不一定会出现在宣传图里，却决定了它是否像一个真正的游戏。

## 八、如何在本地运行

项目使用Vite构建，依赖非常少：

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

运行环境需要支持WebGPU，推荐使用较新的Chrome、Edge或Safari，并且最好具备一块性能较好的GPU。

```bash
git clone https://github.com/dgreenheck/tidewater.git
cd tidewater

npm install
npm run dev
```

项目还提供了测试命令：

```bash
npm test
```

构建生产版本：

```bash
npm run build
npm run preview
```

每次向main分支提交代码后，GitHub Actions会自动构建并部署到GitHub Pages。

## 最后

这个项目最有意思的地方，不只是它能在浏览器里渲染出海水、云层和一座小岛。

它真正展示的是，今天的AI已经可以参与构建一种相当复杂的软件系统：从需求理解开始，到模块拆分、渲染管线、GPU着色器、游戏状态机、音频系统，再到测试和部署，最终形成一个可以打开、可以操作、可以持续探索的完整作品。

当然，Tidewater并不是一款商业级3A游戏，它也不是为了取代专业游戏引擎而存在。

但它把一个很有分量的问题摆到了我们面前：

如果一个模型能够理解实时渲染、游戏循环和系统之间的依赖关系，那么它参与软件开发的边界，可能就不再只是补全函数和生成页面，而是开始接近“共同完成一个作品”。

Tidewater就是一个很直观的例子。

它没有把Opus 5.5的能力写在介绍页上，而是把能力放进了海浪、云影、鱼线、发动机声和那头突然跃出海面的鲸鱼里。

项目地址：

https://github.com/dgreenheck/tidewater

在线体验：

https://dgreenheck.github.io/tidewater/
