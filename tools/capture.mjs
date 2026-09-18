// 상세 페이지 캡처: 헤드리스 Chrome을 DevTools 프로토콜로 직접 제어한다(추가 설치 없음, Node 22+).
//   node tools/capture.mjs [URL]      → screenshots/*.png
// 페이지 전체 높이를 뷰포트로 잡는다. 3D 캔버스는 화면에 보일 때만 그려지므로, 이렇게 해야 모든 꽃다발이 찍힌다.
import { spawn } from 'node:child_process';
import { mkdirSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const URL_ = process.argv[2] || 'https://flower-shop-landing-dun.vercel.app/';
const OUT = join(dirname(fileURLToPath(import.meta.url)), '..', 'screenshots');
const CHROME = process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const PORT = 9333, PROFILE = join(tmpdir(), 'flower-capture-' + process.pid);
const sleep = ms => new Promise(r => setTimeout(r, ms));
mkdirSync(OUT, { recursive: true });

const chrome = spawn(CHROME, ['--headless=new', `--remote-debugging-port=${PORT}`, `--user-data-dir=${PROFILE}`, '--hide-scrollbars',
  '--enable-unsafe-swiftshader', '--use-angle=swiftshader', '--ignore-gpu-blocklist', '--no-first-run', '--no-default-browser-check', 'about:blank'], { stdio: 'ignore' });
const done = code => { try { chrome.kill('SIGKILL'); } catch {} try { rmSync(PROFILE, { recursive: true, force: true }); } catch {} process.exit(code); };

async function connect() {
  for (let i = 0; i < 60; i++) {
    try { const t = await (await fetch(`http://127.0.0.1:${PORT}/json/new?about:blank`, { method: 'PUT' })).json(); return t.webSocketDebuggerUrl; } catch { await sleep(250); }
  }
  throw new Error('Chrome DevTools에 연결하지 못했습니다');
}
function client(wsUrl) {
  const ws = new WebSocket(wsUrl); let id = 0; const pending = new Map();
  ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pending.has(m.id)) { const p = pending.get(m.id); pending.delete(m.id); m.error ? p.rej(new Error(m.error.message)) : p.res(m.result); } };
  const ready = new Promise((res, rej) => { ws.onopen = res; ws.onerror = () => rej(new Error('ws error')); });
  const send = (method, params = {}) => new Promise((res, rej) => { const i = ++id; pending.set(i, { res, rej }); ws.send(JSON.stringify({ id: i, method, params })); });
  return { ready, send };
}
const evalJs = async (c, expression) => (await c.send('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true })).result.value;

async function shoot(c, name, width, mobile, sections) {
  const metrics = (height, dpr) => c.send('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: dpr, mobile });
  await metrics(1000, 1);
  await c.send('Page.navigate', { url: URL_ });
  await sleep(3500);
  await evalJs(c, `document.fonts.ready.then(()=>1)`);
  // 남는 꽃 데모는 비어 있는 상태가 기본이라, 한 다발을 자동 구성해 둔다
  await evalJs(c, `(()=>{const b=document.querySelector('[data-act=left-auto]'); if(b) b.click(); return 1})()`);
  let h = await evalJs(c, 'document.documentElement.scrollHeight');
  await metrics(h, 1); await sleep(600);
  h = await evalJs(c, 'document.documentElement.scrollHeight');       // 뷰포트가 커지며 달라진 높이를 다시 잰다
  const dpr = 2;
  await metrics(h, dpr);
  await sleep(4500);                                                     // 3D 모델 로딩 + 토스트가 사라질 때까지
  const info = await evalJs(c, `JSON.stringify({canvases:document.querySelectorAll('.bq-canvas').length, fallback:document.querySelectorAll('.bq-2d').length})`);
  // 헤드리스 Chrome은 한 번에 약 8,192px(기기 픽셀)보다 높게 찍으면 내용이 되감긴다 → 타일로 나눠 찍고 캔버스에서 이어 붙인다
  const TILE = Math.floor(8000 / dpr), tiles = [];
  for (let y = 0; y < h; y += TILE) {
    const hh = Math.min(TILE, h - y);
    const t = await c.send('Page.captureScreenshot', { format: 'png', clip: { x: 0, y, width, height: hh, scale: 1 } });
    tiles.push({ y, data: t.data });
  }
  const stitched = await evalJs(c, `(async()=>{const T=${JSON.stringify(tiles)},cv=document.createElement('canvas');cv.width=${width * dpr};cv.height=${h * dpr};const g=cv.getContext('2d');
    for(const t of T){const im=new Image();im.src='data:image/png;base64,'+t.data;await im.decode();g.drawImage(im,0,t.y*${dpr})} return cv.toDataURL('image/png').split(',')[1]})()`);
  writeFileSync(join(OUT, `${name}-full.png`), Buffer.from(stitched, 'base64'));
  console.log(`${name}-full.png  ${width}x${h} @${dpr}x  tiles=${tiles.length}  ${info}`);
  if (!sections) return;
  const rects = JSON.parse(await evalJs(c, `JSON.stringify(${JSON.stringify(sections)}.map(([n,sel])=>{const els=sel.split(',').map(s=>document.querySelector(s)).filter(Boolean); if(!els.length) return null; const r=els.map(e=>e.getBoundingClientRect()); const top=Math.min(...r.map(x=>x.top))+scrollY, bottom=Math.max(...r.map(x=>x.bottom))+scrollY; return [n, Math.max(0,top), bottom-top]}).filter(Boolean))`));
  for (const [n, y, hh] of rects) {
    const s = await c.send('Page.captureScreenshot', { format: 'png', clip: { x: 0, y, width, height: hh, scale: 1 } });
    writeFileSync(join(OUT, `${name}-${n}.png`), Buffer.from(s.data, 'base64'));
    console.log(`${name}-${n}.png  ${width}x${Math.round(hh)} @2x`);
  }
}

try {
  const c = client(await connect()); await c.ready;
  await c.send('Page.enable'); await c.send('Runtime.enable');
  await shoot(c, 'desktop', 1280, false, [['01-hero', '.top,.hero,.ticker'], ['02-why', '#why'], ['03-swap', '#swap'], ['04-leftover', '#leftover'],
    ['05-builder', '#builder'], ['06-bid', '#bid'], ['07-day', '#day'], ['08-faq', '#faq'], ['09-final', '.final,footer']]);
  await shoot(c, 'mobile', 390, true, null);
  done(0);
} catch (e) { console.error('실패:', e.message); done(1); }
