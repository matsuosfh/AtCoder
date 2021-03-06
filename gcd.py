def gcd(m,n):
    if n == 0 :
        return m
    return gcd(n, m % n)


N,K= map(int,input().split())

print(gcd(N,K))
