---
title: 카파시 LLM Wiki 세컨드 브레인 구축 가이드
type: source
tags: [구축참고자료, LLM-Wiki, 세컨드브레인, 옵시디언, graphify, 스킬]
created: 2026-04-20
updated: 2026-04-20
sources: [raw/books/2026-04-20_카파시-LLM-Wiki-세컨드브레인-가이드.md]
---

# 카파시 LLM Wiki 세컨드 브레인 구축 가이드

> 원본: `raw/books/2026-04-20_카파시-LLM-Wiki-세컨드브레인-가이드.md`
> 목적: 다른 AI 에이전트에게 옵시디언 + LLM Wiki 틀을 잡아줄 때 이 가이드를 기준으로 사용

---

## 핵심 개념

**RAG vs LLM Wiki:**
- RAG: 매번 검색해서 답을 만든다
- LLM Wiki: 지식이 쌓여서 답이 더 좋아진다 → 개인 지식관리는 축적이 핵심

**Gold In, Gold Out:** 목적 없이 수집하면 쓰레기 데이터. 목적 있게 수집해야 골드 데이터.

---

## 7단계 전체 흐름

| 단계 | 작업 | 결과물 |
|------|------|--------|
| Step 1 | 맥락 인터뷰 (숙제 3가지) | 나의 핵심 맥락.md |
| Step 2 | CLAUDE.md 생성 | AI가 읽는 나의 설명서 |
| Step 3 | LLM Wiki 세팅 | raw/ + wiki/ + Output/ 폴더 구조 |
| Step 4 | 웹 클리퍼 템플릿 | 수집 자동화 JSON 5종 |
| Step 5 | 인제스트 | raw/ → wiki/ 소화 |
| Step 6 | 스킬 만들기 | /ingest, /query, /lint |
| Step 7 | Graphify | 지식 그래프 + 시각화 |

---

## 단계별 핵심 프롬프트

### Step 1 — 맥락 인터뷰
AI가 한 번에 하나씩 3가지 질문:
1. 나는 누구인가 (역할, 강점, 가치관)
2. 왜 기록하고 싶은가 (지금 안 되는 것, 비전)
3. 어떤 아웃풋을 만들고 싶은가 (대상, 형태, 1년 후)
→ STT(음성 입력)로 편하게 답해도 됨

### Step 2 — CLAUDE.md 섹션 구성
1. 나는 누구인가
2. 나의 역할들
3. 나의 비전과 목표
4. AI에게 기대하는 것
5. 작업 규칙

### Step 3 — 폴더 구조
```
볼트/
├── CLAUDE.md
├── raw/
│   ├── articles/ | videos/ | podcasts/ | books/
│   └── CLAUDE.md
├── wiki/
│   ├── index.md | log.md
│   └── CLAUDE.md
└── Output/
    └── CLAUDE.md
```

### Step 4 — 웹 클리퍼 템플릿 5종
Article / YouTube / Podcast / Book / Research
→ 각각 raw/ 하위 폴더에 자동 저장되도록 설정

### Step 5 — 인제스트 프롬프트 2종
- **대화형:** raw/ 파일 읽기 → 소스 요약 → 왜 캡처했는지 질문 → wiki/ 반영
- **빠른:** raw/ 전체 스캔 → 대화 없이 바로 처리

### Step 6 — 스킬 위치
`.claude/skills/<스킬명>/SKILL.md`
- `/ingest` — raw/ 스캔 → wiki/ 정리
- `/query` — wiki/ 기반 질의
- `/lint` — 위키 점검 및 수정

### Step 7 — Graphify 실행 순서
```bash
pip install graphifyy
graphify update .        # 코드 파일 그래프 빌드
graphify claude install  # Claude Code에 통합
```

---

## Karpathy 10대 규칙 (아마테라스 위키에 이미 적용됨)

1. raw/ 수정 절대 금지
2. 페이지 생성/삭제 시 index.md 업데이트
3. 모든 작업 후 log.md 기록
4. 내부 참조는 `[[wikilink]]`
5. 모든 페이지에 YAML frontmatter
6. 모순 발견 시 양쪽 소스 인용
7. 소스 요약은 사실만, 해석은 concept/ 페이지에
8. 질의 시 index.md 먼저, raw/는 최후 수단
9. 새 페이지보다 기존 페이지 업데이트 우선
10. index 항목은 한 줄, 120자 이내

---

## 아마테라스에 적용 현황

| 항목 | 상태 |
|------|------|
| Step 1 맥락 인터뷰 | ✓ IDENTITY.md, SOUL.md로 구현 |
| Step 2 CLAUDE.md | ✓ 각 폴더별 CLAUDE.md 완비 |
| Step 3 LLM Wiki 세팅 | ✓ raw/ wiki/ Output/ 구조 완성 |
| Step 4 웹 클리퍼 템플릿 | ✓ 5종 JSON 생성됨 |
| Step 5 인제스트 | ✓ /ingest 스킬로 자동화 |
| Step 6 스킬 | ✓ /ingest /query /lint /graphify 완성 |
| Step 7 Graphify | ✓ 설치 완료, tools/ 코드 그래프 빌드됨 |

---

## 다른 AI 에이전트 세팅 시 순서

새 에이전트(RealBlack, Level.1 등) 폴더를 세팅할 때:
1. 이 가이드의 Step 1~3 프롬프트를 순서대로 실행
2. 에이전트 목적에 맞는 raw/ 하위 폴더 구성
3. `.claude/skills/` 에 /ingest /query /lint 스킬 복사
4. `graphify claude install` 실행

## 관련 페이지
- [[amateras]] — 아마테라스 현재 적용 현황
- [[proposition-t-site]] — 웹 클리퍼 활용 예시
