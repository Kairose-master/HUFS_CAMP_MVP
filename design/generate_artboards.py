# -*- coding: utf-8 -*-
import json, os
ROOT = os.path.dirname(os.path.abspath(__file__))
P = ROOT  # 산출물은 design/ 바로 아래에 쓴다

# ReBloom 시각 시스템 — landing/app.html 과 같은 토큰(iOS grouped · 라이트)
BG = "#F2F2F7"; CELL = "#FFFFFF"; INNER = "#F2F2F7"; INK = "#000000"; MUTED = "#6C6C70"; GLYPH = "#8E8E93"
SEP = "rgba(60,60,67,.2)"; FILL = "rgba(120,120,128,.12)"; FILL2 = "rgba(120,120,128,.2)"
TINT = "#0066CC"; TINT_FILL = "#0071E3"; TINT_BG = "rgba(0,113,227,.1)"
RED = "#D70015"; RED_BG = "rgba(215,0,21,.08)"; ORANGE = "#A84A00"; ORANGE_BG = "rgba(201,82,0,.1)"
GREEN = "#1D7A34"; GREEN_BG = "rgba(29,122,52,.1)"; STAR = "#FF9500"; SWITCH_ON = "#34C759"
DARK = "#1C1C1E"; DARK_RED = "#FF453A"; DARK_2 = "#AEAEB2"   # 근조 긴급 헤더 전용
FLOAT = "0 10px 30px rgba(0,0,0,.12),0 1px 3px rgba(0,0,0,.08)"; SEGSH = "0 3px 8px rgba(0,0,0,.12),0 1px 1px rgba(0,0,0,.04)"
SANS = "-apple-system,BlinkMacSystemFont,'Apple SD Gothic Neo','Pretendard Variable',Pretendard,'Noto Sans KR',system-ui,sans-serif"

CSS = """
*{box-sizing:border-box}
body{margin:0;background:$BG;color:$INK;font:400 17px/22px $SANS;letter-spacing:-.01em;-webkit-font-smoothing:antialiased;word-break:keep-all;overflow-wrap:break-word}
h1,h2,h3,p{margin:0}a{color:$TINT;text-decoration:none}
button,input{font:inherit;color:inherit;letter-spacing:inherit}button{cursor:pointer}
input[type=number]{-moz-appearance:textfield}
input::-webkit-outer-spin-button,input::-webkit-inner-spin-button{-webkit-appearance:none;margin:0}
.num,.mono{font-variant-numeric:tabular-nums;font-feature-settings:"tnum"}
.t-lt{font-size:34px;line-height:41px;font-weight:700;letter-spacing:-.025em}
.t-t2{font-size:22px;line-height:28px;font-weight:700;letter-spacing:-.02em}.t-t3{font-size:20px;line-height:25px;font-weight:600;letter-spacing:-.02em}
.t-h{font-size:17px;line-height:22px;font-weight:600}.t-s{font-size:15px;line-height:20px}.t-f{font-size:13px;line-height:18px}.t-c{font-size:12px;line-height:16px}
.c2,.muted{color:$MUTED}.c-tint{color:$TINT}.c-red{color:$RED}.c-orange{color:$ORANGE}.c-green{color:$GREEN}.b{font-weight:600}
.grow{flex:1;min-width:0}.r{text-align:right}
.nav{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;height:44px;padding:0 8px;flex-shrink:0}
.nav-t{font-size:17px;line-height:22px;font-weight:600;text-align:center}.nav-r{justify-self:end;display:flex;align-items:center}
.backbtn{display:inline-flex;align-items:center;gap:1px;height:44px;padding:0 8px 0 0;font-size:17px;justify-self:start}
.iconbtn{width:44px;height:44px;border:0;background:none;padding:0;display:flex;align-items:center;justify-content:center;color:$TINT}
.lt{padding:2px 20px 10px}.lede{padding:0 20px 6px;font-size:15px;line-height:20px;color:$MUTED}
.note{padding:0 20px 14px;font-size:13px;line-height:18px;color:$MUTED}
.sec-h{display:flex;align-items:center;justify-content:space-between;gap:12px;margin:28px 20px 10px}
.sec-h.has-n{margin-bottom:2px}.sec-n{margin:0 20px 10px;font-size:13px;line-height:18px;color:$MUTED}
.sec-l{margin:24px 32px 7px;font-size:13px;line-height:18px;color:$MUTED}.sec-f{margin:8px 32px 0;font-size:13px;line-height:18px;color:$MUTED}
.cell{background:$CELL;border-radius:20px;overflow:hidden}.group{margin:0 16px;background:$CELL;border-radius:20px;overflow:hidden}.group+.group{margin-top:12px}
.row{position:relative;display:flex;align-items:center;gap:12px;min-height:52px;padding:10px 16px;color:inherit}
.row+.row::before,.pad+.row::before,.row+.pad::before,.pad+.pad::before{content:"";position:absolute;top:0;left:16px;right:0;height:1px;background:$SEP}
.row.in68+.row.in68::before{left:68px}
.pad{position:relative;padding:14px 16px}
.kv .v{flex:1;min-width:0;text-align:right;color:$MUTED}
.tile{width:40px;height:40px;border-radius:10px;background:$FILL;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.avatar{width:40px;height:40px;border-radius:50%;background:linear-gradient(#73737A,#5C5C61);color:#fff;display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:600;flex-shrink:0;letter-spacing:0}
.avatar.lg{width:60px;height:60px;font-size:26px}
.inbox{border-radius:12px;background:$INNER;padding:10px 12px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:7px;min-height:50px;padding:0 22px;border-radius:999px;border:0;background:$TINT_FILL;color:#fff;font-size:17px;line-height:22px;font-weight:600;white-space:nowrap}
.btn.full{width:100%}.btn.md{min-height:44px;padding:0 18px;font-size:15px}.btn.gray{background:$FILL;color:$TINT}.btn:disabled{background:$FILL;color:$MUTED;cursor:default}
.cap{position:relative;display:inline-flex;align-items:center;justify-content:center;height:32px;min-width:64px;padding:0 16px;border-radius:999px;border:0;background:$FILL;color:$TINT;font-size:15px;line-height:20px;font-weight:700;white-space:nowrap;flex-shrink:0}
.cap::after,.chipb::after{content:"";position:absolute;inset:-6px 0}
.textbtn{border:0;background:none;padding:0;min-height:44px;color:$TINT;font-size:15px;line-height:20px;display:inline-flex;align-items:center;gap:1px;white-space:nowrap}
.stp{display:inline-flex;align-items:center;height:36px;border-radius:999px;background:$FILL;flex-shrink:0}
.stp button{position:relative;width:42px;height:36px;border:0;background:none;padding:0;display:flex;align-items:center;justify-content:center}
.stp button::after{content:"";position:absolute;inset:-4px 0}.stp .n{min-width:26px;text-align:center;font-size:17px;font-weight:600}
.seg{display:grid;grid-auto-flow:column;grid-auto-columns:1fr;padding:2px;border-radius:999px;background:$FILL;margin:0 16px}
.seg button{min-width:0;height:40px;border:0;border-radius:999px;background:transparent;font-size:15px;font-weight:500;padding:0 2px;white-space:nowrap}
.seg button[aria-pressed=true]{background:$CELL;font-weight:600;box-shadow:$SEGSH}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chipb{position:relative;display:inline-flex;align-items:center;gap:2px;height:34px;padding:0 15px;border-radius:999px;border:0;background:$FILL;font-size:15px;line-height:20px;font-weight:500;white-space:nowrap}
.chipb[aria-pressed=true]{background:$INK;color:#fff;font-weight:600}
.badge{display:inline-flex;align-items:center;gap:3px;font-size:12px;line-height:16px;font-weight:600;padding:3px 8px;border-radius:999px;background:$FILL;color:$MUTED;white-space:nowrap}
.badge.green{background:$GREEN_BG;color:$GREEN}.badge.orange{background:$ORANGE_BG;color:$ORANGE}.badge.red{background:$RED_BG;color:$RED}
.badge.fillred{background:$RED;color:#fff}.badge.ink{color:$INK}
.badges{display:flex;flex-wrap:wrap;gap:6px}
.delta{display:inline-flex;align-items:center;gap:2px;font-weight:600;white-space:nowrap}
.fld{display:block;width:100%;height:40px;border:0;border-radius:10px;background:$FILL;padding:0 10px;text-align:right;font-size:17px;font-weight:600;color:$INK}
.fld.focus{box-shadow:0 0 0 3px rgba(0,113,227,.55)}
.ro{height:40px;display:flex;align-items:center;color:$MUTED;font-size:17px}
.slider{-webkit-appearance:none;appearance:none;display:block;width:100%;height:28px;margin:0;background:transparent}
.slider::-webkit-slider-runnable-track{height:4px;border-radius:2px;background:linear-gradient(to right,$TINT_FILL var(--p,50%),$FILL2 var(--p,50%))}
.slider::-webkit-slider-thumb{-webkit-appearance:none;width:28px;height:28px;margin-top:-12px;border-radius:50%;background:#fff;box-shadow:0 3px 8px rgba(0,0,0,.15),0 1px 1px rgba(0,0,0,.16),0 0 0 .5px rgba(0,0,0,.04)}
.slider::-moz-range-track{height:4px;border-radius:2px;background:$FILL2}.slider::-moz-range-progress{height:4px;border-radius:2px;background:$TINT_FILL}
.slider::-moz-range-thumb{width:28px;height:28px;border:0;border-radius:50%;background:#fff;box-shadow:0 3px 8px rgba(0,0,0,.15),0 1px 1px rgba(0,0,0,.16)}
.switch{position:relative;width:51px;height:31px;border-radius:999px;border:0;background:$FILL2;padding:0;flex-shrink:0}.switch::before{content:"";position:absolute;inset:-7px 0}
.switch::after{content:"";position:absolute;top:2px;left:2px;width:27px;height:27px;border-radius:50%;background:#fff;box-shadow:0 3px 8px rgba(0,0,0,.15),0 1px 1px rgba(0,0,0,.16)}
.switch[aria-checked=true]{background:$SWITCH_ON}.switch[aria-checked=true]::after{transform:translateX(20px)}
.meter{height:6px;border-radius:3px;background:$FILL2;overflow:hidden}.meter i{display:block;height:100%;border-radius:3px;background:$TINT_FILL}
.stats{display:flex;text-align:center}.stats>div{flex:1;min-width:0;padding:2px 4px}.stats>div+div{border-left:1px solid $SEP}
.dock{padding:12px 16px 16px;display:flex;flex-direction:column;gap:8px;flex-shrink:0}
.glass{background:rgba(255,255,255,.78);-webkit-backdrop-filter:saturate(180%) blur(24px);backdrop-filter:saturate(180%) blur(24px);box-shadow:$FLOAT}
.acc{display:flex;align-items:center;gap:12px;padding:8px 8px 8px 22px;border-radius:999px;min-height:62px}.acc .btn{min-height:46px}
.tabbar{display:grid;grid-auto-flow:column;grid-auto-columns:1fr;height:62px;padding:4px;border-radius:999px}
.tabbar a{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px;height:54px;border-radius:999px;font-size:11px;line-height:13px;font-weight:500;color:$INK}
.tabbar a[aria-current=page]{color:$TINT;background:$FILL;font-weight:600}
"""
_tok = dict(BG=BG, CELL=CELL, INNER=INNER, INK=INK, MUTED=MUTED, GLYPH=GLYPH, SEP=SEP, FILL2=FILL2, FILL=FILL, TINT_FILL=TINT_FILL, TINT_BG=TINT_BG, TINT=TINT,
            RED_BG=RED_BG, RED=RED, ORANGE_BG=ORANGE_BG, ORANGE=ORANGE, GREEN_BG=GREEN_BG, GREEN=GREEN, SWITCH_ON=SWITCH_ON, FLOAT=FLOAT, SEGSH=SEGSH, SANS=SANS)
for k in sorted(_tok, key=len, reverse=True): CSS = CSS.replace("$" + k, _tok[k])

FONT = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">'

# 보드 크기 — 파일 생성과 canvas.json 이 같이 쓴다
SIZES = {"Main.dc.html": (390,1587), "Builder-Filled.dc.html": (390,1825), "Builder-Detail.dc.html": (390,844),
         "Owner-Today.dc.html": (390,1320), "Owner-Orders.dc.html": (390,1311), "Owner-OrderDetail.dc.html": (390,1292),
         "Owner-Prices.dc.html": (390,1502), "Owner-Prices-Tablet.dc.html": (1024,768), "Owner-Customers.dc.html": (390,1013),
         "Owner-CustomerDetail.dc.html": (390,1134), "Owner-Funeral.dc.html": (390,844)}

def page(title, w, h, body, logic="renderVals(){return {};}", props=None, extra_css=""):
    props = props or {}
    props["$preview"] = {"width": w, "height": h}
    pj = json.dumps(props, ensure_ascii=False).replace("&", "&amp;").replace("'", "&#39;")
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONT}
<style>{CSS}{extra_css}</style>
</helmet>
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{pj}'>
class Component extends DCLogic {{
{logic}
}}
</script>
</body>
</html>
"""

# ---------- icons (inline stroke svg) ----------
def ic(path, size=22, color="currentColor", sw=1.8, st=""):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink:0;{st}">{path}</svg>'
I = dict(
    back='<path d="M15 5l-7 7 7 7"/>',
    sliders='<path d="M4 7h10M18 7h2M4 17h4M12 17h8"/><circle cx="16" cy="7" r="2"/><circle cx="10" cy="17" r="2"/>',
    plus='<path d="M12 5v14M5 12h14"/>',
    minus='<path d="M5 12h14"/>',
    chev='<path d="M6 9l6 6 6-6"/>',
    chevr='<path d="M9 6l6 6-6 6"/>',
    camera='<path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/>',
    bell='<path d="M6 16V11a6 6 0 0112 0v5l2 2H4z"/><path d="M10 20a2 2 0 004 0"/>',
    search='<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/>',
    home='<path d="M4 11l8-7 8 7v9H4z"/><path d="M10 20v-6h4v6"/>',
    list='<path d="M5 6h14M5 12h14M5 18h9"/>',
    chart='<path d="M4 19h16M6 15l4-5 4 3 5-7"/>',
    users='<circle cx="9" cy="8" r="3.5"/><path d="M3 20a6 6 0 0112 0"/><circle cx="17" cy="9" r="2.5"/><path d="M15.5 14a5 5 0 015.5 5"/>',
    more='<circle cx="6" cy="12" r="1.6"/><circle cx="12" cy="12" r="1.6"/><circle cx="18" cy="12" r="1.6"/>',
    copy='<rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V6a2 2 0 00-2-2H6a2 2 0 00-2 2v8a2 2 0 002 2h2"/>',
    check='<path d="M5 12l5 5 9-10"/>',
    ribbon='<path d="M12 3l2 3-2 3-2-3z"/><path d="M12 9v12M8 21l4-4 4 4"/>',
    cake='<path d="M4 20h16v-6H4zM6 14v-3h12v3M12 5v3M9 6v2M15 6v2"/>',
    repeat='<path d="M4 10a6 6 0 0110-4l3 3M20 14a6 6 0 01-10 4l-3-3"/><path d="M17 4v5h-5M7 20v-5h5"/>',
    pin='<path d="M12 21s6-6 6-11a6 6 0 10-12 0c0 5 6 11 6 11z"/><circle cx="12" cy="10" r="2"/>',
    clock='<circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/>',
    send='<path d="M20 4L4 11l7 2 2 7z"/>',
    heart='<path d="M12 20s-7-4.5-7-10a4 4 0 017-2.5A4 4 0 0119 10c0 5.5-7 10-7 10z"/>',
    ban='<circle cx="12" cy="12" r="8"/><path d="M6.5 6.5l11 11"/>',
    x='<path d="M6 6l12 12M18 6L6 18"/>',
    warn='<path d="M12 4l9 16H3z"/><path d="M12 10v4M12 17h.01"/>',
    filter='<path d="M4 6h16M7 12h10M10 18h4"/>',
    bag='<path d="M5 8h14l-1 12H6z"/><path d="M9 8V7a3 3 0 016 0v1"/>',
)
# 유니코드 글리프(▲▼) 대신 쓰는 작은 채움 삼각형
TRI_UP = "M4 1l3.5 6h-7z"; TRI_DOWN = "M4 7L.5 1h7z"
def tri(up, s=8): return f'<svg width="{s}" height="{s}" viewBox="0 0 8 8" fill="currentColor" aria-hidden="true" style="flex-shrink:0;"><path d="{TRI_UP if up else TRI_DOWN}"/></svg>'

# ---------- flower placeholder (꽃만 색을 갖는다) ----------
def flower(petal, center="#EAD6A8", size=64, stem="#7C8F6A"):
    p = []
    for a in (0, 72, 144, 216, 288):
        p.append(f'<ellipse cx="32" cy="18" rx="7" ry="11" fill="{petal}" stroke="rgba(0,0,0,.1)" stroke-width=".8" transform="rotate({a} 32 28)"/>')
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" aria-hidden="true" style="flex-shrink:0;">'
            f'<path d="M32 40v22" stroke="{stem}" stroke-width="3" stroke-linecap="round"/>'
            f'<path d="M32 52c-6-2-9-6-9-10 5 0 8 4 9 10z" fill="{stem}"/>'
            + "".join(p) + f'<circle cx="32" cy="28" r="5" fill="{center}"/></svg>')

def euca(size=64, col="#7C8F6A"):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" aria-hidden="true" style="flex-shrink:0;">'
            f'<path d="M32 62V8" stroke="{col}" stroke-width="2.5" stroke-linecap="round"/>'
            + "".join(f'<circle cx="{32+(-10 if i%2 else 10)}" cy="{12+i*9}" r="6" fill="{col}" opacity="{0.9-i*0.08}"/>' for i in range(6))
            + '</svg>')

WHITE = "#F3EEE3"; PINK = "#E9C4C0"; REDF = "#B84A45"; YEL = "#E7C86A"; IVORY = "#EFE6D2"; PHOTO_BG = "#E5E5EA"

def photo(kind, h=120, bg=PHOTO_BG):
    inner = {"mum": flower(WHITE, size=72), "rose": flower(REDF, "#7D2E2B", 72), "lisi": flower(WHITE, "#D9CBA5", 72),
             "carn": flower(PINK, "#C98A86", 72), "tulip": flower(YEL, "#B89A3E", 72), "euca": euca(72), "ivory": flower(IVORY, "#D9CBA5", 72)}[kind]
    return f'<div style="height:{h}px;background:{bg};display:flex;align-items:center;justify-content:center;">{inner}</div>'

# ---------- shared pieces ----------
def switch(on, label):
    return f'<button type="button" role="switch" aria-checked="{"true" if on else "false"}" aria-label="{label}" class="switch"></button>'

def badge(text, tone="", solid=False):
    # solid: 사진 위에 얹을 때 흰 바탕을 깔아 대비를 지킨다
    bg = {"green": GREEN_BG, "orange": ORANGE_BG, "red": RED_BG}.get(tone, FILL)
    st = f' style="background:linear-gradient({bg},{bg}),#fff;"' if solid else ""
    return f'<span class="badge {tone}"{st}>{text}</span>'

def chip(text, on=False, icon=None):
    return f'<button type="button" class="chipb" aria-pressed="{"true" if on else "false"}">{text}{ic(I[icon],16) if icon else ""}</button>'

def delta(v, size=13):
    if v is None: return f'<span class="num c2" style="font-size:{size}px;">—</span>'
    up = v > 0
    return f'<span class="delta num {"c-red" if up else "c-tint"}" style="font-size:{size}px;">{tri(up)}{abs(v)}%</span>'

def caption(text):
    # 발표용 맥락 한 줄 — 라지 타이틀(또는 상단 바) 아래 13px 보조 글
    return f'<p class="note">{text}</p>'

def tabbar(active):
    tabs = [("오늘", "home"), ("주문", "list"), ("시세", "chart"), ("손님", "users"), ("더보기", "more")]
    out = []
    for name, icon in tabs:
        on = name == active
        out.append(f'<a href="#" aria-current="{"page" if on else "false"}">{ic(I[icon], 24, sw=2 if on else 1.8)}{name}</a>')
    return f'<nav class="tabbar glass" aria-label="주요 메뉴">{"".join(out)}</nav>'

def dock(*parts):
    return f'<div class="dock">{"".join(parts)}</div>'

def iconbtn(icon, label):
    return f'<button type="button" class="iconbtn" aria-label="{label}">{ic(I[icon], 24)}</button>'

def topbar(title, right=None, back="뒤로"):
    l = f'<a class="backbtn" href="#">{ic(I["back"], 24, sw=2.4)}<span>{back}</span></a>' if back else "<span></span>"
    return f'<header class="nav">{l}<h1 class="nav-t">{title}</h1><div class="nav-r">{right or ""}</div></header>'

def ohead(title, sub=None, right=None, note=None):
    # 탭 루트 화면: 44px 바(우측 액션) + 라지 타이틀 + 보조 설명
    return (f'<header class="nav"><span></span><span></span><div class="nav-r">{right or ""}</div></header>'
            f'<h1 class="lt t-lt">{title}</h1>' + (f'<p class="lede">{sub}</p>' if sub else "") + (caption(note) if note else ""))

def sec(title, note=None, right=""):
    cls = "sec-h has-n" if note else "sec-h"
    return f'<div class="{cls}"><h2 class="t-t2">{title}</h2>{right}</div>' + (f'<p class="sec-n">{note}</p>' if note else "")

def root(w, h, inner, bg=BG):
    return f'<div style="width:{w}px;height:{h}px;box-sizing:border-box;background:{bg};display:flex;flex-direction:column;overflow:hidden;position:relative;">{inner}</div>'

def money(n, size=17, weight=600, unit="원", cls=""):
    return f'<span class="num {cls}" style="font-size:{size}px;font-weight:{weight};">{n:,}{unit}</span>'

def btn(text, kind="", icon=None, extra=""):
    return f'<button type="button" class="btn full {kind}" style="{extra}">{ic(I[icon],20,sw=2) if icon else ""}{text}</button>'

# =====================================================================
# CONSUMER BUILDER
# =====================================================================
CATALOG = [
    ("국화", "백선 · 특", 1200, 8, "제철", "mum"),
    ("장미", "레드나오미 · 상", 2800, -5, None, "rose"),
    ("리시안셔스", "화이트 · 특", 3500, 2, None, "lisi"),
    ("카네이션", "핑크 · 상", 1500, -12, "오늘만 할인", "carn"),
    ("튤립", "옐로우 · 특", 2200, 15, None, "tulip"),
    ("유칼립투스", "그린 · 줄기", 1800, None, None, "euca"),
]

def catalog_card(name, sub, price, d, bdg, kind, in_cart=0):
    b = f'<div style="position:absolute;top:10px;left:10px;">{badge(bdg, "green" if bdg == "제철" else "orange", solid=True)}</div>' if bdg else ""
    btnh = (f'<div class="cap" style="width:100%;gap:4px;background:{GREEN_BG};color:{GREEN};">{ic(I["check"],16,sw=2.4)}<span class="num">담김 {in_cart}</span></div>'
            if in_cart else f'<button type="button" class="cap" style="width:100%;" aria-label="{name} 담기">담기</button>')
    return (f'<article class="cell" style="position:relative;display:flex;flex-direction:column;">'
            f'{photo(kind, 124)}{b}'
            f'<div style="padding:10px 12px 14px;display:flex;flex-direction:column;gap:2px;flex:1;">'
            f'<div class="t-h">{name}</div>'
            f'<div style="display:flex;align-items:center;justify-content:space-between;gap:6px;flex-wrap:wrap;"><span class="t-f c2">{sub}</span>{delta(d)}</div>'
            f'<div style="display:flex;align-items:baseline;gap:4px;flex-wrap:wrap;margin:4px 0 10px;"><span class="t-f c2">오늘</span>{money(price)}<span class="t-f c2">/송이</span></div>'
            f'<div style="margin-top:auto;">{btnh}</div></div></article>')

def filters():
    return f'<div class="chips" style="padding:0 16px 12px;">{chip("전체", True)}{chip("제철")}{chip("5천원 이하")}{chip("색상별", icon="chev")}</div>'

def catalog(in_cart=None):
    in_cart = in_cart or {}
    cards = "".join(catalog_card(*c, in_cart=in_cart.get(c[0], 0)) for c in CATALOG)
    return (f'<section>{sec("오늘의 꽃", "aT 화훼공판장 경매 시세 · 05:00 갱신")}'
            f'{filters()}<div style="display:grid;grid-template-columns:repeat(2, minmax(0, 1fr));gap:10px;padding:0 16px;">{cards}</div></section>')

def budget_bar(total, budget=50000, over=False):
    pct = min(100, round(total / budget * 100))
    col = "c-orange" if over else ""
    return (f'<section class="group"><div class="pad" style="display:flex;flex-direction:column;gap:8px;">'
            f'<div style="display:flex;align-items:flex-end;justify-content:space-between;gap:12px;">'
            f'<div><div class="t-f c2">현재 합계</div><div style="display:flex;align-items:baseline;gap:6px;flex-wrap:wrap;">{money(total, 22, 700, cls=col)}<span class="num t-s c2">예산의 {pct}%</span></div></div>'
            f'<div class="r"><div class="t-f c2">예산</div>{money(budget, 17, 600)}</div></div>'
            f'<label style="display:block;"><span style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);">예산 설정</span>'
            f'<input type="range" class="slider" min="10000" max="150000" step="5000" defaultValue="{budget}"></label></div></section>')

def preview_card(filled):
    if not filled:
        body = (f'<div style="height:200px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;padding:16px 24px;text-align:center;">'
                f'<div style="margin-bottom:2px;">{flower("#D1D1D6", "#C7C7CC", 52, "#C7C7CC")}</div><div class="t-t3">꽃을 담아보세요</div><div class="t-s c2">아래에서 송이 단위로 고르면 여기에 쌓여요</div></div>')
    else:
        stems = []
        # 국화 10 · 리시안셔스 3 · 유칼립투스 2 — 겹쳐 쌓은 다발
        pos = [(120,70,58),(160,54,62),(200,66,58),(140,96,56),(184,98,60),(104,104,52),(222,104,54),(156,124,56),(120,134,50),(196,134,52)]
        for x,y,s in pos: stems.append(f'<div style="position:absolute;left:{x}px;top:{y-40}px;">{flower(WHITE, size=s)}</div>')
        for x,y,s in [(92,70,60),(236,72,58),(164,80,54)]: stems.append(f'<div style="position:absolute;left:{x}px;top:{y-40}px;">{flower("#F7F3EA","#D9CBA5",s)}</div>')
        for x,y,s in [(70,90,72),(250,88,70)]: stems.append(f'<div style="position:absolute;left:{x}px;top:{y-40}px;">{euca(s)}</div>')
        body = (f'<div style="height:200px;position:relative;overflow:hidden;">{"".join(stems)}</div>'
                f'<div class="badges" style="padding:0 16px 12px;">{badge("국화 10", "ink")}{badge("리시안셔스 3", "ink")}{badge("유칼립투스 2", "ink")}</div>')
    toggle = f'<div class="row"><span class="grow">플로리스트에게 배치 맡기기</span>{switch(filled, "플로리스트에게 배치 맡기기")}</div>'
    return f'<section class="group" style="margin-top:12px;"><div>{body}</div>{toggle}</section>'

def stepper(n):
    return (f'<div class="stp"><button type="button" aria-label="1송이 빼기">{ic(I["minus"],18,sw=2)}</button>'
            f'<span class="n num">{n}</span>'
            f'<button type="button" aria-label="1송이 더하기">{ic(I["plus"],18,sw=2)}</button></div>')

def cart_row(name, sub, n, price, unit="송이", swiped=False):
    body = (f'<div class="grow" style="display:flex;flex-direction:column;gap:6px;">'
            f'<div style="display:flex;align-items:baseline;justify-content:space-between;gap:12px;"><span class="t-h">{name}</span>{money(n*price)}</div>'
            f'<div style="display:flex;align-items:center;justify-content:space-between;gap:12px;"><span class="t-f c2 num grow">{sub} · {price:,}원/{unit}</span>{stepper(n)}</div></div>')
    if swiped:
        # 밀어서 삭제 상태: 내용은 잘리지 않게 줄어들고 오른쪽에 삭제가 드러난다
        return (f'<div class="row" style="padding:0;gap:0;align-items:stretch;"><div style="flex:1;min-width:0;display:flex;padding:10px 12px 10px 16px;">{body}</div>'
                f'<button type="button" style="width:76px;border:0;background:{RED};color:#fff;font-size:17px;font-weight:600;flex-shrink:0;">삭제</button></div>')
    return f'<div class="row">{body}</div>'

def cart_list(rows):
    title = f'담은 꽃 <span class="num c2" style="font-weight:400;">{len(rows)}</span>'
    if not rows:
        return f'<section>{sec(title)}<div class="group"><div class="pad t-s c2">담은 꽃이 여기에 줄로 쌓여요. 옆으로 밀면 뺄 수 있어요.</div></div></section>'
    head = sec(title, right='<span class="t-f c2">옆으로 밀어 삭제</span>')
    return f'<section>{head}<div class="group">{"".join(rows)}</div></section>'

def bottom_bar(total, enabled, expanded=False):
    # 하단 CTA: 플로팅 글래스 캡슐(app.html 의 .acc)
    return dock(f'<div class="acc glass"><button type="button" class="grow" aria-expanded="{"true" if expanded else "false"}" style="border:0;background:none;padding:0;text-align:left;min-height:44px;">'
                f'<div class="t-c c2">합계</div><div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;"><span class="t-t3 num">{total:,}원</span>'
                f'<span class="t-s c-tint" style="display:inline-flex;align-items:center;gap:1px;">상세{ic(I["chev"],16,sw=2)}</span></div></button>'
                f'<button type="button" class="btn" {"" if enabled else "disabled"}>주문하기</button></div>')

def builder_top():
    return topbar("나만의 꽃다발", iconbtn("sliders", "예산 설정"), back="홈")

def builder(filled, name):
    w, h = SIZES[name]
    rows = [] if not filled else [
        cart_row("국화", "백선 · 특", 10, 1200),
        cart_row("리시안셔스", "화이트 · 특", 3, 3500),
        cart_row("유칼립투스", "그린", 2, 1800, "줄기", swiped=True),
    ]
    total = 37100 if filled else 0
    inner = (builder_top()
             + f'<div style="flex:1;padding:8px 0 12px;">'
             + budget_bar(total) + preview_card(filled) + cart_list(rows)
             + catalog({"국화":10,"리시안셔스":3,"유칼립투스":2} if filled else None) + '</div>'
             + bottom_bar(total, filled))
    return page("ReBloom 꽃다발 빌더 — " + ("담긴 상태" if filled else "빈 상태"), w, h, root(w, h, inner), extra_css=".slider{--p:28.6%}")

def builder_detail():
    w, h = SIZES["Builder-Detail.dc.html"]
    # 어두워진 배경: 담긴 상태 화면의 윗부분
    back = builder_top() + f'<div style="padding:8px 0 0;">' + budget_bar(37100) + preview_card(True) + '</div>'
    # 픽업 전용 — 꽃값 + 부자재 + 디자인비 = 합계
    sheet_rows = [("꽃값", "국화 10 · 리시안셔스 3 · 유칼립투스 2", 26100), ("부자재", "포장지 · 리본", 3000), ("디자인비", "플로리스트 배치", 8000)]
    total = sum(r[2] for r in sheet_rows)
    rows_html = "".join(f'<div class="row"><div class="grow"><div>{a}</div><div class="t-f c2 num">{b}</div></div>{money(c, 17, 400)}</div>' for a, b, c in sheet_rows)
    sheet = (f'<div style="position:absolute;left:0;right:0;bottom:0;background:{BG};border-radius:28px 28px 0 0;display:flex;flex-direction:column;padding-bottom:20px;">'
             f'<div style="display:flex;justify-content:center;padding:6px 0 0;"><div style="width:36px;height:5px;border-radius:3px;background:#C7C7CC;"></div></div>'
             f'<div class="nav" style="height:50px;padding:0 8px 0 16px;"><span></span><h2 class="nav-t">가격 상세</h2><div class="nav-r"><button type="button" class="textbtn" style="padding:0 8px;font-size:17px;font-weight:600;">완료</button></div></div>'
             f'<p class="sec-l" style="margin-top:4px;">오늘 시세 기준 · 05:00 갱신</p>'
             f'<div class="group">{rows_html}'
             f'<div class="pad" style="display:flex;flex-direction:column;gap:10px;"><div style="display:flex;align-items:baseline;justify-content:space-between;gap:12px;"><span class="t-h">합계</span>{money(total, 22, 700)}</div>'
             f'<div class="meter"><i style="width:{round(total/500)}%;"></i></div><div class="t-f c2 num">예산 50,000원의 {round(total/500)}%</div></div></div>'
             f'<div class="group"><div class="pad"><div class="t-h" style="display:flex;align-items:center;gap:6px;flex-wrap:wrap;">이 조합, 어제보다 {delta(4, 17)}</div>'
             f'<div class="t-f c2 num" style="margin-top:4px;">국화 {delta(8)}가 올렸어요 · 어제였다면 꽃값 25,000원 · 지금이 오늘 최저가 기준입니다</div></div></div>'
             f'<div style="padding:16px 16px 0;"><button type="button" class="btn full">주문하기 <span class="num">{total:,}원</span></button></div></div>')
    inner = (f'<div style="flex:1;">{back}</div>'
             f'<div style="position:absolute;inset:0;background:rgba(0,0,0,.36);"></div>{sheet}')
    return page("ReBloom 꽃다발 빌더 — 가격 상세 펼침", w, h, root(w, h, inner), extra_css=".slider{--p:28.6%}")

# =====================================================================
# OWNER APP
# =====================================================================
def stat(label, n, unit="", tone=None, size=28):
    col = {"red": RED, "orange": ORANGE, None: INK}[tone]
    return (f'<div><div class="t-f c2">{label}</div>'
            f'<div class="num" style="font-size:{size}px;line-height:{size+6}px;font-weight:700;letter-spacing:-.02em;color:{col};">{n}<span style="font-size:17px;font-weight:400;margin-left:1px;">{unit}</span></div></div>')

def home():
    w, h = SIZES["Owner-Today.dc.html"]
    def line(left, cnt, right, red=False):
        c = "c-red" if red else ""
        return (f'<div class="row">{left}<span class="num t-h {c}">{cnt}건</span><span class="grow r t-s num {c if red else "c2"}" style="font-weight:{600 if red else 400};">{right}</span></div>')
    more = f'<a href="#" class="textbtn">주문 보기{ic(I["chevr"],16,sw=2)}</a>'
    todo = (f'<section>{sec("오늘 할 일", right=more)}'
            f'<div class="group"><div class="pad">{stat("제작할 주문", 7, "건", size=34)}</div>'
            + line(badge("근조", "fillred"), 2, "13:00 픽업 마감", red=True)
            + line('<span>예약 주문</span>', 3, "내일 09:00")
            + line('<span>일반 · 픽업</span>', 2, "15:00 · 18:00")
            + '</div></section>')
    rows = [("국화 백선 특", "확정 80 · 예약 30 · 구독 10", 120, 60, 60), ("장미 레드나오미 상", "확정 25 · 예약 15", 40, 30, 10),
            ("리시안셔스 화이트 특", "확정 12", 12, 15, 0), ("카네이션 핑크 상", "확정 20", 20, 40, 0)]
    grid = "display:grid;grid-template-columns:minmax(0,1fr) 40px 40px 44px;gap:8px;align-items:center;"
    trs = ""
    for name, src, need, stock, short in rows:
        sh = f'<span class="num c-orange" style="font-weight:700;">{short}</span>' if short else f'<span class="t-s c2">충분</span>'
        trs += (f'<div class="row" style="{grid}">'
                f'<div><div class="t-s b">{name}</div><div class="t-f c2 num">{src}</div></div>'
                f'<span class="num r">{need}</span><span class="num r c2">{stock}</span><span class="r">{sh}</span></div>')
    order = (f'<section>{sec("내일 새벽 발주 제안", "9/19 (토) 새벽 기준")}'
             f'<div class="group"><div class="row t-f c2" style="{grid}min-height:36px;padding-top:8px;padding-bottom:8px;"><span>품목 · 필요 근거</span><span class="r">필요</span><span class="r">재고</span><span class="r">부족</span></div>'
             f'{trs}'
             f'<div class="pad" style="display:flex;flex-direction:column;gap:12px;">'
             f'<div class="inbox t-s b c-orange" style="background:{ORANGE_BG};display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap;"><span>부족 2품목</span><span class="num">국화 3속 · 장미 1속</span></div>'
             f'{btn("발주 메모로 복사", icon="copy")}</div></div></section>')
    stock_rows = [("카네이션 핑크 상", 1, 40, True, "2,900원"), ("튤립 옐로우 특", 2, 8, False, None), ("장미 레드나오미 상", 2, 12, False, None)]
    srs = ""
    for name, days, qty, on, disc in stock_rows:
        dischtml = f'<span class="c-orange b">할인가 {disc}</span>' if disc else ""
        srs += (f'<div class="row"><div class="grow"><div class="t-h">{name}</div>'
                f'<div class="t-f num" style="display:flex;gap:2px 8px;flex-wrap:wrap;"><span class="b {"c-orange" if days <= 1 else ""}">{days}일 남음</span><span class="c2">{qty}송이</span>{dischtml}</div></div>'
                f'{switch(on, name + " 오늘만 할인")}</div>')
    stock = f'<section>{sec("신선기간 임박", "오늘만 할인 · 켜면 소비자 앱에 즉시 노출")}<div class="group">{srs}</div></section>'
    inner = (ohead("오늘", "9월 18일 금요일 · 시세 05:00 갱신됨", iconbtn("bell", "알림"), "문제 1·5 · 새벽 발주를 도박에서 계산으로")
             + f'<div style="flex:1;margin-top:-18px;padding-bottom:12px;">{todo}{order}{stock}</div>'
             + dock(tabbar("오늘")))
    return page("ReBloom 사장님 — 오늘", w, h, root(w, h, inner))

def order_card(kind, title, who, where, budget, comp, colors, delegated, when, msg, urgent=False, status="대기"):
    icon = {"funeral": "ribbon", "birthday": "cake", "sub": "repeat"}[kind]
    tile = f'background:{RED_BG};color:{RED};' if urgent else ""
    tcol = "c-red" if urgent else ""
    return (f'<article class="group">'
            f'<div class="row" style="align-items:flex-start;"><div class="tile" style="{tile}">{ic(I[icon],22)}</div>'
            f'<div class="grow"><div class="t-h {tcol}">{title}</div><div class="t-f c2">{who} · {where}</div></div>'
            f'<div style="display:flex;flex-direction:column;align-items:flex-end;gap:4px;flex-shrink:0;"><span class="num t-s b {tcol}">{when}</span>{badge(status, "orange" if status=="제작 중" else "")}</div></div>'
            f'<div class="pad t-s" style="display:grid;grid-template-columns:44px minmax(0,1fr);gap:6px 10px;">'
            f'<span class="c2">예산</span><span class="num b">{budget}</span>'
            f'<span class="c2">구성</span><span class="num">{comp}</span>'
            f'<span class="c2">색감</span><span style="display:flex;gap:4px 10px;align-items:center;flex-wrap:wrap;">{colors}</span>'
            f'<span class="c2">배치</span><span>{badge("플로리스트 맡김", "green") if delegated else badge("소비자 배치 그대로")}</span>'
            f'<span class="c2">카드</span><span>“{msg}”</span></div></article>')

def swatch(col, name):
    return f'<span class="t-s" style="display:inline-flex;align-items:center;gap:5px;"><span style="width:14px;height:14px;border-radius:50%;background:{col};box-shadow:inset 0 0 0 1px rgba(0,0,0,.12);flex-shrink:0;"></span>{name}</span>'

def orders():
    w, h = SIZES["Owner-Orders.dc.html"]
    seg = (f'<div class="seg">'
           f'<button type="button" aria-pressed="true" class="num">오늘 7</button>'
           f'<button type="button" aria-pressed="false" class="num">예약 3</button>'
           f'<button type="button" aria-pressed="false" class="num">완료 12</button></div>')
    cards = "".join([
        order_card("funeral", '근조 화환 · <span style="white-space:nowrap;">마감 2시간 10분 전</span>', "김민준", "매장 픽업", "150,000원", "국화 백선 60 · 리시안셔스 화이트 10 · 유칼립투스 5",
                   swatch("#F3EEE3", "화이트") + swatch("#7C8F6A", "그린"), True, "13:00 픽업", "삼가 고인의 명복을 빕니다", urgent=True, status="제작 중"),
        order_card("birthday", "생일 · 직접 만든 꽃다발", "이서연", "본인 · 매장 픽업", "50,000원", "국화 백선 10 · 리시안셔스 화이트 3 · 유칼립투스 2",
                   swatch("#F3EEE3", "화이트") + swatch("#7C8F6A", "그린"), False, "15:00 픽업", "서른 살 축하해, 나."),
        order_card("birthday", "생일 · 어머니께", "최유진", "매장 픽업", "80,000원", "리시안셔스 화이트 20 · 장미 레드나오미 5 · 유칼립투스 3",
                   swatch("#F3EEE3", "화이트") + swatch("#B84A45", "레드"), True, "16:00 픽업", "엄마, 올해도 고마워요", status="대기"),
        order_card("sub", "구독 · 매주 금요일", "박지훈", "매장 픽업", "30,000원", "사장님 추천 · 계절꽃 위주", swatch("#E7C86A", "옐로우") + swatch("#E9C4C0", "핑크"), True, "18:00 픽업", "카드 없음"),
    ])
    inner = (ohead("주문", "오늘 7건 · 카드만 보고 만들면 됩니다", iconbtn("search", "주문 검색"), "문제 2·7 · 카톡 30분 상담을 구조화된 주문서 한 장으로")
             + seg + f'<div style="flex:1;padding:14px 0 12px;">{cards}</div>' + dock(tabbar("주문")))
    return page("ReBloom 사장님 — 주문 목록", w, h, root(w, h, inner))

def order_detail():
    w, h = SIZES["Owner-OrderDetail.dc.html"]
    prev = (f'<section class="group" style="height:180px;position:relative;">'
            f'<div style="position:absolute;top:12px;left:12px;z-index:1;">{badge("소비자가 만든 프리뷰", "ink", solid=True)}</div>'
            + "".join(f'<div style="position:absolute;left:{x}px;top:{y}px;">{flower(WHITE,"#D9CBA5",s)}</div>' for x,y,s in [(96,52,56),(140,40,60),(184,50,58),(120,80,52),(164,84,54),(208,80,50),(228,48,52),(76,84,48)])
            + "".join(f'<div style="position:absolute;left:{x}px;top:{y}px;">{flower(REDF,"#7D2E2B",s)}</div>' for x,y,s in [(60,54,52),(250,60,54),(150,110,50)])
            + "".join(f'<div style="position:absolute;left:{x}px;top:{y}px;">{euca(s)}</div>' for x,y,s in [(40,80,64),(270,86,64),(110,100,58)])
            + f'<div style="position:absolute;right:12px;bottom:12px;">{badge("플로리스트 맡김", "green", solid=True)}</div></section>')
    comp = [("리시안셔스 화이트 특", 20, 15, True), ("장미 레드나오미 상", 5, 30, False), ("유칼립투스 그린", 3, 40, False)]
    crs = ""
    for name, need, stock, short in comp:
        st = (f'<span class="num t-f b c-orange">재고 {stock} · 부족 {need-stock}</span>' if short
              else f'<span class="num t-f b c-green" style="display:inline-flex;align-items:center;gap:2px;">{ic(I["check"],14,sw=2.4)}재고 {stock}</span>')
        crs += (f'<div class="row"><div class="grow t-h">{name}</div>'
                f'<div style="display:flex;flex-direction:column;align-items:flex-end;flex-shrink:0;"><span class="num t-h">{need}송이</span>{st}</div></div>')
    sub = (f'<div class="pad"><div class="inbox" style="background:{ORANGE_BG};padding:12px;display:flex;flex-direction:column;gap:10px;">'
           f'<div class="t-s"><span class="b c-orange">대체 제안</span> · 리시안셔스 화이트 {ic(I["chevr"],14,sw=2.4,st="vertical-align:-2px;")} <b>아이보리</b> <span class="num">(재고 25 · 같은 가격)</span></div>'
           f'<div style="display:flex;align-items:center;gap:8px 12px;flex-wrap:wrap;"><button type="button" class="btn md">{ic(I["send"],18,sw=2)}대체 제안 보내기</button>'
           f'<span class="t-f b c-orange" style="display:inline-flex;align-items:center;gap:4px;">{ic(I["clock"],16)}소비자 승인 대기</span></div></div></div>')
    info = (f'<section class="group">'
            f'<div class="row kv"><span>받는 분</span><span class="v">어머니 · 최유진 님이 픽업</span></div>'
            f'<div class="row kv"><span>픽업 시간</span><span class="v num">오늘 16:00</span></div>'
            f'<div class="row kv"><span>예산</span><span class="v num"><span style="color:{INK};font-weight:600;">80,000원</span><br><span class="t-f">소비자 합계 78,400원</span></span></div>'
            f'<div class="row kv"><span>메시지 카드</span><span class="v">“엄마, 올해도 고마워요”</span></div></section>')
    tiles = "".join(f'<div class="inbox" style="padding:12px 6px;display:flex;flex-direction:column;align-items:center;gap:3px;text-align:center;"><span class="c-tint" style="display:flex;">{ic(I[i],22)}</span><span class="t-f b">{t}</span><span class="t-c c2">{s}</span></div>'
                    for i, t, s in [("send", "손님 알림", "사진과 함께 완성 알림"), ("heart", "포트폴리오", "매장 페이지에 자동 등록"), ("users", "손님 이력", "최유진 · 어머니 생일에 저장")])
    complete = (f'<section>{sec("제작 완료", "한 번 찍으면 세 가지가 됩니다")}<div class="group"><div class="pad" style="display:flex;flex-direction:column;gap:10px;">'
                f'<button type="button" class="btn full" style="min-height:56px;">{ic(I["camera"],24,sw=2)}완성 사진 찍기</button>'
                f'<div style="display:flex;justify-content:center;height:18px;"><svg width="240" height="18" viewBox="0 0 240 18" fill="none" stroke="{GLYPH}" stroke-width="1.5" aria-hidden="true"><path d="M120 0v6M120 6H24v12M120 6v12M120 6h96v12"/></svg></div>'
                f'<div style="display:grid;grid-template-columns:repeat(3, minmax(0, 1fr));gap:8px;">{tiles}</div></div></div></section>')
    inner = (topbar("주문 #1043 · 생일", f'<span style="padding-right:8px;display:flex;">{badge("대기", "ink", solid=True)}</span>', back="주문")
             + caption("문제 2·7 · 대화 없이 만들고, 한 번 찍어 세 가지 일을 끝내기")
             + f'<div style="flex:1;padding-bottom:12px;">{prev}{info}'
             + f'<section>{sec("꽃 구성 · 재고 대조")}<div class="group">{crs}{sub}</div></section>'
             + f'{complete}</div>' + dock(tabbar("주문")))
    return page("ReBloom 사장님 — 주문 상세", w, h, root(w, h, inner))

# ---- 시세 data ----
ITEMS = [
    dict(id="mum", name="국화", var="백선", grade="특", box=24000, per=20, margin=2.8, delta=8, stock=60, on=True, disc=False, discPrice=None,
         hist=[20000,20000,21000,22000,21000,22000,23000,22000,22000,23000,22000,22000,22200,24000]),
    dict(id="rose", name="장미", var="레드나오미", grade="상", box=28000, per=10, margin=2.5, delta=-5, stock=30, on=True, disc=False, discPrice=None,
         hist=[30000,31000,30000,29000,30000,32000,31000,30000,29000,30000,29500,29000,29500,28000]),
    dict(id="lisi", name="리시안셔스", var="화이트", grade="특", box=35000, per=10, margin=2.8, delta=2, stock=15, on=True, disc=False, discPrice=None,
         hist=[33000,33000,34000,34000,33000,34000,35000,35000,34000,34000,34500,34000,34300,35000]),
    dict(id="carn", name="카네이션", var="핑크", grade="상", box=30000, per=20, margin=2.8, delta=-12, stock=40, on=True, disc=True, discPrice=2900,
         hist=[36000,36000,35000,35000,34000,35000,34000,34000,33000,34000,34000,34000,34000,30000]),
    dict(id="tulip", name="튤립", var="옐로우", grade="특", box=22000, per=10, margin=3.0, delta=15, stock=0, on=False, disc=False, discPrice=None,
         hist=[18000,18000,19000,19000,18500,19000,19000,20000,19500,19000,19000,19500,19100,22000]),
]

def chart_svg(hist, w, h, color=TINT_FILL):
    lo, hi = min(hist)*0.92, max(hist)*1.04
    pts = []
    for i, v in enumerate(hist):
        x = 8 + i*(w-16)/(len(hist)-1); y = h-18 - (v-lo)/(hi-lo)*(h-32)
        pts.append((round(x,1), round(y,1)))
    d = "M" + " L".join(f"{x} {y}" for x,y in pts)
    area = d + f" L{pts[-1][0]} {h-18} L{pts[0][0]} {h-18} Z"
    grid = "".join(f'<line x1="8" x2="{w-8}" y1="{h-18-(h-32)*k/3:.1f}" y2="{h-18-(h-32)*k/3:.1f}" stroke="{SEP}"/>' for k in range(4))
    return (f'<svg width="100%" viewBox="0 0 {w} {h}" role="img" aria-label="14일 시세 추이" style="display:block;">{grid}'
            f'<path d="{area}" fill="{color}" opacity=".1"/><path d="{d}" fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round"/>'
            f'<circle cx="{pts[-1][0]}" cy="{pts[-1][1]}" r="4" fill="{color}"/>'
            f'<text x="8" y="{h-2}" font-size="12" fill="{MUTED}">9/5</text><text x="{w-8}" y="{h-2}" font-size="12" fill="{MUTED}" text-anchor="end">오늘</text></svg>')

def price_item_mobile(it, editing=False):
    sale = round(it["box"]/it["per"]*it["margin"], -1)
    off = not it["on"]
    lab = lambda t: f'<span class="t-c c2">{t}</span>'
    margin_cell = (f'<label style="display:flex;flex-direction:column;gap:3px;">{lab("마진계수")}'
                   f'<input type="number" step="0.1" aria-label="마진계수" defaultValue="{3.0 if editing else it["margin"]}" class="fld num{" focus" if editing else ""}"></label>')
    new_sale = round(it["box"]/it["per"]*3.0, -1)
    struck = f'<span class="num t-c c2" style="text-decoration:line-through;">{sale:,.0f}</span>'
    sale_cell = (f'<div style="display:flex;flex-direction:column;gap:3px;">{lab("송이 판매가")}<div style="height:40px;display:flex;flex-direction:column;justify-content:center;">'
                 + (f'<span class="num t-h">{new_sale:,.0f}</span>{struck}' if editing
                    else (f'<span class="num t-h c-orange">{it["discPrice"]:,}</span>{struck}' if it["disc"] else f'<span class="num t-h">{sale:,.0f}</span>')) + '</div></div>')
    m = 3.0 if editing else it["margin"]
    expl = f'시세 {it["box"]:,}원/속 ÷ {it["per"]}송이 × 마진 {m} = <b style="color:{INK};">{(new_sale if editing else sale):,.0f}원</b>'
    return (f'<article class="group">'
            f'<div class="row">{switch(it["on"], it["name"] + " 취급")}'
            f'<div class="grow {"c2" if off else ""}"><div class="t-h">{it["name"]} <span style="font-weight:400;">{it["var"]} · {it["grade"]}</span></div>'
            f'<div class="t-f num" style="display:flex;gap:2px 6px;align-items:center;flex-wrap:wrap;"><span class="c2">어제 대비</span>{delta(it["delta"])}<span class="c2">· 재고 {it["stock"]}송이</span></div></div>'
            + (f'<span class="t-f c2" style="flex-shrink:0;">취급 안 함</span>' if off else f'<div style="display:flex;flex-direction:column;align-items:flex-end;gap:3px;flex-shrink:0;"><span class="t-c c2">오늘만 할인</span>{switch(it["disc"], it["name"] + " 오늘만 할인")}</div>')
            + '</div>'
            + ("" if off else
               f'<div class="pad" style="display:grid;grid-template-columns:repeat(4, minmax(0, 1fr));gap:8px;padding-top:10px;padding-bottom:10px;">'
               f'<div style="display:flex;flex-direction:column;gap:3px;">{lab("속 단가")}<div class="ro num">{it["box"]:,}</div></div>'
               f'<div style="display:flex;flex-direction:column;gap:3px;">{lab("송이수/속")}<div class="ro num">{it["per"]}</div></div>'
               f'{margin_cell}{sale_cell}</div>'
               f'<div class="row" style="align-items:center;"><div class="grow t-f c2 num"><div class="b" style="color:{INK};">손님에게 보이는 설명</div>{expl}</div>'
               f'<button type="button" class="cap">보여주기</button></div>')
            + '</article>')

def prices_mobile():
    w, h = SIZES["Owner-Prices.dc.html"]
    cards = "".join(price_item_mobile(it, editing=(i == 0)) for i, it in enumerate(ITEMS))
    chart = (f'<section class="group"><div class="pad" style="display:flex;flex-direction:column;gap:8px;">'
             f'<div style="display:flex;align-items:baseline;justify-content:space-between;gap:8px;flex-wrap:wrap;"><h2 class="t-h">국화 백선 특 · 14일 시세</h2><span class="t-f c2">속 단가 · 원</span></div>'
             f'{chart_svg(ITEMS[0]["hist"], 326, 124)}'
             f'<div class="t-f num" style="display:flex;gap:2px 14px;flex-wrap:wrap;"><span><span class="c2">14일 최저</span> <span class="b">20,000</span></span><span><span class="c2">최고</span> <span class="b">24,000</span></span><span style="display:inline-flex;align-items:center;gap:4px;"><span class="c2">오늘</span> <span class="b c-red">24,000</span>{delta(8)}</span></div></div></section>')
    inner = (ohead("시세 · 품목", "aT 공판장 시세 · 오늘 05:00 갱신", None, "문제 3·4 · “시세가 올라서요” 대신 계산식을 보여주기")
             + f'<p class="sec-l" style="margin-top:0;">회색 글자 = 시세 · 읽기전용 / 회색 칸 = 마진 · 편집</p>'
             + f'<div style="flex:1;padding-bottom:12px;">{cards}{chart}</div>' + dock(tabbar("시세")))
    return page("ReBloom 사장님 — 시세·품목 (모바일)", w, h, root(w, h, inner))

def prices_tablet():
    w, h = SIZES["Owner-Prices-Tablet.dc.html"]
    hdr = "".join(f'<span style="text-align:{a};">{t}</span>' for t, a in [("취급", "left"), ("품목 · 품종 · 등급", "left"), ("속 단가", "right"), ("송이/속", "right"), ("마진계수", "right"), ("송이 판매가", "right"), ("어제 대비", "right"), ("재고", "right"), ("오늘만 할인", "center")])
    # 표 안쪽 폭 672px 에 맞춘 열 — 고정 열 472 + 간격 48 + 품목 열
    cols = "51px minmax(0,1fr) 62px 48px 64px 76px 58px 62px 51px"
    ro = "height:40px;display:flex;align-items:center;justify-content:flex-end;font-size:17px;"
    row = (f'<sc-for list="{{{{items}}}}" as="it" hint-placeholder-count="5">'
           f'<div style="{{{{it.rowStyle}}}}"><span style="position:absolute;top:0;left:16px;right:0;height:1px;background:{SEP};"></span>'
           f'<button type="button" aria-pressed="{{{{it.on}}}}" aria-label="취급" onClick="{{{{it.toggleOn}}}}" style="{{{{it.onStyle}}}}"><span style="{{{{it.onKnob}}}}"></span></button>'
           f'<button type="button" onClick="{{{{it.select}}}}" style="border:0;background:transparent;text-align:left;padding:0;display:flex;flex-direction:column;min-height:44px;min-width:0;justify-content:center;"><span class="t-s b">{{{{it.name}}}} <span style="font-weight:400;">{{{{it.var}}}}</span></span><span class="t-c" style="color:{MUTED};">{{{{it.grade}}}}등급</span></button>'
           f'<div class="num" style="{ro}color:{MUTED};">{{{{it.boxFmt}}}}</div>'
           f'<div class="num" style="{ro}color:{MUTED};">{{{{it.per}}}}</div>'
           f'<input type="number" step="0.1" min="1" max="6" aria-label="마진계수" value="{{{{it.margin}}}}" onChange="{{{{it.onMargin}}}}" class="fld num" style="padding:0 8px;">'
           f'<div style="display:flex;flex-direction:column;align-items:flex-end;justify-content:center;min-height:44px;"><span class="num" style="{{{{it.saleStyle}}}}">{{{{it.saleFmt}}}}</span><sc-if value="{{{{it.disc}}}}" hint-placeholder-val="{{{{false}}}}"><span class="num t-c" style="color:{MUTED};text-decoration:line-through;">{{{{it.baseFmt}}}}</span></sc-if></div>'
           f'<span class="num" style="{{{{it.deltaStyle}}}}"><svg width="8" height="8" viewBox="0 0 8 8" fill="currentColor" aria-hidden="true"><path d="{{{{it.deltaPath}}}}"></path></svg>{{{{it.deltaFmt}}}}</span>'
           f'<input type="number" step="1" min="0" aria-label="재고" value="{{{{it.stock}}}}" onChange="{{{{it.onStock}}}}" class="fld num" style="padding:0 8px;">'
           f'<div style="display:flex;justify-content:center;"><button type="button" aria-pressed="{{{{it.disc}}}}" aria-label="오늘만 할인" onClick="{{{{it.toggleDisc}}}}" style="{{{{it.discStyle}}}}"><span style="{{{{it.discKnob}}}}"></span></button></div>'
           f'</div></sc-for>')
    table = (f'<section class="cell" style="flex:1;min-width:0;display:flex;flex-direction:column;">'
             f'<div class="t-c" style="display:grid;grid-template-columns:{cols};gap:6px;align-items:end;padding:12px 16px 8px;color:{MUTED};">{hdr}</div>'
             f'<div style="display:flex;flex-direction:column;">{row}</div>'
             f'<div class="t-f" style="margin-top:auto;padding:12px 16px;border-top:1px solid {SEP};display:flex;gap:4px 16px;flex-wrap:wrap;color:{MUTED};align-items:center;"><span>회색 글자 = 시세 · 읽기전용</span><span style="display:inline-flex;align-items:center;gap:6px;"><span style="width:28px;height:16px;border-radius:5px;background:{FILL};"></span>회색 칸 = 편집 가능</span><span>마진계수를 고치면 판매가가 바로 바뀝니다</span></div></section>')
    side = (f'<aside style="width:264px;flex-shrink:0;display:flex;flex-direction:column;gap:12px;">'
            f'<section class="cell" style="padding:14px 16px;display:flex;flex-direction:column;gap:8px;">'
            f'<h2 class="t-h">{{{{sel.name}}}} {{{{sel.var}}}} {{{{sel.grade}}}} · 14일 시세</h2>'
            f'<svg width="232" height="150" viewBox="0 0 232 150" role="img" aria-label="14일 시세 추이"><path d="{{{{chartArea}}}}" fill="{TINT_FILL}" opacity=".1"></path><path d="{{{{chartD}}}}" fill="none" stroke="{TINT_FILL}" stroke-width="2" stroke-linejoin="round"></path><circle cx="{{{{lastX}}}}" cy="{{{{lastY}}}}" r="4" fill="{TINT_FILL}"></circle><text x="8" y="148" font-size="12" fill="{MUTED}">9/5</text><text x="224" y="148" font-size="12" fill="{MUTED}" text-anchor="end">오늘</text></svg>'
            f'<div class="t-f num" style="display:flex;gap:2px 12px;flex-wrap:wrap;"><span><span class="c2">최저</span> <span class="b">{{{{loFmt}}}}</span></span><span><span class="c2">최고</span> <span class="b">{{{{hiFmt}}}}</span></span><span style="display:inline-flex;align-items:center;gap:4px;"><span class="c2">오늘</span><span class="b">{{{{sel.boxFmt}}}}</span><span style="{{{{sel.deltaStyle}}}}"><svg width="8" height="8" viewBox="0 0 8 8" fill="currentColor" aria-hidden="true"><path d="{{{{sel.deltaPath}}}}"></path></svg>{{{{sel.deltaFmt}}}}</span></span></div></section>'
            f'<section class="cell" style="padding:14px 16px 16px;display:flex;flex-direction:column;gap:8px;">'
            f'<h2 class="t-h">손님에게 보이는 가격 설명</h2>'
            f'<div class="num">시세 <b>{{{{sel.boxFmt}}}}원</b>/속 ÷ <b>{{{{sel.per}}}}</b>송이 × 마진 <b>{{{{sel.margin}}}}</b> = <span class="t-t3" style="white-space:nowrap;">{{{{sel.baseFmt}}}}원</span></div>'
            f'<div class="t-f c2">마진에는 폐기·포장·인건비가 들어 있어요. 손님 화면과 매장 안내판에 이 문구 그대로 표시됩니다.</div>'
            f'<button type="button" class="btn full" style="margin-top:4px;padding:0 12px;">손님 화면에 보여주기</button></section></aside>')
    inner = (f'<header style="display:flex;align-items:flex-end;justify-content:space-between;gap:16px;padding:20px 24px 14px;"><div style="min-width:0;"><h1 class="t-lt">시세 · 품목</h1><p class="t-s c2" style="margin-top:4px;">aT 화훼공판장 경매 시세 · 오늘 05:00 갱신 · 마진·재고는 바로 고쳐집니다</p>'
             f'<p class="t-f c2" style="margin-top:4px;">문제 3·4 · “시세가 올라서요” 대신 계산식을 보여주기 (태블릿)</p></div>'
             f'<div class="chips" style="flex-shrink:0;">{chip("전체", True)}{chip("취급 중")}{chip("재고 임박")}</div></header>'
             f'<div style="flex:1;display:flex;gap:16px;padding:0 20px 20px;min-height:0;">{table}{side}</div>')
    logic = """
constructor(p){super(p);this.state={sel:'mum',items:%s};}
fmt(n){return Math.round(n).toLocaleString('ko-KR');}
renderVals(){
  const ON='%s',O='%s',R='%s',T='%s',ink='%s',mut='%s',off='%s';
  const sw=(on)=>'width:51px;height:31px;border-radius:999px;border:0;padding:0;position:relative;flex-shrink:0;background:'+(on?ON:off)+';';
  const knob=(on)=>'position:absolute;top:2px;left:'+(on?22:2)+'px;width:27px;height:27px;border-radius:50%%;background:#fff;box-shadow:0 3px 8px rgba(0,0,0,.15),0 1px 1px rgba(0,0,0,.16);';
  const upd=(id,patch)=>this.setState({items:this.state.items.map(x=>x.id===id?{...x,...patch}:x)});
  const items=this.state.items.map(it=>{
    const base=Math.round(it.box/it.per*(parseFloat(it.margin)||0)/10)*10;
    const sale=it.disc&&it.discPrice?it.discPrice:base;
    const selected=it.id===this.state.sel;
    const flat=it.delta===0||it.delta==null;
    return {...it,
      boxFmt:this.fmt(it.box),baseFmt:this.fmt(base),saleFmt:this.fmt(sale),
      saleStyle:'font-size:17px;line-height:22px;font-weight:600;color:'+(it.disc?O:(it.on?ink:mut))+';',
      deltaFmt:flat?'—':Math.abs(it.delta)+'%%',
      deltaPath:flat?'':(it.delta>0?'%s':'%s'),
      deltaStyle:'display:inline-flex;align-items:center;justify-content:flex-end;gap:2px;font-size:15px;font-weight:600;white-space:nowrap;color:'+(flat?mut:(it.delta>0?R:T))+';',
      rowStyle:'position:relative;display:grid;grid-template-columns:%s;gap:6px;align-items:center;padding:8px 16px;'+(selected?'background:%s;':'')+(it.on?'':'color:'+mut+';'),
      onStyle:sw(it.on),onKnob:knob(it.on),discStyle:sw(it.disc),discKnob:knob(it.disc),
      toggleOn:()=>upd(it.id,{on:!it.on}),toggleDisc:()=>upd(it.id,{disc:!it.disc,discPrice:it.discPrice||Math.round(base*0.7/100)*100}),
      onMargin:(e)=>upd(it.id,{margin:e.target.value}),
      onStock:(e)=>upd(it.id,{stock:e.target.value}),
      select:()=>this.setState({sel:it.id})};
  });
  const sel=items.find(x=>x.id===this.state.sel)||items[0];
  const h=sel.hist,w=232,hh=150,lo=Math.min(...h)*0.92,hi=Math.max(...h)*1.04;
  const pts=h.map((v,i)=>[8+i*(w-16)/(h.length-1),hh-18-(v-lo)/(hi-lo)*(hh-32)]);
  const d='M'+pts.map(p=>p[0].toFixed(1)+' '+p[1].toFixed(1)).join(' L');
  const area=d+' L'+pts[pts.length-1][0].toFixed(1)+' '+(hh-18)+' L'+pts[0][0].toFixed(1)+' '+(hh-18)+' Z';
  return {items,sel,chartD:d,chartArea:area,lastX:pts[pts.length-1][0].toFixed(1),lastY:pts[pts.length-1][1].toFixed(1),loFmt:this.fmt(Math.min(...h)),hiFmt:this.fmt(Math.max(...h))};
}""" % (json.dumps(ITEMS, ensure_ascii=False), SWITCH_ON, ORANGE, RED, TINT, INK, MUTED, FILL2, TRI_UP, TRI_DOWN, cols, TINT_BG)
    return page("ReBloom 사장님 — 시세·품목 (태블릿)", w, h, root(w, h, inner), logic)

def customers():
    w, h = SIZES["Owner-Customers.dc.html"]
    soon = "".join(f'<div class="row"><div class="grow"><div class="t-h">{n}</div><div class="t-s c2 num">{e} · {d}</div></div><button type="button" class="cap">제안 보내기</button></div>'
                   for n, e, d in [("박지훈", "아버지 생신", "9/21 월"), ("이서연", "결혼기념일", "9/23 수"), ("최유진", "어머니 생신", "9/24 목")])
    alert = f'<section>{sec("이번 주 경조사 있는 손님 <span class=num>3</span>명", "제안 보내면 미리 발주에 반영")}<div class="group">{soon}</div></section>'
    people = [("이서연", "9/18 오늘", 6, "결혼기념일 9/23", True), ("박지훈", "9/11", 24, "아버지 생신 9/21", True), ("최유진", "9/18 오늘", 3, "어머니 생신 9/24", True),
              ("김민준", "9/18 오늘", 1, None, False), ("정하늘", "6/2", 2, "어머니 생신 10/3", False), ("오세훈", "3/14", 4, "화이트데이 매년 3/14", False), ("한소희", "2025/12/24", 1, None, False)]
    rows = ""
    for n, last, cnt, ev, near in people:
        evh = (f'<span class="num {"b" if near else "c2"}">{ev}</span>' if ev else '<span class="c2">등록된 경조사 없음</span>')
        rows += (f'<a href="#" class="row in68" style="color:{INK};"><div class="avatar">{n[0]}</div>'
                 f'<div class="grow"><div class="t-h">{n}</div><div class="t-f">{evh}</div></div>'
                 f'<div class="r" style="flex-shrink:0;"><div class="num t-s">{last}</div><div class="t-c c2">마지막 주문</div></div>'
                 f'<div class="r" style="width:34px;flex-shrink:0;"><div class="num t-h">{cnt}</div><div class="t-c c2">회</div></div></a>')
    sort = f'<button type="button" class="textbtn">최근 주문순{ic(I["chev"],16,sw=2)}</button>'
    inner = (ohead("손님", "128명 · 사진 찍을 때마다 이력이 쌓입니다", iconbtn("search", "손님 검색"), "문제 6 · 단골을 단골로 알아보기")
             + f'<div style="flex:1;margin-top:-18px;padding-bottom:12px;">{alert}'
             + f'<section>{sec("전체 손님", right=sort)}<div class="group">{rows}</div></section></div>'
             + dock(tabbar("손님")))
    return page("ReBloom 사장님 — 손님 목록", w, h, root(w, h, inner))

def customer_detail():
    w, h = SIZES["Owner-CustomerDetail.dc.html"]
    head = (f'<section style="padding:4px 16px 16px;display:flex;align-items:center;gap:14px;"><div class="avatar lg">이</div>'
            f'<div class="grow"><div class="t-t2">이서연</div><div class="t-f c2 num">첫 주문 2024.05 · 6회 · 누적 312,000원</div></div>'
            f'<button type="button" aria-label="전화" style="width:44px;height:44px;border-radius:50%;border:0;background:{CELL};color:{TINT};display:flex;align-items:center;justify-content:center;flex-shrink:0;padding:0;">{ic(I["send"],20)}</button></section>')
    upcoming = (f'<section class="group"><div class="pad" style="display:flex;flex-direction:column;gap:12px;">'
                f'<div style="display:flex;align-items:baseline;justify-content:space-between;gap:8px;flex-wrap:wrap;"><div class="t-h num">결혼기념일 · 9/23 (수)</div><span class="num t-s b">5일 남음</span></div>'
                f'<div class="inbox" style="display:flex;gap:10px;align-items:center;"><div style="width:44px;height:44px;border-radius:10px;background:{PHOTO_BG};display:flex;align-items:center;justify-content:center;flex-shrink:0;">{flower(WHITE,"#D9CBA5",36)}</div><div class="grow"><div class="t-s b">작년 구성</div><div class="t-f c2 num">리시안셔스 화이트 10 · 장미 5 · 유칼립투스 3 · 52,000원</div></div></div>'
                f'{btn("지난번 구성으로 제안 보내기", icon="send", extra="padding:0 12px;")}<div class="t-f c2 num" style="text-align:center;">오늘 시세로 다시 계산해 54,100원으로 보냅니다</div></div></section>')
    pref = (f'<section>{sec("취향 프로필")}<div class="group">'
            f'<div class="row"><span style="flex-shrink:0;">선호 색감</span><span class="grow" style="display:flex;gap:4px 10px;flex-wrap:wrap;justify-content:flex-end;">{swatch("#F3EEE3","화이트")}{swatch("#7C8F6A","그린")}{swatch("#E9C4C0","연핑크")}</span></div>'
            f'<div class="row"><span style="flex-shrink:0;">피하는 꽃</span><span class="grow badges" style="justify-content:flex-end;"><span class="badge red">{ic(I["ban"],14,sw=2)}백합 · 향이 강함</span></span></div>'
            f'<div class="row"><span style="flex-shrink:0;">분위기</span><span class="grow badges" style="justify-content:flex-end;">{badge("내추럴")}{badge("볼륨 적게")}{badge("크라프트 포장")}</span></div></div></section>')
    hist = [("2026.09.18", "생일 · 본인", 37100, WHITE), ("2025.09.23", "결혼기념일", 52000, WHITE), ("2025.05.08", "어버이날", 45000, PINK), ("2024.12.24", "크리스마스", 38000, REDF), ("2024.05.02", "첫 주문 · 집들이", 30000, YEL)]
    trs = ""
    for i, (d, u, amt, col) in enumerate(hist):
        linehtml = "" if i == len(hist)-1 else f'<span style="width:2px;height:54px;background:{FILL2};"></span>'
        trs += (f'<div style="display:flex;gap:12px;align-items:center;">'
                f'<div style="display:flex;flex-direction:column;align-items:center;width:12px;flex-shrink:0;"><span style="width:10px;height:10px;border-radius:50%;background:{TINT_FILL if i==0 else "#C7C7CC"};"></span>{linehtml}</div>'
                f'<div style="width:52px;height:52px;border-radius:12px;background:{PHOTO_BG};display:flex;align-items:center;justify-content:center;flex-shrink:0;">{flower(col,"#D9CBA5",40)}</div>'
                f'<div class="grow" style="padding-bottom:12px;"><div class="t-h">{u}</div><div class="num t-f c2">{d}</div></div><span style="padding-bottom:12px;flex-shrink:0;">{money(amt, 17, 400)}</span></div>')
    timeline = f'<section>{sec("주문 이력")}<div class="group"><div class="pad" style="padding-bottom:4px;display:flex;flex-direction:column;gap:8px;">{trs}</div></div></section>'
    inner = (topbar("손님 정보", iconbtn("more", "더보기"), back="손님")
             + caption("문제 6 · 작년에 뭘 보냈는지 앱이 기억한다")
             + f'<div style="flex:1;padding-bottom:12px;">{head}{upcoming}{pref}{timeline}</div>' + dock(tabbar("손님")))
    return page("ReBloom 사장님 — 손님 상세", w, h, root(w, h, inner))

def funeral():
    w, h = SIZES["Owner-Funeral.dc.html"]
    shops = [("화양플라워", 0.8, 120), ("반포꽃집", 1.4, 40), ("서초플라워", 2.6, 200)]
    srs = "".join(f'<div class="row"><div class="grow"><div class="t-h">{n}</div><div class="num t-f c2">{d}km · 보유 {q}송이</div></div><button type="button" class="cap num">20송이 요청</button></div>'
                  for n, d, q in shops)
    stats = "".join(f'<div>{s}</div>' for s in [stat("필요 국화", 80, "송이"), stat("내 재고", 60, "송이"), stat("부족", 20, "송이", tone="orange")])
    # 전체 화면 경보 — 헤더만 어둡게 유지한다
    inner = (f'<div style="background:{DARK};color:#fff;padding:8px 16px 18px;display:flex;flex-direction:column;gap:12px;">'
             f'<div style="display:flex;align-items:center;justify-content:space-between;"><div style="display:flex;align-items:center;gap:8px;">{badge("근조", "fillred")}<span class="t-h">근조 주문 도착</span></div><button type="button" aria-label="닫기" style="width:44px;height:44px;border:0;background:transparent;color:#fff;display:flex;align-items:center;justify-content:center;padding:0;">{ic(I["x"],22,sw=2)}</button></div>'
             f'<div style="display:flex;align-items:flex-end;justify-content:space-between;gap:12px;flex-wrap:wrap;"><div><div class="t-f" style="color:{DARK_2};">픽업 마감까지</div><div class="num" style="font-size:48px;line-height:52px;font-weight:700;letter-spacing:-.02em;color:{DARK_RED};">02:10:35</div></div><div class="r"><div class="t-f" style="color:{DARK_2};">마감</div><div class="num t-t2">오늘 13:00</div></div></div>'
             f'<div style="display:flex;gap:8px;align-items:flex-start;">{ic(I["bag"],20)}<div class="grow"><div class="t-s b">매장 픽업 · 김민준 님</div><div class="t-f num" style="color:{DARK_2};">서울성모병원 장례식장 3호실 조문용 · 근조 화환 · 150,000원</div></div></div></div>'
             f'<div style="flex:1;padding:16px 0 0;">'
             f'<section class="group"><div class="pad" style="display:flex;flex-direction:column;gap:12px;"><div class="stats">{stats}</div>'
             f'<div class="inbox t-f b c-orange num" style="background:{ORANGE_BG};">국화 백선 특 기준 · 리시안셔스 10, 유칼립투스 5는 재고 충분</div></div></section>'
             f'<section>{sec("근처 꽃집 재고 요청", "반경 3km 제휴 · 국화 백선 · 직접 가져오기")}<div class="group">{srs}</div></section></div>'
             + dock(f'<div class="glass" style="border-radius:34px;padding:9px;display:flex;flex-direction:column;gap:8px;">{btn("수락 · 제작 시작", icon="check")}{btn("다른 꽃집에 넘기기", "gray")}</div>'))
    return page("ReBloom 사장님 — 근조 긴급", w, h, root(w, h, inner))

# =====================================================================
files = {
    "Main.dc.html": builder(False, "Main.dc.html"),
    "Builder-Filled.dc.html": builder(True, "Builder-Filled.dc.html"),
    "Builder-Detail.dc.html": builder_detail(),
    "Owner-Today.dc.html": home(),
    "Owner-Orders.dc.html": orders(),
    "Owner-OrderDetail.dc.html": order_detail(),
    "Owner-Prices.dc.html": prices_mobile(),
    "Owner-Prices-Tablet.dc.html": prices_tablet(),
    "Owner-Customers.dc.html": customers(),
    "Owner-CustomerDetail.dc.html": customer_detail(),
    "Owner-Funeral.dc.html": funeral(),
}
for name, html in files.items():
    with open(os.path.join(P, name), "w", encoding="utf-8") as f: f.write(html)

sizes = SIZES
titles = {"Main.dc.html": "빌더 · 빈 상태", "Builder-Filled.dc.html": "빌더 · 담긴 상태", "Builder-Detail.dc.html": "빌더 · 가격 상세 펼침",
          "Owner-Today.dc.html": "1 오늘", "Owner-Orders.dc.html": "2 주문 목록", "Owner-OrderDetail.dc.html": "2 주문 상세 · 제작 완료",
          "Owner-Prices.dc.html": "3 시세·품목", "Owner-Prices-Tablet.dc.html": "3 시세·품목 · 태블릿", "Owner-Customers.dc.html": "4 손님",
          "Owner-CustomerDetail.dc.html": "4 손님 상세", "Owner-Funeral.dc.html": "5 근조 긴급"}
boards = {}
x = 0
row1 = ["Main.dc.html", "Builder-Filled.dc.html", "Builder-Detail.dc.html"]
for n in row1:
    w, h = sizes[n]; boards[n] = {"x": x, "y": 0, "w": w, "h": h, "title": titles[n]}; x += w + 80
ROW2 = max(sizes[n][1] for n in row1) + 120 + 240
x = 0
row2 = ["Owner-Today.dc.html", "Owner-Orders.dc.html", "Owner-OrderDetail.dc.html", "Owner-Prices.dc.html", "Owner-Customers.dc.html", "Owner-CustomerDetail.dc.html", "Owner-Funeral.dc.html", "Owner-Prices-Tablet.dc.html"]
for n in row2:
    w, h = sizes[n]; boards[n] = {"x": x, "y": ROW2, "w": w, "h": h, "title": titles[n]}
    if n == "Owner-Prices-Tablet.dc.html": boards[n]["is_interactive"] = True
    x += w + 80
canvas = {"v": 3, "createdOnFiles": {"v": 1, "at": "2026-09-18T03:00:00Z"}, "title": "ReBloom · 꽃다발 빌더 · 꽃집 앱",
          "launch": {"view": "canvas"}, "pages": [], "boards": boards,
          "order": row1 + row2,
          "notes": {"t1": {"x": 0, "y": -300, "text": "ReBloom 꽃다발 빌더 — 소비자 · 모바일 390", "kind": "title1", "maxW": 1330},
                    "t2": {"x": 0, "y": ROW2 - 300, "text": "ReBloom 꽃집 사장님 운영 앱 — 모바일 390 · 시세는 태블릿 1024 포함", "kind": "title1", "maxW": 4400}},
          "designSystems": []}
with open(os.path.join(P, "canvas.json"), "w", encoding="utf-8") as f: json.dump(canvas, f, ensure_ascii=False, indent=1)
print("wrote", len(files) + 1, "files")
