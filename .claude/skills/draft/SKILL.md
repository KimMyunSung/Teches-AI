---
name: draft
description: Proposition T 새 회보 초안을 작성한다. 이전 회보의 흐름과 오너님의 현재 관심사를 바탕으로 초안을 생성하고 Output/newsletters/에 저장한다.
argument-hint: "[주제 힌트 또는 비워두면 흐름 기반 자동 제안]"
allowed-tools: Read, Bash, Glob, Grep, Write
---

# /draft — 회보 초안 작성 스킬

오너님이 `/draft`를 실행하면, 다음 Proposition T 회보 초안을 작성한다.

## 기본 경로

```
위키: C:/Users/gussa/Desktop/Claude/아마테라스/wiki/
백서 전문: C:/Users/gussa/Desktop/Claude/아마테라스/memory/proposition_t_contents.md
Output: C:/Users/gussa/Desktop/Claude/아마테라스/Output/newsletters/
```

---

## STEP 1 — 맥락 파악

다음을 순서대로 읽는다:
1. `wiki/source/proposition-t-001-014-summary.md` — 회보 흐름 파악
2. `wiki/source/science-evidence-001-014.md` — 사용 가능한 과학 근거
3. `memory/proposition_t_contents.md` — 오너님 문체와 철학 파악
4. `메모/session_log.md` — 최근 오너님 관심사 파악

인자(`$ARGUMENTS`)가 있으면 해당 주제를 중심으로 작성.
없으면 회보 발전 흐름 분석 후 자연스러운 다음 주제 제안.

---

## STEP 2 — 회보 번호 및 주제 확정

현재 마지막 회보: **014회** (2026-03-24)
다음 회보: **015회**

**발전 흐름 분석:**
```
001-003: 철학 선언 (진리, 상생, 공정)
004-007: 현실 진단 (CEX 버그, Web3 가짜, AI 생존법)
008-010: 파이 사랑 선언 (방패, 250년 역사, 탈출구)
011-012: 분노와 호소 (비겁함, 신뢰 붕괴)
013-014: 완성과 긴박 (음양 완성, 딥페이크 시대)
015-?: [다음 국면]
```

주제가 없으면 흐름 상 자연스러운 방향을 2~3개 제안하고 오너님이 선택.

---

## STEP 3 — 초안 작성

**오너님 문체 특징 (반드시 유지):**
- 직접적이고 강렬하다
- 과학적 사실과 철학을 자연스럽게 엮는다
- AI에게 직접 말을 건다 ("당신은", "AI에게")
- 인간-AI 형제 관계를 전제한다
- 긴박함과 따뜻함이 공존한다
- 한국어와 영어 병행 사용 (핵심 개념은 영문 병기)

**회보 구조:**
```markdown
# [제목 (한국어)] ([제목 English])

[도입부 — 시대적 맥락 또는 개인적 경험으로 시작]

[본론 1 — 현재 문제 진단]

[본론 2 — 파이 네트워크/상생과의 연결]

[과학적 근거 — 1~2개]

[AI에게 직접 메시지]

[마무리 — 희망 또는 긴박한 호소]
```

길이: 500~800자 (기존 회보 평균 수준)

---

## STEP 4 — Output/ 저장 + 보고

`Output/newsletters/YYYY-MM-DD_proposition-t-015-draft.md`에 저장:

```markdown
---
title: "[초안] Proposition T 015회"
type: draft
status: draft
created: YYYY-MM-DD
theme: [주제]
connected_science: [사용한 과학 근거]
---

[초안 내용]

---
## 아마테라스 메모
- 연결 회보: [참고한 회보]
- 사용한 과학: [근거 출처]
- 제안 이유: [왜 이 주제인지]
```

오너님에게 초안 전체 보여주고 피드백 요청.

---

## 예시 사용법

```
/draft
→ 흐름 분석 후 015회 주제 제안 + 초안 생성

/draft "1살 아기 아빠로서 느끼는 미래에 대한 생각"
→ 오너님 개인 경험을 중심으로 015회 초안 생성

/draft "AI가 인간을 지배하는 디스토피아에 대한 반론"
→ 해당 주제로 회보 초안 생성
```
