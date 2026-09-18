---
name: ReBloom
description: 꽃집의 남는 꽃과 손님을 바로 잇는 웹앱 — Apple HIG 문법, 다크는 Rosé Pine
colors:
  tint-fill: "#0071E3"
  tint-text: "#0066CC"
  tint-text-dark: "#5CB0FF"
  grouped-bg: "#F2F2F7"
  cell: "#FFFFFF"
  label: "#000000"
  label-secondary: "#6C6C70"
  glyph: "#8E8E93"
  page-bg: "#FFFFFF"
  page-alt: "#F5F5F7"
  page-ink: "#1D1D1F"
  page-ink-secondary: "#6E6E73"
  page-hairline: "#D2D2D7"
  discount-red: "#D70015"
  warning-orange: "#A84A00"
  success-green: "#1D7A34"
  switch-on: "#34C759"
  star: "#FF9500"
  rose-pine-base: "#191724"
  rose-pine-surface: "#1F1D2E"
  rose-pine-overlay: "#26233A"
  rose-pine-text: "#E0DEF4"
  rose-pine-subtle: "#A4A0BC"
  rose-pine-muted: "#6E6A86"
  rose-pine-love: "#EB6F92"
  rose-pine-gold: "#F6C177"
  rose-pine-foam: "#9CCFD8"
typography:
  large-title:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Apple SD Gothic Neo', 'Pretendard Variable', Pretendard, 'Noto Sans KR', system-ui, sans-serif"
    fontSize: "34px"
    fontWeight: 700
    lineHeight: "41px"
    letterSpacing: "-0.025em"
  title2:
    fontSize: "22px"
    fontWeight: 700
    lineHeight: "28px"
    letterSpacing: "-0.02em"
  title3:
    fontSize: "20px"
    fontWeight: 600
    lineHeight: "25px"
    letterSpacing: "-0.02em"
  headline:
    fontSize: "17px"
    fontWeight: 600
    lineHeight: "22px"
  body:
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: "-0.01em"
  subhead:
    fontSize: "15px"
    fontWeight: 400
    lineHeight: "20px"
  footnote:
    fontSize: "13px"
    fontWeight: 400
    lineHeight: "18px"
  caption:
    fontSize: "12px"
    fontWeight: 400
    lineHeight: "16px"
  page-display:
    fontSize: "clamp(30px, 7.6vw, 64px)"
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "-0.03em"
  page-headline:
    fontSize: "clamp(30px, 4.6vw, 52px)"
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: "-0.03em"
  page-lede:
    fontSize: "clamp(17px, 1.9vw, 21px)"
    fontWeight: 400
    lineHeight: 1.42
rounded:
  tile-icon: "10px"
  thumb: "14px"
  cell: "20px"
  sheet: "28px"
  page-tile: "28px"
  capsule: "999px"
spacing:
  screen-inset: "16px"
  label-inset: "32px"
  row-pad: "10px 16px"
  group-gap: "12px"
  section-gap: "30px"
  page-section: "88px"
  page-section-wide: "128px"
components:
  button-primary:
    backgroundColor: "{colors.tint-fill}"
    textColor: "#FFFFFF"
    rounded: "{rounded.capsule}"
    height: "50px"
    padding: "0 22px"
  button-gray:
    backgroundColor: "rgba(120,120,128,.12)"
    textColor: "{colors.tint-text}"
    rounded: "{rounded.capsule}"
    height: "44px"
  button-cap:
    backgroundColor: "rgba(120,120,128,.12)"
    textColor: "{colors.tint-text}"
    rounded: "{rounded.capsule}"
    height: "32px"
    padding: "0 16px"
  chip-filter:
    backgroundColor: "rgba(120,120,128,.12)"
    textColor: "{colors.label}"
    rounded: "{rounded.capsule}"
    height: "34px"
  chip-filter-selected:
    backgroundColor: "{colors.label}"
    textColor: "#FFFFFF"
  group:
    backgroundColor: "{colors.cell}"
    rounded: "{rounded.cell}"
  type-tile:
    backgroundColor: "{colors.cell}"
    rounded: "16px"
  type-tile-selected:
    backgroundColor: "rgba(0,113,227,.1)"
    textColor: "{colors.tint-text}"
  page-pill:
    backgroundColor: "{colors.tint-fill}"
    textColor: "#FFFFFF"
    rounded: "{rounded.capsule}"
    height: "44px"
    padding: "0 22px"
---

# Design System: ReBloom

## Overview

**Creative North Star: "시스템 앱처럼 물러나고, 꽃만 색을 갖는다"**

ReBloom은 Apple Human Interface Guidelines의 방식을 그대로 따른다 — 사용자가 고정한 방향이다. 앱(`landing/app.html`)은 iOS 시스템 앱의 문법으로, 소개 페이지(`landing/index.html`)는 apple.com 제품 페이지의 문법으로 지었다. 인터페이스는 회색 바탕, 흰 셀, 시스템 서체, 시스템 블루 하나로만 이루어지고, 색은 3D 꽃다발·작업 사진·로고에서만 나온다.

이전 디자인(크림 바탕 + 딥그린 + IBM Plex Sans/Mono + 칩 더미 + 시세 티커 + eyebrow 라벨)은 폐기했고 되살리지 않는다. 모든 화면은 실제 서비스처럼 보여야 하며, 예시 데이터 고지는 앱의 계정 시트와 소개 페이지 각주 두 곳에만 둔다.

다크 모드는 순검정이 아니라 Rosé Pine 계열 배경을 쓴다(사용자 지정). 구조와 컴포넌트는 라이트와 같고, 배경·글자·의미색만 Rosé Pine 팔레트로 바뀐다. 틴트는 다크에서도 블루다.

**Key Characteristics:**
- inset grouped 리스트: 회색 바탕 위 반경 20px 흰 셀, 테두리 없음, 1px 인셋 구분선
- 라지 타이틀 → 스크롤하면 블러 내비게이션 바의 인라인 타이틀로
- 플로팅 글래스 탭바와 그 위의 액세서리(가격 + 주 버튼)
- 모든 버튼·칩·스테퍼·세그먼트는 캡슐
- 가로 넘침 없음: 가로 스크롤 스트립 대신 줄바꿈 칩과 4열 종류 타일
- 숫자는 같은 서체의 tabular-nums. 모노스페이스 없음

## Colors

절제(Restrained) 전략: 중립색 + 시스템 블루 하나. 의미색은 상태를 말할 때만 쓴다.

### Primary
- **System Blue Fill** (#0071E3): 주 버튼, 슬라이더·미터 채움, 종류 타일의 수량 배지. 흰 글자 대비 4.7:1.
- **System Blue Text** (#0066CC, 다크 #5CB0FF): 링크, 캡슐 버튼 글자, 뒤로가기, 선택된 탭, "입찰 n건" 같은 진행 상태, 시세 하락(▼).

### Neutral
- **Grouped Background** (#F2F2F7): 앱 화면 바탕, 시트 바탕.
- **Cell White** (#FFFFFF): 그룹 셀, 3D 꽃다발 셀, 종류 타일.
- **Label** (#000000) / **Secondary Label** (#6C6C70): 본문과 보조 글자. `rgba(60,60,67,.6)`은 대비가 모자라 글자에 쓰지 않는다.
- **Glyph Gray** (#8E8E93): 셰브런, 빈 상태 아이콘 같은 비글자 요소 전용.
- **Fill** (rgba(120,120,128,.12) / .2): 캡슐 버튼, 칩, 스테퍼, 세그먼트 트랙, 아이콘 타일.
- **Page White / Page Alt** (#FFFFFF / #F5F5F7), **Page Ink** (#1D1D1F), **Page Secondary** (#6E6E73), **Page Hairline** (#D2D2D7): 소개 페이지의 교차 섹션과 글자.

### Semantic
- **Discount Red** (#D70015, 다크 #EB6F92): 할인율, 할인가, 시세 상승(▲ — 한국 관행), 파괴적 동작, 알림 점.
- **Warning Orange** (#A84A00 on rgba(201,82,0,.1), 다크 #F6C177): 예산 초과, 재고 부족, 대체 제안, 신선기간 1일.
- **Success Green** (#1D7A34, 다크 #9CCFD8): 선택 완료, 예약됨, 낙찰, 매진.
- **Switch On** (#34C759), **Star** (#FF9500, 다크 #F6C177).

### Dark: Rosé Pine
- **Base** (#191724) 화면 바탕 · **Surface** (#1F1D2E) 셀 · **Overlay** (#26233A) 안쪽 면과 머티리얼 · **Text** (#E0DEF4) · **Subtle** (#A4A0BC) 보조 글자 · **Muted** (#6E6A86) 글리프와 구분선.

### Named Rules
**The One Tint Rule.** 인터랙티브한 것은 블루, 나머지는 중립. 두 번째 브랜드 색을 들이지 않는다. 색은 꽃이 낸다.
**The Never Black Rule.** 다크 배경에 #000을 쓰지 않는다. 항상 Rosé Pine base/surface/overlay.
**The Up-Is-Red Rule.** 등락은 오르면 빨강·내리면 파랑이고, 항상 삼각형 아이콘과 함께 쓴다.

## Typography

**Display / Body / Label Font:** 시스템 산세리프 한 가지 — `-apple-system, BlinkMacSystemFont, 'Apple SD Gothic Neo'`, Apple 기기가 아니면 Pretendard Variable(jsDelivr 동적 서브셋).

**Character:** 브리프가 Apple의 방식을 고정했으므로 시스템 서체가 곧 목소리다. 로고 워드마크의 세리프는 로고 이미지 안에만 있고 인터페이스에서 흉내 내지 않는다.

### Hierarchy
- **Large Title** (700, 34/41px, -0.025em): 탭 루트 화면의 제목.
- **Title 2** (700, 22/28px): 화면 안 섹션 제목("꽃 고르기", "입찰 3건").
- **Title 3** (600, 20/25px): 액세서리의 금액, 입찰 카드의 금액, 빈 상태 제목.
- **Headline** (600, 17/22px): 행 제목, 버튼.
- **Body** (400, 17px/1.35): 행 라벨, 본문.
- **Subhead** (400, 15/20px): 행 보조 줄, 칩.
- **Footnote** (400, 13/18px): 그룹 위 라벨(좌측 32px 인셋), 그룹 아래 설명, 메타.
- **Caption** (400–600, 12/16px): 배지, 통계 라벨. 탭 라벨은 11px.
- **Page Display** (600, clamp(30px, 7.6vw, 64px), 1.1, -0.03em): 소개 페이지 h1. **Page Headline** (600, clamp(30px, 4.6vw, 52px)). **Page Lede** (clamp(17px, 1.9vw, 21px), #6E6E73).

### Named Rules
**The Tabular Sans Rule.** 가격·수량·시각은 `.num`(tabular-nums)으로 자릿수만 맞춘다. 모노스페이스를 쓰지 않고, "원"을 숫자보다 작게 쓰지 않는다. 금액 입력은 천 단위 콤마로 보여 준다.

## Layout

앱은 폭 480px 중앙 정렬 한 칼럼(데스크톱에서도 폰 폭). 화면 좌우 16px 인셋, 그룹 사이 12px, 섹션 제목 위 30px·아래 10px, 그룹 라벨은 위 24px·아래 7px에 좌측 32px 인셋. 행은 최소 52px, 패딩 10px 16px, 선행 아이콘이 있으면 구분선을 글자 시작점(68px, 썸네일은 92px)까지 들여쓴다. 하단은 플로팅 독이 차지하므로 본문 아래 96px(액세서리가 있으면 172px)을 비운다.

소개 페이지는 1028px 랩, 섹션 세로 88px(900px 이상 128px), 흰색과 #F5F5F7 교차. 만들기 타일은 1180px까지, 900px 이상에서 3D가 왼쪽에 sticky.

**The No Overflow Rule.** 어느 폭(320px부터)에서도 가로 넘침과 잘린 글자가 없어야 한다. 선택지는 가로 스크롤 대신 줄바꿈 칩, 22품목 꽃 목록은 4열 종류 타일 → 고른 종류의 품목만, 사진 줄은 4열 그리드, 비교표는 폭에 맞춘 고정 레이아웃, 긴 select는 라벨 아래 한 줄을 통째로 쓴다.

## Elevation & Depth

앱의 면은 평평하다. 깊이는 회색 바탕과 흰 셀의 톤 차이로 만들고, 그림자는 떠 있는 것에만 쓴다.

### Shadow Vocabulary
- **Float** (`0 10px 30px rgba(0,0,0,.12), 0 1px 3px rgba(0,0,0,.08)`): 탭바, 액세서리, HUD, 알림.
- **Segment** (`0 3px 8px rgba(0,0,0,.12), 0 1px 1px rgba(0,0,0,.04)`): 세그먼트의 선택 조각, 슬라이더·스위치 손잡이.
- **Icon Lift** (`0 8px 28px rgba(0,0,0,.12), 0 0 0 .5px rgba(0,0,0,.08)`): 앱 아이콘 타일.

### Named Rules
**The Material-For-Bars Rule.** 블러 머티리얼(`saturate(180%) blur(20–24px)`)은 내용 위에 떠서 겹치는 것 — 내비게이션 바, 탭바, 액세서리, HUD, 알림, 3D 셀 왼쪽 위의 안내 배지·미리보기 세그먼트 — 에만 쓴다. 장식용 글래스 카드는 없고, 꽃다발 구성 배지는 캔버스 밖(셀 아래)에 둔다.

## Motion

움직임은 상태를 알릴 때만 쓴다. 곡선은 하나 — `cubic-bezier(.2,.8,.2,1)`(빠르게 나와 부드럽게 멈춤).
- **Push / Pop** (.38s): 상세로 들어가면 오른쪽 36px에서, 돌아오면 왼쪽 36px에서 페이드인. 탭 전환은 .2s 페이드. 같은 화면의 상태 변화는 움직이지 않는다.
- **Sheet** (.4s, 아래에서), **Alert** (.3s, scale 1.08 → 1), **HUD** (.35s, 위 14px에서 scale .96 → 1, 2.8초 뒤 사라짐), 배경은 .25s 페이드.
- **Press** (.12s): 버튼·칩·타일은 scale .97 + opacity .75. **Nav material / 인라인 타이틀** .2s, **세그먼트·스위치** .2–.25s, **미터**는 width가 아니라 translateX로 .25s.
- **3D**: 꽃이 담기면 380ms 동안 자라나고, 꽃다발은 천천히 자동 회전하다 끌면 멈춘다. 소개 페이지의 선언문은 화면에 들어올 때 강조 문장이 .9s씩 차례로 짙어진다.
- **Reduced motion**: `prefers-reduced-motion`이면 모든 애니메이션·전환을 끄고 3D 자동 회전과 성장도 멈춘다.

## Shapes

동심원처럼 큰 반경: 아이콘 타일 10px, 썸네일 14–16px, 그룹 셀·종류 타일 16–20px, 시트·페이지 타일 28px. 버튼·칩·스테퍼·세그먼트·배지·탭바·액세서리는 전부 캡슐(999px). 셀에 테두리가 없고, 색 띠·왼쪽 색 테두리·점선 상자를 쓰지 않는다.

## Components

### Buttons
- **Shape:** 캡슐(999px).
- **Primary:** #0071E3 채움, 흰 17px 600, 높이 50px(`.md` 44px). hover #0062C4, active scale .97 + opacity .75, disabled는 fill 배경 + 보조 글자.
- **Gray:** fill 배경 + 블루 글자. 파괴적이면 빨강 글자.
- **Cap:** App Store "받기" 식 32px 캡슐(fill + 블루 700 15px), 터치 영역은 의사 요소로 44px.
- **Page Pill / More:** 소개 페이지의 #0071E3 알약(44px, 17px 400)과 셰브런 달린 텍스트 링크.

### Chips
- **Filter chip:** 34px 캡슐, fill 배경. 선택은 라벨 색 채움 + 반전 글자. 줄바꿈된다.
- **Badge:** 12px 600 캡슐. 회색 / tint / green / orange / red 옅은 배경.

### Cards / Containers
- **Group:** 흰 셀, 반경 20px, 테두리·그림자 없음. 안은 `.row`(구분선 인셋)와 `.pad`.
- **Bid card:** 그룹 하나에 헤더 행 + 사진 4열 + 배지 + 인용 + 동작 버튼.
- **Bento tile (page):** 반경 28px, 크기가 서로 다른 타일에 실제 예시 목록을 담는다.

### Inputs / Fields
- **Field row:** 라벨 왼쪽, 값 오른쪽 정렬, 테두리 없음. select는 블루 글자 + 위아래 셰브런. 긴 선택지는 `.stack`.
- **Stepper:** 36px fill 캡슐 안에 − n +(또는 숫자 입력).
- **Segmented control:** 캡슐 트랙, 선택 조각은 셀 색 + Segment 그림자.
- **Slider / Switch:** iOS 슬라이더(4px 트랙, 28px 흰 손잡이), 51×31 스위치(#34C759). 슬라이더는 값과 나란히 읽히는 곳에만 쓴다. 꽃집 화면의 비율 조절은 전부 같은 틀이다 — 머리줄(라벨 + 현재 값), 슬라이더, 꼬리줄(기준값 · 결과값): 송이 매도 할인율과 남는 꽃 꽃다발 할인율은 0–80% · 1% 단위, 입찰 금액은 예상가 대비 −30%~+30% · 1% 단위(가운데가 기준인 `.slider.bi` 트랙). 금액 입력이 있는 곳은 입력과 슬라이더가 양방향으로 연동되고, 끄는 동안에는 화면을 다시 그리지 않고 숫자만 바꾼다. 예산처럼 값 자체가 목적이면 슬라이더 대신 금액 입력을 쓴다.
- **One-line choices:** 몇 개로 끊어 둔 빠른 선택지(−5%·예상가·+5%, 할인율 20/30/40/50%)를 두지 않는다. 연속값은 슬라이더로, 낱개 선택은 한 줄 세그먼트로.
- **Focus:** `3px solid rgba(0,113,227,.55)`, offset 2px.

### Navigation
- **Nav bar:** 44px, 스크롤하면 머티리얼과 헤어라인이 나타나고 인라인 타이틀이 페이드인. 상세 화면은 블루 셰브런 + 부모 탭 이름.
- **Floating tab bar:** 하단 16px 인셋의 글래스 캡슐, 탭 4개, 선택 탭은 블루 + fill 알약, 알림 점은 빨강.
- **Accessory:** 탭바 바로 위 글래스 캡슐 — 왼쪽 금액(캡션 + Title 3), 오른쪽 주 버튼.
- **Sheet / Alert / HUD / Viewer:** 계정은 하단 시트(28px 상단 반경), 되돌릴 수 없는 선택은 가운데 알림, 피드백은 상단 HUD 캡슐, 사진은 검은 전체 화면 뷰어.
- **Page nav:** 52px 블러 바, 마크 + "ReBloom", 13px 링크, 작은 블루 알약.

### Flower Type Grid (signature)
12종을 4열 타일로 보여 주고(한 송이 3D 렌더 + 이름 + 담은 수량 배지), 고른 종류의 품목만 아래 그룹에 편다. 담은 꽃은 별도 그룹에 소계와 함께 모은다. 손님 만들기와 꽃집 재고가 같은 컴포넌트를 쓴다.

### Flower Stem Icon
품목 아이콘은 그림 기호가 아니라 그 꽃의 3D 모델을 한 송이 그린 투명 PNG다(`Bouquet3D.stem`, 96px, 포장 없이 꽃머리를 가까이에서). 40px 타일·44px 종류 타일 안에서 1.7배로 키워 꽃머리를 채운다(그린은 1.15배). 5꽃잎 SVG 실루엣은 WebGL이 없을 때의 폴백으로만 남긴다.

### Filter Bar
필터는 한 줄로 끝낸다: 왼쪽에 작은 세그먼트(크기 전체·S·M·L), 오른쪽에 블루 팝업 메뉴(용도). 칩 줄을 두 겹으로 쌓지 않는다. 꽃다발 크기는 송이 수에서 나온다(S 9송이 이하 · M 10~15 · L 16 이상).

### 3D Bouquet Cell
300px 흰 셀에 three.js 꽃다발(투명 배경). 구성 배지는 캔버스를 가리지 않게 셀 아래 가운데 정렬 줄에 둔다. 썸네일도 투명 PNG라 라이트/다크 셀 색이 그대로 비친다.

## Do's and Don'ts

### Do:
- **Do** 새 화면을 라지 타이틀 + inset grouped 그룹 + 13px 라벨/각주로 짓는다.
- **Do** 화면의 주 동작 하나를 액세서리(탭바 위 글래스 캡슐)에 올린다.
- **Do** 320px에서 넘침 검사를 통과시킨다(`tools/run-in-page.mjs` + 넘침 시나리오).
- **Do** 다크에서 Rosé Pine 토큰만 쓴다.
- **Do** 로고는 이미지로만 쓴다: 내비게이션·히어로는 마크(`rebloom-mark.png`), 소개 페이지 마무리 블록과 앱 계정 시트는 워드마크까지 든 락업(`rebloom-logo.png`). 다크에서는 밝은 타일(#FFFAF3) 위에 올린다. 로고 PNG 5장은 사용자 제공 원본에서 ImageMagick으로 만든 파생물이고(배경 제거·크롭·리사이즈), 각 파일의 tEXt 청크(`impeccable:prompt`)에 Source / Derived-from / Processing 을 적어 둔다. 새 래스터를 넣을 때도 같은 형식으로 남긴다.
- **Do** 끊기면 어색한 단위("이름 수량 ·", "단가 × n", "= 합계")는 `dots()`/`.nb`로 묶고 구분점은 앞 단위에 붙인다. 360px 미만에서는 묶음을 푼다.
- **Do** 목록 행은 네 줄 안에서 끝낸다. 자세한 구성은 썸네일과 상세 화면이 맡는다.
- **Do** 예시 데이터 고지는 계정 시트와 소개 페이지 각주에만 둔다.

### Don't:
- **Don't** 크림 바탕, 딥그린, IBM Plex, 모노스페이스 숫자로 돌아가지 않는다.
- **Don't** 가로로 스크롤되는 칩 줄·사진 줄·표를 만들지 않는다.
- **Don't** 22품목을 한 목록으로 늘어놓지 않는다 — 종류 타일을 쓴다.
- **Don't** 제목 위에 eyebrow 라벨, 시세 티커, 지표 보드를 두지 않는다.
- **Don't** 유니코드 글리프(★ ▲ ▼ ✓)나 이모지를 아이콘으로 쓰지 않는다 — 1.8px 스트로크 SVG와 채운 별·삼각형 SVG만.
- **Don't** 다크 배경에 #000을, 글자에 `rgba(60,60,67,.6)`을 쓰지 않는다.
- **Don't** 배송·배달을 다시 들이지 않는다 — 픽업 전용.
