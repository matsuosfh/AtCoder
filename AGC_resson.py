# A - Zero-Sum Ranges
N = int(input())
A = list(map(int, input().split()))
S = [0]*N
S[0] = A[0]
DP =[]
count = 0
for i in range(1,N):
    S[i] = S[i-1]+A[i]

for i in range(N):
    if S[i] == 0:
        DP
        count += 1
    else:


print(S)



"""#A - Candy Distribution Again
N,x = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)

tmp = 0
A_1  = x
for i in range(N):
    A_1 = A_1 - a[i]
    if A_1 > 0:
        if i == N-1:
            print(tmp)
            exit()
        else:
            tmp += 1
    elif A_1 == 0:
        tmp += 1
        print(tmp)
        exit()

    else:
        print(tmp)
        exit()
print(tmp)"""