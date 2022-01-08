#055 - Select 5（★2）
N,P,Q =map(int,input().split())
A= list(map(int,input().split()))
B =[]
ans = 0
for i in range(N):
    B.append(A[i]%P)

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            for l in range(k+1,N):
                for m in range(l+1,N):
                    if B[i]%P*B[j]%P*B[k]%P*B[l]%P*B[m]%P == Q:
                        ans += 1


print(ans)
