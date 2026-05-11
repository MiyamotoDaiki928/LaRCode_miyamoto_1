# B - Arrays
# https://atcoder.jp/contests/abc457/tasks/abc457_b

# =======================================================
# 以下に解答を記入してください
# コードテストはTesterファイルをターミナルで実行してください
# =======================================================


n = int(input())
a_list = []
for i in range(n):
    a_list.append(list(map(int,input().split())))
x, y = map(int, input().split())
print(a_list[x-1][y])
