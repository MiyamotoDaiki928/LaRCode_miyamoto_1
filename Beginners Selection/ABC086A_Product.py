# 2018-03-14(水) 12:00 ~ 4018-03-14(水) 21:00
# AtCoder Beginners Selection
# https://atcoder.jp/contests/abs/tasks/abc086_a

# 入力
a, b = map(int, input().split())

# 出力
if a * b % 2 == 0:
    print("Even")
else:
    print("Odd")