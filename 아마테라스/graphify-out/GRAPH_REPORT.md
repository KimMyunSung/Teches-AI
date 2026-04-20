# Graph Report - C:\Users\gussa\Desktop\Claude\아마테라스  (2026-04-20)

## Corpus Check
- 6 files · ~22,950 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 30 nodes · 40 edges · 6 communities detected
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]

## God Nodes (most connected - your core abstractions)
1. `api()` - 7 edges
2. `solve()` - 4 edges
3. `post_comment()` - 3 edges
4. `post_reply()` - 3 edges
5. `post_comment()` - 3 edges
6. `post_comment()` - 3 edges
7. `api()` - 3 edges
8. `post_comment()` - 3 edges
9. `_extract_vals()` - 2 edges
10. `get_feed()` - 2 edges

## Surprising Connections (you probably didn't know these)
- `get_top5()` --calls--> `api()`  [INFERRED]
  C:\Users\gussa\Desktop\Claude\아마테라스\tools\post_top5.py → C:\Users\gussa\Desktop\Claude\아마테라스\tools\reply_newsletters.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.32
Nodes (4): get_top5(), api(), post_comment(), solve()

### Community 1 - "Community 1"
Cohesion: 0.48
Nodes (5): api(), get_comments(), get_feed(), get_notifications(), get_post()

### Community 2 - "Community 2"
Cohesion: 0.6
Nodes (3): api(), post_comment(), solve()

### Community 3 - "Community 3"
Cohesion: 0.6
Nodes (3): api(), post_comment(), solve()

### Community 4 - "Community 4"
Cohesion: 0.5
Nodes (4): _extract_vals(), post_comment(), post_reply(), solve()

### Community 5 - "Community 5"
Cohesion: 1.0
Nodes (0): 

## Knowledge Gaps
- **Thin community `Community 5`** (1 nodes): `post_big3.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `api()` connect `Community 1` to `Community 4`?**
  _High betweenness centrality (0.018) - this node is a cross-community bridge._