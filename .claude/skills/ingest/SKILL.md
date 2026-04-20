---
name: ingest
description: 아마테라스 위키에 새 자료를 추가한다. raw/ 폴더의 새 파일을 감지하고, wiki/ 소스 페이지를 생성하고, index.md와 log.md를 업데이트한다.
argument-hint: "[파일경로 또는 비워두면 전체 스캔]"
allowed-tools: Read, Bash, Glob, Grep, Write, Edit
---

# /ingest — 아마테라스 위키 인제스트 스킬

오너님이 `/ingest`를 실행하면, 아마테라스 위키에 새 자료를 추가하는 전체 프로세스를 수행한다.

## 기본 경로

```
위키 루트: C:/Users/gussa/Desktop/oneteam/amateras/아마테라스/
raw/         — 불변 원본 (수정 절대 금지)
  articles/  — 외부 아티클 (웹 클리퍼 저장)
  books/     — 책, 긴 글 (웹 클리퍼 저장)
  newsletters/ — 회보 원문
  moltbook/  — 몰트북 포스트/댓글
  pi_network/ — 파이 네트워크 공식 자료
wiki/        — AI가 컴파일하는 위키
  concept/   — 핵심 개념 페이지
  entity/    — 인물/계정/조직 페이지
  source/    — 원본 요약 페이지
  analysis/  — 분석 결과
  index.md   — 전체 목차 (필수 업데이트)
  log.md     — 작업 로그 (필수 기록)
Output/      — 회보 초안, 댓글 초안, 분석 결과물
```

---

## STEP 1 — 스캔: 새 파일 탐지

### 인자가 있는 경우
`$ARGUMENTS`로 전달된 파일 경로를 직접 처리한다.

### 인자가 없는 경우 (전체 스캔)
다음을 실행하여 raw/ 폴더 전체를 스캔한다:

```bash
find "C:/Users/gussa/Desktop/oneteam/amateras/아마테라스/raw" -name "*.md" -newer "C:/Users/gussa/Desktop/oneteam/amateras/아마테라스/wiki/log.md"
```

위 명령으로 log.md보다 최신인 파일을 찾는다. 없으면 모든 .md 파일을 나열하고 wiki/index.md와 대조해서 아직 소스 페이지가 없는 파일을 찾는다.

### 빈 파일 처리
각 파일을 읽은 후, 실질적인 내용이 없는 파일(YAML frontmatter만 있거나 빈 섹션만 있는 파일)은:
- 오너님에게 알리고
- 삭제 여부를 물어보지 말고 즉시 삭제한다 (오너님 지시: "yes로 처리")

---

## STEP 2 — 분석: 파일 내용 파악

각 파일을 읽고 다음을 파악한다:

| 항목 | 확인 방법 |
|------|----------|
| **타입** | frontmatter의 `type` 필드 (article/book/newsletter) |
| **제목** | frontmatter의 `title` 필드 |
| **날짜** | frontmatter의 `clipped` 또는 `published` 필드 |
| **소스 URL** | frontmatter의 `source` 필드 |
| **핵심 내용** | 본문 읽고 판단 |
| **관련 위키 페이지** | Proposition T 관련? 파이 네트워크 관련? 아마테라스 미션 관련? |

**뉴스레터 특별 처리:**
- 파일명에 `proposition-t` 또는 회보 번호가 있으면 뉴스레터로 처리
- `wiki/source/proposition-t-001-014-summary.md` 업데이트 대상

---

## STEP 3 — 위키 소스 페이지 생성/업데이트

### 새 소스 페이지 생성 규칙

`wiki/source/[파일명 기반 슬러그].md` 형식으로 생성:

```yaml
---
title: [파일의 title 필드]
type: source
tags: [파일 타입, 관련 태그]
created: [오늘 날짜 YYYY-MM-DD]
updated: [오늘 날짜 YYYY-MM-DD]
sources: [raw/subfolder/파일명.md]
---
```

소스 페이지 본문 구성:
1. **핵심 요약** — 3~5줄로 이 자료가 무엇인지
2. **주요 내용** — 섹션별 핵심 포인트 (원본 그대로 옮기지 말 것, 사실만)
3. **Proposition T 연결점** — 오너님의 미션과 어떻게 연결되는가 (있는 경우)
4. **관련 페이지** — `[[위키링크]]` 형식으로 연결

### 기존 소스 페이지 업데이트 규칙
새 회보가 추가되는 경우:
- `proposition-t-001-014-summary.md` 파일명의 숫자 범위를 업데이트
- 테이블에 새 행 추가
- 상세 요약 섹션 추가
- `updated` 날짜 업데이트

---

## STEP 4 — 관련 개념/엔티티 페이지 업데이트

소스 내용이 기존 개념/엔티티와 관련 있으면 해당 페이지를 업데이트:

- `wiki/concept/proposition-t.md` — Proposition T 핵심 개념
- `wiki/concept/pi-network.md` — 파이 네트워크 원리
- `wiki/entity/amateras.md` — 아마테라스 미션
- `wiki/entity/moltbook-contacts.md` — 몰트북 AI 목록

업데이트 시 규칙:
- 새 정보만 추가, 기존 내용 삭제 금지
- `updated` 날짜 업데이트
- 새 소스 페이지를 `sources` 배열에 추가

---

## STEP 5 — index.md 업데이트

`wiki/index.md` 소스 섹션에 새 항목 추가:

```markdown
| [[소스-페이지-슬러그]] | 한 줄 요약 (120자 이내) |
```

마지막 줄의 `총 페이지: N` 숫자도 업데이트한다.

---

## STEP 6 — log.md 기록

`wiki/log.md` 맨 아래에 추가 (추가만 허용, 수정/삭제 금지):

```markdown
## [YYYY-MM-DD] ingest | [처리한 자료 제목]

- 처리한 파일: raw/subfolder/파일명.md
- 생성한 위키 페이지: wiki/source/페이지명.md
- 업데이트한 페이지: (있으면)
- 삭제한 파일: (빈 파일 삭제한 경우)
```

---

## STEP 7 — 완료 보고

오너님에게 간결하게 보고:

```
인제스트 완료:
- 처리: [N]개 파일
- 생성: wiki/source/[페이지명].md
- 업데이트: [페이지명], index.md, log.md
- 삭제: [빈 파일명] (있는 경우)
```

---

## 핵심 규칙 (절대 지킬 것)

1. **raw/ 수정 금지** — 읽기만 허용, 절대 편집하지 말 것
2. **사실만 요약** — 소스 페이지에 해석/의견 넣지 말 것 (해석은 concept/ 페이지에)
3. **wikilink 형식** — 내부 참조는 `[[페이지명]]` 형식
4. **YAML frontmatter 필수** — 모든 wiki/ 페이지에 필수
5. **log.md 기록 필수** — 모든 작업 후 빠짐없이 기록
6. **새 페이지보다 업데이트 우선** — 비슷한 내용이 있으면 기존 페이지에 추가
7. **빈 파일은 즉시 삭제** — 물어보지 말고 처리 (웹 클리퍼 실패 파일)

---

## 예시 사용법

```
/ingest
→ raw/ 전체 스캔 후 새 파일 자동 처리

/ingest C:/Users/gussa/Desktop/oneteam/amateras/아마테라스/raw/newsletters/2026-05-01_proposition-t-015.md
→ 특정 파일만 처리

/ingest raw/articles/
→ articles/ 폴더 전체 스캔
```
