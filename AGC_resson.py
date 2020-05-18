#A - Range Flip Find Route
def main():
    H, W = map(int, input().split())
    s = []
    for _ in range(H):
        S = input()
        s.append(S)
    print(s)
print(main())

"""#A - Wanna go back home
S =input()
n = 0
w = 0
s = 0
e = 0
for i in range(len(S)):
    if S[i] == "N":
        n += 1
    elif S[i] == "W":
        w += 1
    elif S[i] == "S":
        s += 1
    else:
        e += 1

#print(n,w,s,e)

if (n > 0 and s == 0) or (s > 0 and n == 0):
    print("No")
elif(w > 0 and e == 0) or (e > 0 and w == 0):
    print("No")
else:
    print("Yes")
"""

"""#A - Fairness
A,B,C,K = map(int, input().split())

if K % 2 == 0:
    ans = A - B
else:
    ans = B - A

if abs(ans) >= 10**18:
    print("Unfair")
else:
    print(ans)
"""

"""# A - Zero-Sum Ranges
N = int(input())
A = list(map(int, input().split()))
S = [0]*N
S[0] = A[0]
DP =[]
count = 0
for i in range(1,N):
    S[i] = S[i-1]+A[i]

for i in range(N):
    if S[i] == 0:
        DP
        count += 1
    else:


print(S)"""



"""#A - Candy Distribution Again
N,x = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)

tmp = 0
A_1  = x
for i in range(N):
    A_1 = A_1 - a[i]
    if A_1 > 0:
        if i == N-1:
            print(tmp)
            exit()
        else:
            tmp += 1
    elif A_1 == 0:
        tmp += 1
        print(tmp)
        exit()

    else:
        print(tmp)
        exit()
print(tmp)"""