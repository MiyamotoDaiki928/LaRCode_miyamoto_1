# 2026-02-28(土) 21:00 ~ 2026-02-28(土) 22:40 (100分)
# AtCoder Beginner Contest 447
# https://atcoder.jp/contests/abc447/tasks/abc447_a

# 入力
N, M = map(int, input().split())

# 出力
if 2 * M - 1 <= N:
    print("Yes")
else:
    print("No")