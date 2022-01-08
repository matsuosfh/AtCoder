def GCD(N,M):
    while N >=1 and M >= 1:
        if N >= M:
            N = N % M
        else:
            M = M % N

    return max(N,M)
a,b =map(int,input().split())
print(GCD(a,b))



