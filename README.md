# ReBloom — 꽃다발 입찰 · 남는 꽃 웹앱 핸드오프 번들

- docs/handoff.md — 개발 핸드오프 문서(디자인 토큰, 데이터 모델, 가격 계산 규칙, 화면 명세, 3D 프리뷰 Blender 파이프라인, API 초안, 미결 사항).
  라이브 버전: https://claude.ai/code/artifact/39a44528-d8e6-4c2b-9d73-6e2738d9e6d5
- design/*.dc.html — 디자인 아트보드 11개(자체 완결 HTML, 브라우저에서 바로 열림). canvas.json은 캔버스 배치·크기.
  라이브 캔버스: https://claude.ai/artifact/KBSMW768sMo1XRfTSkCsd7
- landing/index.html — ReBloom 소개 페이지(손님 대상 + "꽃집 사장님" 섹션). apple.com 제품 페이지 문법, 라이트/다크(다크는 Rosé Pine). 3D 꽃다발 만들기와 입찰 미리보기가 페이지 안에서 실제로 동작하고(예시 데이터, 가격은 handoff 공식), 남는 꽃 꽃다발·송이·구해요 예시와 시세표, 가격 공식, FAQ가 있다. 스크립트 상단 `APP_URL`이 CTA 주소다.
  라이브 버전: https://claude.ai/artifact/RMcWCyWFvvSSV3igywuRSL
  배포(Vercel, 프로덕션): https://flower-shop-landing-dun.vercel.app — 프로젝트 `flower-shop-landing`. 저장소: https://github.com/Kairose-master/HUFS_CAMP_MVP (Vercel 프로젝트와 연결 — `main`에 푸시하면 자동 배포). 수동 배포는 저장소 루트에서 `npx vercel deploy --prod`. 루트 `vercel.json`이 `landing/`만 서비스하고, `.vercelignore`가 나머지를 뺀다.
- landing/app.html — ReBloom 앱(배포 주소의 `/app`). iOS 문법(라지 타이틀, inset grouped 리스트, 플로팅 탭바·액세서리, 시트·알림·HUD, 라이트/다크). 로그인 화면은 없고 우상단 계정 버튼의 시트에서 계정을 바꾼다: 손님 최유진(`#/build` `#/left` `#/orders` `#/florists`) · 꽃집 화양플라워/반포꽃집(`#/f/open` 입찰 요청 · `#/f/bids` 내 입찰·판매 · `#/f/stock` 남는 꽃 · `#/f/profile` 프로필). `#/as/f1` 처럼 열면 그 계정으로 바로 들어간다. 다른 역할의 주소는 열리지 않는다.
  손님: 3D로 꽃다발 만들기(꽃 종류 타일 → 품목, 담은 꽃, 예산 직접 입력, 용도별 추천 구성, 픽업 시간) → 입찰 요청 → 꽃집 비교(목록/비교표, 금액·평점·거리·준비순 정렬, 대체 제안 3D 미리보기, 작업 사진·리뷰) → 확인 알림 후 직접 선택 → 완성 사진 확인 → 리뷰(사진 첨부). “남는 꽃” 탭: 꽃다발 예약(크기 S·M·L + 용도로 골라 보기) · 송이 묶음(꽃집이 올린 수량을 묶음째 전부 매수) · 구해요(수량 전체를 댈 수 있는 꽃집만 응함, 부분 체결 없음). 픽업 전용이며 배송은 없다.
  꽃집: 입찰 요청(내 재고 대조, 금액 입력 ↔ 예상가 대비 슬라이더, 대체 꽃 제안, 금액은 서로 비공개) · 내 입찰·판매(입찰 / 송이 매도 / 꽃다발 / 픽업 예약을 한곳에서 — 올린 직후 이 화면으로 이동, 방금 올린 것 표시. 낙찰 시 완성 사진 업로드 → 손님·작업 사진에 반영, 재고 차감) · 남는 꽃(현황: 발주 메모·구해요 응하기·내가 내놓은 것 바로가기 / 꽃다발: 크기 S·M·L(8·12·18송이)을 바꾸면 담아 둔 꽃의 비율대로 송이 수를 맞춤(비어 있으면 자동 구성), 할인율 슬라이더 0~80% → 용도 자동 분류 → 할인 판매 / 송이: 수량·가격 매도(할인율 슬라이더 ↔ 가격 연동, 손님은 묶음 전체로만 산다) / 재고: 종류 타일 → 수량·+1속·남는 꽃 스위치) · 프로필.
  자동 응답: 계정 시트로 직접 들어가 보지 않은 꽃집은 입찰(5~18초)·완성 사진(선택 20초 뒤)·픽업 완료(25초 뒤)·구해요 체결을 자동으로 만든다. 들어가 본 꽃집은 그때부터 직접 처리한다(`S.manual`). 계정 시트의 “처음 상태로 되돌리기”로 초기화.
  상태는 브라우저 localStorage(`rebloom.v1`, 계정은 `rebloom.session`)에만 저장(백엔드 없음). 포트폴리오 예시 사진은 Unsplash 실사진 핫링크, 리뷰·꽃집 이름은 예시.
- screenshots/ — 상세 페이지 캡처(PNG, 2배 해상도). `desktop-full.png`(1280px 전체) · `mobile-full.png`(390px 전체) · `desktop-01-hero` ~ `07-final`(섹션별 컷).
  다시 찍기: `node tools/capture.mjs [URL]` — 헤드리스 Chrome을 DevTools 프로토콜로 제어(추가 설치 없음). 3D는 화면에 보일 때만 그려지므로 페이지 전체를 뷰포트로 잡고, 8,000px 넘는 높이는 타일로 나눠 이어 붙인다.
- tools/run-in-page.mjs — 헤드리스 Chrome에서 페이지를 열고 시나리오(JS)를 실행하는 검증 도구(`DARK=1/0` 다크·라이트 고정, `FULL=1` 전체 페이지 캡처). `node tools/run-in-page.mjs <url> <scenario.js> [shot.png]`. file:// 도 열려 배포 전에 로컬 번들(landing/dist)로 앱 흐름을 끝까지 돌려 볼 수 있다.
- docs/competitors.md — 경쟁사 조사(2026-09-18, 출처 포함).
- blender/make_flowers.py — 꽃 12종(국화·장미·리시안셔스·카네이션·튤립·유칼립투스·거베라·해바라기·백합·수국·작약·안개꽃)을 Blender 파이썬으로 절차적으로 모델링해 glTF로 내보내는 스크립트. 로컬·기본 에셋에 꽃 프리셋이 없어 직접 만들었다(외부 모델 미사용 → 라이선스 문제 없음). blender/flowers.blend 는 열어서 손볼 수 있는 결과물.
  실행: `/Applications/Blender.app/Contents/MacOS/Blender -b --factory-startup --python blender/make_flowers.py`
- landing/models/*.glb — 품목당 1 glTF(528~2,250 tri, 22~68KB, 텍스처 없음). 원점=줄기 밑, +Y 위, 1unit=1m. 색 변형은 `petal` 머티리얼 색만 바꾼다. 실제 앱에서는 /public/models 로 옮겨 쓴다.
- landing/bouquet3d.js — three.js 꽃다발 프리뷰(handoff의 BouquetPreview). `Bouquet3D.thumb`(꽃다발 썸네일, 투명 PNG)와 `Bouquet3D.stem`(품목 아이콘용 한 송이 렌더)도 여기 있다: 동심원 슬롯(1·6·12·18), 고정 시드, InstancedMesh, 끌어서 회전, WebGL 불가 시 2D 실루엣 폴백. landing/models.js 는 GLB의 base64 묶음(자동 생성).
- landing/bundle.py — index.html·app.html + models.js + bouquet3d.js + assets/*.png(로고, data URI)를 한 파일로 묶어 landing/dist/ 에 만든다(단독 실행용 / 아티팩트 게시용).
- landing/assets/ — 로고(사용자 제공 원본 `rebloom-logo-original.png`, 배경을 뺀 `rebloom-logo.png`, 마크 `rebloom-mark.png`, 앱 아이콘 `app-icon-180.png`, 파비콘 `favicon-64.png`).
- PRODUCT.md / DESIGN.md — 제품 사실과 시각 시스템 기록(impeccable). 이전 디자인 원본은 landing/_backup/2026-09-18-pre-rebloom/.
- design/generate_artboards.py — 아트보드를 만든 생성 스크립트(토큰·샘플 데이터의 단일 소스). 2026-09-18에 ReBloom 시각 시스템(iOS 문법, 픽업 전용)으로 11장 전부 다시 만들었고 `design/`에 바로 쓴다. 아트보드 높이는 새 글자 크기에 맞춰 늘었다(canvas.json 참고).

결정(2026-09-18): 거래는 꽃집 ↔ 소비자 사이에서만 한다(꽃다발 · 송이 단위 매수/매도 모두). 꽃집끼리 재고를 사고파는 기능은 넣지 않는다 — 중간 유통 레이어가 생기기 때문. 남는 재고는 꽃다발로 구성해 소비자에게 직접 판다. handoff.md의 "근처 꽃집 재고 요청 / 다른 꽃집에 넘기기"는 이 결정으로 대체된다.
결정(2026-09-18, 추가): 소개 페이지(/)에서 재고 관리 섹션·발주 메모를 뺐다(이전 버전은 landing/_backup/). 입찰 앱 공급자 화면의 재고 입력은 남는 꽃 계산에 필요해 유지.
결정(2026-09-18, 추가): 소개 페이지에서 꽃 스왑 섹션을 뺐고, 핵심 두 문장("손님이 만든 꽃다발에, 꽃집이 금액을 써 냅니다" / "모자란 꽃도 남는 꽃도, 손님에게 바로 닿게")을 첫 화면에 둔다. 입찰 앱의 대체 꽃 제안 기능은 그대로 있다.

결정(2026-09-18, 리디자인): 제품명을 ReBloom으로 통일하고 시각·UX를 Apple HIG 문법으로 교체했다(크림·딥그린·IBM Plex 폐기, 시스템 서체·시스템 블루 단일 틴트, 다크는 Rosé Pine 배경). 배송은 제품에서 뺐다(픽업 전용). 역할 로그인 화면은 계정 시트의 계정 전환으로 바꿨고, 가로 스크롤 스트립은 전부 줄바꿈·그리드로 바꿨다. screenshots/ 는 이전 디자인의 캡처다 — `node tools/capture.mjs` 로 다시 찍어야 한다.

아트보드
- Main.dc.html 빌더 · 빈 상태 / Builder-Filled 담긴 상태 / Builder-Detail 가격 상세 펼침 (소비자, 390px)
- Owner-Today 오늘 / Owner-Orders 주문 목록 / Owner-OrderDetail 주문 상세·제작 완료
- Owner-Prices 시세·품목(모바일) / Owner-Prices-Tablet 시세·품목(1024px, 인터랙티브)
- Owner-Customers 손님 / Owner-CustomerDetail 손님 상세 / Owner-Funeral 근조 긴급

참고: .dc.html은 support.js를 참조하지만 마크업·스타일은 파일 안에 모두 있어 정적 참고용으로 충분합니다.
3D 프리뷰는 디자인에서는 2D 실루엣(폴백)으로 그려져 있고, 실제 구현은 handoff.md의 "3D 꽃다발 프리뷰" 섹션을 따릅니다.
