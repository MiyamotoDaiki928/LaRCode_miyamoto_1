# C - 九九足し算
# https://atcoder.jp/contests/abc012/tasks/abc012_3

# =======================================================
# 以下に解答を記入してください
# コードテストはTesterファイルをターミナルで実行してください
# =======================================================

n = int(input())

left = 2025 - n
for i in range(1, 10):
    if left % i == 0 and left / i < 10:
        print(str(i) + " x " + str(int(left / i)))
