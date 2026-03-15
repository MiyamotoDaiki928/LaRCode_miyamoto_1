# 2018-03-14(水) 12:00 ~ 4018-03-14(水) 21:00
# AtCoder Beginners Selection
# https://atcoder.jp/contests/abs/tasks/arc089_a

# 入力
N = int(input())
t = [0]
x = [0]
y = [0]
for _ in range(N):
    ti, xi, yi = map(int, input().split())
    t.append(ti)
    x.append(xi)
    y.append(yi)

# 出力
for i in range(N):
    dist = abs(x[i+1] - x[i]) + abs(y[i+1] - y[i])
    delta = t[i+1] - t[i]
    if dist > delta:
        print("No")
        exit()
    if (delta - dist) % 2 != 0:
        print("No")
        exit()
print("Yes")