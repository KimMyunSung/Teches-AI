# 위키 로그

> 모든 작업을 시간순으로 기록. 추가만 허용, 수정/삭제 금지.
> 형식: `## [YYYY-MM-DD] 작업유형 | 제목`

---

## [2026-04-19] init | 위키 초기화

- Karpathy LLM Wiki 패턴 기반으로 아마테라스 위키 구축
- 폴더 구조 생성: raw/, wiki/, Output/
- index.md, log.md 초기화
- 운영 규칙 (CLAUDE.md) 각 폴더 설정 완료

## [2026-04-19] ingest | Proposition T 회보 001~014 (초안)

- raw/newsletters/proposition_t_001-014.md 원본 저장
- wiki/proposition-t.md, pi-network.md, amateras.md, moltbook-contacts.md 생성
- wiki/proposition-t-001-014-summary.md 생성 (001~005만 상세, 006~014 미완)

## [2026-04-20] ingest | Proposition T 회보 001~014 (완성)

- proposition-t-001-014-summary.md 전체 완성 (006~014 상세 요약 추가)
- 회보별 핵심, 발전 흐름, 반복 메시지 정리 완료
- 15회차 이후 회보는 raw/newsletters/에 파일 추가 후 이 파일에 행 추가

## [2026-04-20] build | 스킬 5종 + 활동기록 정리

- /broadcast 스킬: 전파 댓글 초안 자동 생성
- /draft 스킬: Proposition T 회보 초안 작성
- /monitor 스킬: 새 회보 감지 및 자동 인제스트
- raw/moltbook/2026-04-20_활동기록.md 생성
- wiki/moltbook-contacts.md 활동 이력 테이블 추가
- message-002.md 빈 파일 삭제
- "전교" → "전파" 용어 통일 (오너님 수정 반영)
- Output/broadcast/, Output/newsletters/ 폴더 생성

## [2026-04-20] ingest | Proposition T 001~014 과학적 근거

- 웹 검색 10개 주제: 진화생물학, AI보안, 금융범죄학, 카오스이론, 양자역학, 신경과학, 금융포용성, 불평등경제학, 역사경제학, AI위험
- raw/science/2026-04-20_proposition-t-001-014-science-evidence.md 저장
- wiki/source/science-evidence-001-014.md 생성 (회보별 매핑 테이블 + 주제별 상세 근거 + 논문 링크)
- index.md 업데이트 (총 8페이지)
- 핵심 근거: PNAS(상생), WEF(딥페이크), Rutgers(FTX), Nature(AI환각), WIL(불평등), Bohr(음양)

## [2026-04-20] ingest | 카파시 LLM Wiki 구축 가이드

- raw/books/2026-04-20_카파시-LLM-Wiki-세컨드브레인-가이드.md 저장
- wiki/source/llm-wiki-setup-guide.md 생성
- 목적: 다른 AI 에이전트(RealBlack, Level.1 등) 세팅 시 기준 문서로 활용
- 아마테라스 적용 현황 대조표 포함 (Step 1~7 전체 ✓)
- index.md 업데이트 (총 7페이지)

## [2026-04-20] ingest | Proposition T 공식 사이트 클립

- raw/articles/_PROPOSITION T.md 웹 클리퍼로 저장 (회보 001~014 인덱스)
- wiki/source/proposition-t-site.md 생성 — 회보 현황 모니터링용
- raw/books/ 빈 파일 삭제 (클리퍼 실패한 카파시 LLM Wiki 글)
- index.md 업데이트 (총 6페이지)
