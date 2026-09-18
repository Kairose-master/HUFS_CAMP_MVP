# -*- coding: utf-8 -*-
"""index.html + models.js + bouquet3d.js 를 한 파일로 묶는다.
   python3 landing/bundle.py  →  landing/dist/flower-landing.html (단독 실행용)
                                 landing/dist/flower-landing.artifact.html (claude.ai 아티팩트 게시용: 문서 래퍼 제거)"""
import base64, os, re
here = os.path.dirname(os.path.abspath(__file__))
read = lambda n: open(os.path.join(here, n), encoding="utf-8").read()
def inline_assets(doc):   # 한 파일로 열어도 로고가 보이게 assets/*.png 를 data URI 로 넣는다
    return re.sub(r'(src|href)="(assets/[^"]+\.png)"', lambda m: '%s="data:image/png;base64,%s"' % (m.group(1), base64.b64encode(open(os.path.join(here, m.group(2)), "rb").read()).decode()), doc)
html = inline_assets(read("index.html"))
for name in ("models.js", "bouquet3d.js"):
    html, n = re.subn(r'<script src="%s(\?v=[^"]*)?"></script>' % re.escape(name), lambda m: "<script>\n" + read(name).replace("</script", "<\\/script") + "</script>", html)
    assert n == 1, name
os.makedirs(os.path.join(here, "dist"), exist_ok=True)
open(os.path.join(here, "dist", "flower-landing.html"), "w", encoding="utf-8").write(html)
art = html.replace('href="app.html"', 'href="https://flower-shop-landing-dun.vercel.app/app"').replace("var APP_URL = 'app.html'", "var APP_URL = 'https://flower-shop-landing-dun.vercel.app/app'")
head = art.split("<!--page-->", 1)[1].split("<!--/head-->", 1)[0]
body = art.split("<body>", 1)[1].rsplit("</body>", 1)[0]
open(os.path.join(here, "dist", "flower-landing.artifact.html"), "w", encoding="utf-8").write(head.strip() + "\n" + body.strip() + "\n")
app = inline_assets(read("app.html"))
for name in ("models.js", "bouquet3d.js"):
    app, n = re.subn(r'<script src="%s(\?v=[^"]*)?"></script>' % re.escape(name), lambda m: "<script>\n" + read(name).replace("</script", "<\\/script") + "</script>", app)
    assert n == 1, name
open(os.path.join(here, "dist", "flower-app.html"), "w", encoding="utf-8").write(app)
print("bundled", len(html), "+", len(app), "bytes")
