# 2018-03-14(水) 12:00 ~ 4018-03-14(水) 21:00
# AtCoder Beginners Selection
# https://atcoder.jp/contests/abs/tasks/abc083_b

# 入力
n, a, b = map(int, input().split())

# 出力
def sum_N(x):
    total = 0
    while x > 0:
        total += x % 10
        x //= 10
    return total

answer = 0
for i in range(1, n+1):
    if a <= sum_N(i) <= b:
        answer += i
print(answer)
