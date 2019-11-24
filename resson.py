# D - Disjoint Set of Common Divisors
import math
A, B = map(int, input().split())

d = math.gcd(A,B)

for i in range(d):



print(math.gcd(A,B))
"""# Triangle
S = int(input())

# Sを満たす長方形の３点を出力する
A =[]
B =[]
C =[]

A = (0, 0)
B = (1, 0)
C = (1, S)



print(A[0],A[1],B[0],B[1],C[0],C[1])
"""

"""# Anti-Division

A, B, C, D = map(int, input().split())


# 最大公約数
def gcd(C, D):
    while D != 0:
        C, D = D, C % D
    return C


w = B // C
x = B // D
y = (A - 1) // C
z = (A - 1) // D
a = B // (C * D // gcd(C, D))
b = (A - 1) // ((C * D) // gcd(C, D))

ans = (B - A + 1) - ((w - y) + (x - z) - (a - b))
print(ans)

#    if i % C > 0 and i % D > 0:
#      count = count + 1
#    else:
#       pass
# print(count)

# 割り切れる数を見つけたら、そこからCやDの数だけiを飛ばしたものが数になる。
"""

"""# Bite Eating
N, L = map(int,input().split())
aji = 0
for i in range(1, N+1):
    if i == 1:
        aji = aji
    elif i == N:
        if L + i - 1 <= 0:
            aji = aji + (L + 1 - 1) # N番目の味がマイナスの場合、N番目のリンゴを食べて1番目のリンゴは残す
        else:
            aji = aji + (L + i - 1)
    else:
        if L + i - 1 == 0:
            aji = aji + L
        else:
            aji = aji + (L + i - 1)

print(aji)
"""

"""# Security
N = str(input())

for i in range(len(N)-1):
    if N[i] == N[i+1]:
        print('Bad')
        exit()
    else:
        pass
print('Good')

"""

"""# Divide the Problems
N = int(input())
d = list(map(int, input().split()))

d = sorted(d)
print(N,d)

if N % 2 == 1: # 奇数個の場合は同じ数にならない
    print(0)
else:
    n = int(N / 2) #半分の数
    if d[n-1] == d[n]:
        print(0)
    else:
        ans = d[n] - d[n-1]
        print(ans)
"""

"""#  Ordinary Number
N = int(input())
A = list(map(int, input().split()))
count = 0
for i in range(1, N-1):
    if A[i-1]< A[i]< A[i+1] or A[i+1] < A[i] < A[i-1]:
        count = count + 1
    else:
        pass

print(count)
"""

"""# Fifty-Fifty
# set関数を使用しても良い
# print("Yes" if len(set(input()))==2 else "No")


S = str(input())

count = 1
ans = 0
for i in range(4):
    print(S[i])
    for j in range(i+1, 4):
        if S[i] == S[j]:
            count = count + 1
            if count == 2:
                count = 1
                ans = ans + 1
            else:
                pass
        else:
            pass
if ans == 2:
    print("Yes")
else:
    print("No")
"""

"""# Green Bin
N = int(input())
# S = str(input())
S = [list(map(str, input().split())) for i in range(N)]

for l in range(N):
    S[l] = list(str(S[l]))
    S[l] = sorted(S[l])
S = sorted(S)
print(S)
count = 0

for i in range(N-1):
    if i == 0:
        k = i + 1
    for j in range(k, N):
        if S[i] == S[j]:
            count = count + 1
        else:
            for m in range(count):
                count =count * i
            k = j + 1
            break
print(count)

# for i in range(N):
#    S[i].sort()
#print(S)

"""

"""# One Clue
N, X = map(int,input().split())

ans_1 = X-N+1
ans_2 = X+N
ans_int = list(range(ans_1, ans_2, 1))

ans=[str(a) for a in ans_int]
ans=" ".join(ans)
print(ans)
"""

""""# - +-x- +-x
A, B = map(int,input().split())

print(max(A+B,A-B,A*B))
"""
"""
# Candies
N = int(input())
X = [list(map(int, input().split())) for i in range(2)]

ans = []
print(N,X)
ans1 = X[0][0]
for i in range(1): # 下にいくタイミング
    for j in range(N-1): #横に行く足し合わせ
        ans1 = ans1 + X[i][j]
        if i == 0 and j == 2:
            ans1 = ans1 + X[1][2]
            break
        elif i == 1 and j == 2:
    ans.append(ans1)


ans = X[0][0]+X[0][1]+X[0][2]+X[1][2]
ans = X[0][0]+X[0][1]+X[1][1]+X[1][2]
ans = X[0][0]+X[0][1]+X[1][1]+X[1][2]
ans = X[0][0]+X[1][0]+X[1][1]+X[1][2]


print(ans)
"""

"""# Dice and Coin
N, K = map(int,input().split())
# N サイコロの面
# K 得点
K3 = []
ans = 0
count = 0  #コイン振る回数 MAX

for i in range(1, N+1):
    K1 = i
    K2 = 0
    count = 0
    while K1 < K:
        K1 = 2 * K1
        count = count + 1
    K2 = 1/N * (1/2)**count
    K3.append(K2)

for k in range(N):
    ans = ans + K3[k]
print(ans)

"""

""""# YYMM or MMYY
S = int(input())

A = S // 100
B = S - (A* 100)
# YY確認
if 1 <= A <= 12:
    if 13 <= B <= 99 or B == 0:
        print('MMYY')
    else:  #1 <= B <= 12
        print('AMBIGUOUS')
elif 1 <= B <= 12:
    if 13 <= A <=99 or A == 0:
        print('YYMM')
    else: #1 <= B <= 12
        print('AMBIGUOUS')
else:
    print("NA")
"""

"""#  Changing a Character
N, K = map(int,input().split())
S = str(input())

# N = 4
# K = 3
# S = 'CABA'
S2 = ''

for i in range(len(S)):
    if i == K-1:
        S2 = S2 + S[K-1].replace('A', 'a').replace('B', 'b').replace('C', 'c')
    else:
        S2 = S2 + S[i]

print(S2)

# 見本
# n,k = map(int, input().split())
# s = str(input())
#
# print(s[:k-1]+s[k-1].lower()+s[k:])
"""

"""# Remainder Minimization 2019

L, R = map(int,input().split())
a = []

for i in range(L, R):
    for j in range(i+1,R+1):
        a.append((i*j)%2019)
        if (i*j)%2019 == 0:
            print("0")
            exit()

print(min(a))

# L, R = map(int, input().split())
# ans = 0
# ans_a = 0
# ans_b = 0
#
# for i in range(L, R):
#     a = i % 2019
#     if ans_a == 0:
#         ans_a = a
#     elif ans_a > a:
#         ans_a = a
#     else:
#         pass
#
# for j in range(L+1, R+1):
#     b = j % 2019
#     if ans_b == 0:
#         ans_b = b
#     elif ans_b > b:
#         ans_b = b
#     else:
#         pass
#
# ans = ans_a * ans_b
# print(ans)
"""

"""# Good Distance
# import math
# N,D = map(int,input().split())
# X = [list(map(int,input().split())) for i in range(N)]
# a = []
# for l in range(N-1):
#     for j in range(l+1,N):
#         b = 0
#         for k in range(D):
#             b += (X[l][k]- X[j][k])**2
#         a.append(math.sqrt(b))
# c = 0
# for m in range(len(a)):
#     if len(str(a[m])) <=5:
#         c += 1
# print(c)



# N, D = map(int, input().split())
# #X = [int(input()) for i in range(N)]
# X = []
# for l in range(N):
#     X.append(list(map(int, input().strip().split())))
#
# print(X)
# r = []
# for i in range(N-1): # 点を動かす
#     for j in range(i+1, N): # もう片方の点を動かす
#         r0 = 0
#         for k in range(D): # 座標の成分を動かす
#             r0 += (X[i][k] - X[j][k]) ** 2
#         r1 = r0 **0.5
#      #r1 = r0 ** 0.5
#         r.append(r1)
# count = 0
# for i in range(len(r)):
#     if r[i].is_integer():
#         count += 1
#     else:
#         pass
# print(count)


print(r)
# r[i] = r0 ** 0.5
# r[i] = ((X[i][j] - X[1][0]) ** 2 + (X[0][1] - X[1][1]) ** 2) ** 0.5

# r1 = ((X[0][0] - X[1][0]) ** 2 + (X[0][1] - X[1][1]) ** 2) ** 0.5
# print(r1)
#
# X1 = [1, 2]
# X2 = [5, 5]
# X3 = [-2, 8]
#
# r1 = ((X1[0]-X2[0])**2+(X1[1]-X2[1])**2)**0.5
# print(r1)

"""

"""# T or T
N, A, B = map(int, input().split())
Train = A * N

if Train <= B:
    print(Train)
else:
    print(B)"""

"""# Shiritori

A, B, C = map(str, input().split())

if A[-1] == B[0] and B[-1] == C[0]:
    print("YES")
else:
    print("NO")"""

"""# Expired?
X, A, B = map(int, input().split())


if B - A <= 0:
    print('delicious')
elif 0 < B - A <=X:
    print('safe')
else:
    print('dangerous')
"""

""""# Choose Integers
A, B, C = map(int, input().split())
a = 0

for i in range(1, B):
    a = A*i % B
    if C == a:
        print("YES")
        exit()
    else:
        pass
print("NO")
"""

"""# Trained?
N = int(input())
a = [int(input()) for k in range(N)]

i = a[0]
count = 1

while count <= N:
    if a[0] == 2:
        print(count)
        exit()
    elif a[i-1] == 2:
        count = count + 1
        print(count)
        exit()
    else:
        i = a[i - 1]
        count = count + 1

print(-1)
"""

"""# Between a and b ...

a, b, x = map(int, input().split())
# a = 9
# b = 9
# x = 2

c = a // x
print(c)
if a == 0:
    ans = (b // x) + 1
else:
    ans = (b // x) - ((a - 1) // x )
    print(a - 1)
print(ans)


# if a % x == 0:
#     for i in range(a, b+1, x):
#         count.append(i)
# else:
#     c = a % x
#     a = a + c
#     for k in range(a, b+1, x):
#         count.append(k)
# print(len(count))
"""

""" # Painting Balls with AtCoDeer
N, K = map(int, input().split())
# N = 10
# K = 8
ans = 0
# i=0の色はK i<=1の色の選択肢はK-1
# K*(K-1)*(K-1)... N回積をとる

# for i in range(1, N+1):
#     if i == 1:
#         ans = K
#     else:
#         ans = ans*(K-1)
ans = K*(K-1)**(N-1)
print(ans)
"""

""""# Training CampTraining Camp
N = int(input())

p = 1
for i in range(1, N+1):
    p = p * i
    p = float(p % (10**9 + 7))

# p = float(p % (10**9 + 7))
print(int(p))
"""

"""# Build Stairs
N = int(input())
H = list(map(int,input().split()))

# N = 4
# H = [1,3,2,1]

for i in range(1, N):
    H[i] = H[i] - 1
    if H[i] < H[i-1]:
        H[i] = H[i] + 1
    else:
        pass

count = 0
for j in range(N-1):
    if H[j] <= H[j+1]:
        count = count + 1
    else:
        count = -1
        break

if 0 <= count <= N:
    print("YES")
else:
    print("NO")
"""

"""# Uneven Numbers
A = int(input())

#A = 100000
A1 = str(A)
print(int(len(A1)))
count = 0
for i in range(1, A+1):
    A2 = str(i)
    if len(A2) % 2 == 0 :
        pass
    else:
        count = count + 1
print(count)
"""

"""# Transfer
A = list(map(int, input().split()))

#A = [12, 3, 7]

b = A[0] - A[1]  # bの残
c = A[2] - b
if c >= 0:
    pass
else:
    c = 0

print(c)
"""

""" # Two Switches
A = list(map(int, input().split()))

# A = [10, 90, 20, 80]

time = 0

if A[1] >= A[2] or A[3] >= A[0]:
    # Aliceが先に押した場合
    if A[1] >= A[3] >= A[2] >= A[0]:
        time = A[3] - A[2]
    elif A[3] >= A[1] >= A[2] >= A[0]:
        time = A[1] - A[2]
    # Bobが先に押した場合
    elif A[3] >= A[1] >= A[0] >= A[2]:
        time = A[1] - A[0]
    elif A[1] >= A[3] >= A[0] >= A[2]:
        time = A[3] - A[0]
    else:
        time = 0
else:
    time = 0

print(time)
"""

""" # Swap 0 or 1 Swap

N = int(input())
p = list(map(int, input().split()))

# N = 5
# p = [1, 2, 3, 4, 5]

pn = sorted(p)

count = 0
for i in range(N):
    if p[i] == pn[i]:
        pass
    else:
        count = count + 1

print(p, pn, count)
if count == 2 or count == 0:
    print('YES')
else:
    print('NO')

"""
