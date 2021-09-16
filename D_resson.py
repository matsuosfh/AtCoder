#D - 2017-like Number
Q = int(input())
A = [list(map(int, input().split())) for i in range(M)]
for

"""# C - 755
N = int(input())
print(N)
count = 0

for i in range(N):
    tmp = str(i)

    #print(tmp[0])
    if ('7' in tmp) and ('5' in tmp) and ('3' in tmp) :
        count += 1
    else:
        pass

print(count)"""

"""# D - Megalomania
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]

print(A)

A.sort(key=lambda x: x[1]) #要素2をソート
print(A)
tmp = 0
for i in range(N):
    tmp += A[i][0]
    if tmp <= A[i][1]:
        pass
    else:
        print('No')
        exit()

print('Yes')"""
