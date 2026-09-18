# 한국 화훼 시장 경쟁사 조사: 3D 커스텀 꽃다발·꽃집 입찰·꽃집 운영 도구

2026-09-18 작성, 같은 날 피벗 반영 개정. 아래 내용은 웹 검색 결과와 실제 페이지에서 확인한 것만 적었고, 확인하지 못한 항목은 "확인 못함"으로 표기했습니다.

피벗 내용(2026-09-18 결정): 꽃집 간 재고 거래·교환은 만들지 않습니다. 꽃집끼리 남는 꽃을 사고팔면 유통 단계가 하나 더 생기기 때문입니다. 대신 각 꽃집이 자기 가게의 남는 재고(신선도 종료 약 2일 전 줄기 − 주문에 잡힌 줄기)만 꽃다발로 만들어 소비자에게 할인가로 직접 팝니다(소비자 "남는 꽃" 탭: 둘러보기 → 예약 → 방문 결제 → 후기). 나머지 컨셉은 그대로입니다.

## 1. 한 문단 요약

한국 소비자용 꽃 서비스는 정해진 상품을 고르는 방식이 대부분입니다. 꾸까·원모먼트·꽃집청년들·전국 꽃배달 체인이 모두 그렇고, 줄기 단위 커스텀이나 도매가와 연동된 가격 공개는 찾지 못했습니다. 견적형 플랫폼인 숨고에는 "플라워 제작" 카테고리가 있지만, 꽃집이 견적을 보낼 때마다 비용을 내고 꽃 전용 기능은 없습니다. 꽃집용 B2B 서비스(피카플라·오늘의꽃·꽃비파트너스)는 도매 주문과 주문 수신에 머물러 있습니다. 도매가 기반 자동 소매가, 재고, 다음 날 발주 추천, 고객관리(CRM)를 묶은 한국어 꽃집 운영 도구는 검색 범위 안에서 찾지 못했습니다. 해외에는 3D 빌더(BloomyPro, Flower Architect)와 도매가 기반 가격 계산(Details Flowers, EveryStem)이 각각 따로 있습니다.

남는 재고 쪽을 보면, 국내 마감할인 서비스(라스트오더, 편의점 마감할인, 2026-06 시작된 배달앱 마감할인, 럭키밀·마구마켓, 마감히어로)는 확인한 범위에서 모두 식품 대상이고, 꽃이나 꽃집이 올라온 사례는 찾지 못했습니다. 해외에서는 Too Good To Go가 이미 꽃·식물 분류(매장 URL의 "flowersplants")로 꽃집·Whole Foods의 남는 꽃을 서프라이즈 백(내용물 비공개, 정가의 약 1/3)으로 팔고 있습니다. 다만 꽃집 재고 도구와 연결돼 있지 않고 내용물을 미리 보여 주지 않습니다. 빈자리는 다음 세 곳입니다.

- 소비자 쪽: 공개 경매가에 연동된 줄기 단위 투명 가격 + 3D 커스텀 + 동네 꽃집 입찰
- 꽃집 쪽: aT 경매 시세에 연동된 한국어 운영 도구(자동 소매가·재고·다음 날 발주 메모·대체꽃 제안)
- 남는 재고: 꽃집 재고에서 바로 나오는 "남는 꽃" 꽃다발의 소비자 직판(예약 → 방문 결제). 국내 꽃 분야에서는 같은 서비스를 찾지 못했습니다(개별 꽃집의 비공식 떨이 판매 규모는 확인 못함).

aT 경락가 데이터는 오픈API로 공개돼 있어 데이터 확보는 가능합니다(자동 승인, 일 1,000건).

## 2. 비교 표

| 경쟁사 | 대상 | 수익모델 | 커스텀 빌더 | 가격 투명성 | 입찰/견적 | 플로리스트 프로필 | 재고·발주 도구 | 남는 재고 소비자 직판(마감할인) |
|---|---|---|---|---|---|---|---|---|
| 꾸까 | 소비자(+B2B) | 직접 판매·구독 | 없음(큐레이션) | 상품가만 | 없음 | 없음 | 없음 | 확인 못함 |
| 피카플라(꾸까) | 꽃집 | 도매 판매 | – | 도매가(회원) | 없음 | – | 주문만 | – (도매) |
| 어니스트플라워 | 소비자·사업자 | 농가 직송 판매·구독 | 없음 | 확인 못함 | 없음 | 없음 | 없음 | 마감할인은 아님. 농부가 고르는 랜덤박스 "파머스 초이스"(농가 출하 부담 완화) |
| 원모먼트 | 소비자(서울 당일) | 직접 판매 | 레터링 정도 | 상품가만 | 없음 | 없음 | – | 확인 못함 |
| 스노우폭스플라워 | 소비자(매장) | 직영 소매 | 없음 | 정찰제(가격표) | 없음 | 없음 | – | 확인 못함 |
| 꽃집청년들·전국 체인 | 소비자 | 상품 판매 → 제휴 꽃집에 주문 전달 | 없음 | 상품가만 | 없음 | 없음 | – | 확인된 것 없음 |
| 꽃비 / 꽃비파트너스 | 양쪽 | 확인 못함 | 없음 | 꽃집별 상품가 비교 | 없음(가격 비교) | 꽃집 목록 | 주문 관리, 생화·부자재 거래 | 확인 못함 |
| 플디 | 양쪽 | 수수료 8~15%(2020년 기사) | 없음 | 상품가 | 없음 | 있음 | 주문·고객 관리 | 확인 못함(서비스 접속 불가) |
| 숨고 | 양쪽(범용) | 견적 발송 캐시 + 숨고페이 3.5% | 없음 | 없음 | 견적(요청서 → 고수) | 있음 | 없음 | 없음 |
| 크몽 | 양쪽(범용) | 구간별 판매 수수료 | 없음 | 서비스 정가 | 제한적 | 있음 | 없음 | 없음 |
| 네이버 예약 / 당근 비즈프로필 | 양쪽(범용) | 결제 수수료 / 광고 | 없음 | 없음 | 없음 | 있음 | 없음 | 전용 기능 없음. 당근은 쿠폰·소식을 무료 발행 가능(꽃집은 "생활" 업종에 포함). 네이버는 "새소식" 글쓰기 |
| 오늘의꽃 | 꽃집 등 | 도매 중개 | – | 품목가 | 없음 | – | 주문만 | – (도매) |
| aT 화훼유통정보 | 공공 | 무료 | – | 경락가 공개·API | – | – | – | – |
| BloomyPro(네덜란드) | 꽃집·도매 | SaaS(가격 확인 못함) | 3D, 소비자용 임베드 가능 | 원가·마진 계산(내부용) | 없음 | 없음 | 컬렉션·발주 | 없음 |
| Flower Architect | 신부·꽃집 | 구독(상세 확인 못함) | 3D | 확인 못함 | 자기 거래 꽃집에 견적 요청 | 없음 | 없음 | 없음 |
| Details Flowers / EveryStem | 이벤트 꽃집 | SaaS $25~150/월, $24.99/월 | 없음 | 도매 실시간가·마크업(내부용) | 제안서 | – | 줄기 수 계산·발주 | 없음 |
| Floranext / Hana POS | 꽃집 | SaaS | 없음 | – | – | – | POS·CRM·배송 | 확인 못함 |
| BloomNation / Floom | 양쪽 | 수수료(BloomNation 약 10%, 2차 출처 / Floom 25%) | 없음 | 꽃집이 직접 가격 설정 | 없음 | 있음 | POS·대시보드 | 확인 못함 |
| FTD / Teleflora | 양쪽 | 주문 수수료 20% + 정산 수수료 7~10% 등 | 없음 | 없음 | 없음 | 없음 | POS | 없음 |
| Florist Trader(미국, 참고) | 꽃집 간 | 무료 앱 | – | – | 경매 기능 | – | – | 없음(꽃집끼리 거래. 우리는 만들지 않음) |
| 라스트오더(미로) | 소비자·식음료 매장·편의점 | 2020년 기사: 입점 무료, 월 3만 원 유료화 검토(현재 요금 확인 못함) | – | 정가 대비 할인율 표시 | 없음 | 없음 | 없음 | 있음, 단 식품만. 꽃·꽃집 사례 찾지 못함 |
| 배달앱 마감할인(배민·쿠팡이츠·요기요) + 럭키밀·마구마켓 | 소비자·식품 매장 | 확인 못함 | – | 할인율 표시 | 없음 | 없음 | 없음 | 있음(2026-06-15 시작), 식품만 |
| 마감히어로 | 소비자·동네 매장 | 확인 못함 | – | 할인율 표시 | 없음 | 없음 | 없음 | 있음, 식음료 중심. 꽃 없음 |
| Too Good To Go(해외) | 소비자·매장 | 미국 기준 봉투당 $1.79 + 연 $89(2023년 기사) | 없음 | 정가 대비 약 1/3 가격 | 없음 | 없음 | 없음 | 있음. 꽃·식물 분류(URL "flowersplants")에 꽃집·Whole Foods 꽃 봉투. 내용물 비공개 |
| hanane 찬스플라워(일본) | 소비자 | 규격 외 꽃 1송이 100엔 판매 | 없음 | 균일가 | 없음 | 없음 | 없음 | 비슷함(농가의 규격 외 꽃. 꽃집 재고는 아님) |
| 카카오메이커스 "못난이 꽃" | 소비자 | 기획 판매 | 없음 | 상품가 | 없음 | 없음 | 없음 | 비슷함(경매 유찰 꽃, 2023년 일회성 기획전) |

## 3. 카테고리별 상세

### A. 한국 소비자 서비스

**꾸까**
- 2014년 국내 최초 꽃 정기구독을 시작했습니다. 2026년에는 LG전자와 "틔운 꽃 구독"을 출시했고, 2주마다 플로리스트가 큐레이션한 꽃을 보냅니다.
- 브랜드 큐레이션이 강점입니다. 소비자가 구성을 고를 수 없고, 동네 꽃집과 연결되지 않습니다.
- kukka.kr 본 페이지는 인증서 오류로 직접 확인하지 못했습니다.
- 출처: [플래텀](https://platum.kr/archives/143045), [굿모닝경제](https://www.goodkyung.com/news/articleView.html?idxno=288067), [구독 페이지](https://kukka.kr/subscription/)

**어니스트플라워**
- 농가 직송(Farm to Table) 방식입니다. 50여 개 협약 농가, 연 300종 이상을 다루고 정기구독도 운영합니다.
- 사이트는 운영 중입니다(푸터 2026, 운영사 ㈜아레스3).
- 손질하지 않은 꽃을 단 단위로 보내는 방식이라, 꽃집이 제작하는 우리 컨셉과는 보완 관계에 가깝습니다.
- 출처: [로켓펀치](https://www.rocketpunch.com/companies/honestflower), [벤처스퀘어](https://www.venturesquare.net/796180), [honestflower.kr](https://honestflower.kr/)

**원모먼트**
- 운영 중입니다. 서울 당일배송, 카탈로그 상품 45,000~159,000원, 커스텀은 레터링 정도입니다.
- 출처: [1moment.co.kr](https://1moment.co.kr/)

**스노우폭스플라워**
- 모든 상품에 가격표를 붙이는 정찰제이고, aT 경매권을 승인받았습니다.
- 가격을 물어봐야 하는 불편을 매장에서 해결한 선례입니다. 다만 도매가 대비 가격 구조를 공개하지는 않습니다.
- 출처: [농촌진흥청 웹진(2020)](https://www.rda.go.kr/webzine/2020/03/sub1-3-2.html), [공식몰](https://snowfoxflowers.com/)

**꽃집청년들·전국 체인**
- 고정 카탈로그 상품을 전국 당일배송하고, 제휴 꽃집에 주문을 전달하는 구조로 보입니다.
- 출처: [f-mans.com](https://www.f-mans.com/)

**전국플라워센터**
- 회원 꽃집 1,500곳 이상이 서로 주문을 주고받는 네트워크입니다. 수수료율은 공개돼 있지 않습니다.
- 출처: [theflowercenter.co.kr](https://theflowercenter.co.kr/)

**오즈플라워 인트라넷**
- 로그인 화면만 확인했습니다.
- 출처: [ozflowerchain.co.kr](https://www.ozflowerchain.co.kr/)

**꽃비(마루웹)**
- 배송지를 입력하면 전국 4,000곳 이상 꽃집의 상품 가격을 비교하고, 실제 출고 사진을 보여 줍니다.
- 앱스토어 평점은 표시되지 않습니다(리뷰 수 부족).
- 출처: [App Store](https://apps.apple.com/us/app/%EA%BD%83%EB%B9%84-%EA%BD%83%EC%A7%91-%EA%BD%83%EB%B0%B0%EB%8B%AC-%EB%B9%84%EA%B5%90-%ED%94%8C%EB%9E%AB%ED%8F%BC/id1543120768)

**플디(체인지메이커)**
- 가장 비슷했던 선행 사례입니다. 주변 꽃집 예약 플랫폼이었고, 2020년 기사 기준 수수료 8~15%, 파트너 꽃집 200여 곳이었습니다. 같은 기사는 기존 중개업체 수수료를 30%로 언급했습니다.
- 현재 fldi.kr은 DNS 조회가 실패합니다. 운영이 중단된 것으로 추정되지만 확정하지는 못했습니다.
- 출처: [서울경제(2020)](https://www.sedaily.com/NewsView/1Z7R1SL0HB), [세계일보(2020)](https://www.segye.com/newsView/20201225503307)

**카카오 선물하기**
- 수수료가 5~11% 수준이라는 보도가 있습니다. 이 수치는 카페 프랜차이즈 모바일 쿠폰 기준이며, 꽃 카테고리 요율은 확인하지 못했습니다.
- 출처: [SBS(2023)](https://news.sbs.co.kr/news/endPage.do?news_id=N1007318789)

**FlowerLikeU**
- 드래그앤드롭 꽃다발 커스텀 → 플로리스트 의뢰 → 채팅으로 이어지는 흐름을 구현했습니다.
- 2022년 10~11월에 진행된 6인 팀 프로젝트(학생 프로젝트로 보임)이고, 상용 서비스로 운영된 흔적은 없습니다.
- 출처: [GitHub](https://github.com/FlowerLikeU-STUDIO/flower_like_u)

### B. 견적·입찰형 플랫폼

**숨고**
- "플라워 제작"(꽃다발·꽃바구니·화환 등) 카테고리가 있습니다. 소비자가 요청서를 쓰면 여러 고수(꽃집)가 견적을 보냅니다.
- 거래액 수수료는 없습니다. 대신 견적을 보낼 때마다 숨고캐시가 들고, 비용은 카테고리와 지역에 따라 달라집니다(고객이 열람하지 않으면 환급). 숨고페이로 결제하면 3.5%가 붙습니다.
- 꽃 구성을 시각화하거나 단가 근거를 보여 주는 기능, 대체꽃 제안 구조는 없습니다.
- 출처: [숨고 플라워 제작](https://soomgo.com/prices/%ED%94%8C%EB%9D%BC%EC%9B%8C-%EC%A0%9C%EC%9E%91), [견적 도움말](https://help.soomgo.com/hc/ko/articles/360044939772), [afterwork30(2026-08)](https://afterwork30.com/reviews/soomgo-pro-cost-structure)

**크몽**
- 구간별 판매 수수료를 받습니다. 70만 원 이하 구간의 실효 수수료는 약 21.7%로 소개됩니다.
- 꽃 제작 거래에 얼마나 쓰이는지는 확인하지 못했습니다.
- 출처: [크몽 수수료 정책](https://support.kmong.com/hc/ko/articles/36616106488729), [에버픽](https://geteverpick.com/ko/side-income/kmong-side-income-fees)

**네이버 예약**
- 예약 기능 자체는 무료입니다. 네이버페이를 연동하면 1.98~3.63%가 붙습니다.
- 출처: [Omago](https://www.omago.ai/ko/blog/naver-booking-fees-truth-korea)

**당근 비즈프로필**
- 등록은 무료이고 광고는 클릭당 과금됩니다. 예약 기능은 뷰티 업종부터 열렸고, 꽃집에 적용되는지는 확인하지 못했습니다.
- 출처: [당근비즈니스](https://business.daangn.com/business-profile/about), [당근 보도자료](https://about.daangn.com/company/pr/archive/%EB%8B%B9%EA%B7%BC%EB%A7%88%EC%BC%93-%EB%B9%84%EC%A6%88%ED%94%84%EB%A1%9C%ED%95%84-%EB%B7%B0%ED%8B%B0%EB%AF%B8%EC%9A%A9-%EC%97%85%EC%A2%85%EC%97%90-%EC%98%88%EC%95%BD-%EA%B8%B0%EB%8A%A5-%EC%98%A4%ED%94%88/)

### C. 꽃집 B2B·운영 도구

**aT 화훼유통정보**
- 일자별 경락가와 실시간 경매(10초 간격 갱신)를 공개합니다.
- 오픈API가 있습니다: 자동 승인, 일 1,000건(증량 문의 가능). 품목·품종·등급별 최고가·최저가·평균가와 물량을 제공합니다.
- 상업적 이용 조건은 페이지에 명시돼 있지 않아 약관을 확인해야 합니다.
- 출처: [오픈API 안내](https://flower.at.or.kr/api/apiOpenInfo.do), [경매시세](https://flower.at.or.kr/yfmc/front/stat/aucPrice.do?menuId=23), [공공데이터포털](https://www.data.go.kr/data/15052544/fileData.do)

**화훼 경매가(앱)**
- 경매 시세를 조회하는 서드파티 앱이 존재합니다. 상세 내용은 확인하지 못했습니다.
- 출처: [Google Play](https://play.google.com/store/apps/details?id=kr.pandoroots.flowerauctionprice)

**피카플라(꾸까)**
- 플로리스트 인증 회원 전용 온라인 도매입니다. 2021년 기사 기준 3,000개 꽃집이 가입했고, 오후 8시까지 주문하면 다음 날 오전에 배송합니다. 사이트는 운영 중입니다.
- 출처: [파이낸셜뉴스(2021)](https://www.fnnews.com/news/202104261756577946), [pik-a-fla.com](https://pik-a-fla.com/faq/?next=/)

**오늘의꽃**
- 밤 11시까지 주문하면 다음 날 오전 10시까지 도매 꽃을 배송합니다.
- 출처: [THE VC](https://thevc.kr/okkot/products), [okkot.com](https://www.okkot.com/products/4366)

**꽃비파트너스**
- 꽃집용 앱입니다. 상품 등록, 주문 알림, 생화·부자재 거래, 커뮤니티, 구인 기능이 있고, 2025-09에 업데이트됐습니다(리뷰 2건).
- 재고 관리나 가격 자동화 기능은 보이지 않습니다.
- 출처: [App Store](https://apps.apple.com/kr/app/id1559151444)

**해외 꽃집 SaaS**
- Floranext: POS, 배송 경로, 기념일 알림 이메일, 구독. [floranext.com](https://floranext.com/florist-pos/)
- Hana POS: CRM 알림, 웨딩 제안서, 꽃집 간 주문 전송(건당 $2.99), 1,198곳 이상 사용. [hanafloristpos.com](https://www.hanafloristpos.com/)
- Details Flowers: 도매 실시간 가격·재고(Details Direct), 자동 마크업, 줄기 수 계산. $25~150/월. [features](https://info.detailsflowers.com/features), [GetApp](https://www.getapp.com/retail-consumer-services-software/a/details-flowers-software/)
- EveryStem: 도매가 → 소매가 계산, 레시피. $24.99/월. [everystem.com](https://www.everystem.com/)
- BloomNation: 2011년 설립, 약 3,500개 꽃집, 꽃집이 직접 찍은 사진만 허용. 수수료 약 10%는 2차 출처입니다. [Wikipedia](https://en.wikipedia.org/wiki/BloomNation), [pricingnow](https://pricingnow.com/question/bloomnation-pricing/)
- Floom: 수수료 25%(검색 결과 요약 기준이며, 원문은 403/429 오류로 직접 확인하지 못함). 꽃집용 대시보드 FloomX 도움말에 대체꽃(Substitutions) 처리 항목이 있습니다. [파트너 페이지](https://www.floom.com/gb/pages/partner-with-floom), [FloomX 도움말](https://help.floomx.com/hc/en-us/articles/12312488338321)
- FTD / Teleflora: 주문을 보낸 꽃집이 20%, 본사가 정산 수수료 7~10%와 전송료를 가져가고, 실제 제작 꽃집은 약 70~73%를 받습니다. [Floranext 해설](https://floranext.com/what-is-flower-wire-service/), [Hana 블로그](https://www.hanafloristpos.com/blog/what-are-floral-wire-service/)
- Lovingly: 월 이용료와 수수료가 없다고 자체 설명합니다. 실제 과금 구조는 확인하지 못했습니다. [lovinglyflorists.com](https://www.lovinglyflorists.com/)

### D. 3D·커스텀 빌더, 도매 연동 가격

**BloomyPro**
- 3D 꽃 3,877종을 제공하고, 데이터와 연결해 꽃다발 가격·마진·원가를 계산합니다. 꽃집 웹샵에 임베드하면 소비자가 직접 꽃다발을 구성할 수 있습니다.
- 기술 면에서 가장 직접적인 경쟁자이자 제휴·벤치마크 후보입니다. 꽃집 매칭, 입찰, 공개 도매가 연동은 없습니다.
- 출처: [bloomypro.com](https://bloomypro.com/), [FloralDaily](https://www.floraldaily.com/article/9284541/bloomy-pro-launches-online-bouquet-maker-for-consumer-use/), [Thursd](https://thursd.com/articles/go-virtual-with-bloomypro)

**Flower Architect**
- 3D 꽃 1,700개 이상을 제공합니다. 자기가 거래하는 꽃집에 견적을 요청하는 패키지가 있습니다.
- 출처: [flowerarchitect.com](https://www.flowerarchitect.com/en)

**Bridal Bouquet Builder**
- 200종 이상을 360도로 돌려 볼 수 있는 웨딩 전용 앱입니다. 가격 연동 여부는 확인하지 못했습니다.
- 출처: [사이트](https://www.bridalbouquetbuilder.com/our-build-a-bouquet-app-features)

**The Little Flower Shop(영국)**
- 단일 꽃집의 줄기당 가격 빌더입니다(예: 거베라 £3, 장미 £6). 시각화는 없습니다.
- 출처: [bouquet-builder](https://the-little-flowershop.co.uk/bouquet-builder/)

### E. 남는 재고·마감할인 직판

**국내 마감할인 플랫폼(모두 식품 대상)**
- 라스트오더(미로): "오늘 팔지 못하면 버려질 음식과 식자재"를 마감세일로 파는 앱입니다. 2020년 인터뷰 기준 입점은 무료였고 월 3만 원 유료화를 검토 중이었습니다. 최소 30% 이상 할인을 요구했고, 편의점 포함 약 1만 6,000개 점포(소상공인 6,000곳) 규모였습니다. 의류·가구·생활용품 입점 문의는 거절한다고 밝혔습니다. 꽃 언급은 없습니다. 현재 요금과 점포 수는 확인 못함. 출처: [myrocompany.com](https://www.myrocompany.com/), [인더뉴스(2020-08)](https://inthenews.co.kr/news/article.html?no=26133)
- 편의점 마감할인: CU "그린세이브"는 라스트오더 앱으로 도시락·샌드위치 등 약 10개 분류 3,000여 식음료를 최대 40% 할인해 팝니다(2020-06 시작). 세븐일레븐·GS25도 라스트오더 등으로 30% 안팎 마감할인을 한다는 보도가 있습니다(검색 요약 기준). 모두 식품입니다. 출처: [머니투데이(2020-06)](https://www.mt.co.kr/living/2020/06/22/2020062209124125173), [뉴데일리(2022)](https://biz.newdaily.co.kr/site/data/html/2022/02/22/2022022200054.html)
- 배달앱 마감할인(2026-06-15 시작): 기후에너지환경부와 배달의민족·쿠팡이츠·요기요, 전용 서비스 럭키밀·마구마켓이 "소비기한이 임박했거나 당일 판매되지 못한 식품"을 할인 판매합니다. 배민은 픽업 메뉴 안에 "마감할인"을 두고 파리바게뜨·뚜레쥬르와 일부 지역에서 시범 운영한다고 보도됐습니다(검색 요약 기준). 대상은 식품뿐이고 수수료는 기사에 없습니다. 출처: [푸드투데이(2026-06-15)](https://www.foodtoday.or.kr/news/article.html?no=205568), [네이트 뉴스(2026-06-15)](https://m.news.nate.com/view/20260615n27739)
- 럭키밀: 베이커리의 마감 임박 빵을 50% 고정 할인 "럭키백"으로 파는 앱입니다(검색 요약 기준). 수수료는 확인 못함. 출처: [뉴스피릿](https://www.newsspirit.kr/news/articleView.html?idxno=24512)
- 마감히어로: "선착순 마감되는 우리동네 할인혜택" 앱입니다. 최대 60% 할인, 매장 찜·재고 알림이 있고 카페·치킨 등 먹거리 중심입니다. 꽃은 보이지 않습니다. 앱스토어 리뷰는 5건(4.8점), 마지막 업데이트는 2025-11입니다. 출처: [App Store](https://apps.apple.com/us/app/id6670562227)
- 정리: 확인한 국내 마감할인 서비스에서 꽃·꽃집 입점 사례는 찾지 못했습니다. 다만 "방문 수령 + 마감 임박 할인"이라는 소비 습관은 정부 지원까지 받으며 자리 잡는 중입니다.

**국내 범용 채널(꽃집이 직접 할인 소식을 올릴 수 있는 곳)**
- 당근: 비즈프로필 운영자는 쿠폰을 비용 없이 만들 수 있습니다. 2022-10 기준 쿠폰 누적 다운로드 550만 건이고, 꽃집은 "생활" 업종(다운로드 비중 16%, 3위)에 묶여 있습니다. 마감할인 전용 기능은 확인 못함. 출처: [당근 보도자료(2022-10)](https://about.daangn.com/company/pr/archive/%EB%8B%B9%EA%B7%BC%EB%A7%88%EC%BC%93-%EB%8F%99%EB%84%A4-%EA%B0%80%EA%B2%8C-%EC%BF%A0%ED%8F%B0-%EB%88%84%EC%A0%81-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-550%EB%A7%8C%EA%B1%B4-%EB%8F%8C%ED%8C%8C-1%EC%9C%84%EB%8A%94-%EB%A7%9B%EC%A7%91/)
- 네이버 스마트플레이스: 사업자 앱에 "새소식 쓰기"가 있어 이벤트를 알릴 수 있습니다. 쿠폰 기능과 비용은 확인 못함. 출처: [App Store](https://apps.apple.com/app/id1521817390)
- 개별 꽃집의 인스타그램 "떨이·마감 꽃" 판매: 웹 검색으로는 구체 사례를 확인 못함(인스타그램 내부 검색이 필요합니다). 플로버스("지역사회 꽃 거래 플랫폼")는 앱스토어 페이지가 404/429로 열리지 않아 확인 못함.

**해외 남는 음식(서플러스) 앱**
- Too Good To Go(TGTG): 매장이 남는 상품을 내용물 비공개 "서프라이즈 백"으로 올리고, 소비자는 앱에서 예약·결제한 뒤 정해진 시간에 방문 수령합니다. 가격은 정가의 약 1/3입니다. 미국 기준 매장 부담은 봉투당 $1.79 + 연회비 $89(첫 $89 매출 이후 부과)로 소개됩니다(2023년 기사). 출처: [Back of House(2023-02)](https://backofhouse.io/resources/app-helping-restaurants-monetize-food-surplus-curb-food-waste-good-to-go)
- TGTG의 꽃: 매장 URL에 "flowersplants" 분류가 있고, 검색 결과에 꽃집(미니애폴리스 Gardenias Florist, 휴스턴 Floral Concepts)과 Whole Foods "Floral bag"이 나옵니다. 설명에는 제철 꽃이나 약간 흠 있는 꽃, 절정이 지난 꽃이 들어갈 수 있다고 돼 있습니다. TGTG 매장 페이지는 429 오류로 직접 열지 못해 검색 결과 요약 기준입니다. Whole Foods 꽃 봉투는 $7.99(정가 $24 상당)로 보도됐습니다. 캐나다 토론토 인근 꽃집 3곳의 꽃 봉투 구매 후기($9.99~19.99, 표시 가치 $30~60)도 확인했습니다. 출처: [TGTG Gardenias Florist](https://www.toogoodtogo.com/en-us/find/minneapolis/gardeniasflorist/flowersplants/flowerssurprisebag-238907990258476193), [TGTG Whole Foods Floral bag](https://www.toogoodtogo.com/en-us/find/newyork/wholefoods-ny/flowersplants/floralbag-181787364913550561), [Daily Dot(2026-02)](https://dailydot.com/whole-foods-flowers-for-cheap-too-good-to-go), [stenoodie 2025-08](https://stenoodie.com/2025/09/01/tgtg-surprise-bags-august-2025/), [stenoodie 2025-09](https://stenoodie.com/2025/10/01/tgtg-surprise-bags-september-2025/)
- TGTG 가격 연구: UCLA·코넬 연구진(2025)은 미국 4개 도시 자료에서 봉투 하나의 평균 한계비용($10.18~14.13)이 소비자 지불액($4.79~5.52)의 두 배를 넘는다고 추정했고, 일률적인 할인폭이 매장 참여를 막는다고 봤습니다. 출처: [UCLA Anderson Review](https://anderson-review.ucla.edu/how-to-price-soon-to-expire-food-to-attract-the-most-merchants-and-consumers)
- Flashfood: 식료품점의 임박 상품(농산물·육류·유제품·베이커리 등)을 최대 50% 할인해 파는 앱입니다. 꽃 분류는 확인되지 않았습니다. 출처: [flashfood.com](https://flashfood.com/)
- Karma, Olio, Phenix: 꽃 취급 여부와 수수료는 확인 못함(검색에서 관련 결과가 나오지 않음).
- TGTG가 한국에 진출했는지는 확인 못함.

**꽃 전용 남는 꽃·규격 외 꽃 모델**
- hanane "찬스플라워"(일본): 규격 미달(줄기 굵기·꽃 크기 등)로 버려질 꽃을 전국 농가에서 모아 1송이 100엔에 팝니다. 도쿄 도라노몬 매장에서 주 2회 "꽃 따기" 행사로 약 25종을 내놓습니다(2021년 기사). 농가 단계의 남는 꽃이고, 꽃집 재고는 아닙니다. 출처: [クウネル(2021-05)](https://kunel-salon.com/life/28788/), [食べチョク&more(2021-11)](https://andmore.tabechoku.com/lifestyle_flowerloss/)
- 카카오메이커스 "못난이 꽃"(한국, 2023-10): 꽃잎 색이 고르지 않아 경매에서 유찰돼 버려질 장미·소국 등을 선별해 팔았고, 두 차례 2,100건(약 3만 송이)이 하루 만에 완판됐습니다. 경매 단계의 남는 꽃이고 일회성 기획전입니다. 할인된 "흠 있는 꽃"에 국내 수요가 있다는 간접 증거입니다. 출처: [이데일리(2023-11)](https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=01817126635803096)
- 어니스트플라워 "파머스 초이스": 농부가 그날 상태 좋은 꽃 3종 이상을 골라 보내는 랜덤박스입니다. 농가의 출하 부담을 덜어 주는 구조이며 할인 판매는 아닙니다. 출처: [소비자평가(2019-12)](http://www.iconsumer.or.kr/news/articleView.html?idxno=10631)
- Morrisons "wonky flowers"(영국, 2018): 폭염으로 줄기가 짧게 자란 해바라기 등을 £3(일반 £5)에 팔았습니다. 슈퍼마켓이 규격 외 꽃을 할인 판매한 사례입니다. 출처: [Positive News(2018-08)](https://www.positive.news/environment/supermarkets-new-wonky-flower-range-stops-imperfect-stems-going-to-waste/)
- Freddie's Flowers(영국 구독): 주문량만큼만 들여오는 구독 방식으로 폐기 5% 미만을 목표로 한다고 자체 설명합니다. 남는 꽃을 파는 게 아니라 처음부터 남기지 않는 방식입니다. 출처: [freddiesflowers.com](https://www.freddiesflowers.com/about-us/sustainable-flower-delivery)
- 기부 모델(판매 아님): Random Acts of Flowers는 기부받은 꽃을 다시 다듬어 48시간 안에 병원 등에 전달합니다. ReBloom은 버려질 꽃을 수거해 다시 꾸며 시설에 전달한 뒤 퇴비화하고, Petal It Forward도 꽃을 나눠 주는 활동으로 소개됩니다(이 둘은 검색 요약 기준). 출처: [Random Acts of Flowers](https://randomactsofflowers.org/floral-and-vase-donations/), [Flower Power Daily](https://flowerpowerdaily.com/giving-back-some-flower-forward-ideas/)
- 꽃집 자체 할인(해외 업계 글): "Flower Happy Hour" 같은 시간대 할인과, 남는 꽃을 섞은 저가 "grab-and-go" 다발이 남는 꽃 처리 방법으로 소개됩니다. 개별 매장의 실행 규모는 확인 못함. 출처: [wholesaleflowers.net(2025-05)](https://www.wholesaleflowers.net/blogs/news/what-happens-to-unsold-flowers-at-florists-and-markets)

**꽃 폐기 규모에 대한 근거**
- 한국: 꽃집의 폐기율 통계는 확인 못함. 2025-08 경남도민일보 기사에서 꽃집 주인들은 "요즘은 파는 것보다 버리는 게 더 많다", "매입 후 2~3일 안에 팔지 못하면 폐기"라고 말했습니다(폭염기 개별 발언이며 통계는 아님). 2019년 기사에는 꽃가게가 "절반 이상을 팔지 못하고 버려야 한다"는 서술이 있지만 출처가 없습니다. 출처: [경남도민일보(2025-08)](https://www.idomin.com/news/articleView.html?idxno=943394), [소비자평가(2019-12)](http://www.iconsumer.or.kr/news/articleView.html?idxno=10631)
- 해외: "꽃집 재고의 30~40%가 버려진다"는 수치가 널리 인용되지만 1차 출처는 찾지 못했습니다. Freddie's Flowers는 "업계 평균 최대 40%"라고 쓰고, 일본 글들은 "국내 생산량의 30~40% 폐기"라고 쓰지만 둘 다 출처를 밝히지 않습니다. 참고 수준으로만 써야 합니다. 출처: [freddiesflowers.com](https://www.freddiesflowers.com/about-us/sustainable-flower-delivery), [メルシーフラワー](https://merci.co.jp/hana-casi/column/knowledge/flowerloss/), [wholesaleflowers.net](https://www.wholesaleflowers.net/blogs/news/what-happens-to-unsold-flowers-at-florists-and-markets)

**소비자 주문에 꽃집이 입찰하는 꽃 전용 서비스**
- 국내외 검색에서 확인되지 않았습니다. 숨고 같은 범용 견적 플랫폼이 이 역할을 대신하고 있습니다.

**Flowerbuyer**
- 꽃집이 도매 꽃을 사는 역더치 경매입니다. 소비자 주문에 꽃집이 입찰하는 방식은 아닙니다.
- 출처: [flowerbuyer.com](https://www.flowerbuyer.com/web/bid)

#### 참고: 꽃집 간 거래(우리는 만들지 않음)

꽃집끼리 남는 꽃을 사고팔면 유통 단계가 하나 더 생기므로 우리 제품에서는 뺐습니다. 아래는 기록용입니다.

- Florist Trader(미국): 꽃집이 남는 재고를 판매·경매하고 대형 작업을 함께 맡을 수 있습니다. 앱은 v1.0.1(2025-06)이고 평점이 표시되지 않아 초기 단계로 보입니다. 출처: [App Store](https://apps.apple.com/us/app/florist-trader/id6740991597)
- 주문 중계(와이어 서비스): FTD·Teleflora, Hana POS의 꽃집 간 주문 전송(건당 $2.99), 국내 전국플라워센터 등은 주문을 주고받는 구조입니다(상세는 A·C 참고).
- 한국의 꽃집 간 교류: 주문을 주고받는 구조(수발주)만 제도화돼 있습니다. 줄기·단 단위 재고 교환 서비스는 확인하지 못했고, 밴드·오픈채팅 같은 비공식 채널이 있을 것으로 추정됩니다.

## 4. 차별점과 위험

**차별점**
1. **공개 경락가에 연동된 줄기 단위 가격 공개.** 국내 소비자 서비스 중 도매가 근거를 보여 주는 곳은 없었습니다. aT API로 구현할 수 있습니다.
2. **3D 커스텀 주문에 꽃집 입찰 결합.** 3D 빌더는 BloomyPro·Flower Architect, 견적은 숨고에 각각 있지만 둘을 합친 사례는 확인되지 않았습니다.
3. **대체꽃 제안을 입찰과 재고에 연결한 흐름.** Floom에도 대체꽃 처리는 있지만 주문 이후의 사후 처리에 가깝습니다.
4. **남는 재고 꽃다발의 소비자 직판.** 주장할 수 있는 범위는 다음과 같습니다.
   - 확인한 국내 마감할인 서비스(라스트오더, 편의점, 배달앱 마감할인, 럭키밀·마구마켓, 마감히어로)는 모두 식품 대상이고, 꽃·꽃집 사례는 찾지 못했습니다. 국내 꽃 분야의 마감할인 전용 서비스도 찾지 못했습니다.
   - "아무도 안 한다"고 말할 수는 없습니다. 개별 꽃집의 인스타그램·당근 떨이 판매는 확인하지 못했을 뿐 있을 가능성이 높고, 해외에서는 TGTG가 이미 꽃 봉투를 팝니다.
   - TGTG와 다른 점: 재고 도구에서 남는 줄기(신선도 종료 약 2일 전 − 예약분)가 자동으로 계산되고, 내용물을 가린 봉투가 아니라 실제 꽃다발을 보여 주며, 방문 결제입니다. 이 조합은 검색 범위에서 확인되지 않았습니다.
   - 수요의 간접 증거: 카카오메이커스 못난이 꽃 약 3만 송이가 하루 만에 완판됐습니다(2023).
5. **한국어 꽃집 운영 도구.** 경매가 → 자동 소매가 → 재고 → 발주 추천 → CRM을 잇는 국내 도구는 찾지 못했습니다.

**위험·약점**
1. **양면 시장 초기 확보(콜드스타트).** 플디는 꽃집 200여 곳까지 모았지만 현재 도메인에 접속되지 않습니다. 같은 "동네 꽃집 연결" 모델의 지속 가능성에 경고가 되는 사례입니다.
2. **꽃집의 수수료 저항.**
   - 중소기업중앙회 조사에서 플랫폼 거래 비용은 월 매출의 평균 21.7%였습니다([한국일보 2026-09-15](https://www.hankookilbo.com/news/article/A2026091515550002707)).
   - 미국 주문 중계 서비스에서는 제작 꽃집이 약 70~73%만 받는다는 불만이 있습니다.
   - 숨고는 낙찰되지 않아도 견적 비용이 드는 구조입니다.
   - 입찰에 과금하면 같은 반발을 살 가능성이 큽니다.
3. **도매가 공개와 입찰에 따른 가격 하향·마진 노출.** 경락가는 도매 경매 가격이라 꽃집의 실제 매입가(중도매인 마진, 폐기 손실, 인건비)와 다릅니다. 소비자가 "원가 대비 비싸다"고 오해할 수 있습니다. 꽃집 반응은 아직 확인하지 못했고 인터뷰로 검증해야 합니다.
4. **3D 꽃 자료 제작 비용.** BloomyPro는 3,877종, Flower Architect는 1,700종 이상을 이미 갖고 있습니다. 또 화면에서 본 것과 실제 받은 꽃이 다르면 불만이 생깁니다. 꽃비가 실제 출고 사진을 내세우는 것도 이 때문입니다.
5. **기존 채널의 관성.** 네이버 예약은 현장 결제 시 수수료가 0원이고, 인스타그램 DM 주문은 무료이며, 피카플라는 회원 3,000곳을 확보했습니다. 꽃집 운영 도구만으로 전환을 끌어낼 수 있을지는 불확실합니다.
6. **할인이 정가 판매를 깎아 먹을 위험(남는 꽃 모델).** 임박 상품 할인 연구(2026-08)는 오래된 재고를 깊게 할인하면 품질을 따지던 손님까지 할인품으로 옮겨 가 정가 매출이 줄 수 있다고 봅니다. 같은 앱 안에 정가 맞춤 주문과 "남는 꽃" 탭이 함께 있으므로, 맞춤 주문 손님이 할인 탭으로 빠지는지 지켜봐야 합니다. TGTG 연구는 할인폭이 크면 매장이 봉투당 손해를 봐서 참여를 꺼린다고 추정했습니다. 꽃집의 브랜드 이미지 훼손에 대한 직접 자료는 확인 못함. 출처: [arXiv 2608.23046](https://arxiv.org/html/2608.23046), [UCLA Anderson Review](https://anderson-review.ucla.edu/how-to-price-soon-to-expire-food-to-attract-the-most-merchants-and-consumers)
7. **임박 꽃의 품질 불만.** TGTG 꽃집 봉투 후기에는 "이틀 만에 시들었다"며 환불받은 사례, "생각보다 빨리 시들었다", "봉투마다 품질이 들쭉날쭉하다"는 평이 있습니다. Whole Foods 꽃 봉투도 "조금 거칠 수 있다"는 전제로 소개됩니다. 남은 관상 기간을 미리 알리지 않으면 후기 점수가 꽃집 프로필 전체에 영향을 줄 수 있습니다. 출처: [stenoodie 2025-09](https://stenoodie.com/2025/10/01/tgtg-surprise-bags-september-2025/), [stenoodie 2025-08](https://stenoodie.com/2025/09/01/tgtg-surprise-bags-august-2025/), [Daily Dot](https://dailydot.com/whole-foods-flowers-for-cheap-too-good-to-go)
8. **표시·환불 규정.** 전자상거래법상 "시간이 지나 다시 판매하기 곤란할 정도로 가치가 떨어진" 물건은 청약철회가 제한되지만, 사업자는 그 사실을 소비자가 알기 쉬운 곳에 분명히 표시해야 합니다. 물건이 표시·광고와 다르면 받은 날부터 3개월(안 날부터 30일) 안에 철회할 수 있습니다. 따라서 "남는 꽃"의 상태·예상 관상 기간·환불 불가 조건을 화면에 적는 편이 안전합니다. 방문 결제(앱에서는 예약만) 방식에 이 법이 그대로 적용되는지와, 생화의 임박 상태 표시를 직접 정한 규정은 확인 못함(법률 검토 필요). 출처: [찾기쉬운 생활법령정보](https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=835&ccfNo=4&cciNo=1&cnpClsNo=2)
9. **공급이 적고 들쭉날쭉해 "남는 꽃" 탭이 비어 보일 위험.** 남는 재고는 꽃집이 발주를 잘할수록 줄어듭니다. 우리 발주 메모 기능이 남는 꽃 공급을 스스로 줄이는 구조입니다. TGTG 후기에도 "꽃 봉투가 꾸준히 올라오지 않는다"는 불만이 있습니다. 초기에 꽃집 수가 적으면 탭이 자주 빌 수 있으므로, 찜한 꽃집의 재고 알림(마감히어로 방식)이나 빈 화면 대체 안내가 필요합니다. 국내 꽃집 한 곳의 하루 남는 꽃 양은 확인 못함(인터뷰 필요). 출처: [stenoodie 2025-08](https://stenoodie.com/2025/09/01/tgtg-surprise-bags-august-2025/), [마감히어로 App Store](https://apps.apple.com/us/app/id6670562227)
10. **마감할인 대형 플랫폼의 확장 가능성.** 배민·쿠팡이츠·요기요가 2026-06부터 정부와 함께 마감할인을 시작했습니다. 지금은 식품만이지만 비식품으로 넓힐 경우 트래픽에서 밀립니다. 확장 계획은 확인 못함. 출처: [푸드투데이(2026-06-15)](https://www.foodtoday.or.kr/news/article.html?no=205568)

## 5. 확인 못한 것 / 추가 조사 필요

- 플디가 실제로 종료했는지와 그 사유. 플로버스("지역사회 꽃 거래 플랫폼", 앱스토어 404/429)의 현황과 기능.
- 국내 꽃배달 체인·수발주 본부의 실제 수수료율. "30%"는 플디 대표의 발언이 유일한 근거입니다.
- 카카오 선물하기 꽃 카테고리 수수료와 꾸까의 현재 상품 구성(kukka.kr 접속 오류).
- 숨고 플라워 카테고리의 실제 견적 발송 단가와 꽃집들의 이용 규모.
- aT 오픈API의 상업적 이용 약관, 양재 외 공판장 포함 범위, 데이터 지연 시간.
- BloomyPro·Flower Architect의 요금과 한국 품종 포함 여부. Floom 25%와 BloomNation 요율의 1차 출처.
- 한국 꽃집 POS·ERP가 있는지(검색에서는 발견하지 못함).
- 멘코넷, 어니스트플라워 B2B 서비스의 상세 내용.
- (남는 꽃) 국내 꽃집의 실제 폐기율과 하루 남는 꽃 양. 공식 통계를 찾지 못했습니다. 꽃집 인터뷰가 필요합니다.
- (남는 꽃) 개별 꽃집의 인스타그램·당근 떨이 판매가 얼마나 흔한지, 할인폭은 어느 정도인지. 인스타그램 내부 검색이 필요합니다.
- (남는 꽃) 라스트오더·럭키밀·마구마켓·배달앱 마감할인의 현재 수수료와 비식품 확장 계획. 라스트오더의 최근 점포 수.
- (남는 꽃) TGTG 매장 페이지 원문(429 오류), TGTG의 국가별 수수료, 꽃집 입점 수, 한국 진출 여부. Karma·Olio·Phenix의 꽃 취급 여부.
- (남는 꽃) "꽃집 재고의 30~40% 폐기" 수치의 1차 출처.
- (남는 꽃) 예약 후 방문 결제 방식에 전자상거래법이 적용되는 범위, 생화 상태 표시에 관한 규정, 꽃 관련 소비자 피해 통계(한국소비자원).
- (남는 꽃) 할인 판매가 꽃집 브랜드와 정가 매출에 주는 영향에 대한 꽃 업종 직접 자료.
- 참고: 꽃집 간 비공식 재고 거래(밴드·오픈채팅)의 규모. 우리는 만들지 않으므로 우선순위는 낮습니다.

## 6. 전체 출처 목록

- https://platum.kr/archives/143045
- https://www.goodkyung.com/news/articleView.html?idxno=288067
- https://kukka.kr/subscription/
- https://www.fnnews.com/news/202104261756577946
- https://pik-a-fla.com/faq/?next=/
- https://www.rocketpunch.com/companies/honestflower
- https://www.venturesquare.net/796180
- https://honestflower.kr/
- https://1moment.co.kr/
- https://www.rda.go.kr/webzine/2020/03/sub1-3-2.html
- https://snowfoxflowers.com/
- https://www.f-mans.com/
- https://theflowercenter.co.kr/
- https://www.ozflowerchain.co.kr/
- https://apps.apple.com/us/app/id1543120768
- https://apps.apple.com/kr/app/id1559151444
- https://www.sedaily.com/NewsView/1Z7R1SL0HB
- https://www.segye.com/newsView/20201225503307
- https://news.sbs.co.kr/news/endPage.do?news_id=N1007318789
- https://github.com/FlowerLikeU-STUDIO/flower_like_u
- https://soomgo.com/prices/%ED%94%8C%EB%9D%BC%EC%9B%8C-%EC%A0%9C%EC%9E%91
- https://help.soomgo.com/hc/ko/articles/360044939772
- https://afterwork30.com/reviews/soomgo-pro-cost-structure
- https://support.kmong.com/hc/ko/articles/36616106488729
- https://geteverpick.com/ko/side-income/kmong-side-income-fees
- https://www.omago.ai/ko/blog/naver-booking-fees-truth-korea
- https://business.daangn.com/business-profile/about
- https://flower.at.or.kr/api/apiOpenInfo.do
- https://flower.at.or.kr/yfmc/front/stat/aucPrice.do?menuId=23
- https://www.data.go.kr/data/15052544/fileData.do
- https://play.google.com/store/apps/details?id=kr.pandoroots.flowerauctionprice
- https://thevc.kr/okkot/products
- https://floranext.com/florist-pos/
- https://floranext.com/what-is-flower-wire-service/
- https://www.hanafloristpos.com/
- https://www.hanafloristpos.com/blog/what-are-floral-wire-service/
- https://info.detailsflowers.com/features
- https://www.getapp.com/retail-consumer-services-software/a/details-flowers-software/
- https://www.everystem.com/
- https://en.wikipedia.org/wiki/BloomNation
- https://pricingnow.com/question/bloomnation-pricing/
- https://www.floom.com/gb/pages/partner-with-floom
- https://help.floomx.com/hc/en-us/articles/12312488338321
- https://www.lovinglyflorists.com/
- https://bloomypro.com/
- https://www.floraldaily.com/article/9284541/bloomy-pro-launches-online-bouquet-maker-for-consumer-use/
- https://thursd.com/articles/go-virtual-with-bloomypro
- https://www.flowerarchitect.com/en
- https://www.bridalbouquetbuilder.com/our-build-a-bouquet-app-features
- https://the-little-flowershop.co.uk/bouquet-builder/
- https://apps.apple.com/us/app/florist-trader/id6740991597
- https://www.flowerbuyer.com/web/bid
- https://www.hankookilbo.com/news/article/A2026091515550002707
- https://www.myrocompany.com/
- https://inthenews.co.kr/news/article.html?no=26133
- https://www.mt.co.kr/living/2020/06/22/2020062209124125173
- https://biz.newdaily.co.kr/site/data/html/2022/02/22/2022022200054.html
- https://www.foodtoday.or.kr/news/article.html?no=205568
- https://m.news.nate.com/view/20260615n27739
- https://www.newsspirit.kr/news/articleView.html?idxno=24512
- https://apps.apple.com/us/app/id6670562227
- https://about.daangn.com/company/pr/archive/%EB%8B%B9%EA%B7%BC%EB%A7%88%EC%BC%93-%EB%8F%99%EB%84%A4-%EA%B0%80%EA%B2%8C-%EC%BF%A0%ED%8F%B0-%EB%88%84%EC%A0%81-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-550%EB%A7%8C%EA%B1%B4-%EB%8F%8C%ED%8C%8C-1%EC%9C%84%EB%8A%94-%EB%A7%9B%EC%A7%91/
- https://apps.apple.com/app/id1521817390
- https://backofhouse.io/resources/app-helping-restaurants-monetize-food-surplus-curb-food-waste-good-to-go
- https://www.toogoodtogo.com/en-us/find/minneapolis/gardeniasflorist/flowersplants/flowerssurprisebag-238907990258476193
- https://www.toogoodtogo.com/en-us/find/houston/floralconcepts/flowersplants/surprisebag-215972351844967745
- https://www.toogoodtogo.com/en-us/find/newyork/wholefoods-ny/flowersplants/floralbag-181787364913550561
- https://dailydot.com/whole-foods-flowers-for-cheap-too-good-to-go
- https://stenoodie.com/2025/09/01/tgtg-surprise-bags-august-2025/
- https://stenoodie.com/2025/10/01/tgtg-surprise-bags-september-2025/
- https://anderson-review.ucla.edu/how-to-price-soon-to-expire-food-to-attract-the-most-merchants-and-consumers
- https://flashfood.com/
- https://kunel-salon.com/life/28788/
- https://andmore.tabechoku.com/lifestyle_flowerloss/
- https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=01817126635803096
- http://www.iconsumer.or.kr/news/articleView.html?idxno=10631
- https://www.positive.news/environment/supermarkets-new-wonky-flower-range-stops-imperfect-stems-going-to-waste/
- https://www.freddiesflowers.com/about-us/sustainable-flower-delivery
- https://randomactsofflowers.org/floral-and-vase-donations/
- https://flowerpowerdaily.com/giving-back-some-flower-forward-ideas/
- https://www.wholesaleflowers.net/blogs/news/what-happens-to-unsold-flowers-at-florists-and-markets
- https://www.idomin.com/news/articleView.html?idxno=943394
- https://merci.co.jp/hana-casi/column/knowledge/flowerloss/
- https://arxiv.org/html/2608.23046
- https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=835&ccfNo=4&cciNo=1&cnpClsNo=2
