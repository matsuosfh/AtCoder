
#C - Minimization
import math
N,K = map(int, input().split())
A = list(map(int, input().split()))

ans = math.ceil((N-K)/(K-1)+1)
#ans = int((N+K)/K) + ((N+K) % K)
print(ans)

"""#C - Walk on Multiplication Table
N = int(input())
for i in range(int(N**0.5),1,-1):
    if N % i == 0:
        A = N//i
        print(A+i-2)
        exit()
    else:
        pass
print(N-1)"""

"""#A - 台形
a = int(input())
b = int(input())
h = int(input())

print(int((a+b)*h/2))"""
"""#C - Splitting Pile
N = int(input())
a = list(map(int, input().split()))
A = 0
s = sum(a)
ans = 10**9
for i in range(N):
    A += a[i]
    tmp = abs(s-2*A)
    ans = min(tmp,ans)

print(ans)"""

"""#C - Unification
import collections
S = input()
S1 = [int(x) for x in list(str(S))]

c = collections.Counter(S1)
#print(c)
ans = 2*min(c[0],c[1])
print(ans)"""

"""#A - お茶
A,B = map(int, input().split())
if B % A == 0:
    print(B // A)
else:
    print(B//A+1)"""

"""#C - Prison
N,M = map(int, input().split())
L = [list(map(int, input().split())) for i in range(M)]
a_max = 0
b_min = 10**9
for i in range(M):
    if b_min >= L[i][1]:
        b_min = L[i][1]
    else:
        pass
    if a_max <= L[i][0]:
        a_max = L[i][0]
    else:
        pass

if a_max > b_min:
    print(0)
else:
    print(b_min - a_max + 1)"""

"""#B - すぬけ君の塗り絵 2 イージー
W, H,N = map(int, input().split())
a = [input().split() for l in range(N)]
tmpx = W
tmpx1 = 0
tmpy = H
tmpy1 = 0
for i in range(N):
    if a[i][2] == "1":
        if tmpx1 < int(a[i][0]):
            tmpx1 = int(a[i][0])
        else:
            pass
    elif a[i][2] == "2" :
        if tmpx > int(a[i][0]):
            tmpx = int(a[i][0])
        else:
            pass
    elif a[i][2] == "3" :
        if tmpy1 < int(a[i][1]):
            tmpy1 = int(a[i][1])
    elif a[i][2] == "4" :
        if tmpy > int(a[i][1]):
            tmpy = int(a[i][1])
    else:
        print(0)
        exit()

if tmpx-tmpx1 <= 0 or tmpy - tmpy1 <=0:
    print(0)
else:
    print(abs(tmpx-tmpx1)*abs(tmpy-tmpy1))"""


"""#C - *3 or /2
N = int(input())
a = list(map(int, input().split()))
tmp = 0
for i in range(N):
    for _ in range(a[i]//2):
        if a[i] % 2 == 0:
            a[i] = a[i] / 2
            tmp += 1
        else:
            break

print(tmp)"""
"""# - Qualification simulator
N, A,B = map(int, input().split())
S = input()
tmp = 0
tmp2 = 0

for i in range(N):
    if S[i] =="a":
        tmp += 1
    elif S[i] =="b":
        tmp2 += 1
    else:
        pass

    if S[i] =="a" and tmp <= A+B:
        print("Yes")
    elif S[i] =="b" and tmp+1 <= A+B and tmp2 <= B:
        tmp += 1
        print("Yes")
    else:
        print("No")"""

"""#B - Colorful Creatures
N = int(input())
A = list(map(int, input().split()))
A.sort()
tmp = 0
for i in range(N-1):
    if A[i+1] <= 2*A[i]:
        tmp += 1
        A[i+1] = A[i]+A[i+1]
    else:
        pass

print(N-tmp)"""


"""#B - 高橋君とパスワード
s = input()
k = int(input())
A = []

if k > len(s):
    print(0)
    exit()
elif k == len(s):
    print(1)
    exit()
else:
    pass

for i in range(len(s)-k+1):
    a = ""
    for j in range(k):
        a += s[i+j]
    A.append(a)
#print(A)

ans = len(set(A))
print(ans)"""

# #B - KEYENCE String
# S =str(input())
# T = "keyence"
#
# s = []
# for i in range(len(S)):
#     S[i]

"""#A - Pair
K = int(input())
if K % 2 == 0:
    print(int(K/2*K/2))
else:
    print(int((K//2+1)*int(K//2)))"""

"""# 高橋君とお肉
N = int(input())
S = [int(input()) for i in range(N)]

S.sort()
if N == 1:
    print(S[0])
elif N == 2:
    print(max(S))
elif N == 3:
    print(max(S[0]+S[1],S[2]))
else:
    print(min(max(S[0] + S[3], S[1] + S[2]),max(S[0]+S[1]+S[2],S[3])))"""


"""#B - Exponential
X = int(input())
for i in range(X,0,-1):
    X_1 = i**0.5
    if X_1.is_integer():
        print(i)
        exit()
    else:
        pass"""

"""#B - Different Distribution
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
A.sort(key=lambda x: x[1])

print((A[0][0])+A[0][1])"""