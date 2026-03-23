# 2026-02-28(土) 21:00 ~ 2026-02-28(土) 22:40 (100分)
# AtCoder Beginner Contest 447
# https://atcoder.jp/contests/abc447/tasks/abc447_d

s = input()
a = 0
ab = 0
ans = 0
for c in s:
    if c == "A":
        a += 1
    elif c == "B":
        if a > 0:
            ab += 1
            a -= 1
    elif c == "C":
        if ab > 0:
            ab -= 1
            ans += 1
print(ans)