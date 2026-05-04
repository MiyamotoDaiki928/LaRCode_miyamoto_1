# D - バスと避けられない運命
# https://atcoder.jp/contests/abc012/tasks/abc012_4

# =======================================================
# 以下に解答を記入してください
# コードテストはTesterファイルをターミナルで実行してください
# =======================================================

n, m = map(int, input().split())

INF = 10**15

dist = [[INF]*n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = t
    dist[b][a] = t

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

ans = INF
for i in range(n):
    worst = max(dist[i])
    ans = min(ans, worst)

print(ans)
