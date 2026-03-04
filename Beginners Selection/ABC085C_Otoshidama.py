# 2018-03-14(水) 12:00 ~ 4018-03-14(水) 21:00
# AtCoder Beginners Selection
# https://atcoder.jp/contests/abs/tasks/abc085_c

# 入力
N, Y = map(int, input().split())

# 出力
for x in range(N + 1):
    for y in range(N - x + 1):
        z = N - x - y
        total = 10000*x + 5000*y + 1000*z
        if total == Y:
            print(x, y, z)
            exit()
print(-1, -1, -1)