#

"""#D - Poker
import collections
K = int(input())
S = input()
T = input()
N = [K]*9
S_N = []
T_N = []

#Sの手
for i in range(1,10):
    a = str(i)
    S_N.append(S.count(a))
    N[i-1] -= S.count(a)
print(S_N)
print(N)
S_1 = 0
for j in range(9):
    S_1 += (j+1) * 10**S_N[j]



#Tの手
for i in range(1,10):
    b = str(i)
    T_N.append(T.count(b))
    N[i - 1] -= T.count(b)
print(T_N)

T_1 = 0
for j in range(9):
    T_1 += (j+1) * 10**T_N[j]

print(S_1)
print(T_1)
print(N)


for i in range(N):"""



# for i in range(1,10):
#     for j in range(0,4):
#         if i == s[]

"""#C - Unexpressed
N = int(input())
A = []

for i in range(2,int(N**0.5)+2):
    for j in range(2,35):
        if i**j <= N:
            A.append(i**j)
        else:
            break
A =set(A)
B = len(A)
#print(A)
print(N-B)"""




"""#B - Play Snuke
N = int(input())
A =[list(map(int, input().split())) for _ in range(N)]

m = 10**10
for i in range(N):
    d = A[i][2] - A[i][0]
    if d > 0:
        m =min(m,A[i][1])

if m == 10**10:
    print(-1)
else:
    print(m)"""


"""#A - Discount
A,B = map(int, input().split())
print((A-B)/A*100)

"""
"""#B - A^B^C
A,B,C = map(int, input().split())
DP = []
for i in range(1,11):
    DP.append((A**i) % 10)

a = DP[0]
for j in range(1,len(DP)):
    if DP[j] == a:
        count = j
        break

print(DP)
print(count)
print(B % count,C % count)
x = ((B % count) ** (C % count))



print(x)
if (B % count) == 0 and (C % count) == 0:
    print(DP[count-1])
    exit()


if x % count == 0:
    print(DP[count-1])
else:
    x = x % count
    print(DP[x-1])"""


"""#A - A*B*C
N = int(input())
ans = 1

def factorization(n):
    arr = []
    temp = n
    a = 0
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
            a += cnt

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return a
for i in range(2,N):
     = factorization(i)
    fa



print(factorization(N))"""


"""#B - -- - B
B,C = map(int, input().split())

if C == 1:
    print(1+1)
    exit()
elif C == 2:
    print(1+2)
    exit()
else:
    pass

if B > 0:
    print(C+abs(B-2)*2)
else:
    print(C + abs(B-2) * 2+1)
"""

"""# A - B = C
T = int(input())
A =[list(map(int, input().split())) for _ in range(T)]

for i in range(T):
    print(((A[i][1]-A[i][0]-1)*(A[i][1]-A[i][0]))//2)

"""


"""#D - Circle Lattice Points
import math
X,Y,R = map(float, input().split())
X =X*10**4
Y =Y*10**4
R =R*10**4

ans = 0
x_1 = math.ceil(X-R)
x_2 = math.floor(X+R)
x_1 = int(X-R)
x_2 = int(X+R)
print(x_1,x_2)
#
# x_1 = int(X-R)
# x_2 = int(X+R)
# y_1 = int(Y-R)
# y_2 = int(Y+R)
#
# print(x_1,x_2,y_1,y_2)

# for i in range(x_1,x_2+1):
#     for j in range(y_1,y_2+1):
#         if (i-X)**2 + (j-Y)**2 <= R**2:
#             ans += 1
#         else:
#             pass

for i in range(x_1,x_2+1):
    p = (R**2-(X-i)**2)**0.5
    # low = int(math.ceil(p-R))
    # high = int(math.floor(p+R))
    low = math.ceil(Y-p)
    high = math.floor(p+Y)
    ans += high - low

print(ans)
#
# for j in range(y_1, y_2 + 1):
#
#         if (i-X)**2 + (j-Y)**2 <= R**2:
#             ans += 1
#         else:
#             pass
# print(ans)
"""

"""#C - Digital Graffiti
H,W = map(int, input().split())"""


"""#B - Remove It
N,X = map(int, input().split())
A = list(map(int,input().split()))
B =[]
for i in range(N):
    if A[i] == X:
        pass
    else:
        B.append(A[i])

print(*B)
"""
"""#A - Vanishing Pitch
V,T,S,D = map(int, input().split())

if D >= V*T and V*S >= D:
    print("No")
else:
    print("Yes")"""

"""#D - Staircase Sequences
N = int(input())
ans = 0
T = 0
for i in range(1,int(N**0.5)+1):
    if N % i == 0 and (i-1)%2 == 0:
        ans += 1
    elif (2*N - (i**2-i))%(2*i) == 0:
        ans += 1
    else:
        pass

    if (N / i) - (i-1)/2 == 0:
        if N % i == 0 or (i-1)%2 == 0:
            ans += 1
    else:
        pass

# for i in range(int(N**0.5)+1):
#     if ((i+1)**2-(i+1)) % 2 == 0 and ((i+1)**2-(i+1)) % 2 < N:
#         ans += 1
#     else:
#         pass
print(ans*2)"""


# N=int(input())
# i=2
# ans=dict()
# div_sum=1
#
# while i*i <=N:
# 	while n%i==0:
# 		n=n//i
# 		if i in ans:
# 			ans[i]+=1
# 		else:
# 			ans[i]=1
# 	i+=1
# if n!=1:
# 	ans[n]=1
#
# ans_list=list(ans.items())
# for j in ans_list:
# 	div_sum*=j[1]+1
# print(ans)
#
# N=int(input())
# yaku=list()
# i=1
# while i*i<=N:
# 	if N%i==0:
# 		yaku.append(i)
# 		yaku.append(N//i)
# 	i+=1
# yaku.sort()
# print(yaku)
# ans = 0
# for i in range(len(yaku)):
#     if (yaku[i]-1) % 2 == 0:
#         ans += 1
#     else:
#         pass
# print(ans)


"""#C - Bowls and Dishes
N,M = map(int, input().split())
A =[list(map(int, input().split())) for _ in range(M)]
K = int(input())
C =[list(map(int, input().split())) for _ in range(K)]

DP = [0]*N
for i in range(K):
"""
"""#B - Magic 3
N,S,D= map(int, input().split())
A =[list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    if A[i][0] < S and A[i][1] > D:
        print("Yes")
        exit()
    else:
        pass

print("No")
"""

"""#A - Very Very Primitive Game
A,B,C= map(int, input().split())
if C == 0:
    if A-1>=B:
        print("Takahashi")
    else:
        print("Aoki")

else:
    if B-1>=A:
        print("Aoki")
    else:
        print("Takahashi")"""


"""#C - オセロ
N,Q= map(int, input().split())
A =[list(map(int, input().split())) for _ in range(Q)]
s = [0]*N
for i in range(Q):
    for j in range (abs(A[i][0]-A[i][1])):
        if s[j] == 0:
            s[j] = 1
        else:
            s[j] = 0

print("".join([str(n) for n in s]))"""

"""#B - ドローン
S = input()
T =int(input())
x = 0
y = 0
z = 0
for i in range(len(S)):
    if S[i] == "L":
        x -= 1
    elif S[i] == "R":
        x += 1
    elif S[i] == "U":
        y += 1
    elif S[i] == "D":
        y -= 1
    else:
        if T == 1:
            z += 1
        else:
            z -= 1

if T ==1:
    ans = abs(x)+abs(y)+z
else:
    ans = max(abs(x)+abs(y)+z,abs(abs(x)+abs(y)+z)%2)

print(ans)"""




"""#C - 経路
import math
w,h= map(int, input().split())

W = math.factorial(w-1)
H = math.factorial(h-1)
WH = math.factorial(w+h-2)
W_H = W*H

ans = (WH//W_H) % (10**9+7)
print(ans)"""

"""#B - ペア
n =int(input())

if n % 2 == 0:
    print(n-1)
else:
    print(n+1)"""

"""#A - テレビ
w,h= map(int, input().split())
if w/h == 4/3:
    print("4:3")
else:
    print("16:9")"""

"""#A - テスト
x,y= map(int, input().split())
if x < y:
    print("Better")
else:
    print("Worse")
"""

"""#C - Mandarin Orange
N = int(input())
A = list(map(int,input().split()))
ans = 0
DP = 0
for i in range(N):
    DP = 0
    for j in range(i,N):
        if A[j] >= A[i]:
            DP += A[i]
        else:
            DP = A[i] * (j-1 - i+1)
            break


    if DP >= ans:
        ans = DP
if A[N-1] > ans:
    ans = A[N-1]

print(ans)"""

"""#B - Alcoholic
N,X= map(int, input().split())
A = [list(map(float, input().split())) for i in range(N)]
alc = 0
X = float(X)
for i in range(N):
    alc += A[i][0]*A[i][1]
    if alc > X*100:
        print(i+1)
        exit()
    else:
        pass

print(-1)"""


"""#A - Slot
C = input()
if C[0]==C[1] == C[2]:
    print("Won")
else:
    print("Lost")"""

"""#B - Mex Boxes
N,K= map(int,input().split())
A = list(map(int,input().split()))
A.sort()
B = []
cn = 0

maxA =max(A)
ans = 0
n = A.count(0)
if K >= n:
    c = n
else:
    c = K




for i in range(maxA+1):
    if A.count(0) == 0:
        break

    if A.count(i) < A.count(i+1):
        cn = A.count(i)
        B.append(i + 1)
    elif

    if A.count(i) == 1:
        B.append(i+1)

    if A.count(i) == 0:
        break

print(B)

print(sum(B))"""


# for _ in range(c):
#     if A.count(0) == 0:
#         break
#     for i in range(maxA+1):
#         if A.count(i) == 0:
#             break
#         m = i+1
#         if A.count(m) == 0:
#             ans += m
#             A.remove(i)
#         else:
#             if A.count(i) == 0:
#                 break
#             else:
#                 A.remove(i)


"""#A - Two Sequences 2
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A_2 =[]
C = []
maxA=0
max = 0

for i in range(N):
    if maxA <= A[i]:
        maxA = A[i]
    else:
        pass
    A_2.append(maxA)
#print(A_2)

for j in range(N):
    if max <= A_2[j]*B[j]:
        max = A_2[j]*B[j]
    C.append(max)

for k in range(len(C)):
    print(C[k])
"""

""""#B - Reversible Cards
N = int(input())
A =[list(map(int, input().split())) for _ in range(N)]
ANS = [0]*N

for i in range(N):
    if
    """
"""#
N,M= map(int,input().split())

# ans = ((10**N)//M)%M
# print(ans)
for M in range(1,21):
    ans = ((10**N)//M)%M
    print(M,ans)"""

"""#D - Choose Me
N = int(input())
A =[list(map(int, input().split())) for _ in range(N)]
A_sum = 0
B_sum = 0
d = []
e = []
for i in range(N):
    A_sum += A[i][0]
    B_sum += A[i][1]
    d.append(A[i][0])
    e.append(A[i][0]+A[i][1])
SUM_AB = A_sum +B_sum

d.sort(reverse=True)
e.sort(reverse=True)
d_1 = 0
ans = 0
B_sum = 0

for j in range(N):
    B_sum += e[j]
    ans += 1
    if B_sum > (A_sum/ 2):
        print(ans)
        exit()
    else:
        pass


print(A_sum,B_sum,d)"""



"""#C - 1-SAT
N = int(input())
S = [input() for _ in range(N)]
S_1 = []
U = []
for i in range(N):
    if S[i][0] == "!":
        U.append(S[i].replace("!",""))

    else:
        S_1.append(S[i])
#print(U)
#print(S_1)
a = set(U) & set(S_1)

V = len(a)
if V == 0:
    print("satisfiable")
else:
    print(a.pop())"""

"""#B - Gentle Pairs
N = int(input())
A =[list(map(int, input().split())) for _ in range(N)]
count = 0

for i in range(N):
    for j in range(i+1,N):
        t = abs(A[i][1]-A[j][1]) / abs(A[i][0]-A[j][0])
        if t <= 1:
            count += 1
        else:
            pass

print(count)
"""

"""#A - Large Digits
A,B = map(str,input().split())

sum_A = int(A[0])+int(A[1])+int(A[2])
sum_B = int(B[0])+int(B[1])+int(B[2])

print(max(sum_A,sum_B))
"""
"""#E - Throne
T = int(input())
A =[list(map(int, input().split())) for _ in range(T)]

for i in range(T):
    if (A[i][0] - A[i][1]) > A[i][2]:
        if (A[i][0] - A[i][1]) % A[i][2] != 0:
            print(-1)
        else:
            print((A[i][0] - A[i][1]) // A[i][2])
    else:
        if A[i][2] % (A[i][0] - A[i][1]) != 0:
            print(-1)
        else:
            print(A[i][2] // (A[i][0] - A[i][1]))


"""



"""#D - Sum of difference
N = int(input())
A = list(map(int,input().split()))

ans = 0
A.sort()
b = 0

for i in range(1,N):
    b -= A[i-1]
    ans += A[i]*i + b

print(ans)"""

"""#C - Unlucky 7

N = int(input())
n = ""
a = []
b = []
e = 0
for i in range(1,N+1):
    n = str(i)
    if '7' in n:
        a.append(i)

for j in range(1,N+1):
    e = str(oct(j))
    if '7' in e:
        b.append(j)
print(N - len(set(a + b)))"""

"""#B - Blocks on Grid
H,W = map(int,input().split())
A =[list(map(int, input().split())) for _ in range(H)]
L = H*W
a = 0
b = 99999
for i in range(H):
    for j in range(W):
        a += A[i][j]
        if b >= A[i][j]:
            b = A[i][j]
print(a - b*L)"""



"""#A - Brick
N,W= map(int,input().split())

print(N//W)"""

"""#D - Stamp
import math
N,M= map(int,input().split())
if M == 0:
    print(1)
    exit()
a = list(map(int,input().split()))
ans = 0
a.sort()
if a[0] - 1 >= 0:
    a_1 = [a[0]]
else:
    pass
for i in range(M-1):
    if a[i+1]-a[i] > 1:
        a_1.append(a[i+1]-a[i])
if N-a[M-1] > 1:
    a_1.append(N-a[M-1])
print(a_1)

if min(a_1) >= 2:
    b = min(a_1)-1
else:


for i in range(M):
    ans += int(math.ceil((a_1[i]-1) / b))

print(ans)"""

"""#C - Duodecim Ferra
L = int(input())"""


"""#B - Smartphone Addiction
N,M,T= map(int,input().split())
A =[list(map(int, input().split())) for _ in range(M)]

a = N
a -= A[0][0]
if a <= 0:
    print("No")
    exit()

if M == 1:
    if N - a >= (A[0][1] - A[0][0]):
        a += (A[0][1] - A[0][0])
    else:
        a = N
else:
    for j in range(M-1):
        if a <= 0:
            print("No")
            exit()
        if a >= N:
            pass
        elif N - a >= (A[j][1] - A[j][0]):
            a += (A[j][1] - A[j][0])
        else:
            a = N
        a -= A[j+1][0] - A[j][1]

    a += (A[M-1][1] - A[M-1][0])

if T-A[M-1][1] < a :
    print("Yes")
else:
    print("No")"""

"""#A - ABC Preparation
a,b,x,y= map(int,input().split())

print(min(a,b,x,y))"""

"""#B - Many 110
N = int(input())
T = input()

if '010' in T or '00' in T or '111' in T:
    print(0)
    exit()

if T == "0" or T == "10" or T == "11" or T == "110":
    print(10**10)
    exit()
elif T == "1":
    print(2*(10**10))
    exit()
elif T == "01" or T == "011" or T == "101":
    print(10**10-1)
    exit()
else:
    pass
if N % 3 ==0 and T.startswith("110"):
    print(10 ** 10 - ((N // 3)-1))
else:
    print(10 ** 10 - (N//3))"""


# a = N // 3
# b = N % 3
#
# print(10**10 - b)

# #A - Redundant Redundancy
# N = int(input())
# a = [2,3,5,7,11,13,17,19,23,29]
#
# # for i in range(2,N):
# #     a += i*(N-i+1)
#
# print(a//N + 1)

"""#A - Hands
a,b,x,y= map(int,input().split())

h = abs(b-a)
ans = min(x*h,y*(h-1)+x,y*h+x)
print(ans)"""

"""#B - log
n = int(input())


if n == 1:
    print(1)
    exit()
elif n == 2:
    print(1)
    exit()
elif n == 3:
    print(2)
    exit()
else:
    pass
for i in range(int((2*(n+1))**0.5+1), 1,-1):
    if 2*(n+1) >= i*(i-1):
        print(n+2-i)
        exit()
    else:
        pass"""

# while a > 0:
#     a -= b
#     ans += 1
#     b -= 1
#
# print(ans)

"""#D - increment of coins
from scipy import special
A,B,C= map(int,input().split())
a=1
b=1
c=1
for i in range(100-A):
    a *= ((A+i)/(A+i+B+C))

x = special.comb(100-A, A,True)
a = x*a

for j in range(100-B):
    b *= ((B+j)/(A+B+j+C))
y = special.comb(100-B, B,True)
b = y*b

for k in range(100-C):
    c *= ((C+k)/(A+B+k+C))
z = special.comb(100-C, C,True)
c = (100-C)**C*c

ans = a+b+c

#ans = (100-A)*(A/(A+B+C)) +(100-B)*(B/(A+B+C))+(100-C)*(C/(A+B+C))

print(ans)"""

"""#C - Super Ryuma
r_1,c_1 = map(int,input().split())
r_2,c_2 = map(int,input().split())

b_1 = r_2 - r_1
b_2 = c_2 - c_1

ans = 0

if b_1 == 0 and b_2 == 0:
    print(ans)
    exit()
elif abs(b_1) == abs(b_2):
    ans += 1
    print(1)
    exit()
else:
    b_2 = b_2 - b_1
    b_1 = 0
    ans += 1

while b_2 >= 0:
    b_2 = b_2 - c_2
    ans += 1

# if c_2 - b_2:
#     ans += (b_2 // 3)
# else:
#     ans += (b_2 // 3)+1
print(ans)"""


"""#B - Quizzes
N,X = map(int,input().split())
S = input()
ans = X
for i in range(len(S)):
    if S[i] == 'o':
        ans += 1
    else:
        if ans == 0:
            pass
        else:
            ans -= 1
print(ans)"""

"""#A - Determinant
a,b = map(int,input().split())
c,d = map(int,input().split())

print(a*d-b*c)"""

"""#B - Abbreviate Fox
s =''
for i in range(100000):
    s += 'f'

for j in range(99999):
    s += 'ox'
s += 't'


N = 200000
S = s
N = int(input())
S = str(input())

for _ in range(int(N**0.5)):
    S = S.replace('fox', '')
    if 'fox' in S:
       pass
    else:
        print(len(S))
        exit()
print(0)"""




"""#A - Sum and Product
S,P = map(int,input().split())
for i in range(1,10**6+1):
    if (P % i) == 0:
        if (P/i)+i ==S:
            print("Yes")
            exit()
        else:
            pass

print("No")"""

"""#D - Water Heater
N,W = map(int,input().split())
T =[list(map(int, input().split())) for i in range(N)]
DP = [0]*(2*10**5+5)
MaxT = 2*10**5+5

T=sorted(T, reverse=False, key=lambda x: x[0])
#print(T)

for i in range(N):
    DP[T[i][0]] += T[i][2]
    DP[T[i][1]] -= T[i][2]

for j in range(MaxT-1):
    DP[j+1]+=DP[j]

for k in range(MaxT):
    if DP[k] > W:
        print("No")
        exit()
print("Yes")
"""


"""#C - Travel
import itertools
N,K= map(int,input().split())
T =[list(map(int, input().split())) for _ in range(N)]
l = [1,2,3]

nums = list(range(1,N))
count = 0
for v in itertools.permutations(nums):
    v = [0]+list(v)
    #print(v)
    ti = 0
    for i in range(N):
        #print(v[i])
        #print(T[v[i]][v[(i+1)%N]])
        ti += T[v[i]][v[(i+1)%N]]
    if ti == K:
        count += 1
print(count)"""



"""#B - Billiards
a,b,A,B= map(int,input().split())
print((A*b+a*B)/(B+b))"""

"""#A - ReLU
x = int(input())
if x >= 0:
    print(x)
else:
    print(0)"""

"""#D - Wandering
N = int(input())
A = list(map(int,input().split()))
ans = 0

for i in range(N):
    count = 0
    for j in range(N):
        if N-
        count += (i*) * A[j]
"""
"""#C - To 3
N = str(input())
A = []
B =[]
ans = 0

for l in range(len(N)):
    if int(N[l])  != 0:
        B.append(N[l])

if int(N) % 3 == 0:
    print(0)
    exit()
else:
    pass

for i in range(len(B)):
    if int(B[i]) % 3 == 0:
        pass
    else:
        A.append(int(B[i]) % 3)
if len(A) == 0:
    print(0)
    exit()
else:
    pass

#print(A)
a = sum(A) % 3

count = 0
for j in range(len(A)):
    if A[j] == a:
        count += 1
    else:
        pass
b =''
for m in range(len(B)):
    b += B[m]
if count >= 1 and int(b)>=3 :
    print(1)

else:
    print(-1)
"""

"""#B - Almost GCD
N = int(input())
a = list(map(int,input().split()))
ans = 0
ans_c = 0

import math

for j in range(1,max(a)+1):
    count = 0
    for i in range(N):
        if a[i] % (j+1) == 0:
            count += 1
        else:
            pass
    if ans_c <= count:
        ans = j+1
        ans_c = count
    else:
        pass

print(ans)
"""



"""#A - twiblr
A,B= map(int,input().split())

print(2*A+100-B)"""

"""#D - Hachi
A = input()
B = []
C = []

A_D = [0]*9
B_D = [0]*
from collections import Counter

for i in range(len(A)):
    A_D[int(A[i])-1] += 1


for j in range(100,1000):
    if j % 8 == 0:
        B.append(str(j))
        C.append(Counter(str(j)))
print(B)
print(C)

if len(A) < 3:
    if len(A) == 1:
        if int(A[0]) == 8:
            print("Yes")
        else:
            print("No")

    elif int(A[0]+A[1]) % 8 ==0 or int(A[1]+A[0]) % 8 ==0:
        print("Yes")
    else:
        print("No")

else:
    pass

for k in range(len(C)):
    if Counter(A) >= C[k]:
        print("Yes")
        exit()

print("No")

print(Counter(A))
"""





"""#C - Collinearity
N = int(input())
A =[list(map(int, input().split())) for i in range(N)]

import math

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N-2):
            if math.sqrt((A[i][1]-A[j][1])**2+(A[i][0]-A[j][0])**2) +math.sqrt((A[i][1]-A[k][1])**2+(A[i][0]-A[k][0])**2) ==math.sqrt((A[j][1]-A[k][1])**2+(A[j][0]-A[k][0])**2) or math.sqrt((A[i][1]-A[j][1])**2+(A[i][0]-A[j][0])**2) +math.sqrt((A[j][1]-A[k][1])**2+(A[j][0]-A[k][0])**2) ==math.sqrt((A[i][1]-A[k][1])**2+(A[i][0]-A[k][0])**2) or math.sqrt((A[i][1]-A[k][1])**2+(A[i][0]-A[k][0])**2) +math.sqrt((A[j][1]-A[k][1])**2+(A[j][0]-A[k][0])**2) ==math.sqrt((A[i][1]-A[j][1])**2+(A[i][0]-A[j][0])**2):
                print("Yes")
                exit()
print("No")"""

# for i in range(N-2):
#     for j in range(i+1,N-1):
#         for k in range(j+1,N):
#             if (((A[i][1]-A[j][1])**2+(A[i][0]-A[j][0])**2)**0.5 +((A[i][1]-A[k][1])**2+(A[i][0]-A[k][0])**2)**0.5 ==((A[j][1]-A[k][1])**2+(A[j][0]-A[k][0])**2)**0.5) or (((A[i][1]-A[j][1])**2+(A[i][0]-A[j][0])**2)**0.5 +((A[j][1]-A[k][1])**2+(A[j][0]-A[k][0])**2)**0.5 ==((A[i][1]-A[k][1])**2+(A[i][0]-A[k][0])**2)**0.5) or (((A[i][1]-A[k][1])**2+(A[i][0]-A[k][0])**2)**0.5 +((A[j][1]-A[k][1])**2+(A[j][0]-A[k][0])**2)**0.5 ==((A[i][1]-A[j][1])**2+(A[i][0]-A[j][0])**2)**0.5):
#                 print("Yes")
#                 exit()
# print("No")


"""#B - Trapezoid Sum
N = int(input())
A =[list(map(int, input().split())) for i in range(N)]
ans = 0
for i in range(N):
    ans += A[i][1]*(A[i][1]+1)/2 - (A[i][0]-1)*(A[i][0])/2

print(int(ans))"""

"""#A - Heavy Rotation
N = int(input())
if N % 2 == 0:
    print("White")
else:
    print("Black")"""

"""#B - Values
N,M= map(int,input().split())
a =list(map(int,input().split()))
b =list(map(int,input().split()))
c =[list(map(int, input().split())) for i in range(M)]
d =[]
e = []


for i in range(N):
    d.append(b[i] - a[i])

# print(d)
# print(sum(d))


if sum(a) == sum(b):
    print("Yes")
else:
    print("No")"""

# if sum(d) == 0:
#     print("Yes")
# else:
#     print("No")

"""#A - 106
N = int(input())

for i in range(1,40):
    for j in range(1,40):
        if N == 3**i +5**j:
            print(i,j)
            exit()
        else:
            pass
print(-1)"""

"""#E - Traveling Salesman among Aerial Cities
N = int(input())
x =[list(map(int, input().split())) for i in range(N)]
X = []
p1 = []
p2 = []
for i in range(N):
    for j in range(N):
        if i == j:
            pass
        else:
            X.append(abs(x[i][0]-x[j][0])+abs(x[i][1]-x[j][1])+max(0,x[i][2]-x[j][2]))
            p1.append(i)
            p2.append(j)

print(X)
print(p1)
print(p2)

df2 = pd.read_csv('../input/datal.csv')
"""


"""#D - Takahashi Unevolved
X,Y,A,B= map(int,input().split())
count = 0

while X < B:
    X = X*A
    if X >= Y:
        break
    else:
        pass
    count += 1
if X >= Y:
    print(count)
    exit()
else:
    pass

if abs(Y - X) % B == 0:
    count += (abs(Y - X) // B)-1
else:
    count += abs(Y - X) // B

print(count)
"""
# while X < Y:
#     if X*A <= X+B:
#         X = X*A
#         if X >= Y:
#             break
#         else:
#             count += 1
#     else:
#         X = X + B
#         if X >= Y:
#             break
#         else:
#             count += 1


"""#C - Cream puff
N = int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

ans = make_divisors(N)
for i in range(len(ans)):
    print(ans[i])"""

"""#B - Various distances
N = int(input())
a = list(map(int,input().split()))
A = 0
B = 0
C = 0
for i in range(N):
    A += abs(a[i])

for j in range(N):
    B += abs(a[j])**2

B = B**0.5

for k in range(N):
    if C <= abs(a[k]):
        C = abs(a[k])

print(A)
print(B)
print(C)"""

"""#A - box
N,A,B= map(int,input().split())
print(N-A+B)"""

"""#A - Fourtune Cookies
A,B,C,D= map(int,input().split())
a = A+B+C+D

if (a - A == A) or a - B == B or a - C == C or a -D ==D or A+B == C+D or A +C == B + D or A + D == B+C:
    print("Yes")
else:
    print("No")"""

"""#B - MAX-=min
N = int(input())
a = list(map(int,input().split()))
ans = 10**10
import math

if N == 1:
    print(a[0])
    exit()
else:
    pass
for i in range(N-1):
    b = math.gcd(a[i], a[i+1])
    if ans >= b:
        ans = b

print(ans)"""



"""#C - Neq Min
N = int(input())
p = list(map(int,input().split()))
l = 0
for i in range(N):
    print(min(p[:i])"""


# s = 0 #出力用
# t = 0 #比較用
# u = 0
# for i in range(N):
#     if p[i] > u:
#         if t <= p[i]:
#             t = p[i]
#         else:
#             pass
#         print(s)
#     else:
#         if p[i] <= u and t > u:
#             u = t + 1
#             s = u
#             print(s)
#         elif p[i] == u:
#             u += 1
#             t = u
#             s = u
#             print(s)
#         else:
#             s = u
#             print(s)




"""#B - Futon
H,W= map(int,input().split())
S =list(input() for i in range(H))
count = 0
for i in range(H):
    for j in range(W-1):
        if S[i][j] == S[i][j+1] and S[i][j] == ".":
            count += 1
        else:
            pass

for k in range(W):
    for l in range(H-1):
        if S[l][k] == S[l+1][k] and S[l][k] == ".":
            count += 1
        else:
            pass

print(count)"""

"""#A - Keyboard
S = input()
T = input()
if S == "Y":
    print(T.upper())
else:
    print(T)"""

"""#B - Integer Preference
A,B,C,D= map(int,input().split())
if B < C or D < A:
    print("No")
else:
    print("Yes")"""

"""#A - Repeat ACL
K = int(input())
a = "ACL"*K
print(a)"""

"""#D - Leaping Tak
N,X,M= map(int,input().split())
a =X
ans = a
for _ in range(N):
    a = (a**2) % M
    ans += a

print(ans)"""


# ans = (X*(1-X**(2**(N-1)+N))%M/(1-X**(N-1))%M) %M

"""#C - A x B + C
N = int(input())
ans = 0
for i in range(1,N-1):
    if i == 1:
        ans += N-1
    else:
        ans += int((N-1) / i)

print(ans+1)"""


# for i in range(1,int(N**0.5)):
#     for j in range(1,int(N**0.5)):
#         if (N - i) % j == 0:
#             ans += 1
#         else:
#             pass
#print(ans)

"""#B - Go to Jail
N = int(input())
x =[list(map(int, input().split())) for i in range(N)]
for i in range(N-2):
    if x[i][0] == x[i][1] and x[i+1][0] == x[i+1][1] and x[i+2][0] == x[i+2][1]:
        print("Yes")
        exit()
    else:
        pass
print("No")"""




"""#A - Plural Form
S = input()
if S[-1] == "s":
    print(S+"es")
else:
    print(S+"s")"""

"""#E - Dist Max
N = int(input())
x =[list(map(int, input().split())) for i in range(N)]
max_x = 0
max_x_i = 0
min_x = 0
min_x_i = 0
for i in range(N):
    if max_x <= x[i][0]+x[i][1]:
        max_x = x[i][0]+x[i][1]
        max_x_i = i
    else:
        pass
    if min_x >= x[i][0]+x[i][1]:
        min_x = x[i][0]+x[i][1]
        min_x_i = i

ans = abs(x[max_x_i][0]-x[min_x_i][0])+abs(x[max_x_i][1]-x[min_x_i][1])
print(ans)
"""
"""#C - Ubiquity
import math
N = int(input())
a = 10**9+7

ans = (10**N)-(2*9**N - 8**N)

# def combinations_count(n, r):
#     return math.factorial(n)%a // (math.factorial(n - r)%a * math.factorial(r))%a
#
# ans =(10**(N-2))%a*(combinations_count(N, 2)*2)%a-combinations_count(N, 2)%a
print(ans%a)"""

"""#B - Product Max
a,b,c,d= map(int,input().split())
print(max(a*c,a*d,b*c,b*d))"""



"""#A - Not
x = int(input())
if x == 1:
    print(0)
else:
    print(1)"""

"""#C - Sum of product of pairs
N = int(input())
A = list(map(int,input().split()))
ans = 0
P = 0
E = 0
for i in range(N):
    P += (A[i]%(10**9+7))**2
    E += A[i]%(10**9+7)

ans =int(((E**2 - P)/2)%(10**9+7))
print(ans)"""

"""#B - Substring
S = input()
T = input()
ans = 10**9
for i in range(len(S)-len(T)+1):
    count = 0
    for j in range(len(T)):
        if S[i+j] != T[j]:
            count += 1
        else:
            pass
    if ans >= count:
        ans = count
    else:
        pass
print(ans)"""

"""#A - Don't be late
D,T,S= map(int,input().split())

if D <= S*T:
    print("Yes")
else:
    print("No")"""

"""#E - Bomber
H,W,M= map(int,input().split())
s =[list(map(int, input().split())) for i in range(M)]
H_t = [0]*H
W_t = [0]*W
b_h = [0]*H
b_w = [0]*W

for j in range(M):
    H_t[s[j][0]-1] += 1

for k in range(M):
    if
    W_t[s[k][1] - 1] += 1

for l in range(H):
    b_h[l] =

print(H_t,W_t)"""

"""#D - Wizard in Maze
H,W= map(int,input().split())
C_H,C_W= map(int,input().split())
D_H,D_W= map(int,input().split())
S = [list(input()) for i in range(H)]

print(S)"""

"""#C - Step
N = int(input())
A = list(map(int,input().split()))
DP = [0]
for i in range(1,N):
    if (A[i-1]+DP[i-1])-A[i] > 0:
        DP.append((A[i-1]+DP[i-1])-A[i])
    else:
        DP.append(0)
print(sum(DP))
"""

"""#B - Multiple of 9
N = input()
L = 0
for i in range(len(N)):
    L += int(N[i])

if L%9 == 0:
    print("Yes")
else:
    print("No")"""

"""#A - Takoyaki
N,X,T= map(int,input().split())

if N%X > 0:
    print(N//X*T+T)
else:
    print(N//X*T)"""

"""#C - Walking Takahashi
X,K,D= map(int,input().split())

a1 = X // D
a2 = (X // D)+1
if min((abs(X)-(a1*D)),(abs(X)-(a2*D))) == (abs(X)-(a1*D)):
    a = a1
else:
    a = a2

if a >= K :
    print(abs(abs(X) - abs(K*D)))
elif (K - a) % 2 == 0 :
    print((abs(abs(X) - abs(a*D))))
else:
    print(min((abs(abs(X) - abs(a * D)-abs(D))),(abs(abs(X) - abs(a * D)+abs(D)))))
"""

"""#B - Making Triangle
N = int(input())
L = list(map(int,input().split()))
count = 0
for i in range(N-2):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if L[i]+L[j]>L[k] and L[i]+L[k]>L[j] and L[k]+L[j]>L[i] and L[i] != L[j] and L[j] != L[k] and L[k]!=L[i]:
                count += 1
            else:
                pass

print(count)"""


"""#A - Rainy Season
S = input()
count = 0
count2 = 0

if S == "RRR":
    print(3)
elif S == "RRS" or S == "SRR":
    print(2)
elif S == "SSS":
    print(0)
else:
    print(1)
"""


"""#D - Alter Altar
N = int(input())
c = input()
W_r = 0
r = 0
w = 0

for i in range(N):
    if c[i] == "R":
        r += 1
    else:
        w += 1

if c[0]=="W" and c[1]=="W" and r >= 2:
    W_r += 1
else:
    pass


for i in range(1,N):
    if c[i-1]=="W" and c[i]=="R" :
        W_r += 1
    else:
        pass

if r == 0:
    W_r = 0

# print(r,w)
print(W_r)"""

"""#C - Repsept
K = int(input())

if K % 2 == 0:
    print(-1)
    exit()
else:
    pass

for i in range()
    10 *
"""


"""#B - Distance
N,D= map(int,input().split())
B = [list(map(int,input().split())) for i in range(N)]
count = 0
for i in range(N):
    if (B[i][0]**2+B[i][1]**2)<=D**2:
        count+=1
    else:
        pass
print(count)"""

"""#A - Air Conditioner
X = int(input())
if X >= 30:
    print("Yes")
else:
    print("No")"""

"""#D - Road to Millionaire
N= int(input())
A= list(map(int,input().split()))
A_s = [0]
B = 1000
C = 0
B_1 = 0
C_1 = 0
for j in range(N-1):
    A_s.append(A[j+1]-A[j])
#print(A_s)

for i in range(N-1):
    if A_s[i+1] > 0:
        B_1 = B - (B // A[i])*A[i]
        C_1 = C + B // A[i]
        B = B_1
        C = C_1
    elif A_s[i+1] <= 0:
        if C > 0:
            B_1 = B + C * A[i ]
            C = 0
            B = B_1
        else:
            pass
    else:
        pass

if C > 0:
    B = B +C*A[N-1]

print(B)"""



"""#B - Magic 2
A,B,C= map(int,input().split())
K = int(input())

for _ in range(K):
    if A < B:
        if B >= C:
            C = C*2
        else:
            pass
    else:
        B = B*2

if A < B <C :
    print("Yes")
else:
    print("No")"""


"""#C - Marks
N,K= map(int,input().split())
A= list(map(int,input().split()))
ans =[]
for i in range(N-K):
    if A[i] < A[i+K]:
        print("Yes")
    else:
        print("No")"""



"""#A - Kyu in AtCoder
X =int(input())

if X <= 1999 and X>=1800:
    print(1)
elif X <= 1799 and X>=1600:
    print(2)
elif X <= 1599 and X>=1400:
    print(3)
elif X <= 1399 and X>=1200:
    print(4)
elif X <= 1199 and X>=1000:
    print(5)
elif X <= 999 and X>=800:
    print(6)
elif X <= 799 and X>=600:
    print(7)
elif X <= 599 and X>=400:
    print(8)"""

""""# C - XYZ Triplets
N = int(input())
ans0 = []

for i in range(100):
    ans = 0
    for j in range(100 - (i + 1) ** 2):
        # a = (i+1)+(j+1)
        # b = (i+1)*(j+1)
        # if (i + 1) ** 2 + (j + 1) ** 2 + (k + 1) ** 2 + (i + 1) * (j + 1) + (j + 1) * (k + 1) + (k + 1) * (
        #         i + 1) == l + 1:
        for k in range(100 - (i + 1) ** 2 - (j + 1) ** 2 - (i + 1) * (j + 1)):
            if (i + 1) ** 2 + (j + 1) ** 2 + (k + 1) ** 2 + (i + 1) * (j + 1) + (j + 1) * (k + 1) + (k + 1) * (
                    i + 1) ==  + 1:
                if i == j == k:
                    ans = 1


                elif (i == j and j != k) or (k == j and i != k):
                    ans = 3

                else:
                    ans = 6
                ans0.append(ans)
                break

            break
for l in range(N):
    print(ans0[l])"""

"""#B - An Odd Problem
N = int(input())
a= list(map(int,input().split()))
ans = 0

for i in range(N):
    if a[i] % 2 == 1 and (i+1) % 2 == 1:
        ans += 1
    else:
        pass
print(ans)"""



"""#A - Number of Multiples
L,R,d= map(int,input().split())
ans = 0
for i in range(L,R+1):
    if i%d == 0:
        ans += 1
    else:
        pass

print(ans)"""

"""#E - Multiplication 4
N,K= map(int,input().split())
A= list(map(int,input().split()))
A.sort(reverse = True)
A_1 = []
A_2 = []

for i in range(N):
    if A[i] >= 0:
        A_1.append(A[i])
    else:
        A_2.append(A[i])
A_2.sort()

for j in range(K):
    A_1[j]
"""


"""#D - Chat in a Circle
N = int(input())
A= list(map(int,input().split()))
A.sort(reverse =True)
print(A)
count = 0
count2 = 0
ans = 0
DP = []

for i in range(A):
    if A[i+1] == A[i]:
        count += 1
        ans += A[i]
        DP.append(A[i])
    else:
        if count > 0:
            ans += DP[-1]
            count -= 1
        else:

        count = 0
        count2 += 1


ans = sum(A[:-1])
print(ans)"""

"""#C - H and V
N,M,K= map(int,input().split())
A= input()
B= input()

for i in range(N):
    for j in range(M):
        

print(A.count("#"))
print(B.count("#"))"""

"""#B - Judge Status Summary
N = int(input())
s =list(input() for i in range(N))
DP = [0]*4
for j in range(N):
    if s[j] == "AC":
        DP[0] += 1
    elif s[j] == "WA":
        DP[1] += 1
    elif s[j] == "TLE":
        DP[2] += 1
    else:
        DP[3] += 1

print("AC x",DP[0])
print("WA x",DP[1])
print("TLE x",DP[2])
print("RE x",DP[3])"""




"""#A - Payment
N = int(input())
a = N % 1000
if N < 1000 :
    ans = 1000- a

elif a == 0:
    ans = 0
elif a < 500:
    ans = 1000 - a

else:
    ans = 1000-a

print(ans)"""

"""#D - Sum of Divisors
# import sympy
# N = int(input())
# ans = 0
# for i in range(1,N+1):
#     ans += sympy.divisor_count(i)
#
# print(ans)

def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

N = int(input())
ans = 1
for i in range(2,N+1):
    ans += i*(len(make_divisors(i**2)))

print(ans)"""

"""#C - Tsundoku
N,M,K= map(int,input().split())
A= list(map(int,input().split()))
B= list(map(int,input().split()))

DP_A = [A[0]]
DP_B = [B[0]]


for i in range(1,N):
    if DP_A[i-1] + A[i] <= K:
        DP_A.append(DP_A[i-1] + A[i])
    else:
        break

for j in range(1,M):
    if DP_B[j-1]+B[j] <= K:
        DP_B.append(DP_B[j-1]+B[j])
    else:
        break
print(DP_A,DP_B)


for k in range(len(DP_A)):
    for l in range(len(DP_B)):
        DP_A[k]"""



"""#B - Minor Change
S =input()
T = input()
cnt =0
for i in range(len(S)):
    if S[i] == T[i]:
        pass
    else:
        cnt += 1
print(cnt)"""

"""#A - Calc
a = int(input())
print(a+a*a+a*a*a)"""


"""#D - Replacing
import collections
N= int(input())
A= list(map(int,input().split()))
Q = int(input())
B = [list(map(int,input().split())) for i in range(Q)]
DP = []
A.sort()
sub = 0
ans = sum(A)

for i in range(Q):
    if A.count(B[i][0]) > 0:
        #for j in range(A.count(B[i][0])):
        ans = ans +(B[i][1] - B[i][0])*A.count(B[i][0])
        DP.append(B[i][0])
        for j in range(N):
            if A[j] == B[i][0]:
                A[j] = B[i][1]
            else:
                pass
        print(ans)
    else:
        print(ans)
"""


"""#C - One Quadrillion and One Dalmatians
N = int(input())

a = [chr(i) for i in range(97,97+26)]
#print(a)

ans = ""
if N <= 26:
    print(a[N-1])
    exit()

# b = N // 26
#
# for i in range(b):
#     ans = a[N % 26 - 1] + ans
#     i += 1
#
# print(ans)

while N // 26 > 0:
    ans = a[N%26-1] + ans
    N = N // 26

if N  1:
    ans = a[N - 1] + ans
else:
    ans = a[N - 2] + ans

print(ans)"""


"""#B - Mix Juice
N,K= map(int,input().split())
p= list(map(int,input().split()))

p.sort()
ans = 0
for i in range(K):
    ans += p[i]

print(ans)"""


"""#A - αlphabet
a = input()
if str.isupper(a):
    print("A")
else:
    print("a")"""


"""#D - Not Divisible
N= int(input())
A= list(map(int,input().split()))
A.sort(reverse=True)
a = 0
ans = 0
DP = []
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if A[i]/2 >= A[j]:
            DP.append(j)
            break
        else:
            pass
if len(DP) == 0:
    print(0)
    exit()

DP.append(N)
print(DP)
print(A)



for k in range(len(A)):
    a = 0
    for l in range(DP[k],len(A)):
        if A[k] % A[l] == 0 :
            break
        else:
            a += 1
    if a == N - DP[k]:
        ans += 1
    else:
        pass

print(ans)"""

# for i in range(int(max(A)**0.5)):
#     for j in range(len(A)):
#         if A[j] % i == 0:



"""#C - Forbidden List
X,N= map(int,input().split())
p= list(map(int,input().split()))
A= list(range(-200,200))
#print(A)
for i in range(N):
    A.remove(p[i])

D = 201
ans = -100
for j in range(len(A)):
    if D > abs(X - A[j]):
        D = abs(X - A[j])
        ans = A[j]

    else:
        pass
print(ans)"""


"""#B - Crane and Turtle
X,Y= map(int,input().split())

if 2*X-Y/2 >= 0 and 2*X-Y/2 <= 50 and Y % 2 == 0:
    print("Yes")
else:
    print("No")
"""
"""#A - Five Variables
A= list(map(int,input().split()))

for i in range(len(A)):
    if A[i] == 0:
        print(i+1)
        exit()

print(0)"""



"""#C - Lamps
N,K= map(int,input().split())
A = list(map(int, input().split()))
# DP = [0]*N
# DP2 = [0]*N
DP = [0]*N
DP2 = [[0] *N for p in range(N)]
for _ in range(K):
    for i in range(N):
        for j in range(A[i],-A[i]-1,-1):
            if A[i] == 0:
                DP[i] += 1
            else:
                pass
            if i != i-j and i-j >= 0 and i-j < N and DP2[i-j][i] ==0:
                DP[i-j] += 1
                DP2[i-j][i] = 1

            else:
                pass
    print(DP)
    for k in range(len(DP)):
        A[k] += DP[k]
    DP = [0]*N
    print(DP2)
    #print(A)

L=[str(a) for a in A]
L=" ".join(L)
print(L)"""



"""#B - Tag
A,V= map(int,input().split())
B,W= map(int,input().split())
T= int(input())

k = abs(B-A)
a = V*T
b = W*T



if a >= k + b:
    print("YES")
else:
    print("NO")"""

"""#A - Nickname
S = input()
print(S[:3])"""

"""#D - Div Game
N = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
A = factorization(N)
#print(factorization(N))
ans = 0
if N == 1:
    print(0)
    exit()

for i in range(len(A)):
    if A[i][1] == 1:
        ans += 1
    else:
        k = A[i][1]
        for j in range(A[i][1]):
            if k-j > j:
                k -= j
                ans += 1
            else:
                break
print(ans)"""

"""#C - Multiplication 3
from decimal import Decimal
A,B= map(str,input().split())
A2 = Decimal(A)
B2 = Decimal(B)
#print(A*B*100000)
print(int(A2*B2))"""

"""#C - Multiplication 3

A,B= input().split()
A = int(A)
B = float(B)
B = int(B*1000)
#print(A*B*100000)
print(int(A*B/1000))"""

"""#B - Multiplication 2
N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 1
for i in range(N):
    if A[i] == 0:
        print(0)
        exit()
    else:
        pass
    ans *= A[i]
    if ans <= 1000000000000000000:
        pass
    else:
        print(-1)
        exit()
print(ans)"""

"""#A - Multiplication 1]
A,B= map(int, input().split())
print(A*B)"""

"""#C - Folia
N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N,0,-1):
    if 2**i >= ans:
        ans += A[i]+ans
    else:
        ans += 2**i-A[i]


print(ans)"""



"""#B - Postdocs
T = input()
print(T.replace('?','D'))"""



"""#A - Study Scheduling
H1,M1,H2,M2,K = map(int, input().split())
H=(H2-H1)*60
M=(M2-M1)
ans = K-(H+M)
print(abs(ans))"""


"""#C - : (Colon)
import math
A,B,H,M = map(int, input().split())
h = (H*60+M)*360/(12*60)
m = M*360/60

# h = H*30
# h = h + 0.5*M
# m = M*6
w = 0

w = h - m
if w > 180:
    w = w
# elif w < 0:
#     w = w+180
elif w == 180:
    print(abs(A+B))
    exit()
elif w == 0:
    print(abs(A-B))
    exit()
else:
    pass
#print(h,m,w)

c = A**2+B**2-2*A*B*math.cos(math.radians(w))
print(c**(1/2))"""

"""#B - ... (Triple Dots)
K = int(input())
S = input()
if len(S) <=K:
    print(S)
else:
    print(S[0:K]+"...")"""

"""#A - ∴ (Therefore)
N = input()
if N[-1]=="3":
    print("bon")
elif N[-1]=="0"or N[-1]=="1"or N[-1]=="6"or N[-1]=="8":
    print("pon")
else:
    print("hon")"""


"""#D - Teleporter
N,K = map(int, input().split())
A = list(map(int, input().split()))
DP = []
DP.append(A[0])
for i in range(N):
    DP.append(A[DP[i]-1])
print(DP)

B = [i for i, x in enumerate(DP) if x == DP[N]]
print(B[1]-B[0])
c = len(DP) % (B[1]-B[0])
print(c)
# DP2 = []
# for j in range(N):
#     DP[]
if N >= K:
    print(DP[K%len(DP)-1])
else:
    print(DP[K % len(DP)-1+c])

# for j in range(len(DP)):"""




"""#C - Skill Up
N,M,X = map(int, input().split())
C =[list(map(int, input().split())) for i in range(M)]"""


"""#B - Easy Linear Programming
A,B,C,K = map(int, input().split())

if K >= A:
    a = A
else:
    print(K)
    exit()
if A == 0 and C == 0:
    print(0)
    exit()

if A == 0 and B == 0:
    print(-1*K)
    exit()

if K - (A+B) >= 0:
    c = -1 * (K - (A + B))
else:
    c = 0

print(a+c)"""


"""#A - Registration
S = input()
T =input()
if S == T[:-1]:
    print("Yes")
else:
    print("No")"""

"""#D - I hate Factorization
X = int(input())
for i in range(-int(X**(1/5)),int(X**(1/5))):
    for j in range(-int(X**(1/5)),int(X**(1/5))):
        if i**5 - j**5 ==X:
            print(i,j)
            exit()
"""
"""#C - Peaks
N,M = map(int, input().split())
H =list(map(int, input().split()))
x =[list(map(int, input().split())) for i in range(M)]
DP = [1]*N
for i in range(M):
    tmp = min(H[x[i][0]-1],H[x[i][1]-1])
    if H[x[i][0]-1] == H[x[i][1]-1]:
        DP[x[i][0] - 1] = 0
        DP[x[i][1] - 1] = 0
    elif tmp == H[x[i][0]-1]:
        DP[x[i][0]-1] = 0
    else:
        DP[x[i][1] - 1] = 0

#print(DP)
ans = sum(DP)
print(ans)"""

"""#B - Trick or Treat
N,K = map(int, input().split())
D =[]
A =[]
for _ in range(K):
    d = int(input())
    a =list(map(int, input().split()))

    D.append(d)
    A.append(a)
# print(D,A)

for i in range(1,K):
    A[0].extend(A[i])
# print(A[0])

print(N-len(set(A[0])))"""



"""#A - A?C
S = input()
if S == "ABC":
    print("ARC")
else:
    print("ABC")"""

"""#D - Floor Function
A,B,N = map(int, input().split())

if B>N:
    a = (A*N)//B
    b = N//B
    print(a-A*b)
    exit()
else:
    N = B-1
    a = (A*N)//B
    b = N//B
    print(a-A*b)"""
"""
#C - Many Requirements
N,M,Q = map(int, input().split())
x =[list(map(int, input().split())) for i in range(Q)]


A  =[]
B = []
a = []
for i in range(N):
    a.append(i)
    for j in range(M):
        a.append(j+1)
    for k in range(j,M):
        a.append(k+1)

print(A)
"""

"""# B - 1%
X =int(input())
a = 100
for i in range(3761):
    a = int(a*1.01)
    if a >= X:
        print(i+1)
        exit()
    else:
        pass"""

"""#A - We Love Golf
K = int(input())
A,B = map(int, input().split())

if B-A == 0:
    if A%K==0:
        print("OK")
        exit()
    else:
        print("NG")
        exit()
else:
    pass

for i in range(A,B+1):
    if i % K == 0:
        print("OK")
        exit()
    else:
        pass
print("NG")"""



"""#D - Multiple of 2019
import re
S = str(input())
cnt =0
DP =[]
DP2 = []
n = 2019
m = 1

for i in range(99):
    DP.append(2019*(i+1))
print(DP)



for j in range(len(DP)):
    DP2.append(S.count(str(DP[j])))
"""

# for i in range(len(S)-3):
#     s = S[i]
#     for j in range(i+1,len(S)):
#          s += S[j]
#          if j >= 3:
#              if int(s) % 2019 == 0:
#                  cnt += 1
#              else:
#                  pass
#          else:
#              pass
#print(sum(DP2))


"""#C - gacha
N = int(input())
a = [str(input()) for i in range(N)]

print(len(set(a)))"""

"""#B - Battle
A,B,C,D= map(int, input().split())

a = A//D
if A%D > 0:
    a += 1

b = C//B
if C%B > 0:
    b += 1

if a >= b:
    print("Yes")
else:
    print("No")
"""

"""#A - Sheep and Wolves
S,W= map(int, input().split())
if S <= W:
    print("unsafe")
else:
    print("safe")"""
"""#C - management
import collections
N = int(input())
A =list(map(int, input().split()))
A_n = collections.Counter(A)

for i in range(N):
    print(A_n[i+1])"""


"""#B - Homework
N,M= map(int, input().split())
A =list(map(int, input().split()))

if sum(A) <= N:
    print(N-sum(A))
else:
    print(-1)"""

"""#A - Circle Pond
import math
R =int(input())
print(2*math.pi*R)"""

"""#D - RGB Triplets
N = int(input())
S =input()
DP = [0]*len(S)
for i in range(N-2):
    for j in range(N-1):
        if S[i] != S[j]:
            DP[i] = S[i]

print(DP)"""

"""#C - Sum of gcd of Tuples (Easy)
K = int(input())
DP =[]
ans = 0
import math
# from functools import reduce
# def gcd(*numbers):
#     return reduce(math.gcd, numbers)


# def gcd_list(numbers):
#     return reduce(math.gcd, numbers)

for i in range(1, K + 1):
    for j in range(1, K + 1):
        a = math.gcd(i,j)
        for k in range(1,K+1):
            b = math.gcd(a,k)
            ans += b

print(ans)
"""
"""#B - FizzBuzz Sum
N = int(input())
sum = 0
for i in range(1,N+1):
    if i % (3*5) ==0:
        pass
        #sum += i
        #print("FizzBuzz")
    elif i % 3 == 0:
        pass
        #sum += i
        #print("Fizz")
    elif i % 5 == 0:
        pass
        #sum += i
        #print("Buzz")
    else:
        sum += i
print(sum)"""

"""#A - Lucky 7
N = str(input())
if N[0] == "7" or N[1] == "7" or N[2] == "7":
    print("Yes")
else:
    print("No")"""

"""N = int(input())
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

a = sorted(make_divisors(N))
print(a)"""

"""#E - Yutori
N,K,C= map(int, input().split())
S = input()
DP =[]
NG = -1
for i in range(N):
    if S[i] == 'o' and i > NG:
        DP.append(i+1)
        NG = i+C
    else:
        pass
print(DP)

#for j in range(len(DP))"""

#D - Lunlun Number
# K = int(input())
# lst = []
# while K > 0:
#     lst.append(K%10)
#     K //= 10 # 必須
# lst.reverse()
# print(lst)
#
# K = input()
# ans = 0
# DP= []
# for i in range(len(N)):
#     ans = S[i]
#
#



"""#C - Replacing Integer
N,K= map(int, input().split())
a = N % K
if a <= abs(a-K):
    print(a)
else:
    print(abs(a-K))"""

"""#B - Popular Vote
N,M= map(int, input().split())
A =list(map(int, input().split()))
tmp = 0
for i in range(N):
    if A[i] >= (sum(A)/(4*M)):
        tmp += 1
    else:
        pass

if tmp >= M:
    print("Yes")
else:
    print("No")"""


"""#A - ABC Swap
A,B,C= map(int, input().split())

print(C,A,B)"""

"""#E - Red and Green Apples
X,Y,A,B,C= map(int, input().split())
a =sorted(list(map(int, input().split())),reverse=True)
b =sorted(list(map(int, input().split())),reverse=True)
c =sorted(list(map(int, input().split())),reverse=True)
print(a,b,c)
DP_a =a[:X]
DP_b =b[:Y]
print(DP_b)
DP_a.extend(DP_b)
DP_a.extend(c)
ans = sorted(DP_a,reverse=True)
print(sum(ans[:X+Y]))"""

# j = 1
# k = 1
# a_s =sum(a[:X])
# b_s =sum(b[:Y])
#
# for i in range(C):
#     if c[i] > a[X-j] or c[i] > b[Y-k]:
#         if c[i] > a[X-j] and a[X-j] > b[Y-k]:
#             j += 1
#             if j >= X:
#                 DP_a.append(c[i])
#             else:
#                 pass
#         elif c[i] > b[Y-k] :
#             k += 1
#             if k >= Y:
#                 DP_b.append(c[i])
#             else:
#                 pass
#         else:
#             pass
#     else:
#         break
#
# a_s = a_s-sum(a[X-len(DP_a):X])+sum(DP_a)
# b_s = b_s-sum(b[Y-len(DP_b):Y])+sum(DP_b)




"""#D - Line++
N,X,Y= map(int, input().split())
ans=[]
for i in range(N):
    if i ==0:
        ans.append(N)"""


"""#C - Traveling Salesman around Lake
K,N= map(int, input().split())
A =list(map(int, input().split()))
B =[]
ans = 0
for i in range(N-1):
    B.append(A[i+1]-A[i])
    ans += A[i+1]-A[i]
B.append(abs(K-A[N-1]+A[0]))
ans = K-max(B)
print(ans)"""

"""#B - Golden Coins
X = int(input())

ans1 = X // 500
ans2 = (X - 500*ans1)//5

print(ans1*1000+ans2*5)"""


"""#A - Coffee
S =input()
if S[2] == S[3] and S[4] == S[5]:
    print("Yes")
else:
    print("No")"""

"""#D - Banned K
import collections
from collections import defaultdict
d = defaultdict(list)
import copy
N = int(input())
A = list(map(int, input().split()))
tmp = []

a = collections.Counter(A)
print(a)
for k,v in a.items():
    v_1 = ((v - 1) * (v - 2) )// 2
    v = (v*(v-1))//2
    d[k].append(v)
    d[k].append(v_1)
    print(k,v,v_1)

print(d)
print(d[1])

for i in range(N):
    print(d[A[i]][1] + sum(d.values())-d[A[i]][0])"""





# for i in range(N):
#     tmp = A[:]
#     tmp.pop(i)
#     t = collections.Counter(tmp)
#
#
#     print(t)
#     tmp.clear()



"""#C - Maximum Volume
L=int(input())
V = (L/3)**3
# for i in range(1,L):
#     for j in range(1,L-i):
#         if L-i-j > 0:
#             tmp = i*(L-i)*(L-i-j)
#             if tmp >= V:
#                 V = tmp
#             else:
#                 pass
#         else:
#             pass
print(V)"""

"""#B - String Palindrome
S = input()

for i in range((len(S)-1)//2):
    if S[i] == S[i+(len(S)+3)//2-1]:
        pass
    else:
        print("No")
        exit()
print("Yes")
"""

"""#A - The Number of Even Pairs
N,M= map(int, input().split())

ans = (N*(N-1))//2 +(M*(M-1))//2

print(ans)"""

"""def c(n,k):
  return 1 if(k<=0 or n<=k) else c(n-1, k-1) + c(n-1, k)

A = [c(N-2,j) for j in range(N-2+1)]
for i in range(N-2+1):
    if i % 2 != 0:
        A[i] = -1*A[i]
    else:
        pass

for i in range(N-1):
    ans += A[i]*a_2[i]


print(A)
print(a_2)"""



"""#A - Range Flip Find Route
H,W= map(int, input().split())

s =list(input() for i in range(H))
print(s)"""

"""#D - String Equivalence
N = int(input())

if N == 1:
    print("a")
else:
    for i in range(1,N):
        chr_s = str(chr(i + 96))
        for j in range(N):
            chr_s += str(chr(j + 96))
            print(chr_s)


# for i in range(len(N)):
#     chi
"""
"""
#C - Sqrt Inequality
# from decimal import *
#
# getcontext().prec = 20
#
# import math
# a,b,c= map(int, input().split())
# # if int(Decimal(a).sqrt())+ int(Decimal(b).sqrt()) < int(Decimal(c).sqrt()):
# #     print("Yes")
# # else:
# #     print("No")

#C - Sqrt Inequality
import math
a,b,c= map(int, input().split())

if c >= a+b:
#if float(math.sqrt(a))+ float(math.sqrt(b)) < float(math.sqrt(c)):
    if 4*a*b < (c-a-b)**2:
        print("Yes")
    else:
        print("No")
else:
    print("No")

"""
"""
#B - Bishop
import math
H,W= map(int, input().split())
print(int(math.ceil(H/2) * math.ceil(W/2) + math.floor(H/2)*math.floor(W/2)))
"""
# if H % 2 == 0 and W %2 == 0:
#     print((H / 2) * (W /2))
# elif H % 2 == 1 and W %2 == 1:
#     print((H // 2  + 1) * (W // 2 + 1) -1 )



#print(math.ceil(H/2) * math.ceil(W/2) + math.floor(H/2)*math.floor(W/2))
"""
#A - Kth Term
S = int(input())
A = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]

print(A[S-1])"""

"""#B - Nice Shopping
A,B,M= map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x =[list(map(int, input().split())) for i in range(M)]

tmp_min = min(a)+min(b)

for i in range(M):
    tmp = a[x[i][0]-1]+b[x[i][1]-1] - x[i][2]
    if tmp < tmp_min:
        tmp_min = tmp
    else:
        pass

print(tmp_min)"""



"""#A - Hitachi String
S = list(input())
count = 0
if len(S) % 2 == 1:
    print("No")
    exit()
else:

    for i in range(0,int(len(S)//2),2):
        if S[i]+S[i+1] == "hi":
            pass
        else:
            print("No")
            exit()

    print("Yes")"""


"""#D - String Formation
S=input()
Q=int(input())
query=[]
for _ in range(Q):
    query.append(input().split())

flag = True
t=""
u=""

for i in query:
    if i[0]=="1":
        u,t=t,u
        flag = not flag
#        S=S[::-1]
    else:
        if i[1]=="1":
            t+=i[2]
        else:
            u+=i[2]
if flag:
    print(t[::-1]+S+u)
else:
    print(t[::-1]+S[::-1]+u)
"""


# S = list(str(input()))
# Q = int(input())
# q = [input().split() for i in range(Q)]
#
# #print(S)
# #print(q)
# tmp = 0
# for i in range(Q):
#     tmp1 = ""
#     if q[i][0] == "1" and i == Q - 1 and tmp % 2 == 1:
#         S = S[::-1]
#     elif q[i][0] == '1':
#         tmp += 1
#        # tmp1 = S[0]
#        # S[0] = S[-1]
#        # S[-1] = tmp1
#     else:
#         if q[i][1] == "1":
#             if tmp % 2 ==0:
#                 S.insert(0,q[i][2])
#             else:
#                 S = S[::-1]
#                 S.insert(0, q[i][2])
#         else:
#             if tmp % 2 ==0:
#                 S.append(q[i][2])
#             else:
#                 S = S[::-1]
#                 S.append(q[i][2])
#
# ans = ''.join(S)
# print(ans)


"""#C - Tax Increase
import math
A,B= map(int, input().split())
for i in range(1,100*1000):
    if math.floor(i * 0.08) == A and math.floor(i * 0.1) == B:
        print(i)
        exit()
    else:
        pass

print(-1)"""


"""#B - Count Balls
N, A,B= map(int, input().split())

a = N % (A+B)
b = N // (A+B)
if a <= A:
    print(b*A+a)
else:
    print(b*A+A)"""

"""#A - Station and Bus
S = input()
if S == "AAA" or S == "BBB":
    print("No")
else:
    print("Yes")"""

"""#C - Guess The Number
N, M = map(int, input().split())
s =[list(map(int, input().split())) for i in range(M)]

s = list(map(list, set(map(tuple, s))))
s.sort(key=lambda x: x[0],reverse = True)
if s[0][0] == N:
    if s[0][1] == 0 and N != 1:
        print(-1)
        exit()
    else:
        pass
else:
    print(-1)
    exit()

s.sort(key=lambda x: x[0])

#print(s)
ans = [0 for a in range(3)]
ans2 = str("")
t_b = [1 for a in range(3)]
tmp_a = 0 #桁


if len(s) == 1:
    if s[0][0] == 1 and s[0][1] == 0:
        print(0)
        exit()
    elif s[0][0] == 1 and s[0][1] > 0:
        print(s[0][1])
        exit()

for i in range(len(s)):
    if ans[s[i][0]-1] == 0:
        if s[i][1] > 0:
            ans[s[i][0] - 1] = s[i][1]
    else:
        print(-1)
        exit()

if N == 2:
    ans2 = str(ans[1])+str(ans[2])
elif N == 3:
    ans2 += str(ans[0])+str(ans[1])+str(ans[2])
else:
    ans2 = str(ans[2])

print(int(ans2))
"""

"""#B - Bingo
A =[list(map(int, input().split())) for i in range(3)]
N = int(input())
b = [int(input()) for j in range(N)]
A_n = [[0 for a in range(3)] for c in range(3)]

for k in range(3):
    for l in range(3):
        for m in range(N):
            if A[k][l] == b[m]:
                A_n[k][l] = 1
            else:
                pass

if A_n[0][0]+A_n[0][1]+A_n[0][2]==3 or A_n[1][0]+A_n[1][1]+A_n[1][2] == 3 or A_n[2][0]+A_n[2][1]+A_n[2][2] == 3:
    print("Yes")
elif A_n[0][0]+A_n[1][0]+A_n[2][0]==3 or A_n[0][1]+A_n[1][1]+A_n[2][1] == 3 or A_n[0][2]+A_n[1][2]+A_n[2][2] == 3:
    print("Yes")
elif A_n[0][0]+A_n[1][1]+A_n[2][2]==3 or A_n[0][2]+A_n[1][1]+A_n[2][0]==3:
    print("Yes")
else:
    print("No")"""





"""#A - Duplex Printing
N = int(input())
if N%2 == 0:
    print(int(N/2))
else:
    print(int(N/2)+1)"""

"""# D - Bouquet
n, a, b = map(int, input().split())
from operator import mul
from functools import reduce
MOD = 10**9 + 7

def cmb(n, k, mod, fac, ifac):
#    
#     nCkを計算する
#     
#     k = min(k, n-k)
#     return fac[n] * ifac[k] * ifac[n-k] % mod
#
#
# def make_tables(mod, n):
#     
#     階乗テーブル、逆元の階乗テーブルを作成する
#     
#     fac = [1, 1] # 階乗テーブル・・・(1)
#     ifac = [1, 1] #逆元の階乗テーブル・・・(2)
#     inverse = [0, 1] #逆元テーブル・・・(3)

    for i in range(2, n+1):
        fac.append((fac[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod//i)) % mod)
        ifac.append((ifac[-1] * inverse[-1]) % mod)
    return fac, ifac

fac, ifac = make_tables(MOD, n)
tmp2 = 1
for l in range(n):
    tmp2 *= 2
    tmp2 = tmp2 % (MOD)

ans = ((tmp2 -1) - cmb(n, a, MOD, fac, ifac)- cmb(n, b, MOD, fac, ifac))
print(ans)
"""
"""#C - Rally
N = int(input())
X = list(map(int, input().split()))

ans = []
for i in range(100):
    tmp = 0
    for j in range(len(X)):
        tmp += (i - X[j])**2
    ans.append(tmp)

print(min(ans))"""

"""#B - Digits
N,K = map(int,input().split())
ans = 0
while N > 0:
    N = N//K
    ans += 1

print(ans)"""

"""#A - Beginner
N,R = map(int,input().split())

if N >= 10:
    print(R)
else:
    print(R+(100*(10-N)))"""

"""#C - Poll
import collections
N = int(input())
S = [str(input()) for i in range(N)]
S = sorted(S)
count = 1
tmpcount = 1
DP = [S[0]]
for i in range(1,N):
    if S[i] == S[i-1]:
        count += 1
        if tmpcount < count:
            DP.clear()
            DP.append(S[i])
            tmpcount = count
        elif tmpcount == count:
            DP.append(S[i])
        else:
            pass
    else:
        count = 1
        if tmpcount == count:
            DP.append(S[i])
        else:
            pass

for l in range(len(DP)):
     print(DP[l])
"""

# print(S)
#
# A = collections.Counter(S)
# maxS = [kv[0] for kv in A.items() if kv[1] == max(A.values())]
# #print(A)
# for l in range(len(maxS)):
#     print(maxS[l])


"""#B - Papers, Please
N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    if A[i] % 2 == 0:
        if A[i] % 3 == 0 or A[i] % 5 == 0:
            pass
        else:
            print("DENIED")
            exit()
    else:
        pass

print("APPROVED")"""

"""#A - Poor
A,B,C = map(int,input().split())
if (A == B and B == C) or (A != B and B != C and A != C):
    print("No")
else:
    print("Yes")"""

"""#D - Dice in Line
N,K = map(int,input().split())
p = list(map(int, input().split()))
S = [0]*N
s = 0
s_t = 0
S[0] = (1+p[0])/2

if N == 1:
    print(S[0])
    exit()
else:
    pass

for i in range(N-1):
    S[i+1] =S[i]+(1+p[i+1])/2

if N == K:
    print(S[N-1])
    exit()
else:
    pass

for j in range(N-K):
    s_t = S[j+K]-S[j]
    if s_t >= s:
        s = s_t
    else:
        pass

print(s)"""

"""#C - Distinct or Not
N = int(input())
A = list(map(int, input().split()))
A_1 = list(set(A))
if len(A) == len(A_1):
    print("YES")
else:
    print("NO")"""

"""#B - I miss you...
S = str(input())
print("x"*len(S))"""

"""#A - Remaining Balls
S,T = map(str,input().split())
A,B = map(int,input().split())
U = str(input())
if U == S:
    print(A-1,B)
else:
    print(A,B-1)"""

"""#E - Crested Ibis vs Monster
H,N = map(int,input().split())
A =[list(map(int, input().split())) for i in range(N)]
tmp = 0
ans = 0
for i in range(N):
    A[i].append(A[i][0]-A[i][1])
    A[i].append((A[i][0]-A[i][1])/(A[i][0]))

A.sort(key=lambda x: x[3],reverse = True)
min_A = max(A, key = lambda x:x[2])
print(A)
while tmp < H - A[0][0]:
    tmp += A[0][0]
    ans += A[0][1]

# if tmp < H:
#     while tmp < H:
#         tmp += int(min_A[0])
#         ans += int(min_A[1])
# else:
#     pass

print(ans)"""

"""#D - Caracal vs Monster
H = int(input())

a = 1
b = 0
while ( a <= H):
    a *= 2
    b += 1

print(2**b-1)"""

"""#C - Fennec vs Monster
N,K = map(int,input().split())
H = list(map(int, input().split()))
ans = 0
H.sort(reverse=True)

for i in range(K,N):
    ans += H[i]

print(ans)"""

"""#B - Common Raccoon vs Monster
H,N = map(int,input().split())
A = list(map(int, input().split()))

sum_A = sum(A)
if H <= sum_A:
    print("Yes")
else:
    print("No")"""

"""#A - Serval vs Monster
H,A = map(int,input().split())

if H % A > 0:
    print(int(H/A)+1)
else:
    print(int(H/A))"""

"""# D - Handstand 2
N = int(input())
count = 0
tmp = 0
DP = []

if N < 10:
    print(N)
    exit()
else:
    n = str(N)
    for i in range(N):
        I = str(i)
        for j in range(int(I[-1]),N+1,10):
            J = str(j)
            if J[-1] == I[0] and J[0] == I[-1]:
                count += 1
    print(count)

    # for i in range(1,N+1):
    #     I = str(i)
    #     DP.append(I)
    #     count += tmp
    #     for j in range(1,int(DP[-1])+1):
    #         tmp = 0
    #         J = str(j)
    #         if J[-1] == I[0] and J[0] == I[-1]:
    #             tmp += 1
"""

"""#C - Low Elements
N = int(input())
A = list(map(int, input().split()))
count = 1
print(A)
tmp = A[0]
for i in range(1,N):
    if A[i] <= tmp:
        count += 1
        tmp = A[i]
    else:
        pass
print(count)"""

"""# B - Comparing Strings
a,b = map(str,input().split())
ans_1 = a *int(b)
ans_2 = b *int(a)
#print(ans_1,ans_2)
if a >= b:
    print(ans_2)
else:
    print(ans_1)"""

"""#A - AC or WA
N,M = map(int, input().split())

if N == M:
    print("Yes")
else:
    print("No")"""

"""# C - Subarray Sum
N,K,S = map(int, input().split())
A = []
count = 0
if N == 1:
    A.append(S)
    A = [str(a) for a in A]
    A = " ".join(A)
    print(A)
    exit()
else:
    while count < K:
        A.append(S)
        count += 1

    if N - len(A) > 0:
        if S < 1000000000:
            while len(A) < N:
                A.append(S + 1)
        else:
            while len(A) < N:
                A.append(S - 1)

    else:
        pass
    A = [str(a) for a in A]
    A = " ".join(A)
    print(A)"""

"""else:
    A.append(S // 2)
    if S % 2 == 0:
        while count < K -1:
            A.append(S-A[0])
            count += 1
    else:
        while count < K -1:
            A.append(S - A[0])
            count += 1
            if count < K -2:
                A.append(S // 2)
    if N - len(A) > 0:
        A.append(S)
        while len(A) < N:
            A.append(S+1)
    else:
        pass"""

"""# B - Robot Arms
N = int(input())
a =[list(map(int, input().split())) for i in range(N)]
#print(a)
count  = 0

a.sort()
#print(a)
for i in range(N-1):
    right = a[i][0] + a[i][1]
    left = a[i+1][0] - a[i+1][1]
    if right <= left:
        pass
    else:
        count += 1
        if a[i][0] + a[i][1] >= a[i+1][0] + a[i+1][1] and a[i][0] + a[i][1] > a[i+1][0]:
            pass
        else:
            a[i+1][0] = a[i][0]
            a[i+1][1] = a[i][1]
print(N -count)"""

"""#A - Painting
H = int(input())
W = int(input())
N = int(input())

a = max(H,W)
if N % a > 0:
    print((N // a)+1)
else:
    print(N // a)"""

"""# C - Welcome to AtCoder
N,M = map(int, input().split())
s = list(input().split() for i in range(M))

if M == 0:
    print(0,0)
    exit()
else:
    pass

AC = 0
WA = 0
Num = s[0][0]
AC_count = 0
WA_count = 0



for i in range(M):
    tmp_N = Num
    if tmp_N == s[i][0]:
        pass
    else:
        tmp_N = s[i][0]
        Num = tmp_N
        AC_count = 0
        WA_count = 0

    if s[i][1] == 'AC':
        AC_count += 1
        if AC_count == 1:
            AC += 1
            WA += WA_count
            WA_count = 0
        else:
            WA_count = 0
    else:
        if AC_count == 0:
            WA_count += 1
        else:
            pass

print(AC,WA)
"""
"""#B - Achieve the Goal
N,K,M = map(int, input().split())
A = list(map(int, input().split()))
point = 0

for i in range(N-1):
    point += A[i]
ans = M*N-point

if ans <= K:
    if ans <= 0:
        print(0)
    else:
        print(ans)
else:
    print(-1)"""

"""#A - Next Alphabet
A = str(input())

print(chr(ord(A) + 1))"""

"""# B - Fusing Slimes
N = int(input())
x = list(map(int, input().split()))
"""
"""# A - Falling Asleep
N = int(input())
s = list(input().split() for i in range(N))
X = str(input())
ans = 0
#print(N,s,X)
#print(s[0][0])
count = 0
for i in range(N):
    ans += 1
    if str(s[i][0]) == X:
        break
    else:
        pass

#print(count)

for j in range(count+1,N):
    ans += int(s[j][1])

print(ans)"""

"""#C - Count Order
from itertools import permutations
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
l = list(range(1,N+1))
count = 0
ans_p = 0
ans_q = 0
for i in permutations(l):
    count += 1
#    print(i)
#    print(P)
    if i == P:
        ans_p = count
    else:
        pass
    if i == Q:
        ans_q = count
    else:
        pass
#print(ans_p,ans_q)
print(abs(ans_p - ans_q))"""
"""#E - Handshake
N,K = map(str, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
count = K
tmp = 0
for i in range(N):
    tmp += 2*A[i]
    count -= 1
    if count == 0:
        print(tmp)
    else:
        tmp = A[i]+A[i-1]
        count -= 1
        if count == 0:
        print(tmp)

A[i] + A[i]"""

"""#D - Prediction and Restriction
N,K = map(int, input().split())
R,S,P = map(int, input().split())
t = min(R,S,P)
if t == R:
    t_1 = "r"
elif t == S:
    t_1 = "s"
else:
    t_1 = "p"
ans = 0
T = str(input())
C = []
DP = []
for i in range(N):

    if T[i] == "p":
        C.append("s")
        DP.append(S)
    elif T[i] == "s":
        C.append("r")
        DP.append(R)
    else:
        C.append("p")
        DP.append(P)

for k in range(K):
    ans += DP[k]

for j in range(K,N):
    if DP[j] == DP[j-K]:
        ans += 0
        DP[j] = 0
    else:
        ans += DP[j]

print(ans)"""

"""# C - Next Prime
X = int(input())
n = int(10**5)**2
def is_prime(n):
    for k in range(2, n):
        if n % k == 0:
            return False
        else:
            continue
    return True

if is_prime(X) == True:
    print(X)
else:
    for i in range(X+1,n+1):
        if is_prime(i) == True:
            print(i)
            exit()
        else:
            pass"""

"""# B - Greedy Takahashi
A,B,K = map(int, input().split())

if (K-A)>=0:
    ans1 = 0
    ans2 = B-(K-A)
else:
    ans1 = A-K
    ans2 = B

if ans2 < 0:
    ans2 = 0
else:
    pass

print(ans1,ans2)"""

"""# A - Strings
A,B = map(str, input().split())
print(B+A)"""
"""#E - Double Factoria
N = int(input())
ans = 1
if N % 2 !=0:
    print(0)
else:
    N_1 = N // 10
    for i in range(N,1,-2):
        ans *= i
    print(ans,N_1)"""

"""# D - Brick Break
N = int(input())
A = list(map(int, input().split()))
DP = []
tmp = 0

for i in range(N):
    if A[i] == tmp +1:
        DP.append(A[i])
        tmp += 1
    else:
        pass

if len(DP) >= 1:
    print(N-len(DP))
else:
    print(-1)"""

"""# C - Snack
import fractions
A,B = map(int, input().split())
ans = (A * B) // fractions.gcd(A, B)
print(ans)"""
"""# B - Strings with the Same Length
N = int(input())
S,T = map(str, input().split())
ans = ""
for i in range(N):
    ans += S[i]+T[i]

print(ans)"""

"""# A - Round One
A = int(input())
B = int(input())

if A == 2 and B == 1:
    print(3)
elif B == 2 and A == 1:
    print(3)
elif A == 3 and B == 1:
    print(2)
elif B == 3 and A == 1:
    print(2)
elif A == 2 and B == 3:
    print(1)
else:
    print(1)"""

"""# D - Xor Sum 4
N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        ans += int(A[i]^A[j])
print(ans % 1000000007)
#print(int(A[0]^A[1])+int(A[0]^A[2])+int(A[1]^A[2]))

# for i in range(N):
#     A[i]= (format(A[i],'b'))
# print(A)

"""

"""# C - HonestOrUnkind2

N = int(input())
A = [0]*N
x = [0]*N
ans0 = [1] * N
ans = 0
ans1 = 1
for i in range(N):
    A[i] = int(input())
    x[i] = [list(map(int, input().split())) for j in range(A[i])]

print(N,A,x)
print(x[0],x[0][0],x[0][0][0])

for k in range(N):
    for l in range(N-1):
        # if A[k] == 1:
        #     for m in range
        #     if x[k][l][0]:
        #         if x[k][l][1] == 0:
        #             ans0[m] = ans0[m] * -1
        #         else:
        #             ans0[m] = ans0[m] * 1
        # else:
        for m in range(N): #対象選択
            if x[k][l][0] == m+1:
                if x[k][l][1] == 0:
                    ans0[m] = ans0[m] * -1
                else:
                    ans0[m] = ans0[m] * 1
print(ans0)

for m in range(N):
    ans1 *= ans0[m]

if ans1 == 1:
    ans = 1

for m in range(N):
    if ans0[m] == 1:
        ans += ans0[m]
    else:
        pass
print(ans)"""

"""# B - Palindrome-philia
S = str(input())
N = len(S)
count = 0
for i in range(N//2):
    if S[i] == S[(N-1)-i]:
        pass
    else:
        count += 1
print(count)"""

"""# A - Blackjack
A, B, C = map(int, input().split())
if A+B+C <= 21:
    print('win')
else:
    print('bust')"""

"""# D - Lucky PIN
N = int(input())
S = str(input())
"""

"""# C - 100 to 105
X = int(input())

for a in range(2501):
    for b in range(2501-100*a):
        for c in range(2501-100*a-101*b):
            for d in range(2501-100*a-101*b-102*c):
                for e in range(2501-100*a-101*b-102*c-103*d):
                    for f in range(2501-100*a-101*b-102*c*103*d-104*e):
                        if 100*a+101*b+102*c+103*d+104*e+105*f == X:
                            print(1)
                            exit()
                        else:
                            pass
print(0)"""
"""# B - Tax Rate
import math
N = int(input())
tmp = round(N / 1.08)

if math.floor(tmp * 1.08) == N:
    print(int(tmp))
elif math.floor((tmp+1) * 1.08) == N:
    print(int(tmp+1))
else:
    print(":(")"""

"""# A - November 30
M1, D1 = map(int, input().split())
M2, D2 = map(int, input().split())

if (M1 == 1 or M1 ==3 or M1 ==5 or M1 ==7 or M1 ==8 or M1 ==10 or M1 ==12) and D1 == 31:
    print(1)
elif (M1 == 4 or M1 == 6 or M1 ==9 or M1 ==11) and D1 == 30:
    print(1)
elif M1 == 2 and D1 == 28:
    print(1)
else:
    print(0)"""

"""# C - Buy an Integer
A, B, X = map(int, input().split())
DP =[]
tmp = 0
for i in range(1,10):
    tmp = (X - B*i)//A
    DP.append(tmp)
#print(DP)
#print(len(str(DP[8])))

for i in range(9):
    if DP[i] <= 0:
        print(0)
        exit()
    elif i+1 == len(str(DP[i])):
        if i == 8:
            print(DP[8])
        else:
            print(DP[i])
        exit()
    elif len(str(DP[i])) >= 10:
        print(1000000000)
        exit()
    else:
        pass
print(0)
"""

# for i in range(1,10):
#     DP[i]


"""# B - ROT N
N = int(input())
S = str(input())
def caesar(s, n):
    ns = []
    for ch in s:
        # A - Z
        if ('A' <= ch and ch <= 'Z'):
            ns.append(chr((ord(ch) - ord('A') + n) % 26 + ord('A')))
        # no change for other characters
        else:
            ns.append(ch)
    return "".join(ns)

result = caesar(S, N)
print(result)"""

"""# A - Can't Wait for Holiday
S =str(input())
if S == "SUN":
    print(7)
elif S == "MON":
    print(6)
elif S == "TUE":
    print(5)
elif S == "WED":
    print(4)
elif S == "THU":
    print(3)
elif S == "FRI":
    print(2)
else:
    print(1)"""

"""# B - Iron Bar Cutting
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

"""

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
