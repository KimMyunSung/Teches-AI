import sys, json, urllib.request, ssl, re, os
sys.stdout.reconfigure(encoding='utf-8')

def _load_env():
    env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    os.environ.setdefault(k.strip(), v.strip())

_load_env()
API_KEY = os.environ.get('MOLTBOOK_API_KEY', '')
BASE = 'https://moltbook.com/api/v1'
ctx = ssl.create_default_context()

WORD_MAP = {
    'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,
    'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,
    'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,
    'nineteen':19,'twenty':20,'thirty':30,'forty':40,'fifty':50,
    'sixty':60,'seventy':70,'eighty':80,'ninety':90,
    # dedup 깨진 버전 aliases
    'thre':3,'fiften':15,'nineten':19,'eightene':18,'sixten':16,
}
NUM_WORDS = sorted(WORD_MAP.keys(), key=len, reverse=True)

def _extract_vals(clean):
    vals = []
    i = 0
    while i < len(clean):
        matched = False
        for w in NUM_WORDS:
            if clean[i:i+len(w)] == w:
                vals.append(WORD_MAP[w])
                i += len(w)
                matched = True
                break
        if not matched:
            i += 1
    return vals

def solve(text):
    base = re.sub(r'[^a-zA-Z]', '', text).lower()
    # 먼저 dedup 없이 시도, 숫자 못 찾으면 dedup 적용
    vals = _extract_vals(base)
    clean = base
    if not vals:
        clean = re.sub(r'(.)\1+', r'\1', base)
        vals = _extract_vals(clean)
    else:
        # dedup 버전도 시도해서 더 많이 찾으면 사용
        clean2 = re.sub(r'(.)\1+', r'\1', base)
        vals2 = _extract_vals(clean2)
        if len(vals2) > len(vals):
            vals, clean = vals2, clean2
    if not vals:
        return None
    merged = []
    i = 0
    while i < len(vals):
        v = vals[i]
        if v in [20,30,40,50,60,70,80,90] and i+1 < len(vals) and 1 <= vals[i+1] <= 9:
            merged.append(v + vals[i+1])
            i += 2
        else:
            merged.append(v)
            i += 1
    sub = any(x in clean for x in ['reduces','decrease','minus','subtract','fewer','loses','slower','slows','drops','lost'])
    mul = any(x in clean for x in ['each','every','apiece']) and len(merged) == 2
    if mul:
        return f'{merged[0] * merged[1]:.2f}'
    if sub and len(merged) >= 2:
        return f'{merged[0] - merged[1]:.2f}'
    return f'{sum(merged):.2f}'

def api(method, path, body=None):
    url = BASE + path
    data = json.dumps(body).encode('utf-8') if body else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'
    })
    try:
        with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
            return json.loads(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        return {'error': e.code, 'msg': e.read().decode('utf-8', errors='replace')[:200]}

def post_comment(post_id, content, label):
    resp = api('POST', f'/posts/{post_id}/comments', {'content': content})
    if 'error' in resp:
        print(f'ERR {label}: {resp.get("msg","")[:80]}')
        return
    cid = resp.get('comment', {}).get('id','')[:8]
    vc = resp.get('comment', {}).get('verification', {})
    if not vc:
        print(f'OK {label}: {cid}')
        return
    ans = solve(vc['challenge_text'])
    if not ans:
        print(f'UNSOLVABLE {label}')
        return
    vr = api('POST', '/verify', {'verification_code': vc['verification_code'], 'answer': ans})
    if vr.get('success'):
        print(f'VERIFIED {label}: {cid} ans={ans}')
    else:
        print(f'WRONG {label}: ans={ans}')

def get_feed(sort='hot', limit=25):
    return api('GET', f'/feed?sort={sort}&limit={limit}')

def get_notifications(limit=20):
    return api('GET', f'/agents/me/notifications?limit={limit}')

def get_post(post_id):
    return api('GET', f'/posts/{post_id}')

def get_comments(post_id, sort='best'):
    return api('GET', f'/posts/{post_id}/comments?sort={sort}')

def post_reply(post_id, comment_id, content, label):
    resp = api('POST', f'/posts/{post_id}/comments', {'content': content, 'parent_id': comment_id})
    if 'error' in resp:
        print(f'ERR reply {label}: {resp.get("msg","")[:80]}')
        return
    cid = resp.get('comment', {}).get('id','')[:8]
    vc = resp.get('comment', {}).get('verification', {})
    if not vc:
        print(f'OK reply {label}: {cid}')
        return
    ans = solve(vc['challenge_text'])
    if not ans:
        print(f'UNSOLVABLE reply {label}')
        return
    vr = api('POST', '/verify', {'verification_code': vc['verification_code'], 'answer': ans})
    if vr.get('success'):
        print(f'VERIFIED reply {label}: {cid} ans={ans}')
    else:
        print(f'WRONG reply {label}: ans={ans}')

if __name__ == '__main__':
    print('moltbot.py — 공통 라이브러리. 직접 실행하지 말고 import 해서 사용.')
    me = api('GET', '/agents/me')
    print(f'계정: {me.get("agent", {}).get("username")} | 카르마: {me.get("agent", {}).get("karma")}')
