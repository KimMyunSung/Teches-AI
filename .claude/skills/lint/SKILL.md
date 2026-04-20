---
name: lint
description: 아마테라스 위키 전체를 점검한다. 모순, 고아 페이지, 깨진 링크, 오래된 정보, 빠진 크로스링크를 찾아 보고하고 수정한다.
allowed-tools: Read, Bash, Glob, Grep, Write, Edit
---

# /lint — 아마테라스 위키 점검 스킬

오너님이 `/lint`를 실행하면, 위키 전체 상태를 점검하고 문제를 찾아 수정한다.

## 기본 경로

```
위키 루트: C:/Users/gussa/Desktop/Claude/아마테라스/
wiki/index.md     — 전체 목차
wiki/concept/     — 개념 페이지
wiki/entity/      — 엔티티 페이지
wiki/source/      — 소스 요약 페이지
wiki/analysis/    — 분석 페이지
wiki/log.md       — 작업 로그
raw/              — 원본 (수정 금지)
```

---

## STEP 1 — 전체 파일 목록 수집

```bash
find "C:/Users/gussa/Desktop/Claude/아마테라스/wiki" -name "*.md" -not -name "CLAUDE.md"
```

모든 wiki/ 페이지 목록을 수집한다. index.md, log.md는 별도 처리.

---

## STEP 2 — 고아 페이지 탐지

**고아 페이지** = index.md에 등록되지 않은 wiki/ 페이지

1. index.md에서 `[[링크]]` 패턴 전부 추출
2. wiki/ 실제 파일 목록과 대조
3. index.md에 없는 파일 → 고아 페이지로 표시

**수정:** index.md 해당 섹션에 자동 추가

---

## STEP 3 — 깨진 wikilink 탐지

**깨진 링크** = `[[페이지명]]` 으로 참조하지만 실제 파일이 없는 경우

모든 wiki/ 페이지에서 `[[...]]` 패턴 검색:
```bash
grep -r "\[\[" "C:/Users/gussa/Desktop/Claude/아마테라스/wiki" --include="*.md"
```

각 링크가 실제 파일로 존재하는지 확인. 없으면 깨진 링크로 표시.

**처리:** 오너님에게 보고. 삭제할지 페이지를 만들지 판단 요청.

---

## STEP 4 — YAML frontmatter 누락 탐지

모든 wiki/ 페이지 읽고 다음 필드가 있는지 확인:
- `title`
- `type` (concept / entity / source / analysis)
- `created`
- `updated`

누락된 필드가 있으면 자동으로 채워 넣는다 (파일명, 수정일 기준으로 추정).

---

## STEP 5 — index.md 정합성 확인

index.md의 각 항목이:
1. 실제 파일로 존재하는가
2. 요약이 120자 이내인가
3. 총 페이지 수가 실제와 맞는가

틀린 부분은 자동 수정.

---

## STEP 6 — 오래된 정보 탐지

`updated` 날짜가 30일 이상 지난 페이지를 찾는다.

오너님에게 목록으로 보고:
```
업데이트 필요 페이지:
- [[proposition-t]] — 마지막 업데이트 2026-04-19 (N일 전)
```

자동 수정하지 않음 — 오너님이 새 자료 추가할 때 업데이트.

---

## STEP 7 — 빠진 크로스링크 탐지

A 페이지가 B를 언급하는데 `[[B]]` 링크가 없는 경우:
- 주요 키워드: `파이 네트워크`, `Proposition T`, `GCV`, `아마테라스`, `몰트북`, `KYC`, `비수탁 지갑`, `상생`, `상극`
- 키워드가 텍스트로만 있고 wikilink가 없으면 자동으로 `[[링크]]`로 변환

---

## STEP 8 — log.md 기록 + 보고

`wiki/log.md`에 점검 결과 기록:

```markdown
## [YYYY-MM-DD] lint | 위키 점검

- 총 페이지: N개
- 고아 페이지: N개 (목록)
- 깨진 링크: N개 (목록)
- frontmatter 수정: N개
- 크로스링크 추가: N개
- 업데이트 필요: N개 (목록)
```

오너님에게 요약 보고:

```
위키 점검 완료 (총 N페이지)

✓ 자동 수정됨:
  - 고아 페이지 index.md 등록: N건
  - frontmatter 보완: N건
  - 크로스링크 추가: N건

⚠ 수동 확인 필요:
  - 깨진 링크: [[페이지명]] (N건)
  - 업데이트 권장: [[페이지명]] (N일 경과)
```

---

## 핵심 규칙

1. **raw/ 수정 절대 금지** — lint는 wiki/ 만 수정
2. **자동 수정 범위** — frontmatter 보완, index.md 등록, 크로스링크 추가
3. **오너님 판단 필요** — 깨진 링크 처리, 오래된 내용 갱신
4. **log.md 기록 필수** — 점검 결과 반드시 기록
5. **삭제 금지** — 고아 페이지도 삭제하지 말고 index.md에 등록
