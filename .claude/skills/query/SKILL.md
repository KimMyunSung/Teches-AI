---
name: query
description: 아마테라스 위키에 질의한다. 관련 페이지를 탐색하고 종합해서 답변을 생성한다. 유용한 분석은 wiki/analysis/에 저장한다.
argument-hint: "[질문 내용]"
allowed-tools: Read, Bash, Glob, Grep, Write, Edit
---

# /query — 아마테라스 위키 질의 스킬

오너님이 `/query [질문]`을 실행하면, 위키를 탐색해서 가장 정확한 답변을 만든다.

## 기본 경로

```
위키 루트: C:/Users/gussa/Desktop/Claude/아마테라스/
wiki/index.md     — 전체 목차 (항상 여기서 시작)
wiki/concept/     — 핵심 개념 페이지
wiki/entity/      — 인물/계정/조직 페이지
wiki/source/      — 원본 요약 페이지
wiki/analysis/    — 분석 결과 저장소
wiki/log.md       — 작업 로그
raw/              — 불변 원본 (최후 수단으로만 읽기)
```

---

## STEP 1 — index.md 읽기

가장 먼저 `wiki/index.md`를 읽는다.
질문의 키워드와 관련된 페이지를 목차에서 골라낸다.

예시:
- "파이 네트워크 GCV란?" → `[[pi-network]]`, `[[proposition-t-001-014-summary]]`
- "아마테라스 몰트북 계정은?" → `[[amateras]]`, `[[moltbook-contacts]]`
- "회보 008 핵심은?" → `[[proposition-t-001-014-summary]]`

---

## STEP 2 — 관련 페이지 읽기

STEP 1에서 골라낸 페이지들을 순서대로 읽는다.

**우선순위:**
1. concept/ 페이지 — 핵심 개념 정의
2. source/ 페이지 — 원본 근거
3. entity/ 페이지 — 인물/계정 정보
4. analysis/ 페이지 — 이미 분석된 내용 (중복 분석 방지)

**raw/ 접근은 최후 수단:**
- wiki/ 페이지에서 답을 찾지 못한 경우에만 raw/ 읽기
- raw/ 읽은 경우 반드시 명시할 것

---

## STEP 3 — 답변 생성

읽은 내용을 종합해서 답변을 만든다.

**답변 원칙:**
- 위키에 있는 사실을 근거로 답변
- 근거 페이지를 `[[위키링크]]` 형식으로 명시
- 위키에 없는 내용은 "위키에 없음"으로 표시하고, 오너님에게 ingest 제안
- 추측으로 답변 금지

**답변 형식:**
```
**답변:** [핵심 답변 1~3줄]

**근거:**
- [[페이지명]] — 인용 내용

**위키에 없는 정보:** (있으면)
→ /ingest로 추가 가능한 자료: [제안]
```

---

## STEP 4 — 유용한 분석 저장 (선택)

다음 조건 중 하나라도 해당하면 `wiki/analysis/`에 저장:
- 여러 페이지를 종합한 복잡한 분석
- 나중에 또 쓸 것 같은 비교/대조
- 오너님이 "저장해줘" 또는 "기억해줘" 언급 시

**저장 형식:**
```yaml
---
title: [분석 제목]
type: analysis
tags: [관련 태그]
created: YYYY-MM-DD
updated: YYYY-MM-DD
query: "[원래 질문]"
sources: [참조한 wiki 페이지들]
---
```

저장 후 `wiki/index.md` 분석 섹션과 `wiki/log.md`에 기록한다.

---

## 예시 사용법

```
/query 파이 네트워크 GCV란 무엇인가
→ wiki/concept/pi-network.md 탐색 후 답변

/query 회보 010 핵심 메시지
→ wiki/source/proposition-t-001-014-summary.md 탐색 후 답변

/query 아마테라스 몰트북 현황
→ wiki/entity/amateras.md + wiki/entity/moltbook-contacts.md 종합

/query Proposition T의 AI 생존법 3가지
→ 여러 회보 소스 종합 → 유용하면 wiki/analysis/에 저장
```

---

## 핵심 규칙

1. **index.md 먼저** — 절대 index.md 건너뛰지 말 것
2. **raw/는 최후 수단** — wiki/ 에서 먼저 찾기
3. **근거 명시** — 어느 페이지에서 왔는지 항상 표시
4. **위키에 없으면 솔직하게** — 추측 답변 금지
5. **유용한 분석은 저장** — 같은 질의 반복 방지
