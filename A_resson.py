# A - Restaurant
N = int(input())

ans = N * 800
tmp = int((N // 15) * 200)

print(ans-tmp)


"""# A - Christmas Eve Eve Eve
D = int(input())
if D == 25:
    print('Christmas')
elif D == 24:
    print('Christmas Eve')
elif D == 23:
    print('Christmas Eve Eve')
else:
    print('Christmas Eve Eve Eve')"""

"""# A - 753
N = int(input())

if N == 3 or N== 5 or N == 7:
    print('YES')
else:
    print('NO')"""

"""# A - Day of Takahashi
a, b = map(int, input().split())

if a <= b:
    print(a)
else:
    print(a-1)"""

"""# A - Garden
A, B = map(int, input().split())
print(A*B-A-B+1)"""

"""#B - Balance
N = int(input())
W = list(map(int, input().split()))

print(c1[0]+c2[1]+c3[2])
"""
"""# A - ringring
A = list(map(int,input().split()))
A.sort()
print(A[0]+A[1])"""

"""# A - Good Integer
N = str(input())

a = N[0]
b = N[1]
c = N[2]
d = N[3]

if a == b == c or b == c == d:
    print("Yes")
else:
    print("No")"""




"""# A - One out of Three
A, B, C = map(int, input().split())

if A == B:
    print(C)
elif B == C:
    print(A)
else:
    print(B)
"""
"""# A - Airplane
A = list(map(int,input().split()))
A.sort()

print(A[0]+A[1])
"""
"""# A - RGB Cards
r, g, b = map(str,input().split())

if int(r+g+b) % 4 ==0:
    print('YES')
else:
    print('NO')
"""

"""# A - Remaining Time
A, B = map(int,input().split())
ans = A + B
if ans >= 24:
    ans = ans - 24
else:
    pass
print(ans)
"""
"""# A - Palindromic Number
N = str(input())
if N[0] == N[2]:
    print('Yes')
else:
    print('No')"""
"""# A - Restricted
A, B = map(int,input().split())

if A+B >= 10:
    print("error")
else:
    print(A+B)
"""
"""# A - Round Up the Mean
import math
a, b = map(int,input().split())
print(math.ceil((a+b)/2))
"""
"""# A - Cats and Dogs
A, B, X = map(int, input().split())
if A <= X <= A + B:
    print('YES')
else:
    print('NO')
"""
"""# A - Double Helix

b= str(input())
if b == 'A':
	print('T')
elif b =='T':
	print('A')
elif b == 'C':
	print('G')
else:
	print('C')
"""
"""# A - Buttons
A, B= map(int,input().split())
ans=0
count=0
for i in range(2):
	if  A >= B:
		ans += A
		A= A-1
		count = i
	else:
		ans += B
		B = B-1
		count = i

print(ans)
"""
"""# A - Colorful Transceivers
A, B, C, D = map(int,input().split())
if abs(A-C) <= D:
    print('Yes')
elif abs(A-B) <= D and abs(B-C) <= D:
    print('Yes')
else:
    print('No')
"""
"""# A - ABD
N= int(input())
if N <= 999 :
	print('ABC')
else:
	print('ABD')
"""
"""# A - Maximize the Formula
A = list(map(int,input().split()))
A_new=sorted(A,reverse=True)
A2=str(A_new[0])+str(A_new[1])
ans = int(A2)+ A_new[2]
print(ans)
"""

"""# A - Between Two Integers
A, B, C = map(int,input().split())
if A <= C <= B:
    print('Yes')
else:
    print('No')
"""
"""# A - ι⊥l
a, b, c = map(int,input().split())

if b-a == c-b:
    print('YES')
else:
    print('NO')
"""
"""# A - Ferris Wheel
A, B = map(int,input().split())

if A >= 13:
    print(B)
elif 6 <= A <= 12:
    print(int(B/2))
else:
    print(0)
"""

"""# A - Fifty-Fifty
A = str(input())
Acount =[]
ans = 'No'

for i in range(len(A)):
    if A.count(A[i]) == 2:
        Acount.append(2)
    else:
        Acount.append(0)

if Acount == [2,2,2,2]:
	print('Yes')
else:
	print('No')
"""
"""# A - Product
a, b = map(int,input().split())

A = a * b
if A % 2 == 0:
    print("Even")
else:
    print('Odd')"""

"""# A - Buying Sweets
X = int(input())
A = int(input())
B = int(input())

ans = (X-A) % B
print(ans)
"""
"""# A - Rated for Me
R = int(input())

if R < 1200:
    print('ABC')
elif 1200 <= R <2800:
    print('ARC')
else:
    print('AGC')
"""
"""# A - Discount Fare
X, Y = list(map(int, input().split()))
ans = X+0.5*Y
print(int(ans))
"""
"""
# A - 居合を終え、青い絵を覆う / UOIAUAI
c = str(input())
if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
    print('vowel')
else:
    print('consonant')"""

"""# A - AtCoDeerくんとペンキ / AtCoDeer and Paint Cans

A = list(map(str, input().split()))
count = 0
for i in range(len(A)-1):
    if A[i] != A[i+1]:
        count += 1
    else:
        pass
if A[0] != A[2]:
    count += 1
else:
    pass
if A[0] == A[1] ==A[2]:
    count = 1

print(count)
"""
"""# A - AtCoder *** Contest

H = list(map(str, input().split()))
print(H[0][0]+H[1][0]+H[2][0])
"""
"""# A - Rounding
X, A = list(map(int, input().split()))
if X < A:
    print(0)
else:
    print(10)
"""
"""# A - Harmony
A, B = list(map(int, input().split()))

if (A + B) % 2 == 0:
    ans = int((A + B) / 2)
    print(ans)
else:
    print('IMPOSSIBLE')
"""

"""# A - AKIBA
S = str(input())

# 文字列からAを抜いて KIHBRになればOK

if S.find('AA') == -1 :
    if S.find('KA') == -1 :
        if S.find('IA') == -1:
            S2 = S.replace('A','')
            if S2 == 'KIHBR':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')

#  sankou
import re
S = input()
if re.match("A?KIHA?BA?RA?$",S):
    print("YES")
else:
    print("NO")
"""

"""# A - AtCoder Group Contest
N = int(input())
A = list(map(int, input().split()))
i = 1
ans = 0
A.sort(reverse=True)
print(A)

while i <= 2*N:
    ans = ans + A[i]
    i += 2

print(ans)

#A[1]+A[3]+A[5]
"""
"""# A - Three-letter acronym
s1,s2,s3 = map(str, input().split())

s1 = s1.upper()
s2 = s2.upper()
s3 = s3.upper()
print(s1[0],s2[0],s3[0],sep='')
"""
"""# A - Biscuit Generator
A, B, T = map(int,input().split())
ans = 0
for i in range(1, T+1):
    if i % A == 0:
        ans = ans + B
    else:
        pass

print(ans)
"""
"""# A - HonestOrDishonest
a, b = map(str,input().split())
if a == 'H':
    print(b)
else:
    if b == 'H':
        print('D')
    else:
        print('H')
"""
