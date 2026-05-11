# C - Long Sequence
# https://atcoder.jp/contests/abc457/tasks/abc457_c

# =======================================================
# 以下に解答を記入してください
# コードテストはTesterファイルをターミナルで実行してください
# =======================================================


n, k = map(int, input().split())
la_list = []
for i in range(n):
    la_list.append(list(map(int, input().split())))
c_list = list(map(int, input().split()))

for i in range(n):
    L = la_list[i][0]
    if k > L*c_list[i]:
        k -= L*c_list[i]
    else:
        k = (k-1)%L
        print(la_list[i][k+1])
        break
