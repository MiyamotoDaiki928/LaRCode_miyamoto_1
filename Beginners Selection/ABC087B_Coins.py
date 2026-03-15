# 2018-03-14(水) 12:00 ~ 4018-03-14(水) 21:00
# AtCoder Beginners Selection
# https://atcoder.jp/contests/abs/tasks/abc087_b

# 入力
a, b, c, x = [int(input()) for _ in range(4)]

# 出力
count = 0
for i in range(a + 1):  
    for j in range(b + 1):
        rest = x - 500 * i - 100 * j
        if rest < 0:
            continue
        k = rest // 50
        if 0 <= k <= c:
            count += 1
print(count)