"""#A - 天下一プログラマーコンテスト1998
a0 = 100
a1 = 100
a2 = 200
a = [100,100,200]

for i in range(2,20):
    a.append(a[i] + a[i-1] + a[i-2])

print(a[19])"""

"""#B - 歩く人
N,K = map(int,input().split())
a = list(int(input()) for i in range(N))
a_all = 0
for i in range(N):
    a_all += a[i]
    if a_all >= K:
        print(i+1)
        exit()
    else:
        pass"""

"""#B - トリボナッチ数列
n = int(input())
c = 0
b = 0
a = 1
d = 0
if n == 1 or n == 2:
    print(0)
    exit()
elif n == 3:
    print(1)
    exit()
else:
    pass

for _ in range(n-3):
    d = c%10007
    c = b%10007
    b = a%10007
    a = (b + c + d)%10007

# for i in range(n):
#     a.append(a[i]+a[i+1]+a[i+2])

print(a%10007)"""

"""#B - Cut and Count
# import math
N = int(input())
S = input()
s = set(S)
print(math.len(s)//2)"""

"""#B - Shiritori
N = int(input())
S = list(input() for i in range(N))
if len(S) != len(set(S)):
    print("No")
else:
    for i in range(N-1):
        if S[i][-1] == S[i+1][0]:
            pass
        else:
            print("No")
            exit()
    print("Yes")
"""

"""#B - AtCoderトランプ
S = input()
T = input()
tmp = 0
for i in range(len(S)):
    if S[i] == T[i]:
        pass
    elif S[i] == '@':
        if T[i] == 'a' or T[i] == 't' or T[i] == 'c' or T[i] == 'o' or T[i] == 'd' or T[i] == 'e' or T[i] == 'r' or T[i] == '@':
            pass
        else:
            tmp += 1
    elif T[i] == '@':
        if S[i] == 'a' or S[i] == 't' or S[i] == 'c' or S[i] == 'o' or S[i] == 'd' or S[i] == 'e' or S[i] == 'r' or S[i] == '@':
            pass
        else:
            tmp += 1
    else:
        tmp += 1
if tmp >= 1:
    print("You will lose")
else:
    print("You can win")"""

"""#B - さかさま辞書
N = int(input())
S = list(input() for i in range(N))
S_r =[]
for i in range(N):
    S_r.append(S[i][::-1])

S_r = sorted(S_r)

for i in range(N):
    S_a = S_r[i][::-1]
    print(S_a)"""


"""#B - Indeedなう！
N = int(input())
S = list(input() for i in range(N))
s0 = sorted('indeednow')

print(s0)

for i in range(N):
   tmp = sorted(S[i])
   if tmp == s0:
       print("Yes")
   else:
       print("No")"""


"""#B - Between a and b ...
def main(a,b,x):
    return int(b//x - (a-1)//x)

a,b,x = map(int, input().split())
ans = main(a,b,x)
print(ans)
"""
"""#B - たてなが
def main(N):
    for i in range(N):
        print(''.join(L[i]))
        print(''.join(L[i]))

H,W = map(int, input().split())
L = [input().split() for l in range(H)]
main(H)"""

"""#B - Digit Sums
N= str(input())
S = 0
for i in range(len(N)):
    S += int(N[i])

if int(N)%S==0:
    print("Yes")
else:
    print("No")"""

"""#B - Chocolate
N = int(input())
D, X = map(int, input().split())
A = list(int(input()) for i in range(N))
ans = 0

for i in range(N):
    tmp = 0
    while tmp < D:
        tmp += A[i]
        ans += 1
print(ans+X)"""


"""#B - i18n
s = str(input())
number = str((len(s)-2))
print(s[0]+number+s[len(s)-1])"""

"""# B - Snake Toy
N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
A.sort(reverse=True)

for i in range(K):
    ans += A[i]

print(ans)"""

"""# B - Christmas Eve Eve
N = int(input())
A = list(int(input()) for i in range(N))

A.sort(reverse=True)

A[0] = int(A[0]//2)
ans = 0
for i in range(len(A)):
    ans += A[i]

print(ans)"""

"""# B - Maximum Sum
#A, B, C = map(int, input().split())
A = list(map(int, input().split()))
K = int(input())
A.sort(reverse=True)

ans = A[0]*(2**K)+A[1]+A[2]

print(ans)
"""
"""# B - 105
N = int(input())

ans = 0
if N < 105:
    print(0)
    exit()
else:
    for i in range(105,N+1,2):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
            else:
                pass
        if count == 8:
            ans += 1
        else:
            pass

print(ans)"""

"""# B - Balance
N = int(input())
W = list(map(int, input().split()))
sum_l = 0
sum_r = sum(W)
abs_W =[]
for i in range(N):
    sum_l += W[i]
    sum_r -= W[i]
    abs_W.append(abs(sum_r - sum_l))

print(min(abs_W))"""

# sum1 = 0
# sum1n = 0
# sum2 = 0
# i = 0
# j = 0
# while sum1 < sum(W)/2:
#     sum1 += W[i]
#     i += 1
#
# while sum1n <= sum(W)/2:
#     sum1n += W[j]
#     j += 1
#
# sum2 = sum(W)-sum1
# sum2n = sum(W)-sum1n
# ans = min(abs(sum2-sum1),abs(sum2n-sum1n))

#ans = abs(sum(W) - sum1-sum1)



"""# ABC087B - Coins
A = int(input())
B = int(input())
C = int(input())
X = int(input())
count = 0

for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if 500*i+100*j+50*k == X:
                count += 1
            else:
                pass
print(count)"""

"""# B - 文字数カウント
S = str(input())

print(S.count('A'),S.count('B'),S.count('C'),S.count('D'),S.count('E'),S.count('F'))
"""

"""# B - 754
S = str(input())
ans = 754

for i in range(len(S)-2):
    tmp = abs(753 - int(S[i]+S[i+1]+S[i+2]))
    if ans >= tmp:
        ans = tmp
    else:
        pass

print(ans)"""


"""# B - Shift only

N = int(input())
A = list(map(int, input().split()))

count = 0
for i in range(max(A)//2):
    for j in range(N):
        if A[j] % 2 == 1:
            print(count)
            exit()
        else:
            A[j] = A[j]//2
    count += 1"""




"""# B - Palindromic Numbers
A,B = list(map(int, input().split()))
count = 0
for i in range(A,B+1):
    C = str(i)
    if C[0] == C[4] and C[1] == C[3]:
        count += 1
    else:
        pass
print(count)"""

"""#B - Balance
N = int(input())
W = list(map(int, input().split()))
tmp = sum(W) // 2
ans_l = 0
i = 0

while ans_l < tmp:
    ans_l += W[i]
    i += 1

ans_r = sum(W)- ans_l
ans = abs(ans_r - ans_l)
print(ans)"""

"""未完# B - ss
S = str(input())
count = 0
ans_s = S[:-1]

while count <= len(ans_s):
    len_a = int(len(ans_s)/2)

    if len(ans_s) % 2 != 0:
        ans_s = ans_s[:-1]
        count += 1
    elif ans_s[:len_a] == ans_s[len_a:]:
        print(len(ans_s))
        exit()
    else:
        ans_s = ans_s[:-1]
        count += 1"""

"""途中# B - Minesweeper
H, W = map(int, input().split())
S = [str(input()) for i in range(H)]
print(S)

for i in range(H):
    for j in range(W):
        if i == 0:
            
        S[i-1][W-1]
"""
"""# B - Lucas Number
N = int(input())

L = [0]*(N+1)
L[0] = 2
L[1] = 1
for i in range(2,N+1):
    L[i] = L[i-1]+L[i-2]

print(L[N])"""

"""# B - Traveling AtCoDeer Problem
N = int(input())
a = list(map(int, input().split()))

ans = max(a)-min(a)
# A = set(a)
# A1 = sorted(A)
# count = 0
# for i in range(len(A)-1) :
#     count += A1[i+1]-A1[i]

print(ans)
"""

"""# B - 1 Dimensional World's Tale
N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

for i in range(-100, 100):
    if X < i <= Y and max(x) < i <= min(y):
        print('No War')
        exit()
    else:
        pass
print('War')
"""

"""# B - Great Ocean View
N = int(input())
H = list(map(int, input().split()))
count = 1
tmp = H[0]

for i in range(1,N):
    if tmp > H[i]:
        pass
    else:
        tmp = H[i]
        count += 1

print(count)
"""

"""途中# B - ss
s = str(input())

s_new = s[:-1]


for i in range(int(len(s_new))):

    if s_new[i] == s_new[int(len(s_new)/2)+i]:
        break
    else:
        s_new = s_new[:-1]

print(len(s_new))
"""
"""# B - Two Anagrams
s = str(input())
t = str(input())

new_s = sorted(s,reverse=False)
new_t = sorted(t,reverse=True)

if new_s < new_t:
    print('Yes')
else:
    print('No')

print(new_s,new_t)
"""
"""# B - Varied
S = str(input())

if len(set(S)) == len(S):
    print('yes')
else:
    print('no')
"""
"""# B - ATCoder
S = str(input())
count = 0
ans = 0
for i in range(len(S)):
    if S[i] == 'A' or S[i] =='C' or S[i] == 'G' or S[i] =='T':
        count += 1
        if ans <= count:
            ans = count
        else:
            pass
    else:
        count = 0

print(ans)
"""
"""# B - Toll Gates
N, M, X = map(int, input().split())
A = list(map(int, input().split()))
tmp = 0
for i in range(M):
    if X < A[i]:
        tmp = i
        break
    else:
        pass
if tmp > M/2:
    print(M-tmp)
else:
    print(tmp)
"""

"""# B - Stone Monument
a, b = map(int, input().split())

tmp = (b-a)*(b-a-1)/2

print(int(tmp-a))
"""


"""# B - Trained?
N = int(input())
a = [int(input()) for k in range(N)]
count = 1
tmp = a[a[0]-1]
while count <= N:
    if a[0] == 2:
        print(count)
        exit()
    elif tmp == 2:
        count += 1
        print(count)
        exit()
    else:
        tmp = a[tmp-1]
        count += 1

print(-1)
"""

"""# B - Counting Roads
N, M = map(int,input().split())
city = [list(map(int, input().split())) for i in range(M)]
road = [0]*N

for i in range(N):
    count = 0
    for j in range(M):
        if i+1 == city[j][0]:
            count += 1
        else:
            pass
        if i+1 == city[j][1]:
            count += 1
        else:
            pass
    road[i] = count
for k in range(N):
    print(road[k])
"""
"""# B - ∵∴∵
O = str(input())
E = str(input())
ans =""

if len(O) == len(E):
    for i in range(len(O)):
        ans += O[i]+E[i]
elif len(O) >= len(E):
    for i in range(len(E)):
        ans += O[i]+E[i]
    ans += O[len(O)-1]
elif len(O) >= len(E):
    for i in range(len(O)):
        ans += O[i]+E[i]
    ans += E[len(E)-1]

print(ans)
"""
"""# B - Algae
r, D, x = map(int,input().split())

for i in range(10):
    x = r * x - D
    print(x)
"""

"""# B - 1 21
a, b = map(str,input().split())
A = int(a+b)
A = A**0.5

if A.is_integer():
    print("Yes")
else:
    print("No")
"""


"""# B - AcCepted
S = str(input())
count = 0
if S[0] == 'A':
    for i in range(2,len(S)-1):
        if S[i] == 'C':
            count += 1
        else:
            pass

    if count == 1:
        S_1 = set(S)
        S_1.remove('A')
        S_1.remove('C')
        if str(S_1).islower() :
            print('AC')
        else:
            print('WA')
    else:
        print('WA')
else:
    print('WA')
"""

"""# B - Exponential
X = int(input())

for i in range(X,0,-1):
    for b in range(1,X+1):
        for q in range(2,10):
            if i == b**q:
                print(i)
                exit()
            else:
                pass
"""

"""# B - Checkpoints
N, M = list(map(int, input().split()))
P = [list(map(int, input().split())) for i in range(N)]
C = [list(map(int, input().split())) for i in range(M)]

ans = [0] * N
for i in range(N): # i番目の人
    D = [10 ** 10] * M
    D_hikaku = 10 ** 10
    for j in range(M): # jのチェックポイント

        D = abs(P[i][0]-C[j][0]) + abs(P[i][1]-C[j][1])
        if D < D_hikaku:
            D_hikaku = D
            ans[i] = j + 1
        else:
            pass

for i in range(N):
    print(ans[i])
"""

"""# B - Bounding
N, X = map(int,input().split())
L = list(map(int, input().split()))
D = 0
count = 1

for i in range(N):
    D += L[i]
    if D <= X:
        count += 1
    else:
        break

print(count)
"""

"""# B - Coins
A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if X == 500 * i + 100 * j + 50 * k:
                count += 1

print(count)
"""
"""中断# B - Comparison
import math
A = int(input())
B = int(input())

A = math.log(A)
B = math.log(B)

if A > B:
    print('GREATER')
elif A < B:
    print('LESS')
else:
    print('EQUAL')
"""

"""# B - Resale
N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

sum_v = []
ans = 0
for i in range(N):
    sum_v.append(V[i]-C[i])
sum_v.sort(reverse=True)

for j in range(N):
    if sum_v[j] > 0:
        ans += sum_v[j]
    else:
        break

print(ans)
"""
"""
#B - リモコン
A, B = map(int,input().split())
sa = abs(B - A)
x = sa // 10
x1 = sa % 10
if x > 0:
    if x1 == 0:
        ans = x
    elif x1 == 1 or x1 == 2 or x1 == 3 :
        ans = x + x1
    elif x1 == 4 or x1 == 6:
        ans = x + 1 + 1
    elif x1 == 5:
        ans = x + 1
    elif x1 == 7:
        ans = x + 1 + 2
    else:
        ans = x + 1 + (10 - x1)
else:
    if x1 <= 3:
        ans = x1
    elif x1 == 4 or x1 == 6:
        ans = 1 + 1
    elif x1 == 5:
        ans = 1
    elif x1 == 7:
        ans = 1 + 2
    else:
        ans = 1 +(10 - x1)

print(ans)

"""

"""# B - NarrowRectanglesEasy
W, a, b = map(int,input().split())

if a + W < b:
    print(b - (a+W))
elif b + W < a:
    print(a - (b + W))
elif a <= b <= a+W or b <= a <= b+W:
    print(0)
"""
