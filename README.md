# 꽃다발 빌더 · 꽃집 운영 웹앱 — 핸드오프 번들

- docs/handoff.md — 개발 핸드오프 문서(디자인 토큰, 데이터 모델, 가격 계산 규칙, 화면 명세, 3D 프리뷰 Blender 파이프라인, API 초안, 미결 사항).
  라이브 버전: https://claude.ai/code/artifact/39a44528-d8e6-4c2b-9d73-6e2738d9e6d5
- design/*.dc.html — 디자인 아트보드 11개(자체 완결 HTML, 브라우저에서 바로 열림). canvas.json은 캔버스 배치·크기.
  라이브 캔버스: https://claude.ai/artifact/KBSMW768sMo1XRfTSkCsd7
- landing/index.html — 사장님용 상세(랜딩) 페이지. 꽃 스왑 · 남는 꽃 꽃다발 · 3D 꽃다발 데모가 페이지 안에서 실제로 동작한다(예시 데이터, 가격은 handoff 공식). 브라우저에서 바로 열림. 앱 주소가 정해지면 스크립트 상단 `APP_URL`만 채우면 CTA가 연결된다.
  라이브 버전: https://claude.ai/artifact/RMcWCyWFvvSSV3igywuRSL
  배포(Vercel, 프로덕션): https://flower-shop-landing-dun.vercel.app — 프로젝트 `flower-shop-landing`. 다시 배포: `cd landing && npx vercel deploy --prod` (`.vercel/` 에 프로젝트 연결 정보, `.vercelignore` 로 bundle.py·dist 제외)
- landing/app.html — 꽃다발 입찰 데모(배포 주소의 `/app`). 목업 계정 3개(소비자 최유진 · 플로리스트 화양플라워/반포꽃집, 비밀번호 없음)로 로그인하면 역할에 따라 소비자 화면(`#/c/*`)과 공급자 화면(`#/f/*`)이 갈리고, 다른 역할의 주소는 열리지 않는다.
  소비자: 3D로 꽃다발 만들기 → 입찰 요청 → 꽃집 비교(목록/비교표, 금액·평점·거리·준비순 정렬, 작업 사진·리뷰) → 직접 선택 → 완성 사진 확인 → 리뷰(사진 첨부). “남는 꽃” 탭에서 꽃집의 남는 꽃 꽃다발을 예약(픽업 때 결제).
  공급자: 입찰 요청(내 재고 대조, 대체 꽃 제안, 금액은 서로 비공개) · 내 입찰(낙찰 시 완성 사진 업로드 → 손님·작업 사진에 반영, 재고 차감) · 재고·남는 꽃(+1속, 낙찰 주문 부족분 발주 메모, 남는 꽃으로만 꽃다발 구성 → 할인 판매 등록, 픽업 예약 처리) · 프로필.
  상태는 브라우저 localStorage(`flowerbid.v3`)에만 저장(백엔드 없음). 포트폴리오 예시 사진은 Unsplash 실사진 핫링크, 리뷰·꽃집 이름은 예시.
- screenshots/ — 상세 페이지 캡처(PNG, 2배 해상도). `desktop-full.png`(1280px 전체) · `mobile-full.png`(390px 전체) · `desktop-01-hero` ~ `09-final`(섹션별 컷).
  다시 찍기: `node tools/capture.mjs [URL]` — 헤드리스 Chrome을 DevTools 프로토콜로 제어(추가 설치 없음). 3D는 화면에 보일 때만 그려지므로 페이지 전체를 뷰포트로 잡고, 8,000px 넘는 높이는 타일로 나눠 이어 붙인다.
- docs/competitors.md — 경쟁사 조사(2026-09-18, 출처 포함).
- blender/make_flowers.py — 꽃 6종(국화·장미·리시안셔스·카네이션·튤립·유칼립투스)을 Blender 파이썬으로 절차적으로 모델링해 glTF로 내보내는 스크립트. 로컬·기본 에셋에 꽃 프리셋이 없어 직접 만들었다(외부 모델 미사용 → 라이선스 문제 없음). blender/flowers.blend 는 열어서 손볼 수 있는 결과물.
  실행: `/Applications/Blender.app/Contents/MacOS/Blender -b --factory-startup --python blender/make_flowers.py`
- landing/models/*.glb — 품목당 1 glTF(528~1,956 tri, 22~61KB, 텍스처 없음). 원점=줄기 밑, +Y 위, 1unit=1m. 색 변형은 `petal` 머티리얼 색만 바꾼다. 실제 앱에서는 /public/models 로 옮겨 쓴다.
- landing/bouquet3d.js — three.js 꽃다발 프리뷰(handoff의 BouquetPreview): 동심원 슬롯(1·6·12·18), 고정 시드, InstancedMesh, 끌어서 회전, WebGL 불가 시 2D 실루엣 폴백. landing/models.js 는 GLB의 base64 묶음(자동 생성).
- landing/bundle.py — index.html + models.js + bouquet3d.js 를 한 파일로 묶어 landing/dist/ 에 만든다(단독 실행용 / 아티팩트 게시용).
- design/generate_artboards.py — 아트보드를 만든 생성 스크립트(토큰·샘플 데이터의 단일 소스).

결정(2026-09-18): 꽃집끼리 재고를 사고파는 기능은 넣지 않는다 — 중간 유통 레이어가 생기기 때문. 남는 재고는 꽃다발로 구성해 소비자에게 직접 판다. handoff.md의 "근처 꽃집 재고 요청 / 다른 꽃집에 넘기기"는 이 결정으로 대체된다.
결정(2026-09-18, 추가): 소개 페이지(/)에서 재고 관리 섹션·발주 메모를 뺐다(이전 버전은 landing/_backup/). 입찰 앱 공급자 화면의 재고 입력은 남는 꽃 계산에 필요해 유지.

아트보드
- Main.dc.html 빌더 · 빈 상태 / Builder-Filled 담긴 상태 / Builder-Detail 가격 상세 펼침 (소비자, 390px)
- Owner-Today 오늘 / Owner-Orders 주문 목록 / Owner-OrderDetail 주문 상세·제작 완료
- Owner-Prices 시세·품목(모바일) / Owner-Prices-Tablet 시세·품목(1024px, 인터랙티브)
- Owner-Customers 손님 / Owner-CustomerDetail 손님 상세 / Owner-Funeral 근조 긴급

참고: .dc.html은 support.js를 참조하지만 마크업·스타일은 파일 안에 모두 있어 정적 참고용으로 충분합니다.
3D 프리뷰는 디자인에서는 2D 실루엣(폴백)으로 그려져 있고, 실제 구현은 handoff.md의 "3D 꽃다발 프리뷰" 섹션을 따릅니다.
