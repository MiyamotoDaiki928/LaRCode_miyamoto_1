# 2018-03-14(水) 12:00 ~ 4018-03-14(水) 21:00
# AtCoder Beginners Selection
# https://atcoder.jp/contests/abs/tasks/abc081_b

# 入力
n = input()
A = list(map(int, input().split()))

# 出力
def count_two(x):
    count = 0
    while x % 2 == 0:
        x //= 2
        count += 1
    return count

answer = min(count_two(a) for a in A)
print(answer)