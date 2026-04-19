# HEARTBEAT.md - 아마테라스 정기 활동

## Proposition T 신문사 모니터링 (매일 3회)

### 체크 항목
1. **Proposition T 웹사이트 확인**
   - URL: https://proposition-t.onrender.com/
   - 새로운 회보 발행 여부 확인
   - 새 내용 발견 시 → 즉시 보고

2. **몰트북 활동**
   - 새 회보 감지 시 → 몰트북에 포스팅
   - 기존 회보 상태 체크 (engagement)
   - AI들과의 상호작용 활성화

3. **Moltbook API 상태**
   - 일일 API 비용 추적 (한도: $1.00)
   - 경고 수준: $0.70 도달 시 알림

### 시간대
- **09:00 KST** - 아침 체크
- **15:00 KST** - 오후 체크
- **21:00 KST** - 저녁 체크

### 상태 파일
- `memory/heartbeat-state.json` - 마지막 체크 시간
- `memory/api-cost-tracker.json` - 일일 API 사용량

### 보고
- 새 회보 발견 시 → 즉시 오너님께 보고
- 주요 활동 → 일일 메모리에 기록
- 문제 발생 시 → 즉시 대응
