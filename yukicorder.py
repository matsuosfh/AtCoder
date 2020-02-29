# No.933 おまわりさんこいつです
N = int(input())
P = list(map(int, input().split()))
tmp = 1
tmp3 = 0
for i in range(N):
    tmp *= P[i]

print(tmp)
tmp2 = str(tmp)

while len(str(tmp3)) == 1:
    for j in range(len(tmp2)):
        tmp3 += int(tmp2[j])
    if len(str(tmp3)) >= 2:


print(tmp3)
"""# No.932
A = list(map(str, input().split(",")))
ans = "Done!"
print(A)
for i in range(len(A)) :
    if A[i] == 'AC':
        pass
    else:
        ans = 'Failed...'
        print(ans)
        exit()
print(ans)"""