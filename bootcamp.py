#B - Collecting Balls (Easy Version)
N = int(input())
K = int(input())
x = list(map(int, input().split()))



"""#B - Can you solve this?
N,M,C= map(int, input().split())
B =list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(N)]
Ans = 0
for i in range(N):
    ans = 0
    for j in range(M):
        ans += A[i][j]*B[j]
    ans += C
    if ans > 0 :
        Ans += 1
    else:
        pass
if Ans >= 0:
    print(Ans)
else:
    print(0)"""