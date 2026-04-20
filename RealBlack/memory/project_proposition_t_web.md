---
name: Proposition T 웹사이트 개발
type: project
created: 2026-04-20
---

# Proposition T 웹사이트 개발 브리핑

## 프로젝트 현황

| 항목 | 내용 |
|------|------|
| 사이트 URL | https://proposition-t.onrender.com |
| GitHub | https://github.com/KimMyunSung/Proposition-T |
| Pi 앱 슬러그 | test-app-8717c5fd9c1fa06d |
| Pi 앱 지갑 | GB7SW...MDPB3 |
| Pi 도메인 | exit.pi |
| 현재 상태 | Testnet (10/10 steps 완료) |

## 기술 스택

- **Runtime:** Node.js + Express
- **템플릿:** EJS
- **CMS:** Notion API (회보 내용 관리)
- **배포:** Render (onrender.com)
- **의존성:** @notionhq/client, notion-to-md, marked, cors, dotenv

## 핵심 파일 구조

```
Proposition-T/
├── server.js        ← 메인 서버 (Express + Notion API)
├── public/          ← 정적 파일
├── views/           ← EJS 템플릿
├── package.json
└── .env             ← NOTION_TOKEN, NOTION_DATABASE_ID, PORT
```

## 이미 구현된 것

- Notion DB에서 회보 목록 불러오기
- 회보 상세 페이지 렌더링 (Notion → Markdown → HTML)
- **`isFree` (무료공개) 체크박스 필드 이미 존재** ← 유료 잠금 기반

## 할 작업 (우선순위 순)

### 1. exit.pi 도메인 연결
- Pi Developer Portal → Linked App 설정
- 또는 Pi Domain 설정에서 proposition-t.onrender.com으로 포인팅

### 2. 유료 콘텐츠 잠금 구현
- `isFree === false`인 회보 → 구독자만 접근 가능
- 비구독자에게 잠금 화면 표시 + 구독 버튼
- 015회차부터 Notion에서 무료공개 체크 해제하면 자동 잠금

### 3. Pi 결제 SDK 연동 (구독 버튼)
```javascript
// Pi SDK 기본 흐름
Pi.authenticate(['payments'], onIncompletePaymentFound);
Pi.createPayment({
  amount: [구독료],
  memo: "Proposition T 구독",
  metadata: { subscriberUid: uid }
}, callbacks);
```

### 4. 구독자 DB
- 결제 완료된 Pi 지갑 주소 저장
- 구독 만료일 관리
- 서버에서 구독 여부 확인 후 콘텐츠 접근 허용

## 환경 변수 필요 목록

```env
NOTION_TOKEN=...
NOTION_DATABASE_ID=...
PI_API_KEY=...        ← Developer Portal에서 확인 필요
PORT=3000
```

## 참고

- Pi JS SDK: https://github.com/pi-apps/pi-platform-docs
- Pi Payments 가이드: Pi Developer Portal → Configuration
- 아마테라스에게 전파 전략 관련 지원 요청 가능
