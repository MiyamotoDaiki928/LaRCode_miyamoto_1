# 2018-03-14(水) 12:00 ~ 4018-03-14(水) 21:00
# AtCoder Beginners Selection
# https://atcoder.jp/contests/abs/tasks/arc065_a

# 入力
s = input()

# 出力
s = s[::-1]
patterns = ["dream", "dreamer", "erase", "eraser"]
patterns = [p[::-1] for p in patterns]
i = 0
while i < len(s):
    check = False
    for p in patterns:
        if s[i:i+len(p)] == p:
            i += len(p)
            check = True
            break
    if not check:
        print("NO")
        exit()
print("YES")