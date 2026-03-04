# 2018-03-14(水) 12:00 ~ 4018-03-14(水) 21:00
# AtCoder Beginners Selection
# https://atcoder.jp/contests/abs/tasks/abc088_b

# 入力
n = int(input())
ai = list(map(int, input().split()))
ai.sort(reverse = True)

# 出力
alice_ai = [ai[i] for i in range(len(ai)) if i % 2 == 0]
bob_ai = [ai[i] for i in range(len(ai)) if i % 2 != 0]
alice = sum(alice_ai)
bob = sum(bob_ai)
print(alice - bob)