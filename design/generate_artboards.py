# -*- coding: utf-8 -*-
import json, os
ROOT = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(ROOT, "project")

GREEN = "#1F5A3C"; GREEN_T = "#E3EEE5"; ORANGE = "#B85A0C"; ORANGE_T = "#FBEBD9"
RED = "#B3261E"; RED_T = "#FAE3E0"; INK = "#1E1B16"; MUTED = "#6B655B"; LINE = "#E6DED1"
CREAM = "#F6F1E8"; CARD = "#FFFDF9"; SOFT = "#EFE9DE"

CSS = """
body{margin:0;font-family:'IBM Plex Sans KR',system-ui,-apple-system,sans-serif;background:%(cream)s;color:%(ink)s;-webkit-font-smoothing:antialiased}
a{color:%(green)s;text-decoration:none}a:hover{color:#143D29}
button,input{font-family:inherit;color:inherit}
button{cursor:pointer}
.mono{font-family:'IBM Plex Mono',ui-monospace,Menlo,monospace;font-variant-numeric:tabular-nums;letter-spacing:-0.02em}
.muted{color:%(muted)s}
.up{color:#C2382B}.down{color:%(green)s}.flat{color:#8A8378}
.card{background:%(card)s;border:1px solid %(line)s;border-radius:14px}
.ro{background:%(soft)s;color:#4A4439;border-radius:8px}
.ed{background:#fff;border:1.5px solid %(green)s;border-radius:8px}
input[type=range]{accent-color:%(green)s}
input[type=number]{-moz-appearance:textfield}
input::-webkit-outer-spin-button,input::-webkit-inner-spin-button{-webkit-appearance:none;margin:0}
""" % dict(cream=CREAM, ink=INK, green=GREEN, muted=MUTED, card=CARD, line=LINE, soft=SOFT)

FONT = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500;600;700&display=swap">'

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
def ic(path, size=22, color="currentColor", sw=1.8):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>'
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
    truck='<path d="M3 7h11v9H3zM14 10h4l3 3v3h-7z"/><circle cx="7" cy="18" r="1.8"/><circle cx="17" cy="18" r="1.8"/>',
)

# ---------- flower placeholder ----------
def flower(petal, center="#EAD6A8", size=64, stem="#7C8F6A"):
    p = []
    for a in (0, 72, 144, 216, 288):
        p.append(f'<ellipse cx="32" cy="18" rx="7" ry="11" fill="{petal}" transform="rotate({a} 32 28)"/>')
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" aria-hidden="true">'
            f'<path d="M32 40v22" stroke="{stem}" stroke-width="3" stroke-linecap="round"/>'
            f'<path d="M32 52c-6-2-9-6-9-10 5 0 8 4 9 10z" fill="{stem}"/>'
            + "".join(p) + f'<circle cx="32" cy="28" r="5" fill="{center}"/></svg>')

def euca(size=64, col="#7C8F6A"):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" aria-hidden="true">'
            f'<path d="M32 62V8" stroke="{col}" stroke-width="2.5" stroke-linecap="round"/>'
            + "".join(f'<circle cx="{32+(-10 if i%2 else 10)}" cy="{12+i*9}" r="6" fill="{col}" opacity="{0.9-i*0.08}"/>' for i in range(6))
            + '</svg>')

WHITE = "#F3EEE3"; PINK = "#E9C4C0"; REDF = "#B84A45"; YEL = "#E7C86A"; IVORY = "#EFE6D2"

def photo(kind, h=120, bg="#ECE5D8"):
    inner = {"mum": flower(WHITE, size=72), "rose": flower(REDF, "#7D2E2B", 72), "lisi": flower(WHITE, "#D9CBA5", 72),
             "carn": flower(PINK, "#C98A86", 72), "tulip": flower(YEL, "#B89A3E", 72), "euca": euca(72), "ivory": flower(IVORY, "#D9CBA5", 72)}[kind]
    return f'<div style="height:{h}px;background:{bg};display:flex;align-items:center;justify-content:center;">{inner}</div>'

# ---------- shared pieces ----------
def switch(on, label, big=False):
    w, h, k = (52, 30, 24) if big else (44, 26, 20)
    bg = GREEN if on else "#C9C1B3"
    left = w - k - 3 if on else 3
    return (f'<button type="button" aria-pressed="{"true" if on else "false"}" aria-label="{label}" '
            f'style="width:{w}px;height:{h}px;border-radius:999px;border:0;background:{bg};position:relative;padding:0;flex-shrink:0;">'
            f'<span style="position:absolute;top:3px;left:{left}px;width:{k}px;height:{k}px;border-radius:50%;background:#fff;box-shadow:0 1px 2px rgba(0,0,0,.25);"></span></button>')

def chip(text, on=False, tone=None):
    if tone == "green": return f'<span style="font-size:11px;font-weight:600;padding:3px 8px;border-radius:6px;background:{GREEN_T};color:{GREEN};">{text}</span>'
    if tone == "orange": return f'<span style="font-size:11px;font-weight:600;padding:3px 8px;border-radius:6px;background:{ORANGE_T};color:{ORANGE};">{text}</span>'
    if tone == "red": return f'<span style="font-size:11px;font-weight:700;padding:3px 8px;border-radius:6px;background:{RED};color:#fff;">{text}</span>'
    if tone == "soft": return f'<span style="font-size:12px;font-weight:500;padding:3px 9px;border-radius:999px;background:{SOFT};color:#4A4439;">{text}</span>'
    if on: return f'<button type="button" aria-pressed="true" style="height:36px;padding:0 14px;border-radius:999px;border:1.5px solid {GREEN};background:{GREEN};color:#fff;font-size:13px;font-weight:600;white-space:nowrap;">{text}</button>'
    return f'<button type="button" aria-pressed="false" style="height:36px;padding:0 14px;border-radius:999px;border:1.5px solid {LINE};background:{CARD};color:{INK};font-size:13px;font-weight:500;white-space:nowrap;">{text}</button>'

def delta(v):
    if v is None: return f'<span class="mono flat" style="font-size:12px;font-weight:600;">—</span>'
    if v > 0: return f'<span class="mono up" style="font-size:12px;font-weight:700;">▲{v}%</span>'
    return f'<span class="mono down" style="font-size:12px;font-weight:700;">▼{-v}%</span>'

def caption(text):
    return (f'<div style="height:36px;background:{GREEN};color:#fff;display:flex;align-items:center;gap:8px;padding:0 16px;font-size:12.5px;font-weight:500;">'
            f'<span style="font-size:10px;font-weight:700;letter-spacing:.08em;opacity:.75;">해결하는 문제</span><span>{text}</span></div>')

def tabbar(active):
    tabs = [("오늘", "home"), ("주문", "list"), ("시세", "chart"), ("손님", "users"), ("더보기", "more")]
    out = []
    for name, icon in tabs:
        on = name == active
        col = GREEN if on else MUTED
        out.append(f'<a href="#" aria-current="{"page" if on else "false"}" style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;height:60px;color:{col};font-size:11px;font-weight:{700 if on else 500};">{ic(I[icon], 24, sw=2 if on else 1.8)}{name}</a>')
    return f'<nav aria-label="주요 메뉴" style="height:60px;background:{CARD};border-top:1px solid {LINE};display:flex;flex-shrink:0;">{"".join(out)}</nav>'

def iconbtn(icon, label, size=44):
    return f'<button type="button" aria-label="{label}" style="width:{size}px;height:{size}px;border:0;background:transparent;display:flex;align-items:center;justify-content:center;border-radius:12px;padding:0;">{ic(I[icon], 24)}</button>'

def topbar(title, right=None, back=True):
    r = right if right else f'<div style="width:44px;height:44px;"></div>'
    l = iconbtn("back", "뒤로") if back else '<div style="width:44px;height:44px;"></div>'
    return (f'<header style="height:56px;display:flex;align-items:center;justify-content:space-between;padding:0 8px;flex-shrink:0;">'
            f'{l}<h1 style="margin:0;font-size:17px;font-weight:700;">{title}</h1>{r}</header>')

def root(w, h, inner, bg=CREAM):
    return f'<div style="width:{w}px;height:{h}px;box-sizing:border-box;background:{bg};display:flex;flex-direction:column;overflow:hidden;position:relative;">{inner}</div>'

def money(n, size=20, weight=700, unit="원", cls=""):
    return f'<span class="mono {cls}" style="font-size:{size}px;font-weight:{weight};">{n:,}<span style="font-size:{max(11,int(size*0.6))}px;font-weight:600;margin-left:1px;">{unit}</span></span>'

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

def catalog_card(name, sub, price, d, badge, kind, in_cart=0):
    b = ""
    if badge == "제철": b = f'<div style="position:absolute;top:8px;left:8px;">{chip("제철", tone="green")}</div>'
    if badge == "오늘만 할인": b = f'<div style="position:absolute;top:8px;left:8px;">{chip("오늘만 할인", tone="orange")}</div>'
    btn = (f'<div style="height:44px;border-radius:10px;background:{GREEN_T};color:{GREEN};display:flex;align-items:center;justify-content:center;gap:6px;font-size:13px;font-weight:700;">{ic(I["check"],16)}담김 {in_cart}</div>'
           if in_cart else
           f'<button type="button" style="height:44px;border-radius:10px;border:1.5px solid {GREEN};background:{CARD};color:{GREEN};font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:4px;">{ic(I["plus"],16)}담기</button>')
    return (f'<article class="card" style="overflow:hidden;position:relative;display:flex;flex-direction:column;">'
            f'{photo(kind, 124)}{b}'
            f'<div style="padding:10px 12px 12px;display:flex;flex-direction:column;gap:8px;">'
            f'<div style="display:flex;flex-direction:column;gap:1px;"><div style="font-size:15px;font-weight:600;">{name}</div><div class="muted" style="font-size:12px;">{sub}</div></div>'
            f'<div style="display:flex;align-items:baseline;justify-content:space-between;">'
            f'<div style="display:flex;align-items:baseline;gap:4px;"><span class="muted" style="font-size:11px;">오늘</span>{money(price, 18)}<span class="muted" style="font-size:11px;">/송이</span></div>{delta(d)}</div>'
            f'{btn}</div></article>')

def filters():
    return (f'<div style="display:flex;gap:8px;padding:0 16px;overflow:hidden;">{chip("전체", True)}{chip("제철")}{chip("5천원 이하")}'
            f'<button type="button" aria-pressed="false" style="height:36px;padding:0 12px 0 14px;border-radius:999px;border:1.5px solid {LINE};background:{CARD};font-size:13px;font-weight:500;display:flex;align-items:center;gap:2px;white-space:nowrap;">색상별{ic(I["chev"],16)}</button></div>')

def catalog(in_cart=None):
    in_cart = in_cart or {}
    cards = "".join(catalog_card(*c, in_cart=in_cart.get(c[0], 0)) for c in CATALOG)
    return (f'<section style="display:flex;flex-direction:column;gap:12px;">'
            f'<div style="display:flex;align-items:baseline;justify-content:space-between;padding:0 16px;"><h2 style="margin:0;font-size:16px;font-weight:700;">오늘의 꽃</h2><span class="muted" style="font-size:11.5px;">aT 화훼공판장 경매 시세 · 05:00 갱신</span></div>'
            f'{filters()}<div style="display:grid;grid-template-columns:repeat(2, minmax(0, 1fr));gap:10px;padding:0 16px;">{cards}</div></section>')

def budget_bar(total, budget=50000, over=False):
    pct = min(100, round(total / budget * 100))
    col = ORANGE if over else GREEN
    return (f'<section class="card" style="margin:0 16px;padding:12px 16px 14px;display:flex;flex-direction:column;gap:8px;">'
            f'<div style="display:flex;align-items:baseline;justify-content:space-between;">'
            f'<div style="display:flex;align-items:baseline;gap:6px;"><span class="muted" style="font-size:12px;">예산</span>{money(budget, 17, 600)}</div>'
            f'<div style="display:flex;align-items:baseline;gap:6px;"><span class="muted" style="font-size:12px;">현재 합계</span><span style="color:{col};">{money(total, 20)}</span><span class="mono" style="font-size:12px;color:{col};font-weight:600;">{pct}%</span></div></div>'
            f'<label style="display:flex;flex-direction:column;gap:4px;"><span style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);">예산 설정</span>'
            f'<input type="range" min="10000" max="150000" step="5000" defaultValue="{budget}" style="width:100%;margin:0;height:28px;"></label></section>')

def preview_card(filled):
    toggle = (f'<div style="position:absolute;top:12px;right:12px;display:flex;align-items:center;gap:8px;background:{CARD};border:1px solid {LINE};border-radius:999px;padding:5px 6px 5px 12px;">'
              f'<span style="font-size:12px;font-weight:600;">플로리스트에게 배치 맡기기</span>{switch(filled, "플로리스트에게 배치 맡기기")}</div>')
    if not filled:
        body = (f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;border:1.5px dashed #D3C9B8;border-radius:10px;margin:52px 14px 14px;">'
                f'<div style="opacity:.55;">{flower("#DDD3C2", "#CDBF9F", 56)}</div><div style="font-size:15px;font-weight:600;">꽃을 담아보세요</div><div class="muted" style="font-size:12.5px;">아래에서 송이 단위로 고르면 여기에 쌓여요</div></div>')
    else:
        stems = []
        # mums x10 (white), lisianthus x3, eucalyptus x2 — stacked bouquet
        pos = [(120,70,58),(160,54,62),(200,66,58),(140,96,56),(184,98,60),(104,104,52),(222,104,54),(156,124,56),(120,134,50),(196,134,52)]
        for x,y,s in pos: stems.append(f'<div style="position:absolute;left:{x}px;top:{y}px;">{flower(WHITE, size=s)}</div>')
        for x,y,s in [(92,70,60),(236,72,58),(164,80,54)]: stems.append(f'<div style="position:absolute;left:{x}px;top:{y}px;">{flower("#F7F3EA","#D9CBA5",s)}</div>')
        for x,y,s in [(70,90,72),(250,88,70)]: stems.append(f'<div style="position:absolute;left:{x}px;top:{y}px;">{euca(s)}</div>')
        body = (f'<div style="flex:1;position:relative;overflow:hidden;">{"".join(stems)}'
                f'<div style="position:absolute;left:0;right:0;bottom:0;height:56px;background:linear-gradient(to top, {CARD}, rgba(255,253,249,0));"></div>'
                f'<div style="position:absolute;left:14px;bottom:12px;display:flex;gap:6px;">{chip("국화 10", tone="soft")}{chip("리시안셔스 3", tone="soft")}{chip("유칼립투스 2", tone="soft")}</div></div>')
    return f'<section class="card" style="margin:0 16px;height:230px;position:relative;display:flex;flex-direction:column;overflow:hidden;">{toggle}{body}</section>'

def stepper(n):
    return (f'<div style="display:flex;align-items:center;border:1.5px solid {LINE};border-radius:10px;background:{CARD};height:40px;">'
            f'<button type="button" aria-label="1송이 빼기" style="width:40px;height:40px;border:0;background:transparent;display:flex;align-items:center;justify-content:center;">{ic(I["minus"],18)}</button>'
            f'<span class="mono" style="width:30px;text-align:center;font-size:16px;font-weight:700;">{n}</span>'
            f'<button type="button" aria-label="1송이 더하기" style="width:40px;height:40px;border:0;background:transparent;display:flex;align-items:center;justify-content:center;">{ic(I["plus"],18)}</button></div>')

def cart_row(name, sub, n, price, unit="송이", swiped=False):
    row = (f'<div style="display:flex;align-items:center;gap:10px;padding:10px 16px;background:{CARD};min-width:100%;box-sizing:border-box;{"transform:translateX(-84px);" if swiped else ""}">'
           f'<div style="flex:1;min-width:0;"><div style="font-size:15px;font-weight:600;">{name}</div><div class="muted" style="font-size:12px;">{sub} · {money(price,12,600,"원")}/{unit}</div></div>'
           f'{stepper(n)}<div class="mono" style="width:72px;text-align:right;font-size:16px;font-weight:700;">{n*price:,}<span style="font-size:11px;">원</span></div></div>')
    if swiped:
        row = f'<div style="position:relative;overflow:hidden;background:{RED};"><div style="position:absolute;right:0;top:0;bottom:0;width:84px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:14px;font-weight:700;">삭제</div>{row}</div>'
    return row

def cart_list(rows):
    if not rows:
        return (f'<section style="padding:0 16px;display:flex;flex-direction:column;gap:8px;"><div style="display:flex;align-items:baseline;gap:6px;"><h2 style="margin:0;font-size:16px;font-weight:700;">담은 꽃</h2><span class="mono muted" style="font-size:14px;">0</span></div>'
                f'<div class="muted" style="font-size:13px;padding:6px 0 0;">담은 꽃이 여기에 줄로 쌓여요. 옆으로 밀면 뺄 수 있어요.</div></section>')
    body = "".join(rows)
    return (f'<section style="display:flex;flex-direction:column;gap:8px;"><div style="display:flex;align-items:baseline;justify-content:space-between;padding:0 16px;"><div style="display:flex;align-items:baseline;gap:6px;"><h2 style="margin:0;font-size:16px;font-weight:700;">담은 꽃</h2><span class="mono muted" style="font-size:14px;">3</span></div><span class="muted" style="font-size:11.5px;">옆으로 밀어 삭제</span></div>'
            f'<div style="margin:0 16px;border:1px solid {LINE};border-radius:14px;overflow:hidden;display:flex;flex-direction:column;background:{CARD};">{body}</div></section>')

def bottom_bar(total, enabled, expanded=False):
    btn_bg = GREEN if enabled else "#C9C1B3"
    return (f'<footer style="height:84px;background:{CARD};border-top:1px solid {LINE};display:flex;align-items:center;justify-content:space-between;padding:0 16px;flex-shrink:0;box-shadow:0 -6px 16px rgba(30,27,22,.05);">'
            f'<div style="display:flex;flex-direction:column;gap:2px;"><span class="muted" style="font-size:11.5px;">합계</span>'
            f'<button type="button" aria-expanded="{"true" if expanded else "false"}" style="border:0;background:transparent;padding:0;display:flex;align-items:center;gap:4px;height:32px;">{money(total, 22)}<span style="display:flex;align-items:center;gap:1px;color:{GREEN};font-size:12.5px;font-weight:600;margin-left:4px;">상세{ic(I["chev"],16)}</span></button></div>'
            f'<button type="button" {"" if enabled else "disabled"} style="width:148px;height:52px;border:0;border-radius:14px;background:{btn_bg};color:#fff;font-size:16px;font-weight:700;">주문하기</button></footer>')

def builder(filled, h):
    rows = [] if not filled else [
        cart_row("국화", "백선 · 특", 10, 1200),
        f'<div style="height:1px;background:{LINE};margin:0 16px;"></div>',
        cart_row("리시안셔스", "화이트 · 특", 3, 3500),
        f'<div style="height:1px;background:{LINE};margin:0 16px;"></div>',
        cart_row("유칼립투스", "그린", 2, 1800, "줄기", swiped=True),
    ]
    total = 37100 if filled else 0
    inner = (topbar("나만의 꽃다발", iconbtn("sliders", "예산 설정"))
             + f'<div style="flex:1;display:flex;flex-direction:column;gap:16px;padding-bottom:20px;">'
             + budget_bar(total) + preview_card(filled) + cart_list(rows)
             + catalog({"국화":10,"리시안셔스":3,"유칼립투스":2} if filled else None) + '</div>'
             + bottom_bar(total, filled))
    return page("꽃다발 빌더 — " + ("담긴 상태" if filled else "빈 상태"), 390, h, root(390, h, inner))

def builder_detail():
    h = 844
    # dimmed background: top of the filled screen
    back = (topbar("나만의 꽃다발", iconbtn("sliders", "예산 설정")) + f'<div style="display:flex;flex-direction:column;gap:16px;">' + budget_bar(37100) + preview_card(True) + '</div>')
    sheet_rows = [("꽃값", "국화 10 · 리시안셔스 3 · 유칼립투스 2", "26,100"), ("부자재", "포장지 · 리본", "3,000"), ("디자인비", "플로리스트 배치", "8,000"), ("배송비", "3만원 이상 무료", "0")]
    rows_html = "".join(
        f'<div style="display:flex;align-items:baseline;justify-content:space-between;padding:10px 0;"><div><div style="font-size:14.5px;font-weight:500;">{a}</div><div class="muted" style="font-size:12px;">{b}</div></div><span class="mono" style="font-size:16px;font-weight:600;">{c}<span style="font-size:11px;">원</span></span></div>'
        for a, b, c in sheet_rows)
    sheet = (f'<div style="position:absolute;left:0;right:0;bottom:0;background:{CARD};border-radius:22px 22px 0 0;box-shadow:0 -10px 30px rgba(30,27,22,.18);display:flex;flex-direction:column;">'
             f'<div style="display:flex;justify-content:center;padding:10px 0 2px;"><div style="width:40px;height:4px;border-radius:2px;background:#D3C9B8;"></div></div>'
             f'<div style="padding:6px 20px 0;display:flex;align-items:center;justify-content:space-between;"><h2 style="margin:0;font-size:17px;font-weight:700;">가격 상세</h2><span class="muted" style="font-size:11.5px;">오늘 시세 기준 · 05:00</span></div>'
             f'<div style="padding:4px 20px 0;display:flex;flex-direction:column;">{rows_html}</div>'
             f'<div style="margin:6px 20px 0;border-top:1.5px solid {INK};padding:12px 0 0;display:flex;align-items:baseline;justify-content:space-between;"><span style="font-size:15px;font-weight:700;">합계</span>{money(37100, 26)}</div>'
             f'<div style="margin:8px 20px 0;display:flex;align-items:center;gap:10px;"><div style="flex:1;height:6px;border-radius:3px;background:{SOFT};overflow:hidden;"><div style="width:74%;height:100%;background:{GREEN};"></div></div><span class="mono muted" style="font-size:12px;font-weight:600;">예산 50,000원의 74%</span></div>'
             f'<div style="margin:14px 20px 0;padding:12px 14px;border-radius:12px;background:{GREEN_T};display:flex;flex-direction:column;gap:3px;">'
             f'<div style="display:flex;align-items:center;gap:6px;font-size:14.5px;font-weight:700;color:{GREEN};">이 조합, 어제보다 <span class="mono up">▲4%</span></div>'
             f'<div style="font-size:12px;color:#3C5A48;">국화 ▲8%가 올렸어요 · 어제였다면 꽃값 25,000원 · 지금이 오늘 최저가 기준입니다</div></div>'
             f'<div style="padding:16px 20px 24px;">'
             f'<button type="button" style="width:100%;height:56px;border:0;border-radius:14px;background:{GREEN};color:#fff;font-size:17px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:10px;">주문하기 <span class="mono" style="font-weight:700;">37,100원</span></button></div></div>')
    inner = (f'<div style="flex:1;display:flex;flex-direction:column;">{back}</div>'
             f'<div style="position:absolute;inset:0;background:rgba(30,27,22,.42);"></div>{sheet}')
    return page("꽃다발 빌더 — 가격 상세 펼침", 390, h, root(390, h, inner))

# =====================================================================
# OWNER APP
# =====================================================================
def ohead(title, sub=None, right=None):
    r = right or ""
    subhtml = f'<div class="muted" style="font-size:12.5px;margin-top:2px;">{sub}</div>' if sub else ""
    return (f'<header style="display:flex;align-items:flex-end;justify-content:space-between;padding:14px 16px 10px;">'
            f'<div><h1 style="margin:0;font-size:22px;font-weight:700;">{title}</h1>{subhtml}</div>{r}</header>')

def stat(label, n, unit="", tone=None, size=40):
    col = {"red": RED, "orange": ORANGE, None: INK}[tone]
    return (f'<div style="display:flex;flex-direction:column;gap:2px;"><span class="muted" style="font-size:12px;">{label}</span>'
            f'<span class="mono" style="font-size:{size}px;font-weight:700;line-height:1;color:{col};">{n}<span style="font-size:14px;font-weight:600;margin-left:2px;">{unit}</span></span></div>')

def big_btn(text, primary=True, icon=None, h=52, w="100%"):
    st = (f'background:{GREEN};color:#fff;border:0;' if primary else f'background:{CARD};color:{GREEN};border:1.5px solid {GREEN};')
    return f'<button type="button" style="width:{w};height:{h}px;border-radius:14px;{st}font-size:16px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:8px;">{ic(I[icon],20) if icon else ""}{text}</button>'

def home():
    h = 1120
    todo = (f'<section class="card" style="margin:0 16px;padding:16px;display:flex;flex-direction:column;gap:14px;">'
            f'<div style="display:flex;align-items:center;justify-content:space-between;"><h2 style="margin:0;font-size:15px;font-weight:700;">오늘 할 일</h2><a href="#" style="font-size:13px;font-weight:600;display:flex;align-items:center;">주문 보기{ic(I["chevr"],16)}</a></div>'
            f'<div style="display:flex;align-items:flex-end;gap:24px;">{stat("제작할 주문", 7, "건", size=52)}'
            f'<div style="display:flex;flex-direction:column;gap:8px;flex:1;">'
            f'<div style="display:flex;align-items:center;justify-content:space-between;padding:8px 10px;border-radius:10px;background:{RED_T};"><div style="display:flex;align-items:center;gap:6px;">{chip("근조", tone="red")}<span class="mono" style="font-size:15px;font-weight:700;color:{RED};">2</span></div><span class="mono" style="font-size:12px;font-weight:700;color:{RED};">13:00 배송 마감</span></div>'
            f'<div style="display:flex;align-items:center;justify-content:space-between;padding:8px 10px;border-radius:10px;background:{SOFT};"><div style="display:flex;align-items:center;gap:6px;"><span style="font-size:12px;font-weight:600;">예약 발송</span><span class="mono" style="font-size:15px;font-weight:700;">3</span></div><span class="mono muted" style="font-size:12px;font-weight:600;">내일 09:00</span></div>'
            f'<div style="display:flex;align-items:center;justify-content:space-between;padding:8px 10px;border-radius:10px;background:{SOFT};"><div style="display:flex;align-items:center;gap:6px;"><span style="font-size:12px;font-weight:600;">일반 · 픽업</span><span class="mono" style="font-size:15px;font-weight:700;">2</span></div><span class="mono muted" style="font-size:12px;font-weight:600;">15:00 · 18:00</span></div>'
            f'</div></div></section>')
    rows = [("국화 백선 특", "확정 80 · 예약 30 · 구독 10", 120, 60, 60), ("장미 레드나오미 상", "확정 25 · 예약 15", 40, 30, 10),
            ("리시안셔스 화이트 특", "확정 12", 12, 15, 0), ("카네이션 핑크 상", "확정 20", 20, 40, 0)]
    trs = ""
    for name, src, need, stock, short in rows:
        sh = f'<span class="mono" style="font-size:18px;font-weight:700;color:{ORANGE};">{short}</span>' if short else f'<span class="mono flat" style="font-size:14px;">충분</span>'
        trs += (f'<div style="display:grid;grid-template-columns:1fr 56px 56px 56px;align-items:center;gap:6px;padding:10px 0;border-top:1px solid {LINE};">'
                f'<div><div style="font-size:14px;font-weight:600;">{name}</div><div class="muted" style="font-size:11.5px;">{src}</div></div>'
                f'<span class="mono" style="text-align:right;font-size:15px;font-weight:600;">{need}</span><span class="mono muted" style="text-align:right;font-size:15px;">{stock}</span><span style="text-align:right;">{sh}</span></div>')
    order = (f'<section class="card" style="margin:0 16px;padding:16px;display:flex;flex-direction:column;gap:10px;">'
             f'<div style="display:flex;align-items:baseline;justify-content:space-between;"><h2 style="margin:0;font-size:15px;font-weight:700;">내일 새벽 발주 제안</h2><span class="muted" style="font-size:11.5px;">9/19 (토) 새벽 기준</span></div>'
             f'<div style="display:grid;grid-template-columns:1fr 56px 56px 56px;gap:6px;font-size:11px;font-weight:600;color:{MUTED};"><span>품목 · 필요 근거</span><span style="text-align:right;">필요</span><span style="text-align:right;">재고</span><span style="text-align:right;">부족</span></div>'
             f'<div style="display:flex;flex-direction:column;">{trs}</div>'
             f'<div style="display:flex;align-items:center;justify-content:space-between;padding:10px 12px;border-radius:10px;background:{ORANGE_T};"><span style="font-size:13px;font-weight:600;color:{ORANGE};">부족 2품목</span><span class="mono" style="font-size:13px;font-weight:700;color:{ORANGE};">국화 3속 · 장미 1속</span></div>'
             f'{big_btn("발주 메모로 복사", icon="copy")}</section>')
    stock_rows = [("카네이션 핑크 상", 1, 40, True, "2,900원"), ("튤립 옐로우 특", 2, 8, False, None), ("장미 레드나오미 상", 2, 12, False, None)]
    srs = ""
    for name, days, qty, on, disc in stock_rows:
        dcol = ORANGE if days <= 1 else INK
        dischtml = f'<span class="mono" style="color:{ORANGE};font-weight:600;">할인가 {disc}</span>' if disc else ""
        srs += (f'<div style="display:flex;align-items:center;gap:10px;padding:10px 0;border-top:1px solid {LINE};">'
                f'<div style="flex:1;"><div style="font-size:14px;font-weight:600;">{name}</div><div style="font-size:12px;display:flex;gap:8px;"><span class="mono" style="font-weight:700;color:{dcol};">{days}일 남음</span><span class="mono muted">{qty}송이</span>{dischtml}</div></div>'
                f'<span style="font-size:11.5px;font-weight:600;color:{MUTED};">오늘만 할인</span>{switch(on, name + " 오늘만 할인")}</div>')
    stock = (f'<section class="card" style="margin:0 16px;padding:16px 16px 6px;display:flex;flex-direction:column;gap:8px;">'
             f'<div style="display:flex;align-items:center;justify-content:space-between;"><h2 style="margin:0;font-size:15px;font-weight:700;display:flex;align-items:center;gap:6px;"><span style="width:8px;height:8px;border-radius:50%;background:{ORANGE};"></span>신선기간 임박</h2><span class="muted" style="font-size:11.5px;">할인 켜면 소비자 앱에 즉시 노출</span></div>'
             f'<div style="display:flex;flex-direction:column;">{srs}</div></section>')
    inner = (caption("문제 1·5 · 새벽 발주를 도박에서 계산으로")
             + ohead("오늘", "9월 18일 금요일 · 시세 05:00 갱신됨", iconbtn("bell", "알림"))
             + f'<div style="flex:1;display:flex;flex-direction:column;gap:14px;padding-bottom:16px;">{todo}{order}{stock}</div>'
             + tabbar("오늘"))
    return page("사장님 — 오늘", 390, h, root(390, h, inner))

def order_card(kind, title, who, where, budget, comp, colors, delegated, when, msg, urgent=False, status="대기"):
    icon = {"funeral": ("ribbon", RED, RED_T), "birthday": ("cake", GREEN, GREEN_T), "sub": ("repeat", GREEN, GREEN_T)}[kind]
    tcol = RED if urgent else INK
    return (f'<article class="card" style="padding:14px;display:flex;flex-direction:column;gap:10px;{"border-color:" + RED + ";" if urgent else ""}">'
            f'<div style="display:flex;align-items:center;gap:10px;"><div style="width:40px;height:40px;border-radius:10px;background:{icon[2]};color:{icon[1]};display:flex;align-items:center;justify-content:center;">{ic(I[icon[0]],22)}</div>'
            f'<div style="flex:1;"><div style="font-size:15px;font-weight:700;color:{tcol};">{title}</div><div class="muted" style="font-size:12px;">{who} · {where}</div></div>'
            f'<div style="display:flex;flex-direction:column;align-items:flex-end;gap:2px;"><span class="mono" style="font-size:15px;font-weight:700;color:{tcol};">{when}</span>{chip(status, tone="orange" if status=="제작 중" else "soft")}</div></div>'
            f'<div style="display:grid;grid-template-columns:52px 1fr;gap:4px 8px;font-size:13px;">'
            f'<span class="muted">예산</span><span class="mono" style="font-weight:700;">{budget}</span>'
            f'<span class="muted">구성</span><span>{comp}</span>'
            f'<span class="muted">색감</span><span style="display:flex;gap:6px;align-items:center;">{colors}</span>'
            f'<span class="muted">배치</span><span>{chip("플로리스트 맡김", tone="green") if delegated else chip("소비자 배치 그대로", tone="soft")}</span>'
            f'<span class="muted">카드</span><span style="font-style:italic;">“{msg}”</span></div></article>')

def swatch(col, name):
    return f'<span style="display:inline-flex;align-items:center;gap:4px;font-size:12px;"><span style="width:14px;height:14px;border-radius:50%;background:{col};border:1px solid rgba(0,0,0,.12);"></span>{name}</span>'

def orders():
    h = 1080
    seg = (f'<div style="margin:0 16px;display:flex;background:{SOFT};border-radius:12px;padding:3px;">'
           f'<button type="button" aria-pressed="true" style="flex:1;height:38px;border:0;border-radius:10px;background:{CARD};font-size:13.5px;font-weight:700;box-shadow:0 1px 3px rgba(0,0,0,.08);">오늘 7</button>'
           f'<button type="button" aria-pressed="false" style="flex:1;height:38px;border:0;border-radius:10px;background:transparent;font-size:13.5px;font-weight:500;color:{MUTED};">예약 3</button>'
           f'<button type="button" aria-pressed="false" style="flex:1;height:38px;border:0;border-radius:10px;background:transparent;font-size:13.5px;font-weight:500;color:{MUTED};">완료 12</button></div>')
    cards = "".join([
        order_card("funeral", "근조 화환 · 마감 2시간 10분 전", "김민준", "서울성모병원 장례식장 3호", "150,000원", "국화 백선 60 · 리시안셔스 화이트 10 · 유칼립투스 5",
                   swatch("#F3EEE3", "화이트") + swatch("#7C8F6A", "그린"), True, "13:00 배송", "삼가 고인의 명복을 빕니다", urgent=True, status="제작 중"),
        order_card("birthday", "생일 · 직접 만든 꽃다발", "이서연", "본인 · 강남구 역삼동", "50,000원", "국화 백선 10 · 리시안셔스 화이트 3 · 유칼립투스 2",
                   swatch("#F3EEE3", "화이트") + swatch("#7C8F6A", "그린"), False, "15:00 배송", "서른 살 축하해, 나."),
        order_card("birthday", "생일 · 어머니께", "최유진", "송파구 잠실동", "80,000원", "리시안셔스 화이트 20 · 장미 레드나오미 5 · 유칼립투스 3",
                   swatch("#F3EEE3", "화이트") + swatch("#B84A45", "레드"), True, "16:00 배송", "엄마, 올해도 고마워요", status="대기"),
        order_card("sub", "구독 · 매주 금요일", "박지훈", "매장 픽업", "30,000원", "사장님 추천 · 계절꽃 위주", swatch("#E7C86A", "옐로우") + swatch("#E9C4C0", "핑크"), True, "18:00 픽업", "카드 없음"),
    ])
    inner = (caption("문제 2·7 · 카톡 30분 상담을 구조화된 주문서 한 장으로")
             + ohead("주문", "오늘 7건 · 카드만 보고 만들면 됩니다", iconbtn("search", "주문 검색"))
             + seg + f'<div style="flex:1;display:flex;flex-direction:column;gap:10px;padding:12px 16px 16px;">{cards}</div>' + tabbar("주문"))
    return page("사장님 — 주문 목록", 390, h, root(390, h, inner))

def order_detail():
    h = 1140
    prev = (f'<section class="card" style="margin:0 16px;height:170px;position:relative;overflow:hidden;">'
            f'<div style="position:absolute;top:10px;left:12px;">{chip("소비자가 만든 프리뷰", tone="soft")}</div>'
            + "".join(f'<div style="position:absolute;left:{x}px;top:{y}px;">{flower(WHITE,"#D9CBA5",s)}</div>' for x,y,s in [(96,52,56),(140,40,60),(184,50,58),(120,80,52),(164,84,54),(208,80,50),(228,48,52),(76,84,48)])
            + "".join(f'<div style="position:absolute;left:{x}px;top:{y}px;">{flower(REDF,"#7D2E2B",s)}</div>' for x,y,s in [(60,54,52),(250,60,54),(150,110,50)])
            + "".join(f'<div style="position:absolute;left:{x}px;top:{y}px;">{euca(s)}</div>' for x,y,s in [(40,80,64),(270,86,64),(110,100,58)])
            + f'<div style="position:absolute;right:12px;bottom:10px;display:flex;gap:6px;">{chip("플로리스트 맡김", tone="green")}</div></section>')
    comp = [("리시안셔스 화이트 특", 20, 15, True), ("장미 레드나오미 상", 5, 30, False), ("유칼립투스 그린", 3, 40, False)]
    crs = ""
    for name, need, stock, short in comp:
        st = (f'<span class="mono" style="font-size:12px;font-weight:700;color:{ORANGE};">재고 {stock} · 부족 {need-stock}</span>' if short
              else f'<span class="mono" style="font-size:12px;font-weight:600;color:{GREEN};display:inline-flex;align-items:center;gap:2px;">{ic(I["check"],14)}재고 {stock}</span>')
        crs += (f'<div style="display:flex;align-items:center;justify-content:space-between;padding:10px 0;border-top:1px solid {LINE};">'
                f'<div style="font-size:14.5px;font-weight:600;">{name}</div><div style="display:flex;align-items:baseline;gap:12px;"><span class="mono" style="font-size:18px;font-weight:700;">{need}<span style="font-size:11px;">송이</span></span>{st}</div></div>')
    sub = (f'<div style="margin-top:4px;padding:12px;border-radius:12px;background:{ORANGE_T};display:flex;flex-direction:column;gap:10px;">'
           f'<div style="display:flex;align-items:center;gap:8px;font-size:13.5px;"><span style="font-weight:700;color:{ORANGE};">대체 제안</span><span>리시안셔스 화이트 → <b>아이보리</b> (재고 25 · 같은 가격)</span></div>'
           f'<div style="display:flex;align-items:center;gap:8px;"><button type="button" style="flex:1;height:44px;border:0;border-radius:10px;background:{ORANGE};color:#fff;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:6px;">{ic(I["send"],18)}대체 제안 보내기</button>'
           f'<span style="display:inline-flex;align-items:center;gap:5px;font-size:12px;font-weight:600;color:{ORANGE};padding:0 6px;">{ic(I["clock"],16)}소비자 승인 대기</span></div></div>')
    info = (f'<section class="card" style="margin:0 16px;padding:14px 16px;display:flex;flex-direction:column;gap:2px;">'
            f'<div style="display:grid;grid-template-columns:64px 1fr;gap:6px 8px;font-size:13.5px;">'
            f'<span class="muted">받는 분</span><span>어머니 · 송파구 잠실동 (배송)</span>'
            f'<span class="muted">배송</span><span class="mono" style="font-weight:700;">오늘 16:00</span>'
            f'<span class="muted">예산</span><span class="mono" style="font-weight:700;">80,000원 <span class="muted" style="font-weight:500;font-size:12px;">· 소비자 합계 78,400원</span></span>'
            f'<span class="muted">메시지 카드</span><span style="font-style:italic;">“엄마, 올해도 고마워요”</span></div></section>')
    complete = (f'<section class="card" style="margin:0 16px;padding:16px;display:flex;flex-direction:column;gap:12px;">'
                f'<div><h2 style="margin:0;font-size:15px;font-weight:700;">제작 완료</h2><div class="muted" style="font-size:12.5px;">한 번 찍으면 세 가지가 됩니다</div></div>'
                f'<button type="button" style="height:64px;border:0;border-radius:16px;background:{GREEN};color:#fff;font-size:18px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:10px;">{ic(I["camera"],26)}완성 사진 찍기</button>'
                f'<div style="display:flex;justify-content:center;height:18px;"><svg width="240" height="18" viewBox="0 0 240 18" fill="none" stroke="{GREEN}" stroke-width="1.5" aria-hidden="true"><path d="M120 0v6M120 6H24v12M120 6v12M120 6h96v12"/></svg></div>'
                f'<div style="display:grid;grid-template-columns:repeat(3, minmax(0, 1fr));gap:8px;">'
                + "".join(f'<div style="padding:10px 8px;border-radius:10px;background:{GREEN_T};display:flex;flex-direction:column;align-items:center;gap:4px;text-align:center;"><span style="color:{GREEN};">{ic(I[i],20)}</span><span style="font-size:12.5px;font-weight:700;color:{GREEN};">{t}</span><span style="font-size:11px;color:#3C5A48;">{s}</span></div>'
                          for i, t, s in [("send", "손님 알림", "사진과 함께 완성 알림"), ("heart", "포트폴리오", "매장 페이지에 자동 등록"), ("users", "손님 이력", "최유진 · 어머니 생일에 저장")])
                + '</div></section>')
    inner = (caption("문제 2·7 · 대화 없이 만들고, 한 번 찍어 세 가지 일을 끝내기")
             + topbar("주문 #1043 · 생일", f'<div style="width:44px;height:44px;display:flex;align-items:center;justify-content:center;">{chip("대기", tone="soft")}</div>')
             + f'<div style="flex:1;display:flex;flex-direction:column;gap:14px;padding:4px 0 16px;">{prev}{info}'
             + f'<section class="card" style="margin:0 16px;padding:14px 16px;display:flex;flex-direction:column;"><h2 style="margin:0 0 4px;font-size:15px;font-weight:700;">꽃 구성 · 재고 대조</h2>{crs}{sub}</section>'
             + f'{complete}</div>' + tabbar("주문"))
    return page("사장님 — 주문 상세", 390, h, root(390, h, inner))

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

def chart_svg(hist, w, h, color=GREEN):
    lo, hi = min(hist)*0.92, max(hist)*1.04
    pts = []
    for i, v in enumerate(hist):
        x = 8 + i*(w-16)/(len(hist)-1); y = h-14 - (v-lo)/(hi-lo)*(h-28)
        pts.append((round(x,1), round(y,1)))
    d = "M" + " L".join(f"{x} {y}" for x,y in pts)
    area = d + f" L{pts[-1][0]} {h-14} L{pts[0][0]} {h-14} Z"
    grid = "".join(f'<line x1="8" x2="{w-8}" y1="{h-14-(h-28)*k/3:.1f}" y2="{h-14-(h-28)*k/3:.1f}" stroke="{LINE}" stroke-dasharray="2 4"/>' for k in range(4))
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="14일 시세 추이">{grid}'
            f'<path d="{area}" fill="{color}" opacity=".08"/><path d="{d}" fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round"/>'
            f'<circle cx="{pts[-1][0]}" cy="{pts[-1][1]}" r="4" fill="{color}"/>'
            f'<text x="8" y="{h-2}" font-size="10" fill="{MUTED}" font-family="IBM Plex Mono">9/5</text><text x="{w-8}" y="{h-2}" font-size="10" fill="{MUTED}" text-anchor="end" font-family="IBM Plex Mono">오늘</text></svg>')

def price_item_mobile(it, editing=False, selected=False):
    sale = round(it["box"]/it["per"]*it["margin"], -1)
    off = not it["on"]
    op = "opacity:.5;" if off else ""
    border = f"border:1.5px solid {GREEN};" if selected else ""
    margin_cell = (f'<label style="display:flex;flex-direction:column;gap:3px;"><span class="muted" style="font-size:10.5px;">마진계수 <span style="color:{GREEN};font-weight:700;">편집</span></span>'
                   f'<input type="number" step="0.1" defaultValue="{3.0 if editing else it["margin"]}" class="ed mono" style="height:40px;width:100%;box-sizing:border-box;padding:0 10px;font-size:18px;font-weight:700;{"box-shadow:0 0 0 3px " + GREEN_T + ";" if editing else ""}"></label>')
    new_sale = round(it["box"]/it["per"]*3.0, -1)
    sale_cell = (f'<div style="display:flex;flex-direction:column;gap:3px;"><span class="muted" style="font-size:10.5px;">송이 판매가 <span style="font-weight:600;">자동</span></span>'
                 + (f'<div style="height:40px;display:flex;align-items:center;gap:6px;"><span class="mono" style="font-size:20px;font-weight:700;color:{GREEN};">{new_sale:,.0f}</span><span class="mono muted" style="font-size:11px;text-decoration:line-through;">{sale:,.0f}</span></div>' if editing
                    else (f'<div style="height:40px;display:flex;align-items:center;gap:6px;"><span class="mono" style="font-size:20px;font-weight:700;color:{ORANGE};">{it["discPrice"]:,}</span><span class="mono muted" style="font-size:11px;text-decoration:line-through;">{sale:,.0f}</span></div>' if it["disc"]
                          else f'<div class="mono" style="height:40px;display:flex;align-items:center;font-size:20px;font-weight:700;">{sale:,.0f}</div>')) + '</div>')
    m = 3.0 if editing else it["margin"]
    expl = f'시세 {it["box"]:,}원/속 ÷ {it["per"]}송이 × 마진 {m} = <b>{(new_sale if editing else sale):,.0f}원</b>'
    return (f'<article class="card" style="padding:12px 14px;display:flex;flex-direction:column;gap:10px;{border}">'
            f'<div style="display:flex;align-items:center;gap:10px;{op}">{switch(it["on"], it["name"] + " 취급")}'
            f'<div style="flex:1;"><div style="font-size:15px;font-weight:700;">{it["name"]} <span style="font-weight:500;">{it["var"]}</span> <span class="muted" style="font-size:12px;">· {it["grade"]}</span></div>'
            f'<div style="font-size:12px;display:flex;gap:8px;align-items:center;"><span class="muted">어제 대비</span>{delta(it["delta"])}<span class="muted">·</span><span class="muted">재고</span><span class="mono" style="font-weight:600;">{it["stock"]}송이</span></div></div>'
            + (f'<span style="font-size:11px;font-weight:600;color:{MUTED};">취급 안 함</span>' if off else f'<div style="display:flex;flex-direction:column;align-items:flex-end;gap:2px;"><span class="muted" style="font-size:10.5px;">오늘만 할인</span>{switch(it["disc"], it["name"] + " 오늘만 할인")}</div>')
            + '</div>'
            + ("" if off else
               f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr 1.1fr;gap:8px;">'
               f'<div style="display:flex;flex-direction:column;gap:3px;"><span class="muted" style="font-size:10.5px;">속 단가 <span style="font-weight:600;">시세</span></span><div class="ro mono" style="height:40px;display:flex;align-items:center;padding:0 8px;font-size:15px;font-weight:600;">{it["box"]:,}</div></div>'
               f'<div style="display:flex;flex-direction:column;gap:3px;"><span class="muted" style="font-size:10.5px;">송이수/속</span><div class="ro mono" style="height:40px;display:flex;align-items:center;padding:0 8px;font-size:15px;font-weight:600;">{it["per"]}</div></div>'
               f'{margin_cell}{sale_cell}</div>'
               f'<div style="display:flex;align-items:center;justify-content:space-between;gap:8px;padding:8px 10px;border-radius:10px;background:{GREEN_T};">'
               f'<div style="font-size:12px;color:#2E4A3A;"><span style="font-weight:700;color:{GREEN};">손님에게 보이는 설명</span> · {expl}</div>'
               f'<button type="button" style="height:32px;padding:0 10px;border:0;border-radius:8px;background:{GREEN};color:#fff;font-size:12px;font-weight:700;white-space:nowrap;">보여주기</button></div>')
            + '</article>')

def prices_mobile():
    h = 1280
    cards = "".join(price_item_mobile(it, editing=(i == 0), selected=(i == 0)) for i, it in enumerate(ITEMS))
    chart = (f'<section class="card" style="padding:14px 16px;display:flex;flex-direction:column;gap:8px;">'
             f'<div style="display:flex;align-items:baseline;justify-content:space-between;"><h2 style="margin:0;font-size:14px;font-weight:700;">국화 백선 특 · 14일 시세</h2><span class="mono muted" style="font-size:11.5px;">속 단가 · 원</span></div>'
             f'{chart_svg(ITEMS[0]["hist"], 326, 120)}'
             f'<div style="display:flex;gap:14px;font-size:12px;"><span><span class="muted">14일 최저</span> <span class="mono" style="font-weight:600;">20,000</span></span><span><span class="muted">최고</span> <span class="mono" style="font-weight:600;">24,000</span></span><span><span class="muted">오늘</span> <span class="mono up" style="font-weight:700;">24,000 ▲8%</span></span></div></section>')
    inner = (caption("문제 3·4 · “시세가 올라서요” 대신 계산식을 보여주기")
             + ohead("시세 · 품목", "aT 공판장 시세 · 오늘 05:00 갱신", f'<div style="display:flex;flex-direction:column;align-items:flex-end;gap:2px;font-size:10.5px;color:{MUTED};"><span class="ro" style="padding:2px 6px;">읽기전용 = 시세</span><span class="ed" style="padding:2px 6px;color:{GREEN};font-weight:600;">편집 = 마진 · 재고</span></div>')
             + f'<div style="flex:1;display:flex;flex-direction:column;gap:10px;padding:4px 16px 16px;">{cards}{chart}</div>' + tabbar("시세"))
    return page("사장님 — 시세·품목 (모바일)", 390, h, root(390, h, inner))

def prices_tablet():
    w, h = 1024, 768
    hdr = "".join(f'<span style="text-align:{a};">{t}</span>' for t, a in [("취급", "left"), ("품목 · 품종 · 등급", "left"), ("속 단가", "right"), ("송이/속", "right"), ("마진계수", "right"), ("송이 판매가", "right"), ("어제 대비", "right"), ("재고", "right"), ("오늘만 할인", "center")])
    cols = "48px 1.4fr 88px 64px 84px 104px 76px 84px 78px"
    row = (f'<sc-for list="{{{{items}}}}" as="it" hint-placeholder-count="5">'
           f'<div style="{{{{it.rowStyle}}}}">'
           f'<button type="button" aria-pressed="{{{{it.on}}}}" aria-label="취급" onClick="{{{{it.toggleOn}}}}" style="{{{{it.onStyle}}}}"><span style="{{{{it.onKnob}}}}"></span></button>'
           f'<button type="button" onClick="{{{{it.select}}}}" style="border:0;background:transparent;text-align:left;padding:0;display:flex;flex-direction:column;gap:1px;height:44px;justify-content:center;"><span style="font-size:15px;font-weight:700;">{{{{it.name}}}} <span style="font-weight:500;">{{{{it.var}}}}</span></span><span class="muted" style="font-size:12px;">{{{{it.grade}}}}등급</span></button>'
           f'<div class="ro mono" style="height:40px;display:flex;align-items:center;justify-content:flex-end;padding:0 10px;font-size:15px;font-weight:600;">{{{{it.boxFmt}}}}</div>'
           f'<div class="ro mono" style="height:40px;display:flex;align-items:center;justify-content:flex-end;padding:0 10px;font-size:15px;font-weight:600;">{{{{it.per}}}}</div>'
           f'<input type="number" step="0.1" min="1" max="6" aria-label="마진계수" value="{{{{it.margin}}}}" onChange="{{{{it.onMargin}}}}" class="ed mono" style="height:40px;width:100%;box-sizing:border-box;padding:0 10px;text-align:right;font-size:16px;font-weight:700;">'
           f'<div style="display:flex;flex-direction:column;align-items:flex-end;justify-content:center;height:44px;"><span class="mono" style="{{{{it.saleStyle}}}}">{{{{it.saleFmt}}}}</span><sc-if value="{{{{it.disc}}}}" hint-placeholder-val="{{{{false}}}}"><span class="mono muted" style="font-size:11px;text-decoration:line-through;">{{{{it.baseFmt}}}}</span></sc-if></div>'
           f'<span class="mono" style="{{{{it.deltaStyle}}}}">{{{{it.deltaFmt}}}}</span>'
           f'<input type="number" step="1" min="0" aria-label="재고" value="{{{{it.stock}}}}" onChange="{{{{it.onStock}}}}" class="ed mono" style="height:40px;width:100%;box-sizing:border-box;padding:0 10px;text-align:right;font-size:16px;font-weight:700;">'
           f'<div style="display:flex;justify-content:center;"><button type="button" aria-pressed="{{{{it.disc}}}}" aria-label="오늘만 할인" onClick="{{{{it.toggleDisc}}}}" style="{{{{it.discStyle}}}}"><span style="{{{{it.discKnob}}}}"></span></button></div>'
           f'</div></sc-for>')
    table = (f'<section class="card" style="flex:1;display:flex;flex-direction:column;overflow:hidden;">'
             f'<div style="display:grid;grid-template-columns:{cols};gap:10px;padding:10px 16px;font-size:11.5px;font-weight:600;color:{MUTED};border-bottom:1px solid {LINE};background:{SOFT};">{hdr}</div>'
             f'<div style="display:flex;flex-direction:column;">{row}</div>'
             f'<div style="margin-top:auto;padding:10px 16px;border-top:1px solid {LINE};display:flex;gap:16px;font-size:12px;color:{MUTED};align-items:center;"><span class="ro" style="padding:3px 8px;">회색 = 시세 · 읽기전용</span><span class="ed" style="padding:3px 8px;color:{GREEN};font-weight:600;">초록 테두리 = 편집 가능</span><span>마진계수를 고치면 판매가가 바로 바뀝니다</span></div></section>')
    side = (f'<aside style="width:300px;display:flex;flex-direction:column;gap:12px;">'
            f'<section class="card" style="padding:14px 16px;display:flex;flex-direction:column;gap:8px;">'
            f'<div style="display:flex;align-items:baseline;justify-content:space-between;"><h2 style="margin:0;font-size:14px;font-weight:700;">{{{{sel.name}}}} {{{{sel.var}}}} {{{{sel.grade}}}} · 14일 시세</h2></div>'
            f'<svg width="268" height="150" viewBox="0 0 268 150" role="img" aria-label="14일 시세 추이"><path d="{{{{chartArea}}}}" fill="{GREEN}" opacity=".08"></path><path d="{{{{chartD}}}}" fill="none" stroke="{GREEN}" stroke-width="2" stroke-linejoin="round"></path><circle cx="{{{{lastX}}}}" cy="{{{{lastY}}}}" r="4" fill="{GREEN}"></circle><text x="8" y="148" font-size="10" fill="{MUTED}" font-family="IBM Plex Mono">9/5</text><text x="260" y="148" font-size="10" fill="{MUTED}" text-anchor="end" font-family="IBM Plex Mono">오늘</text></svg>'
            f'<div style="display:flex;gap:12px;font-size:12px;"><span><span class="muted">최저</span> <span class="mono" style="font-weight:600;">{{{{loFmt}}}}</span></span><span><span class="muted">최고</span> <span class="mono" style="font-weight:600;">{{{{hiFmt}}}}</span></span><span><span class="muted">오늘</span> <span class="mono" style="{{{{sel.deltaStyle}}}}">{{{{sel.boxFmt}}}} {{{{sel.deltaFmt}}}}</span></span></div></section>'
            f'<section style="padding:14px 16px;border-radius:14px;background:{GREEN_T};display:flex;flex-direction:column;gap:8px;">'
            f'<div style="font-size:12px;font-weight:700;color:{GREEN};">손님에게 보이는 가격 설명</div>'
            f'<div style="font-size:14px;line-height:1.5;color:#2E4A3A;">시세 <span class="mono" style="font-weight:700;">{{{{sel.boxFmt}}}}원</span>/속 ÷ <span class="mono" style="font-weight:700;">{{{{sel.per}}}}</span>송이 × 마진 <span class="mono" style="font-weight:700;">{{{{sel.margin}}}}</span> = <span class="mono" style="font-size:18px;font-weight:700;color:{GREEN};">{{{{sel.baseFmt}}}}원</span></div>'
            f'<div style="font-size:11.5px;color:#3C5A48;">마진에는 폐기·포장·인건비가 들어 있어요. 손님 화면과 매장 안내판에 이 문구 그대로 표시됩니다.</div>'
            f'<button type="button" style="height:44px;border:0;border-radius:10px;background:{GREEN};color:#fff;font-size:14px;font-weight:700;">손님 화면에 보여주기</button></section></aside>')
    inner = (caption("문제 3·4 · “시세가 올라서요” 대신 계산식을 보여주기 (태블릿)")
             + f'<header style="display:flex;align-items:flex-end;justify-content:space-between;padding:16px 24px 12px;"><div><h1 style="margin:0;font-size:24px;font-weight:700;">시세 · 품목</h1><div class="muted" style="font-size:13px;margin-top:2px;">aT 화훼공판장 경매 시세 · 오늘 05:00 갱신 · 마진·재고는 바로 고쳐집니다</div></div>'
             f'<div style="display:flex;gap:8px;">{chip("전체", True)}{chip("취급 중")}{chip("재고 임박")}</div></header>'
             f'<div style="flex:1;display:flex;gap:16px;padding:0 24px 20px;min-height:0;">{table}{side}</div>')
    logic = """
constructor(p){super(p);this.state={sel:'mum',items:%s};}
fmt(n){return Math.round(n).toLocaleString('ko-KR');}
renderVals(){
  const G='%s',O='%s',R='#C2382B',ink='%s',line='%s';
  const sw=(on,c)=>'width:44px;height:26px;border-radius:999px;border:0;padding:0;position:relative;flex-shrink:0;background:'+(on?c:'#C9C1B3')+';';
  const knob=(on)=>'position:absolute;top:3px;left:'+(on?21:3)+'px;width:20px;height:20px;border-radius:50%%;background:#fff;box-shadow:0 1px 2px rgba(0,0,0,.25);';
  const upd=(id,patch)=>this.setState({items:this.state.items.map(x=>x.id===id?{...x,...patch}:x)});
  const items=this.state.items.map(it=>{
    const base=Math.round(it.box/it.per*(parseFloat(it.margin)||0)/10)*10;
    const sale=it.disc&&it.discPrice?it.discPrice:base;
    const selected=it.id===this.state.sel;
    return {...it,
      boxFmt:this.fmt(it.box),baseFmt:this.fmt(base),saleFmt:this.fmt(sale),
      saleStyle:'font-size:18px;font-weight:700;color:'+(it.disc?O:ink)+';',
      deltaFmt:it.delta===0||it.delta==null?'—':(it.delta>0?'▲'+it.delta+'%%':'▼'+(-it.delta)+'%%'),
      deltaStyle:'text-align:right;font-size:14px;font-weight:700;color:'+(it.delta>0?R:(it.delta<0?G:'#8A8378'))+';',
      rowStyle:'display:grid;grid-template-columns:%s;gap:10px;align-items:center;padding:8px 16px;border-bottom:1px solid '+line+';'+(selected?'background:'+'%s'+';':'')+(it.on?'':'opacity:.45;'),
      onStyle:sw(it.on,G),onKnob:knob(it.on),discStyle:sw(it.disc,O),discKnob:knob(it.disc),
      toggleOn:()=>upd(it.id,{on:!it.on}),toggleDisc:()=>upd(it.id,{disc:!it.disc,discPrice:it.discPrice||Math.round(base*0.7/100)*100}),
      onMargin:(e)=>upd(it.id,{margin:e.target.value}),
      onStock:(e)=>upd(it.id,{stock:e.target.value}),
      select:()=>this.setState({sel:it.id})};
  });
  const sel=items.find(x=>x.id===this.state.sel)||items[0];
  const h=sel.hist,w=268,hh=150,lo=Math.min(...h)*0.92,hi=Math.max(...h)*1.04;
  const pts=h.map((v,i)=>[8+i*(w-16)/(h.length-1),hh-14-(v-lo)/(hi-lo)*(hh-28)]);
  const d='M'+pts.map(p=>p[0].toFixed(1)+' '+p[1].toFixed(1)).join(' L');
  const area=d+' L'+pts[pts.length-1][0].toFixed(1)+' '+(hh-14)+' L'+pts[0][0].toFixed(1)+' '+(hh-14)+' Z';
  return {items,sel,chartD:d,chartArea:area,lastX:pts[pts.length-1][0].toFixed(1),lastY:pts[pts.length-1][1].toFixed(1),loFmt:this.fmt(Math.min(...h)),hiFmt:this.fmt(Math.max(...h))};
}""" % (json.dumps(ITEMS, ensure_ascii=False), GREEN, ORANGE, INK, LINE, cols, GREEN_T)
    return page("사장님 — 시세·품목 (태블릿)", w, h, root(w, h, inner), logic)

def customers():
    h = 920
    alert = (f'<section style="margin:0 16px;padding:14px 16px;border-radius:14px;background:{GREEN};color:#fff;display:flex;flex-direction:column;gap:10px;">'
             f'<div style="display:flex;align-items:center;justify-content:space-between;"><div style="font-size:15px;font-weight:700;">이번 주 경조사 있는 손님 <span class="mono" style="font-size:20px;">3</span>명</div><span style="font-size:11.5px;opacity:.85;">제안 보내면 미리 발주에 반영</span></div>'
             f'<div style="display:flex;flex-direction:column;gap:6px;">'
             + "".join(f'<div style="display:flex;align-items:center;justify-content:space-between;padding:8px 10px;border-radius:10px;background:rgba(255,255,255,.12);"><div style="font-size:13.5px;"><b>{n}</b> · {e}</div><div style="display:flex;align-items:center;gap:8px;"><span class="mono" style="font-size:12.5px;font-weight:700;">{d}</span><button type="button" style="height:32px;padding:0 10px;border:0;border-radius:8px;background:#fff;color:{GREEN};font-size:12px;font-weight:700;">제안 보내기</button></div></div>'
                       for n, e, d in [("박지훈", "아버지 생신", "9/21 월"), ("이서연", "결혼기념일", "9/23 수"), ("최유진", "어머니 생신", "9/24 목")])
             + '</div></section>')
    people = [("이서연", "9/18 오늘", 6, "결혼기념일 9/23", True), ("박지훈", "9/11", 24, "아버지 생신 9/21", True), ("최유진", "9/18 오늘", 3, "어머니 생신 9/24", True),
              ("김민준", "9/18 오늘", 1, None, False), ("정하늘", "6/2", 2, "어머니 생신 10/3", False), ("오세훈", "3/14", 4, "화이트데이 매년 3/14", False), ("한소희", "2025/12/24", 1, None, False)]
    rows = ""
    for n, last, cnt, ev, soon in people:
        rows += (f'<a href="#" style="display:grid;grid-template-columns:1fr 90px 44px;align-items:center;gap:8px;padding:12px 16px;border-top:1px solid {LINE};color:{INK};">'
                 f'<div style="display:flex;align-items:center;gap:10px;"><div style="width:36px;height:36px;border-radius:50%;background:{SOFT};display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;color:{GREEN};">{n[0]}</div>'
                 f'<div><div style="font-size:15px;font-weight:600;">{n}</div><div style="font-size:12px;">' + (f'<span style="color:{GREEN if soon else MUTED};font-weight:{700 if soon else 500};">{ev}</span>' if ev else f'<span class="muted">등록된 경조사 없음</span>') + '</div></div></div>'
                 f'<div style="text-align:right;"><div class="mono" style="font-size:13px;font-weight:600;">{last}</div><div class="muted" style="font-size:11px;">마지막 주문</div></div>'
                 f'<div style="text-align:right;"><div class="mono" style="font-size:16px;font-weight:700;">{cnt}</div><div class="muted" style="font-size:11px;">회</div></div></a>')
    inner = (caption("문제 6 · 단골을 단골로 알아보기")
             + ohead("손님", "128명 · 사진 찍을 때마다 이력이 쌓입니다", iconbtn("search", "손님 검색"))
             + f'<div style="flex:1;display:flex;flex-direction:column;gap:14px;padding:4px 0 16px;">{alert}'
             + f'<section style="display:flex;flex-direction:column;"><div style="display:flex;align-items:baseline;justify-content:space-between;padding:0 16px 8px;"><h2 style="margin:0;font-size:15px;font-weight:700;">전체 손님</h2><span class="muted" style="font-size:12px;display:flex;align-items:center;gap:2px;">최근 주문순{ic(I["chev"],14)}</span></div><div style="margin:0 16px;border:1px solid {LINE};border-radius:14px;overflow:hidden;background:{CARD};">{rows}</div></section></div>'
             + tabbar("손님"))
    return page("사장님 — 손님 목록", 390, h, root(390, h, inner))

def customer_detail():
    h = 1080
    head = (f'<section style="padding:4px 16px 0;display:flex;align-items:center;gap:14px;"><div style="width:56px;height:56px;border-radius:50%;background:{GREEN_T};display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:700;color:{GREEN};">이</div>'
            f'<div style="flex:1;"><div style="font-size:20px;font-weight:700;">이서연</div><div class="muted" style="font-size:12.5px;">첫 주문 2024.05 · <span class="mono">6</span>회 · 누적 <span class="mono" style="font-weight:600;">312,000원</span></div></div>'
            f'<button type="button" aria-label="전화" style="width:44px;height:44px;border-radius:12px;border:1.5px solid {LINE};background:{CARD};display:flex;align-items:center;justify-content:center;">{ic(I["send"],20)}</button></section>')
    upcoming = (f'<section class="card" style="margin:0 16px;padding:14px 16px;display:flex;flex-direction:column;gap:10px;border-color:{GREEN};">'
                f'<div style="display:flex;align-items:center;justify-content:space-between;"><div style="font-size:15px;font-weight:700;">결혼기념일 · 9/23 (수)</div><span class="mono" style="font-size:13px;font-weight:700;color:{GREEN};">5일 남음</span></div>'
                f'<div style="display:flex;gap:10px;align-items:center;padding:10px;border-radius:10px;background:{SOFT};"><div style="width:44px;height:44px;border-radius:8px;background:#E4DCCB;display:flex;align-items:center;justify-content:center;">{flower(WHITE,"#D9CBA5",36)}</div><div style="flex:1;font-size:12.5px;"><div style="font-weight:600;">작년 구성</div><div class="muted">리시안셔스 화이트 10 · 장미 5 · 유칼립투스 3 · <span class="mono">52,000원</span></div></div></div>'
                f'{big_btn("지난번 구성으로 제안 보내기", icon="send", h=48)}<div class="muted" style="font-size:11.5px;text-align:center;">오늘 시세로 다시 계산해 <span class="mono">54,100원</span>으로 보냅니다</div></section>')
    pref = (f'<section class="card" style="margin:0 16px;padding:14px 16px;display:flex;flex-direction:column;gap:10px;"><h2 style="margin:0;font-size:15px;font-weight:700;">취향 프로필</h2>'
            f'<div style="display:grid;grid-template-columns:64px 1fr;gap:8px;align-items:center;font-size:13px;">'
            f'<span class="muted">선호 색감</span><span style="display:flex;gap:8px;flex-wrap:wrap;">{swatch("#F3EEE3","화이트")}{swatch("#7C8F6A","그린")}{swatch("#E9C4C0","연핑크")}</span>'
            f'<span class="muted">피하는 꽃</span><span style="display:flex;gap:6px;"><span style="display:inline-flex;align-items:center;gap:4px;padding:3px 8px;border-radius:6px;background:{RED_T};color:{RED};font-size:12px;font-weight:600;">{ic(I["ban"],14)}백합 · 향이 강함</span></span>'
            f'<span class="muted">분위기</span><span style="display:flex;gap:6px;">{chip("내추럴", tone="soft")}{chip("볼륨 적게", tone="soft")}{chip("크라프트 포장", tone="soft")}</span></div></section>')
    hist = [("2026.09.18", "생일 · 본인", 37100, WHITE), ("2025.09.23", "결혼기념일", 52000, WHITE), ("2025.05.08", "어버이날", 45000, PINK), ("2024.12.24", "크리스마스", 38000, REDF), ("2024.05.02", "첫 주문 · 집들이", 30000, YEL)]
    trs = ""
    for i, (d, u, amt, col) in enumerate(hist):
        linehtml = "" if i == len(hist)-1 else f'<span style="width:2px;height:54px;background:{LINE};"></span>'
        trs += (f'<div style="display:flex;gap:12px;align-items:center;">'
                f'<div style="display:flex;flex-direction:column;align-items:center;width:12px;"><span style="width:10px;height:10px;border-radius:50%;background:{GREEN if i==0 else "#C9C1B3"};"></span>{linehtml}</div>'
                f'<div style="width:52px;height:52px;border-radius:8px;background:#E4DCCB;display:flex;align-items:center;justify-content:center;flex-shrink:0;">{flower(col,"#D9CBA5",40)}</div>'
                f'<div style="flex:1;padding-bottom:12px;"><div style="font-size:14px;font-weight:600;">{u}</div><div class="mono muted" style="font-size:12px;">{d}</div></div><span class="mono" style="font-size:15px;font-weight:700;padding-bottom:12px;">{amt:,}<span style="font-size:11px;">원</span></span></div>')
    timeline = f'<section class="card" style="margin:0 16px;padding:14px 16px 4px;display:flex;flex-direction:column;gap:8px;"><h2 style="margin:0 0 4px;font-size:15px;font-weight:700;">발송 이력</h2>{trs}</section>'
    inner = (caption("문제 6 · 작년에 뭘 보냈는지 앱이 기억한다")
             + topbar("손님", iconbtn("more", "더보기"))
             + f'<div style="flex:1;display:flex;flex-direction:column;gap:14px;padding:0 0 16px;">{head}{upcoming}{pref}{timeline}</div>' + tabbar("손님"))
    return page("사장님 — 손님 상세", 390, h, root(390, h, inner))

def funeral():
    h = 844
    shops = [("화양플라워", 0.8, 120), ("반포꽃집", 1.4, 40), ("서초플라워", 2.6, 200)]
    srs = "".join(f'<div style="display:flex;align-items:center;gap:10px;padding:10px 0;border-top:1px solid {LINE};"><div style="flex:1;"><div style="font-size:14px;font-weight:600;">{n}</div><div class="mono muted" style="font-size:12px;">{d}km</div></div><span class="mono" style="font-size:16px;font-weight:700;">{q}<span style="font-size:11px;">송이</span></span><button type="button" style="height:40px;padding:0 14px;border:1.5px solid {GREEN};border-radius:10px;background:{CARD};color:{GREEN};font-size:13px;font-weight:700;">20송이 요청</button></div>'
                  for n, d, q in shops)
    inner = (f'<div style="background:{INK};color:#fff;padding:16px 16px 14px;display:flex;flex-direction:column;gap:10px;">'
             f'<div style="display:flex;align-items:center;justify-content:space-between;"><div style="display:flex;align-items:center;gap:8px;">{chip("근조", tone="red")}<span style="font-size:15px;font-weight:700;">근조 주문 도착</span></div><button type="button" aria-label="닫기" style="width:44px;height:44px;border:0;background:transparent;color:#fff;display:flex;align-items:center;justify-content:center;">{ic(I["x"],22)}</button></div>'
             f'<div style="display:flex;align-items:flex-end;justify-content:space-between;"><div><div style="font-size:12px;opacity:.7;">배송 마감까지</div><div class="mono" style="font-size:48px;font-weight:700;line-height:1;color:#FFB4AB;">02:10:35</div></div><div style="text-align:right;"><div style="font-size:12px;opacity:.7;">마감</div><div class="mono" style="font-size:22px;font-weight:700;">오늘 13:00</div></div></div>'
             f'<div style="display:flex;gap:8px;align-items:flex-start;font-size:13.5px;padding-top:4px;">{ic(I["pin"],18)}<div><div style="font-weight:600;">서울성모병원 장례식장 3호실</div><div style="opacity:.75;font-size:12.5px;">서초구 반포대로 222 · 매장에서 2.1km · 근조 화환 · 150,000원</div></div></div></div>'
             f'<div style="flex:1;display:flex;flex-direction:column;gap:12px;padding:14px 16px 0;">'
             f'<section class="card" style="padding:14px 16px;display:flex;flex-direction:column;gap:8px;"><div style="display:grid;grid-template-columns:repeat(3, minmax(0, 1fr));gap:8px;">'
             f'{stat("필요 국화", 80, "송이", size=34)}{stat("내 재고", 60, "송이", size=34)}{stat("부족", 20, "송이", tone="orange", size=34)}</div>'
             f'<div style="padding:8px 10px;border-radius:10px;background:{ORANGE_T};font-size:12.5px;color:{ORANGE};font-weight:600;">국화 백선 특 기준 · 리시안셔스 10, 유칼립투스 5는 재고 충분</div></section>'
             f'<section class="card" style="padding:14px 16px 4px;display:flex;flex-direction:column;"><div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:6px;"><h2 style="margin:0;font-size:15px;font-weight:700;">근처 꽃집 재고 요청</h2><span class="muted" style="font-size:11.5px;">반경 3km 제휴 · 국화 백선</span></div>{srs}</section>'
             f'<div style="margin-top:auto;"></div></div>'
             f'<div style="padding:12px 16px 24px;display:flex;flex-direction:column;gap:10px;background:{CARD};border-top:1px solid {LINE};">'
             f'{big_btn("수락 · 제작 시작", icon="check", h=60)}{big_btn("다른 꽃집에 넘기기", primary=False, h=52)}</div>')
    return page("사장님 — 근조 긴급", 390, h, root(390, h, inner))

# =====================================================================
files = {
    "Main.dc.html": builder(False, 1460),
    "Builder-Filled.dc.html": builder(True, 1600),
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

sizes = {"Main.dc.html": (390,1460), "Builder-Filled.dc.html": (390,1600), "Builder-Detail.dc.html": (390,844),
         "Owner-Today.dc.html": (390,1120), "Owner-Orders.dc.html": (390,1080), "Owner-OrderDetail.dc.html": (390,1140),
         "Owner-Prices.dc.html": (390,1280), "Owner-Prices-Tablet.dc.html": (1024,768), "Owner-Customers.dc.html": (390,920),
         "Owner-CustomerDetail.dc.html": (390,1080), "Owner-Funeral.dc.html": (390,844)}
titles = {"Main.dc.html": "빌더 · 빈 상태", "Builder-Filled.dc.html": "빌더 · 담긴 상태", "Builder-Detail.dc.html": "빌더 · 가격 상세 펼침",
          "Owner-Today.dc.html": "1 오늘", "Owner-Orders.dc.html": "2 주문 목록", "Owner-OrderDetail.dc.html": "2 주문 상세 · 제작 완료",
          "Owner-Prices.dc.html": "3 시세·품목", "Owner-Prices-Tablet.dc.html": "3 시세·품목 · 태블릿", "Owner-Customers.dc.html": "4 손님",
          "Owner-CustomerDetail.dc.html": "4 손님 상세", "Owner-Funeral.dc.html": "5 근조 긴급"}
boards = {}
x = 0
for n in ["Main.dc.html", "Builder-Filled.dc.html", "Builder-Detail.dc.html"]:
    w, h = sizes[n]; boards[n] = {"x": x, "y": 0, "w": w, "h": h, "title": titles[n]}; x += w + 80
ROW2 = 1600 + 120 + 240
x = 0
row2 = ["Owner-Today.dc.html", "Owner-Orders.dc.html", "Owner-OrderDetail.dc.html", "Owner-Prices.dc.html", "Owner-Customers.dc.html", "Owner-CustomerDetail.dc.html", "Owner-Funeral.dc.html", "Owner-Prices-Tablet.dc.html"]
for n in row2:
    w, h = sizes[n]; boards[n] = {"x": x, "y": ROW2, "w": w, "h": h, "title": titles[n]}
    if n == "Owner-Prices-Tablet.dc.html": boards[n]["is_interactive"] = True
    x += w + 80
canvas = {"v": 3, "createdOnFiles": {"v": 1, "at": "2026-09-18T03:00:00Z"}, "title": "꽃다발 빌더 · 꽃집 사장님 앱",
          "launch": {"view": "canvas"}, "pages": [], "boards": boards,
          "order": ["Main.dc.html", "Builder-Filled.dc.html", "Builder-Detail.dc.html"] + row2,
          "notes": {"t1": {"x": 0, "y": -300, "text": "꽃다발 빌더 — 소비자 · 모바일 390", "kind": "title1", "maxW": 1330},
                    "t2": {"x": 0, "y": ROW2 - 300, "text": "꽃집 사장님 운영 앱 — 모바일 390 · 시세는 태블릿 1024 포함", "kind": "title1", "maxW": 4400}},
          "designSystems": []}
with open(os.path.join(P, "canvas.json"), "w", encoding="utf-8") as f: json.dump(canvas, f, ensure_ascii=False, indent=1)
print("wrote", len(files) + 1, "files")
