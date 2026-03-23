# 2026-02-28(土) 21:00 ~ 2026-02-28(土) 22:40 (100分)
# AtCoder Beginner Contest 447
# https://atcoder.jp/contests/abc447/tasks/abc447_c

s = input()
t = input()

if s.replace("A", "") != t.replace("A", ""):
    print("-1")
    exit()

def blocks(x):
    res = []
    cnt = 0
    for c in x:
        if c == "A":
            cnt += 1
        else:
            res.append(cnt)
            cnt = 0
    res.append(cnt)
    return res

ls = blocks(s)
lt = blocks(t)

ans = 0
for i in range(len(ls)):
    ans += abs(ls[i] - lt[i])

print(ans)