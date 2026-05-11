# D - Raise Minimum
# https://atcoder.jp/contests/abc457/tasks/abc457_d

# =======================================================
# 以下に解答を記入してください
# コードテストはTesterファイルをターミナルで実行してください
# =======================================================


n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))

def isok(x):
    nk = 0
    for i in range(1, n + 1):
        if a[i] < x:
            nk += (x - a[i] + i - 1) // i
            if nk > k:
                return False
    return True

ok = 1
ng = a[1] + k + 1

while ng - ok > 1:
    m = (ok + ng) // 2
    if isok(m):
        ok = m
    else:
        ng = m

print(ok)
