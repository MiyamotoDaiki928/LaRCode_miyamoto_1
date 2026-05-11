# B - 456
# https://atcoder.jp/contests/abc456/tasks/abc456_b

# =======================================================
# 以下に解答を記入してください
# コードテストはTesterファイルをターミナルで実行してください
# =======================================================

A = [list(map(int, input().split())) for _ in range(3)]

count = 0
for i in range(6):
    for j in range(6):
        for k in range(6):
            vals = [A[0][i], A[1][j], A[2][k]]
            
            if sorted(vals) == [4, 5, 6]:
                count += 1

print(count / 216)
