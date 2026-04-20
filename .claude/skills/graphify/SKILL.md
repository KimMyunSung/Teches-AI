---
name: graphify
description: 아마테라스 위키를 지식 그래프로 변환한다. 키워드 검색이 아닌 관계 기반으로 AI가 답변할 수 있게 해준다. wiki/ 문서가 늘어날수록 효과적.
argument-hint: "[query 질문 | --update | 비워두면 전체 빌드]"
allowed-tools: Read, Bash, Glob, Grep, Write, Edit
---

# /graphify — 아마테라스 지식 그래프 스킬

오너님이 `/graphify`를 실행하면, wiki/ 전체를 그래프 구조로 변환하거나 그래프 기반으로 질의한다.

## 기본 경로

```
위키 루트: C:/Users/gussa/Desktop/Claude/아마테라스/
wiki/           — 그래프 빌드 대상
graphify-out/   — 결과물 저장 폴더 (자동 생성)
  graph.json    — AI가 참조하는 그래프 데이터
  graph.html    — 브라우저 시각화
  GRAPH_REPORT.md — 그래프 분석 리포트
```

---

## 사용법별 동작

### `/graphify` — 전체 빌드
```bash
cd "C:/Users/gussa/Desktop/Claude/아마테라스" && graphify wiki/
```
wiki/ 전체를 읽어 그래프 생성. 처음 실행 또는 대규모 변경 후 사용.

### `/graphify --update` — 증분 업데이트
```bash
cd "C:/Users/gussa/Desktop/Claude/아마테라스" && graphify wiki/ --update
```
새로 추가된 파일만 업데이트. 토큰 절약. 인제스트 후 습관적으로 실행.

### `/graphify query "[질문]"` — 그래프 기반 질의
```bash
cd "C:/Users/gussa/Desktop/Claude/아마테라스" && graphify query "[질문]"
```
노드·엣지 관계를 탐색해서 의미적 연결 기반으로 답변.

---

## 일반 /query vs /graphify query 차이

| | /query | /graphify query |
|--|--------|----------------|
| 탐색 방식 | 텍스트 키워드 grep | 그래프 노드·엣지 관계 |
| 강점 | 빠름, 직접적 | 간접 연결 발견, 관계 기반 |
| 적합한 질문 | "회보 008 핵심은?" | "파이 네트워크와 상생의 관계는?" |

---

## 실행 후 처리

1. `graphify-out/GRAPH_REPORT.md` 읽고 주요 발견 오너님에게 보고
2. 고립된 노드(연결 없는 페이지) 있으면 /lint 권장
3. `wiki/log.md`에 기록:

```markdown
## [YYYY-MM-DD] graphify | 지식 그래프 빌드

- 대상: wiki/ 전체 (또는 --update)
- 노드: N개, 엣지: N개
- 결과물: graphify-out/graph.json, graph.html, GRAPH_REPORT.md
```

---

## 권장 워크플로우

```
새 자료 추가
    ↓
/ingest        → wiki/ 업데이트
    ↓
/graphify --update  → 그래프 증분 업데이트
    ↓
/graphify query "[질문]"  → 관계 기반 답변
```
