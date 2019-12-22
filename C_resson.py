#早めのクリスマスプレゼント
import math
N = int(input())
N_S = math.sqrt(N)
for x in range(1,int(N_S)):
    tmp = N-x**2
    y = math.sqrt(tmp)
    if y.is_integer():
        print(x,int(y))
        exit()
    else:
        pass
print(-1)


"""# C - Cat Snuke and a Voyage
N,M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(M)]
goal2 = []
goal1 = []
for i in range(M):
    if A[i][1] == N:
        goal2.append(A[i][0])
    elif A[i][0] == 1:
        goal1.append(A[i][1])
    else:
        pass

if len(set(goal1)&set(goal2)) != 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")"""






"""# C - City Savers
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if B[0]-A[0] >= 0:
    ans = B[0]
    B[0] = B[0]-A[0]
    if B[0] - A[1] >= 0:
        A[1] = 0
    else:
        A[1] = A[1]-B[0]
else:
    ans = B[0]
    B[0] = 0

for i in range(1,N):
    tmp = B[i] - A[i]
    if tmp > 0:
        ans += A[i]
        if tmp - A[i+1] >= 0:
            ans += A[i + 1]
            A[i+1] = 0

        else:
            A[i+1] = A[i+1] - tmp
    else:
        ans += B[i]
if B[N-1]-A[N] > 0:
    ans += A[N]
else:
    ans += B[N-1]


print(ans)"""

"""# C - Grid Repainting 2
H, W = map(int,input().split())
S = [list(str(input())) for i in range(H)]

print(S)

for h in range(H):
    for w in range(W):
        # if S[0][j] == '#':
        #     if S[0][j+1]=='#' or S[1][j] == '#' or S[i][j+1] == '#':
        #         pass
        if S[h][w] == '#':
            tmp = 0
            if w != W-1:
                if S[h][w+1] == '#':
                    tmp = 1
            if h != 0:
                if S[h-1][w] =='#':
                    tmp = 1
            if h != H-1:
                if S[h + 1][w] == '#':
                    tmp = 1
            if w != 0:
                if S[h][w - 1] == '#' and w != 0:
                    tmp = 1
            if tmp == 0:
                print('No')
                exit()
print('Yes')"""

"""途中# C - To Infinity
S = str(input())
K = int(input())
ans = 0
for i in range(len(S)):
    if S[i] == '1' and i <= K:
        ans = 1
    elif S[i] != '1' and i <= K:
        ans = S[i]
        print(ans)
        exit()
    else:

print(1)"""

"""# C - 数を3つ選ぶマン
A,B,C,D,E = map(int, input().split())

tmp1 = A+D+E
tmp2 = B+C+E

if tmp1 >= tmp2:
    print(tmp1)
else:
    print(tmp2)"""

"""# C - Typical Stairs
N,M = map(int, input().split())
a = [int(input()) for i in range(M)]
tmp0 = 1
tmp1 = 1
#穴がある場合の場合わけ
if len(a) == 1:
    tmp = 2*3
else:
    for i in range(1,M):
        if a[i] == a[i-1]+1:
            print(0)
            exit()
        elif a[i] == 1 or a[i] == N-1:
            tmp0 *= 2
        elif a[i] == a[i-1]+2:
            tmp0 *= 2*2
        else:
            tmp1 *= 2*3
    tmp = tmp0 + tmp1

ans = int(2**(N+1-2)/(tmp))
print(ans % (10**9+7))"""

"""#未完 C - Not so Diverse
N,K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
count = 1
ans = 0
B = []

for i in range(1,N+1):
    if i == N:
        if A[i-1] == A[i - 2]:
            count += 1
            B.append(count)
        else:
            count = 1
            B.append(count)
    elif A[i] == A[i-1]:
        count += 1
    else:
        B.append(count)
        count = 1
B.sort()

for j in range(len(B)-K):
    ans += B[j]

print(ans)"""

"""# C - pushpush
from collections import deque
n = int(input())
a = list(map(int, input().split()))
b = deque()
for i in range(n):
    if n % 2 == 0:
        if i % 2 ==0:
            b.append(a[i])
        else:
            b.appendleft(a[i])
    else:
        if i % 2 !=0:
            b.append(a[i])
        else:
            b.appendleft(a[i])

print(*b, end=" ")


# for i in range(n//2):
#     b.append(a[n-(i*2)])
#
# for i in range(n//2,n):
#     b.append(a[n - (i * 2)])


#
# b[0] = a[N-0]
# b[1] = a[N-2]
# b[2] = a[N-4]
# b[3] = a[0]
# b[4] = a[N-5]
# b[5] = a[N-3]
# b[6] = a[N-1]
"""

"""# C - Reconciled?
N, M = map(int, input().split())
ans_N = 1
ans_M = 1
mod = 10**9+7

if abs(N - M) >= 2:
    print(0)
else:
    for i in range(N):
        ans_N = ans_N * ((M - i) * (N - i)) % mod
    for j in range(M):
        ans_M = ans_M * ((M - j) * (N - j)) % mod
    print((ans_N+ans_M)% mod)"""

"""# Candies
N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
ans = 0
for i in range(N):
    A1_sum = 0
    A2_sum = 0
    A1_sum = sum(A1[i] for i in range(i+1))
    A2_sum = sum(A2[i] for i in range(i,N))

    tmp = A1_sum+A2_sum
    if ans <= tmp:
        ans = tmp
    else:
        pass

print(ans)
"""
"""# C - Colorful Leaderboard
N = int(input())
a = list(map(int, input().split()))
DP = [0]*8
tmp = 0

for i in range(N):
    if 1 <= a[i] <= 399:
        DP[0] = 1
    elif 400 <= a[i] <= 799:
        DP[1] = 1
    elif 800 <= a[i] <= 1199:
        DP[2] = 1
    elif 1200 <= a[i] <= 1599:
        DP[3] = 1
    elif 1600 <= a[i] <= 1999:
        DP[4] = 1
    elif 2000 <= a[i] <= 2399:
        DP[5] = 1
    elif 2400 <= a[i] <= 2799:
        DP[6] = 1
    elif 2800 <= a[i] <= 3199:
        DP[7] = 1
    else:
        tmp += 1

ans1 = sum(DP)

if ans1 == 0:
    ans1 = 1
else:
    pass

ans2 = sum(DP)+tmp
print(ans1,ans2)

"""

"""# C - String Transformation
import collections
S = str(input())
T = str(input())

S1 = sorted(collections.Counter(S).values())
T1 = sorted(collections.Counter(T).values())

if S1 == T1:
    print('Yes')
else:
    print('No')
# s =S.count('z')
# t =T.count('p')
# print(s,t)
"""
"""# C - Digits in Multiplication
N = int(input())

A = int(N**0.5)
# print(A)
ans = 1
for i in range(A,0,-1):
    if N % i == 0:
        tmp = N / i
        ans = len(str(int(tmp)))
        break
    else:
        pass

print(ans)
"""

"""# C - いっしょ / Be Together
N = int(input())
A = list(map(int, input().split()))
ans = 10**8

for X in range(-100,101):
    tmp = 0
    for i in range(N):
        tmp += (A[i]-X)**2
    if ans >= tmp:
        ans = tmp
    else:
        pass

print(ans)

# A_s = set(A)
#
# A_s_a = int(sum(A_s)//len(A_s))
#
# if N % 2 != 0:
#     if A[N//2+1-1] <= A_s_a:
#         pass
#     else:
#         A_s_a = A_s_a + 1
# else:
#     pass
#
# ans = 0
# # print(A_s,A_s_a)
# for i in range(N):
#     ans += (A[i]-A_s_a)**2

"""

"""# C - Multiple Clocks
# import math mathはatcoderでは使えない
from fractions import gcd
N = int(input())
T = [int(input()) for i in range(N)]
# 最小公倍数を求める
if N == 1:
    print(T[0])
else:
    DP = [0]*(N-1)
    DP[0] = (T[0]*T[1])//gcd(T[0],T[1])
    for i in range(1,N-1):
        DP[i] = (DP[i-1]*T[i+1]) // gcd(DP[i-1],T[i+1])
    print(DP[-1])
"""

"""# C - Bugged
N = int(input())
s = [int(input()) for i in range(N)]
s.sort()

ans = sum(s)
if ans % 10 != 0:
    print(ans)
else:

    for i in range(len(s)):
        if s[i] % 10 != 0:
            print(ans -s[i])
            exit()
        else:
            pass
    print(0)
"""

"""途中# C - GeT AC
N, Q = map(int, input().split())
S = str(input())
A = [list(map(int, input().split())) for i in range(Q)]
S1 = [0]*N
count = 0
for j in range(len(S)):
    if S[j] == 'A' and S[j + 1] == 'C':
        count += 1
    else:
        pass
    S1[j] = count
print(S1)

for k in range(Q):
    print(S1[A[k][1]-1]-S1[A[k][0]-1])

# for i in range(Q):
#     count = 0
#     ans = [k for k in S1 if A[i][0] <= k < A[i][1]]
#     print(len(ans))
    # for k in range(len(S1)):
    #     if A[i][0] <= S1[k] < A[i][1]:
    #         count += 1
    #     else:
    #         pass
    # print(count)

# for i in range(Q):
#     count = 0
#     for j in range(A[i][0]-1,A[i][1]-1):
#         if S[j] == 'A' and S[j+1] == 'C':
#             count += 1
#         else:
#             pass
#     print(count)
"""
"""# C - Exception Handling
N = int(input())
A = [int(input()) for i in range(N)]

#print(A)
max1 = sorted(A, reverse=True)
max2 = max1[0]

for i in range(N):
    if A[i] == max2:
        print(max1[1])

    else:
        print(max2)
"""

"""# C - 柱柱柱柱柱
N = int(input())
a = list(map(int, input().split()))
dp = [float('inf')]*N

dp[0] = 0
for i in range(1,N):
    if i == 1:
        dp[1] = abs(a[1]-a[0])
    else:
        dp1 = dp[i - 1]+abs(a[i]-a[i-1])
        dp2 = dp[i - 2]+abs(a[i]-a[i-2])
        if dp1 <= dp2:
            dp[i] = dp1
        else:
            dp[i] = dp2

#print(a,dp)
print(dp[N-1])
"""

"""途中# C - ID
from operator import itemgetter

N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(M)]

for l in range(M):
    A[l].insert(0, l)

# print(A)
A.sort(key=itemgetter(2))
A.sort(key=itemgetter(1))
# print(A)

ID1 = [['0' for i in range(2)] for j in range(M)]
ID2 = [['0' for i in range(2)] for j in range(M)]
# print(ID1)

for i in range(M):
    ID1[i][0] = str(A[i][0])
    ID1[i][1] = str(A[i][1])
    while len(ID1[i][1]) < 6:
        ID1[i][1] = "0" + ID1[i][1]
ID1.sort(key=itemgetter(1))
# print(ID1)

count = 1
for j in range(1, M+1):
    if j <= M - 1:
        ID2[j - 1][0] = str(A[j - 1][0])
        if A[j - 1][1] == A[j][1]:
            ID2[j - 1][1] = str(count)
            count += 1
        else:
            ID2[j - 1][1] = str(count)
            count = 1
        while len(ID2[j - 1][1]) < 6:
            ID2[j - 1][1] = "0" + ID2[j - 1][1]
    else:
        ID2[M-1][0] = str(A[M-1][0])
        if A[M-1][1] == A[j - 2][1]:
            ID2[M-1][1] = str(count)
        else:
            ID2[M-1][1] = str(1)
        while len(ID2[M-1][1]) < 6:
            ID2[M-1][1] = "0" + ID2[M-1][1]

# print(ID2)

ID1.sort(key=itemgetter(0))
ID2.sort(key=itemgetter(0))

for n in range(M):
    ans = str(ID1[n][1])+str(ID2[n][1])
    print(ans)

#
# while len(ID2) <= 6:
#     ID2 = "0" + ID2
#
# ID = ID1+ID2
#
# print(A)
# print(ID)
"""
"""未完# C - GCD on Blackboard
N = int(input())
A = list(map(int, input().split()))
GCD = 0
A.sort(reverse=True)
print(A)
GCD = A[0]-A[N-1]

for i in range(1, N):
    if A[i]-A[i+1] == GCD:
        pass
    else:
        A[i+1] = A[i]
"""

"""# C - Big Array
from operator import itemgetter
N, K = map(int,input().split())
A = [list(map(int, input().split())) for i in range(N)]
S = 0
A.sort(key=itemgetter(0))

for i in range(N):
    S += A[i][1]
    if S >= K:
        print(A[i][0])
        exit()
    else:
        pass
"""

"""# C - 怪文書 / Dubious Document 未完
import collections
n = int(input())
S = [list(str(input())) for i in range(n)]
print(S)

S.sort(key=len)
print(S)

A = collections.Counter(S[0])
B = collections.Counter(S[1])
print(A,B)
print(A.keys(),B.keys())
"""
"""# C - All Green 未完
D, G = map(int, input().split())
p = [list(map(int, input().split())) for i in range(D)]

score = 0
count = 0

for i in range(D-1, -1, -1):
    while score <= G:
        for j in range(p[i][0]):
            score += 100 * (i + 1)
            count += 1
            if j == p[i][0]:
                score += p[i][1]
            else:
                pass

print(D,G,p,p[0][0])
print(count)
"""
"""# C - Train Ticket 桁ごとにリスト格納
A = str(input())
l = [int(x) for x in list(str(A))]
if l[0]+l[1]+l[2]+l[3] == 7 :
    print('{0}+{1}+{2}+{3}=7'.format(l[0],l[1],l[2],l[3]))
elif l[0]-l[1]+l[2]+l[3] == 7 :
    print('{0}-{1}+{2}+{3}=7'.format(l[0], l[1], l[2], l[3]))
elif l[0]+l[1]-l[2]+l[3] == 7 :
    print('{0}+{1}-{2}+{3}=7'.format(l[0], l[1], l[2], l[3]))
elif l[0]+l[1]+l[2]-l[3] == 7:
    print('{0}+{1}+{2}-{3}=7'.format(l[0], l[1], l[2], l[3]))
elif l[0]-l[1]-l[2]+l[3] == 7:
    print('{0}-{1}-{2}+{3}=7'.format(l[0], l[1], l[2], l[3]))
elif l[0]+l[1]-l[2]-l[3] == 7:
    print('{0}+{1}-{2}-{3}=7'.format(l[0], l[1], l[2], l[3]))
elif l[0]-l[1]+l[2]-l[3] == 7:
    print('{0}-{1}+{2}-{3}=7'.format(l[0], l[1], l[2], l[3]))
elif l[0]-l[1]-l[2]-l[3] == 7:
    print('{0}-{1}-{2}-{3}=7'.format(l[0], l[1], l[2], l[3]))
"""

"""# C - Many Medians
import copy
N = int(input())
X = list(map(int, input().split()))
X2 = []

X2 = copy.copy(X)
X2.sort(reverse=True)
Xm_1 = X2[N//2]
Xm_2 = X2[(N//2)-1]
print(Xm_1,Xm_2)

for i in range(N):
    if X[i] <= Xm_1:
        print(Xm_2)
    else:
        print(Xm_1)
"""

"""# C - Splitting Pile
N = int(input())
a = list(map(int, input().split()))
sum_s = a[0]
tmp = sum(a)
sum_a = tmp - sum_s
ans = abs(sum_s - sum_a)

for i in range(1,N):
    sum_a = tmp - sum_s
    if ans > abs(sum_s - sum_a):
        ans = abs(sum_s - sum_a)
        sum_s += a[i]
    else:
        sum_s += a[i]
print(ans)
"""

# for i in range(1,N):
#     if sum_s < tmp:
#         sum_s += a[i]
#         if sum_s > tmp:
#             sum_s -= a[i]
#             break
#     else:
#         break
# sum_a = sum(a) - sum_s
# ans = abs(sum_s - sum_a)
# print(ans)

"""# C - Prison
N, M = map(int, input().split())
L = [list(map(int, input().split())) for i in range(M)]
print(N,M,L,L[0],L[0][1])
new_L = []
new_R = []
for i in range(M):
    new_L.append(L[i][0])
    new_R.append(L[i][1])
print(new_L,new_R)
if min(new_R) - max(new_L) >= 0:
    ans = min(new_R) - max(new_L) + 1
else:
    ans = 0
print(ans)
"""

"""# C - Christmas Eve
N, K = map(int, input().split())
h = [int(input()) for i in range(N)]
H = list(h)
H.sort(reverse=True)
print(H)
ans = H[0]-H[N-1]
tmp = 0
for i in range(len(H)-K+1):
    tmp = H[i]-H[i+K-1]
    if ans >= tmp:
        ans = tmp
    else:
        pass
print(ans)
"""

"""# C - Good Sequence
import collections
N = int(input())
a = list(map(int, input().split()))
count = 0

a_1 = collections.Counter(a)
print(a_1)
for k,v in a_1.items():
    if k <= v:
        count += v-k
    else:
        count += v

print(count)


# for i in range(N):
#     if a[i] == a.count(a[i]):
#         pass
#     else:
#         a[i] = ''
#         count += 1
#
# print(count)

"""

""""途中？# C - Sequence
n = int(input())
a = list(map(int, input().split()))
count = 0

for i in range(n):
    if sum(a[0:i+1]) != 0 and a[i-1]*a[i] < 0:
        pass
    else:
        if a[i-1]*a[i] >= 0:
            while a[i-1]*a[i] < 0:
                a[i] = a[i]-1
                count = count + 1
                if sum(a[0:i + 1]) != 0:
                    break
        else:
            while sum(a[0:i+1]) != 0 and a[i-1]*a[i] < 0:
                a[i] = a[i]+1
                count = count + 1
                if sum(a[0:i + 1]) != 0:
                    break
print(count)
"""

"""途中# C - GCD on Blackboard
N = int(input())
A = list(map(int, input().split()))
GCD = 0
A.sort(reverse=True)
print(A)
GCD = A[0]-A[N-1]

for i in range(1, N):
    if A[i]-A[i+1] == GCD:
        pass
    else:
        A[i+1] = A[i]
"""

"""
# Go Home
S = int(input())
count = 0
for t in range(S):
    if (t*(t+1))/2 >= S:
        break
    else:
        count = count + 1

print(count)
"""
