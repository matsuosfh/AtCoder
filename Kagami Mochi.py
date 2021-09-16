# Kagami Mochi
N = int(input())
A = [int(input()) for i in range(N)]

# N = 4
# A = [10, 8, 6, 8]
ans = 0

# 昇順にソート
A.sort()

# 要素を合計するが、同じ値の場合はカウントしない。

for i in range(N):
    if i == 0:
        ans = ans + 1
    elif A[i] == A[i-1]:
        pass
    else:
        ans = ans + 1

print(ans)