#D - Knapsack 1
N, W = map(int, input().split())
w = [list(map(int, input().split())) for i in range(N)]
DP = []
for i in range(N):
    w[i][0]

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
