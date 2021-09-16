#B - Joker
N = int(input())
P = list(map(int, input().split()))
ans = 0
a = 0
M = [1]*(N**2)

for i in range(N**2):
    if P[i] <= N or P[i] >= N*(N-1) or P[i] % N == 1 or P[i] % N == 0:
        M[i] = 0
    else:
        for j in range(N):
         a+
         M[P[i]+1] M[P[i]-N] M[P[i]-1] M[P[i]+N]



"""#A - Pay to Win
T = int(input())
N = [list(map(int, input().split())) for i in range(T)]

#print(N)

def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
        if b == 6:
            break

    if n > 1:
        fct.append(n)
    return fct

print(factorize(N[3][0]+1),factorize(N[3][0]-1))
ans = N[3][1]*2+N[3][2]*1+N[3][4]*2448691153937
print(ans)"""
"""# A - Table Tennis Training
N,A,B = map(int, input().split())

if (B-A) % 2 == 0:
    ans = int((B-A)/2)
else:
    # ansB1 = A-1
    # ansB2 = int((B - A-1) / 2)
    # ansB = A-1 +1+ ansB2

    ansC2 = int((B - A-1) // 2)
    ans = min(N-B,A-1) +1+ ansC2

print(int(ans))"""