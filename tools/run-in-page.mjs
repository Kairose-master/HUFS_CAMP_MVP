// 헤드리스 Chrome에서 페이지를 열고 시나리오(JS 파일, async 함수 본문)를 실행해 결과를 출력한다.
//   node tools/run-in-page.mjs <url> <scenario.js> [shot.png] [width] [height]
// file:// 도 열린다(localStorage·해시 라우팅 동작). Browser pane의 data: 미리보기로는 앱을 검증할 수 없어서 만든 도구.
import { spawn } from 'node:child_process'; import { readFileSync, writeFileSync, rmSync } from 'node:fs'; import { tmpdir } from 'node:os'; import { join } from 'node:path';
const [url, scenario, shot, W = '480', H = '900'] = process.argv.slice(2);
const PORT = 9340 + Math.floor(Math.random() * 50), PROFILE = join(tmpdir(), 'flower-e2e-' + process.pid), sleep = ms => new Promise(r => setTimeout(r, ms));
const chrome = spawn(process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', ['--headless=new', `--remote-debugging-port=${PORT}`, `--user-data-dir=${PROFILE}`,
  '--enable-unsafe-swiftshader', '--use-angle=swiftshader', '--ignore-gpu-blocklist', '--allow-file-access-from-files', '--hide-scrollbars', 'about:blank'], { stdio: 'ignore' });
const done = c => { try { chrome.kill('SIGKILL'); } catch {} try { rmSync(PROFILE, { recursive: true, force: true }); } catch {} process.exit(c); };
let wsUrl; for (let i = 0; i < 60; i++) { try { wsUrl = (await (await fetch(`http://127.0.0.1:${PORT}/json/new?about:blank`, { method: 'PUT' })).json()).webSocketDebuggerUrl; break; } catch { await sleep(250); } }
const ws = new WebSocket(wsUrl); let id = 0; const pend = new Map(), errs = [];
ws.onmessage = e => { const m = JSON.parse(e.data); if (m.method === 'Runtime.exceptionThrown') errs.push(m.params.exceptionDetails.exception?.description || m.params.exceptionDetails.text); if (m.id && pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); } };
await new Promise(r => ws.onopen = r);
const send = (method, params = {}) => new Promise(res => { const i = ++id; pend.set(i, res); ws.send(JSON.stringify({ id: i, method, params })); });
await send('Page.enable'); await send('Runtime.enable');
await send('Emulation.setDeviceMetricsOverride', { width: +W, height: +H, deviceScaleFactor: 2, mobile: +W < 700 });
await send('Page.navigate', { url }); await sleep(2500);
const body = readFileSync(scenario, 'utf8');
const r = await send('Runtime.evaluate', { expression: `(async()=>{const W=ms=>new Promise(r=>setTimeout(r,ms)),q=s=>document.querySelector(s),qa=s=>[...document.querySelectorAll(s)];
  const click=async s=>{const el=typeof s==='string'?q(s):s;if(!el)throw new Error('없음: '+s+' @'+location.hash);el.click();await W(90)};
  const set=async(s,v)=>{const el=q(s);if(!el)throw new Error('없음: '+s+' @'+location.hash);el.value=v;el.dispatchEvent(new Event('input',{bubbles:true}));el.dispatchEvent(new Event('change',{bubbles:true}));await W(150)};
  const go=async h=>{location.hash=h;await W(450)}, text=s=>(q(s)?.innerText||'').replace(/\\n+/g,' | ');
  const login=async id=>{if(q('[data-act=logout]')){await click('[data-act=logout]');await W(200)}await click('[data-act=login][data-id='+id+']');await W(300)};
  ${body}
})()`, awaitPromise: true, returnByValue: true });
if (r.result?.exceptionDetails) { console.log('시나리오 실패:', r.result.exceptionDetails.exception?.description || r.result.exceptionDetails.text); }
else console.log(typeof r.result?.result?.value === 'string' ? r.result.result.value : JSON.stringify(r.result?.result?.value, null, 1));
if (errs.length) console.log('페이지 오류:\n' + errs.join('\n'));
if (shot) { await sleep(800); const p = await send('Page.captureScreenshot', { format: 'png' }); writeFileSync(shot, Buffer.from(p.result.data, 'base64')); }
done(r.result?.exceptionDetails || errs.length ? 1 : 0);
