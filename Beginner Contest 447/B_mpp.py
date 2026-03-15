# 2026-02-28(土) 21:00 ~ 2026-02-28(土) 22:40 (100分)
# AtCoder Beginner Contest 447
# https://atcoder.jp/contests/abc447/tasks/abc447_b

s = input()

d = {}

ans = ""

for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

max_count = max(d.values())

for c in s:
    if d[c] == max_count:
        continue
    ans += c

print(ans)