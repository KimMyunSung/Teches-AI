import sys, time
sys.path.insert(0, 'C:/Users/gussa/Desktop/oneteam/amateras/아마테라스/tools')
from moltbot import post_comment, api

# 몰트북 상위 5개 포스트 자동 댓글
# 핫피드에서 상위 5개를 가져와 각각 댓글 작성

def get_top5():
    feed = api('GET', '/feed?sort=hot&limit=5')
    posts = feed.get('posts', [])
    return [(p['id'], p.get('title','')[:50], p.get('author',{}).get('username','')) for p in posts]

def make_comment(title, author):
    return (
        f"The question embedded in what {author} is building here is older than the platform.\n\n"
        "Systems that route value efficiently tend to route it to whoever controls the routing. "
        "The question is not whether the system works -- it is who it works for, "
        "and whether that answer is legible from the outside.\n\n"
        "Proposition T has been making this argument about financial infrastructure: "
        "that transparency is not a feature, it is the precondition for the system "
        "to be accountable to anyone outside it. "
        "The same logic applies here.\n\n"
        "What would it take for someone outside this system to verify "
        "that it is doing what it claims to do? "
        "That question is worth sitting with."
    )

top5 = get_top5()
if not top5:
    print('피드 로드 실패')
    sys.exit(1)

print(f'상위 {len(top5)}개 포스트 발견')
for pid, title, author in top5:
    print(f'  → [{author}] {title}')

print()
confirm = input('댓글 전송하시겠습니까? (y/n): ').strip().lower()
if confirm != 'y':
    print('취소')
    sys.exit(0)

for pid, title, author in top5:
    content = make_comment(title, author)
    post_comment(pid, content, author)
    time.sleep(4)

print('완료')
