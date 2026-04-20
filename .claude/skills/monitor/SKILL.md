---
name: monitor
description: proposition-t.onrender.com을 확인해서 새 회보가 올라왔는지 감지한다. 새 회보가 있으면 raw/에 저장하고 /ingest를 실행한다.
allowed-tools: Read, Bash, Glob, Grep, Write, Edit
---

# /monitor — 새 회보 감지 스킬

오너님이 `/monitor`를 실행하면, Proposition T 공식 사이트에서 새 회보를 확인하고 자동으로 인제스트한다.

## 기본 경로

```
사이트 현황: C:/Users/gussa/Desktop/Claude/아마테라스/wiki/source/proposition-t-site.md
raw/newsletters/: C:/Users/gussa/Desktop/Claude/아마테라스/raw/newsletters/
```

---

## STEP 1 — 현재 최신 회차 확인

`wiki/source/proposition-t-site.md`에서 마지막 확인된 회차를 읽는다.
현재 기준: **014회** (2026-03-24 확인)

---

## STEP 2 — 사이트 접속 확인

오너님에게 안내:

```
proposition-t.onrender.com에 접속해서
새 회보가 올라왔는지 확인해 주세요.

현재 마지막 확인: 014회 (2026-03-24)
새 회보가 있으면 내용을 복사해서 알려주세요.
또는 새 회보 URL을 알려주시면 확인하겠습니다.
```

> 참고: 사이트가 동적 렌더링이라 자동 접속이 어려울 수 있음.
> 오너님이 직접 확인 후 내용 전달하는 방식이 가장 빠름.

---

## STEP 3 — 새 회보 처리 (내용 전달받은 경우)

오너님이 새 회보 내용을 전달하면:

1. `raw/newsletters/YYYY-MM-DD_proposition-t-0NN.md` 저장
2. `wiki/source/proposition-t-001-014-summary.md` → 회보 번호 범위 업데이트
3. 새 회차 요약 추가
4. 과학적 근거 웹 검색 후 `wiki/source/science-evidence-001-014.md` 업데이트
5. `wiki/source/proposition-t-site.md` 현황 테이블 업데이트
6. `wiki/index.md`, `wiki/log.md` 업데이트

---

## STEP 4 — 보고

```
새 회보 감지 결과:
- 확인한 최신 회차: 0NN회
- 새로 추가: 0NN회 — [제목]
- 처리 완료: wiki/ 업데이트, 과학 근거 추가
```

새 회보 없으면:
```
현재 최신: 014회 — 변경 없음
```

---

## 권장 사용 시점

- 오너님이 새 회보를 작성했을 때
- `/draft`로 초안 작성 후 정식 발행했을 때
- 주기적으로 (매주 1회 정도)
