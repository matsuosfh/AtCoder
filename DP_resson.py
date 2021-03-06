# N,W = map(int, input().split())
# w = []
# v = []
# V = int(1e5) # problem constraints
# INF = int(1e9+5)
#
# for _ in range(N):
#     weight,value = map(int, input().split())
#     w.append(weight)
#     v.append(value)
#
# # rows = items, cols = values
# dp = [[INF for col in range(V+1)] for row in range(N+1)]
# dp[0][0] = 0
#
# for i in range(1, N+1):
#     for j in range(0, V+1):
#         w_i = w[i-1]
#         v_i = v[i-1]
#         if j - v_i >= 0:
#             dp[i][j] = min(dp[i-1][j], dp[i-1][j-v_i]+w_i)
#         else:
#             dp[i][j] = dp[i-1][j]
#
# maxval = 0
# for j in range(1, V+1):
#     w_j = dp[N][j]
#     if w_j <= W:
#         maxval = max(maxval, j)
# print(maxval)

"""#E - Knapsack 2
N,W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
#INF = int(1e9+5)
v_max = 0
for k in range(N):
    v_max += A[k][1]
#v_max = int(1e5)

# dp[i][j]: i番目までの品物を使って価値jの組み合わせを作るときの重さの総和の最小値
dp = [[10**20 for col in range(v_max+1)] for row in range(N+1)]
dp[0][0] = 0

for i in range(1,N+1):
    for j in range(v_max+1):
        if j-A[i-1][1] >= 0:
            dp[i][j] = min(dp[i-1][j],dp[i-1][j-A[i-1][1]]+A[i-1][0])
        else:
            dp[i][j] =dp[i-1][j]
ans = 0
for k in range(1,v_max+1):
    if dp[N][k] <= W:
        ans = max(ans,k)
print(ans)"""

"""#D - Knapsack 1
N,W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]

# dp[i][j]: i番目までのもので 重さjの時の 価値の最大値
dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(W+1):
        dp[i][j] = dp[i-1][j]
        if j-A[i][0] >= 0:
            dp[i][j] = max(dp[i][j],dp[i-1][j-A[i][0]]+A[i][1])
        else:
            pass

print(dp[N-1][W])"""

"""# C Vacation
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]

#print(N,A)

dp = [[0] * 3 for _ in range(N)]
dp[0][0] = A[0][0]
dp[0][1] = A[0][1]
dp[0][2] = A[0][2]
#print(dp)

for i in range(1,N):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i][j] = max(dp[i][j],dp[i-1][k]+A[i][j])

print(max(dp[N-1]))"""

"""#B - Frog 2
N, K = map(int, input().split())
h = list(map(int, input().split()))
dp = [10 ** 9] * N
dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2,N):
    for j in range(K,0,-1):
        dp[i] = min(dp[i],dp[i-j] + abs(h[i] - h[i-j]))

#print(dp)
print(dp[N-1])
"""

"""# B - Frog 2
def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    dp = [10 ** 9] * N

    dp[0] = 0
    dp[1] = abs(h[1] - h[0])
    for i in range(2, N):
        tmp = i - K
        if tmp < 0:
            tmp = 0
        for j in range(i - K, i):
            dp1 = dp[j] + abs(h[i] - h[j])
            if dp[i] >= dp1:
                dp[i] = dp1
                if dp[i] == 0:
                    break
            else:
                pass

    print(dp[N - 1])

main()
"""
"""
DP = []
A = []
B = 0

for i in range(N):
    A = []
    if i == 0:
        DP.append(0)
    elif i == 1:
        DP.append(abs(h[1]-h[0]))
    else:
        if i >= K:
            for j in range(0, K):

                # 1個進む
                A.append(DP[i-(j+1)] + abs(h[i] - h[i-(j+1)]))
                # 2個進む
                #B = DP[i-2] + abs(h[i] - h[i-2])
                if j == 0:
                    B = A[j]
                elif A[j] < A[j-1]:
                    B = A[j]
                else:
                    B = A[j-1]
        else:
            for l in range(0, K-i):

                # 1個進む
                A.append(DP[i - (l+1)] + abs(h[i] - h[i - (l+1)]))
                # 2個進む
                # B = DP[i-2] + abs(h[i] - h[i-2])
                if l == 0:
                    B = A[l]
                elif A[l] < A[l - 1]:
                    B = A[l]
                else:
                    B = A[l - 1]

        DP.append(B)

ans = DP[N-1]
print(ans)"""

"""# A - Frog 1
N = int(input())
h = list(map(int, input().split()))
DP = []

for i in range(N):
    if i == 0:
        DP.append(0)
    elif i == 1:
        DP.append(abs(h[1]-h[0]))
    else:
        # 1個進む
        A = DP[i-1] + abs(h[i] - h[i-1])

        # 2個進む
        B = DP[i-2] + abs(h[i] - h[i-2])
        if A < B:
            DP.append(A)

        else:
            DP.append(B)

ans = DP[N-1]
print(ans)

"""
