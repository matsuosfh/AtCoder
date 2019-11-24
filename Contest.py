# B - Iron Bar Cutting
N = int(input())
A = list(map(int, input().split()))
A_1 = sum(A)//2
A_tmp = 0
for i in range(N):
    A_tmp += A[i]
    if A_tmp < A_1:
        pass
    elif A_tmp == A_1:
        print(0)
        exit()
    else:
        A_tmp2 = A_tmp-A[i]
        ans1 = abs(A_tmp - (sum(A) - A_tmp))
        ans2 = abs(A_tmp2 - (sum(A) - A_tmp2))
        print(min(ans1,ans2))
        exit()



"""# A - DDCC Finals
x,y = map(int, input().split())
X = 0
Y = 0


if x == 3:
    X = 100000
elif x == 2:
    X = 200000
elif x == 1:
    X = 300000
else :
    X = 0

if y == 3:
    Y = 100000
elif y == 2:
    Y = 200000
elif y == 1:
    Y = 300000
else:
    Y = 0

if x == 1 and y == 1:
    print(X+Y+400000)
else:
    print(X +Y)"""




"""# C - Average Length
import math
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]

tmp = 0
for i in range(N):
    for j in range(N):
        if i == j:
            pass
        else:
            tmp += (((A[i][0]-A[j][0])**2)+((A[i][1]-A[j][1])**2))**0.5
tmp = tmp* math.factorial(N-1)

ans = tmp/math.factorial(N)
print(ans)
"""
"""# B - Echo
N =int(input())
S = str(input())
S_1 = S[:int(N/2)]
S_2 = S[int(N/2):]

if N % 2 != 0:
    print("No")
elif S_1== S_2:
    print("Yes")
else:
    print("No")"""

"""# A - Circle
r = int(input())

print(r**2)"""



# # C - Swaps
# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
#
# count = 0
# count2 = 0
# count3 = 0
#
# for i in range(len(A)):
#     if A[i] > B[i]:
#         count += 1
#         count2 += 1
#     elif A[i] < B[i]:
#         count += -1
#     else:
#         pass
#
# A.sort(reverse=True)
# B.sort(reverse=True)
# # print(A)
# for i in range(len(A)):
#     if A[i] > B[i]:
#         count3 += 1
#     else:
#         pass
#
# if count <= 0 and count2 < N-2 and count3 <= 0:
#     print('Yes')
# else:
#     print('No')

"""# B - Counting of Trees
import collections
N = int(input())
D = list(map(int, input().split()))

#
c = collections.Counter(D)
# DP =[1]*max(c)
# c.most_common()
#print(c)
ans = 1
tmp = 1
if D[0] > 0:
    print(0)
    exit()
elif c[0] != 1:
    print(0)
    exit()
else:
    for i in range(1,max(D)+1):
        ans *= (tmp ** c[i])
        ans = ans % 998244353
        tmp = c[i]
print(ans)"""

"""# A - Sum of Two Integers
N = int(input())

if N % 2 ==0:
    ans = (N-2)/2
else:
    ans = (N-1)/2
print(int(ans))
"""
"""# A - ><
S = str(input())

ans = 0
tmp = 0

for i in range(len(S)+1):
    if i == 0 and S[0] == "<":
        tmp = 0
    elif i == len(S) and S[i-1] == ">":
        tmp = 0
    elif i == len(S) and S[i-1] == "<":
        tmp += 1
#    elif i == len(S) and S[i] == ">":

    elif S[i-1] == ">" and S[i] == "<":
        tmp = 0
    elif i >= 3 and S[i-2] == "<" and S[i-1] == ">" and S[i] == ">":
        tmp = 1
    elif i >= 3 and S[i-2] == "<" and S[i-1] == ">" and S[i] == "<":
        tmp = 0
    else:
        tmp += 1
    ans += tmp

print(ans)"""




"""# D - Water Bottle
import math
a,b,x = map(int, input().split())

tmp = x/(a**2)
# tmp2 = x/(b**2)
tmp2 = (2*x)/(a*b)

if tmp2 < a:
    print(90-math.degrees(math.atan2(tmp2,b)))
else:
    #print(tmp)
    tmp3 = (2*b-((2*x)/(a*a)))
    #print(tmp3)
    print(90-math.degrees(math.atan2(a,tmp3)))"""

"""# C - Walk on Multiplication Table
N = int(input())
n = int(N**(1/2))
for i in range(n,0, -1):
    if N % i == 0:
        print(i-1+int(N/i)-1)
        exit()
    else:
        pass"""



"""# B - 81
N = int(input())

for i in range(1,10):
    if N % i == 0 and N / i <= 9:
        print('Yes')
        exit()
    else:
        pass

print("No")"""

"""
# A - 9x9
N,M = map(int, input().split())

if N <= 9 and M <= 9:
    print(N*M)
else:
    print(-1)"""

"""# D - Triangles
N = int(input())

L.sort(reverse=True)
count = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if L[j] < L[k] + L[i] and L[k] < L[j] + L[i] and L[i] < L[j] + L[k]:
                count += 1
            else:
                break
print(count)"""

# for i in range(N-2):
#     if L[i+2] < L[i+1]+L[i] and L[i+1] < L[i+2]+L[i] and L[i] < L[i+1]+L[i+2]:
#         count += 1
#     else:
#         pass


# for i in range(N):
#     for j in range(N):
#         if i == j:
#             pass
#         for
#         elif L[i] < L[j]

"""# C - Slimes
N = int(input())
S = str(input())
count = 0

for i in range(N):
    if i == 0:
        count += 1
    elif S[i-1] == S[i]:
        pass
    else:
        count += 1

print(count)"""
"""# B - TAKOYAKI FESTIVAL 2019
N = int(input())
d = list(map(int, input().split()))
tmp = 0


for i in range(N):
    for j in range(N):
        if j == i:
            pass
        else:
            tmp += d[i]*d[j]
ans = tmp / 2
print(int(ans))"""

"""# A - Curtain
A, B = map(int, input().split())

if A - 2*B >= 0:
    print(A-2*B)
else:
    print(0)"""

"""# A - Connection and Disconnection
S = str(input())
K = int(input())
count =  0
tmp = 0
N = len(S)

if N == 1:
    if K >= 2:
        count = 1 * (K//2)
    else:
        count = 0
elif S[0] == S[N-1] == S[N-2]:
    count += 1
else:
    pass

for i in range(1,N-1):
    if S[i-1] == S[i] == S[i+1] and tmp == 0:
        tmp = 1
    else:
        tmp = 0
    if S[i-1] == S[i] and tmp == 0:
        count += 1
    else:
        pass
# if S[N-2] == S[N-1] and tmp == 1:
#     count += 1
# else:
#     pass


if K <= 1:
    print(count)
elif N == 2 and S[0] == S[N-1]:
    print(count*K)
elif N == 2 and S[0] != S[N-1]:
    print(0)
elif N == 3 and S[0] == S[N-1] == S[N-2]:
    print(count + (K - 1) * (count + 1))
elif N < 4 and S[0] == S[N-1]:
    print((K-1)*(count+1))
elif N < 4 and S[0] != S[N-1] :
    print(count + (K-1)*(count+1) )
elif N >= 4 and S[0] == S[N-1] == S[N-2]:
    print(count+(K-1)*(count))
elif N >= 4 and S[0] == S[N-1]:
    print(count + (K - 1) * (count + 1))
else:
    print(count+(K-1)*(count))

# if N == 1 and tmp == 0:
#     print(count)
# elif N == 3 and tmp == 0:
#     print(count*(K-1))
# elif N == 3 and tmp == 1:
#     print(count + K)
# elif N >= 4 and S[0] == S[N-1] != S[N-2]:
#      print(count+(K-1)*(count+1))
# else:
#     ans = count * K
#     print(ans)"""

"""# 未完D - Disjoint Set of Common Divisors
A, B = map(int, input().split())

d = int(min(A, B)**0.5)
#print(d)
tmp = 0
DP =[1]
if A % 2 == 0 and B % 2 == 0:
    DP.append(2)

for i in range(3,d+1):
    if A % i == 0 and B % i == 0:
        tmp = 0
        for j in range(1,len(DP)):
            if i % DP[j] == 0:
                tmp = 0
                break
            else:
                tmp = 1
        if tmp == 1:
            DP.append(i)
        # else:
        #     for j in range(1,len(DP)):
        #         if i % DP[j] == 0:
        #             tmp = 0
        #             break
        #         else:
        #             tmp = 1
        #     if tmp == 1:
        #         DP.append(i)

    else:
        pass

print(len(DP))
"""

"""# C - Go to School
N = int(input())
A = list(map(int,input().split()))
B = [0]*N

for i in range(N):
    B[A[i]-1] = i+1

for s in B:
  print(s, end =" ")
"""

"""# B - Roller Coaster
N, K = map(int, input().split())
h = list(map(int,input().split()))
count = 0

for i in range(N):
    if h[i] >= K:
        count += 1
    else:
        pass

print(count)
"""
"""# A - Odds of Oddness
N = int(input())

if N % 2 == 0:
    ans = (N/2)/N
else:
    ans = ((N //2)+1) / N
print(ans)
"""
"""# A - 01 Matrix
import copy
H, W, A, B = map(int, input().split())

ans = [[0 for s in range(W)] for t in range(H)]
for i in range(H):
    for j in range(W):
        if A == min(ans[i].count(0), ans[i].count(1)):
            break
        else:
            ans[i][j] = 1

for k in range(W-1):
    tmp = 0
    for l in range(H):
        tmp += ans[l][k]
    if B == tmp:
        break
    else:
        for m in range(k+1,H):
            tmp2 = ans[m][k+1]
            ans[m][k+1] = ans[m][k]
            ans[m][k] = tmp2

if A != min(ans[i].count(0), ans[i].count(1)):
    print('No')
else:
    for a in ans:
        print(*a, sep="")

"""
"""# D - Powerful Discount Tickets
import copy
N, M = map(int, input().split())
A = list(map(int,input().split()))
Y = copy.cpoy(A)
ans =0

print(N,M,A)
A.sort(reverse=True)
for i in range(A):
    A[i]
        Y[i] = A[i]//2**(M-j)
        ans += Y[i]

    Y
"""

"""# C - Attack Survival
from collections import Counter

N, K, Q = map(int, input().split())
a = [int(input()) for i in range(Q)]
A = Counter(a)
B = 1 - (K-Q)
#print(N,K,Q,a,A,B)

for i in range(N):
    if A[i+1] >= B:
        print('Yes')
    else:
        print('No')

"""

"""# B - Tap Dance
S = str(input())
ans =''
for i in range(len(S)):
    if (i+1) % 2 == 0:
        if S[i] != 'R':
            ans = 'Yes'
        else:
            ans = 'No'
            print(ans)
            exit()
    else:
        if S[i] != 'L':
            ans = 'Yes'
        else:
            ans = 'No'
            print(ans)
            exit()

print(ans)
"""

"""# A - Weather Prediction
S = str(input())

if S == 'Sunny':
    print('Cloudy')
elif S == 'Cloudy':
    print('Rainy')
else:
    print('Sunny')
"""
"""# E - Second Sum
N = int(input())
P = list(map(int,input().split()))
tmp = 0
ans = 0

# for i in range(N):
#     for j in range(i+1,N):
#         if j == i + 1:
#             if P[i] > P[j]:
#                 tmp = P[j]
#                 ans += tmp
#             else:
#                 tmp = P[j-1]
#                 ans += tmp
#         else:
#             if tmp > P[j]:
#                 tmp = P[j-1]
#                 ans += tmp
#             else:
#                 tmp = P[j]
#                 ans += tmp
# print(ans)

P.sort(reverse=True)
for i in range(1,N):
    ans += P[i]*i
print(ans)
"""
"""# D - Face Produces Unhappiness
N, K = map(int,input().split())
S = str(input())

S[l]

count = 0
for i in range(N-1):
    if S[i] == S[i+1]:
        count += 1
    else:
        pass
print(count)
"""

"""# C - Maximal Value
N = int(input())
B = list(map(int,input().split()))
A = [10**6]*N

A[0] = B[0]
A[1] = B[0]
for i in range(1,N-1):
    if A[i] >= B[i]:
        A[i] = B[i]
        A[i+1] = B[i]
    else:
        A[i+1] = B[i]

print(sum(A))
"""

"""# B - Buffet
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

ans = 0
for i in range(len(A)):
    j = A[i]
    ans += B[int(j-1)]
    if i == 0:
        pass
    else:
        if A[i]-A[i-1] == 1:
            ans += C[int(j-2)]
print(ans)"""

"""# A - Password
N = int(input())

print(N**3)
"""

"""# D - ModSum
# import numpy as np
N = int(input())

ans = (N*(N-1))/2
print(int(ans))

# if N > 1:
#     N_1 = np.array(list(range(1, N+1)))
#     P_1 = np.array(list(range(2, N+1)))
#     P_1 = np.append(P_1, 1)
#
#     print(N_1,P_1)
#     print(N_1 % P_1)
#     ans = sum(N_1 % P_1)
#     print(ans)
# else:
#     print(0)
"""
"""# C - Lower
N = int(input())
H = list(map(int, input().split()))
max = 0
count_i = 0
for i in range(N-1):
    if H[i] >= H[i+1]:
        count_i += 1
    else:
        if max > count_i:
            count_i = 0
        else:
            max = count_i
            count_i = 0

    if max > count_i:
        pass
    else:
        max = count_i
print(max)
"""
"""# B - Power Socket
A, B = map(int, input().split())

A_new = A
if B == 1:
    count = 0
else:
    count = 1
    while A_new <= B:
        if A_new == B:
            break
        else:
            A_new = A_new-1
            A_new += A
            count += 1
print(count)
"""
"""# A - Tenki

S = str(input())
T = str(input())
count = 0

for i in range(len(S)):
    if S[i] == T[i]:
        count += 1
    else:
        pass
print(count)
"""

"""# B - Kleene Inversion
N, K = map(int,input().split())
A = list(map(int, input().split()))
count = 0
count2 = 0
ans = 0
#A_new = K * A

# for i in range(N-1):
#     if A[i] > A[i + 1]:
#         count = count + 1
#     else:
#         pass
#         print(count)
#
# for j in range(N, K*N-1):
#     if A_new[j] > A_new[j + 1]:
#         count2 = count2 + 1
#     else:
#         pass
# ans = (count + count2 + count) % (10**9+7)

for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            count = count + 1
        else:
            pass
print(count)

A_new = 2 * A
for k in range(N, 2*N):
    for l in range(N+1, 2*N):
        if A_new[k] > A_new[l]:
            count2 = count2 + 1
        else:
            pass

count1 = K*count
count2 = (K-1) * count2
for m in range(1,K % (10**9+7)):
    ans = ans + K*count + (K-m)*count2

#ans = ans % (10**9+7)
#print(A_new)
#print(count2)
print(ans)
"""
"""# A - Takahashi Calendar
M, D = map(int,input().split())
count = 0
for k in range(4, M+1):
    for i in range(22, D+1):
        if i // 10 >= 2 and i % 10 >= 2:
            if k == (i//10)*(i % 10):
                count = count + 1
            else:
                pass
        else:
            pass
print(count)
"""

"""# D - Ki
N, Q = map(int, input().split())
a = [list(map(int, input().split())) for i in range(N - 1)]
p = [list(map(int, input().split())) for j in range(Q)]
ans = []
print(N, Q, a, p)

print(a[0][0], a[0][1], p[0][0])
for i in range(len(a)):
    a[i].append(0)
print(a)

for i in range(N):
    ans.append(0)
print(ans)

for i in range(len(p)):
    for j in range(len(a)):
        if p[i][0] == a[j][0]:
            for k in range(1, len(ans)+1):
                if k == a[j][1] or k == a[j][0]:
                    ans[k-1] = ans[k-1] + p[i][1]
                else:
                    pass
                #a[j][2] = a[j][2] + p[i][1]

        else:
            pass

print(ans[0], ans[1],ans[2],ans[3])
"""
"""# C - Alchemist
N = int(input())
v = list(map(int, input().split()))

new_v = sorted(v)

for i in range(N-1):
    if i == 0 :
        a = (new_v[i]+new_v[i+1])/2
    else:
        a = (a + new_v[i+1])/2
print(a)

# a[i][k]= (v[i]+v[i+k])/2
# a[i][k]
"""

"""# B - Resistors in Parallel
N = int(input())
A = list(map(int, input().split()))
B = 0
ans = 0
for i in range(N):
    B = B + 1/(A[i])

ans = 1/B
print(ans)
"""

"""# Red or Not
N = int(input())
s = str(input())

if N >= 3200 :
    print(s)
else:
    print('red')
"""

"""# Dividing a String
S = str(input())
count = 0
i = 0
j = 0
# for i in range(len(S)-1):
for k in range(len(S)-1):
    if S[k] == S[k+1]:
        j = j + 1
    else:
        break


while i <= len(S)-1:

    if i == 0:
        count = count + 1
        i = i + 2
    elif i % 3 == 0:
        if i == len(S)-1 :
            break
        else:
            count = count + 1
            i = i + 2
    elif i < len(S) - 1:
        if S[i - 2] != S[i - 1] and S[i-1] != S[i]and S[i] != S[i + 1]:
            count = count + 2
            i = i + 1
        else:
            count = count + 1
            i = i + 1
    else:
        if S[i - 1] != S[i - 2] and S[i] != S[i - 1]:
            count = count + 1
            i = i + 1
        else:
            i = i + 1

if len(S) <= 2 and j <= 2:
    count = 1
else:
    count = count + 1
print(count)


    # if w == S[i+1]:
    #     w = w + S[i+1]
    #     i = i + 1
    # else:
    #     w = S[i+1]
    #     i = i + 1
    #     count = count + 1
# i = 0:
# count = 1
# i = 2:
# count = 2
# i = 3:
# count = 3
# i = 5
# if i % 3 == 0:
#     if S[i-1] != S[i] and S[i+1] != S[i]

"""
