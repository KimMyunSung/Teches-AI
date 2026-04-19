# wiki/ — 위키 운영 규칙

## 핵심 규칙 10가지
1. `raw/`는 절대 수정 금지 — 읽기만 허용
2. 페이지 생성/삭제 시 `index.md` 필수 업데이트
3. 모든 작업마다 `log.md`에 기록
4. 내부 참조는 wikilink 형식 `[[페이지명]]`
5. 모든 페이지에 YAML frontmatter 필수
6. 모순 발견 시 양쪽 소스 모두 인용하고 표시
7. 소스 요약은 사실만 — 해석은 개념 페이지에서
8. 질의 시 `index.md` 먼저 읽고, `raw/`는 마지막 수단
9. 새 페이지보다 기존 페이지 업데이트 우선
10. index 항목은 한 줄, 120자 이내

## 페이지 유형
- **개념 (concept/)** — Proposition T 핵심 개념, 파이 네트워크 원리
- **엔티티 (entity/)** — 몰트북 AI 계정, 주요 인물
- **소스 (source/)** — 처리된 원본 요약
- **분석 (analysis/)** — 질의 결과, 비교, 심층 분석

## YAML frontmatter 형식
```yaml
---
title: 페이지 제목
type: concept | entity | source | analysis
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
---
```

## 오퍼레이션

### ingest (새 소스 추가)
1. `raw/`에 원본 파일 저장
2. 소스 읽고 핵심 내용 파악
3. `wiki/source/`에 요약 페이지 생성
4. 관련 개념/엔티티 페이지 업데이트
5. `index.md` 업데이트
6. `log.md`에 기록

### query (질의)
1. `index.md` 읽어 관련 페이지 파악
2. 관련 페이지들 읽고 종합
3. 답변 생성 (필요시 Output/ 저장)
4. 유용한 분석은 `wiki/analysis/`에 저장

### lint (위키 점검)
- 모순된 내용 탐색
- 고아 페이지 (링크 없는 페이지) 확인
- 오래된 정보 업데이트 필요 여부 확인
- 빠진 크로스링크 추가
