#F - 回文行列
from collections import Counter
N = int(input())
s = [str(input()) for i in range(N)]
t =""
DP = []
print(s)
for i in range(N):
    t += s[i]
print(t)
counter = Counter(t).most_common()
print(counter)
print(counter[0][1])

if N % 2 == 0:
    N_1 = N
    for j in range(len(counter)):
        if counter[j][1] % 2 == 0:
            if N_1 - counter[j][1] >= 0:
                DP.append(counter[j])
                N_1 -= counter[j][1]
            else:
                pass
            if N_1 <= 0:
                break
            else:
                pass
print(DP)

"""#E - スプリンクラー
N,M,Q = map(int, input().split())
if M >= 1:
    v = [list(map(int, input().split())) for i in range(M)]
else:
    pass
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(Q)]
DP = [[] for p in range(N)]

if M == 0:
    DP = [[]]
elif M==1:
    DP[v[0][0] - 1].append(v[0][1])
    DP[v[0][1] - 1].append(v[0][0])
else:
    for i in range(M):
        DP[v[i][0]-1].append(v[i][1])
        DP[v[i][1]-1].append(v[i][0])

for k in range(Q):
    if s[k][0] == 1:
        print(c[s[k][1]-1])
        if len(DP[s[k][1]-1]) == 0:
            pass
        elif len(DP[s[k][1]-1]) == 1:
            c[DP[s[k][1]-1][0]-1] = c[s[k][1]-1]
        else:
            for l in range(len(DP[s[k][1]-1])):
                c[DP[s[k][1]-1][l]-1] = c[s[k][1]-1]
    else:
        print(c[s[k][1] - 1])
        c[s[k][1] - 1] = s[k][2]"""


"""#D - 電光掲示板
N = int(input())
s = [list(map(str,input().split())) for i in range(5)]
print(s)

for i in range(5)
    for j in range(N):
s[1][2] s[2][2] s[3][2]=="."
"""




"""#C - 等比数列
import math
A,R,N = map(int, input().split())
T = math.log(1000000000)
if math.log(A)+(N-1)*math.log(R) >T:
    print("large")
else:
    print(A*(R**(N-1)))"""


"""#B - ダイナミック・スコアリング
N,M,Q = map(int, input().split())
s = [list(map(int, input().split())) for i in range(Q)]
DP = [[[0] * M for k in range(2)]for l in range(N)]
DP_m = [N]*M
print(DP)
for i in range(Q):
    if s[i][0] == 1:
        for j in range(M):
            if DP[s[i][1]-1][1][j] == 1:
                DP[s[i][1]-1][0][j] = DP_m[j]
            else:
                pass
        print(sum(DP[s[i][1]-1][0]))
    else:
        if DP_m[s[i][2]-1] > 0:
            DP_m[s[i][2]-1] -= 1
        else:
            pass

        DP[s[i][1] - 1][1][s[i][2] - 1] = 1"""








"""#A - ケース・センシティブ
s=input()
t=input()

if s == t:
    print("same")
elif s.lower()==t.lower():
    print("case-insensitive")
else:
    print("different")"""


"""# F - DoubleCamelCase Sort
S = str(input())
T = ""
DP =[]
ans = ""
count = 0

for i in range(len(S)):
    T += S[i]
    if S[i].isupper() == True:
        count += 1
        if count == 2:
            DP.append(T)
            T = ""
            count = 0
        else:
            pass
    else:
        pass
DP.sort(key=str.lower)
ans=''.join(DP)
print(ans)"""

"""# E - SNS のログ / Restore
N,Q = map(int, input().split())
S = [list(map(int, input().split())) for i in range(Q)]

ans = [["N" for i in range(N)] for j in range(N)]
tmp = ["N"]*N

for i in range(Q):
    if S[i][0] == 1 :
        ans[S[i][1]-1][S[i][2]-1] = "Y"
    elif S[i][0] == 2:
        for j in range(N):
            if ans[j][S[i][1]-1] == "Y" and j != S[i][1]-1:
                ans[S[i][1]-1][j] = "Y"
            else:
                pass
    else:
        for k in range(N):
            if ans[S[i][1]-1][k] == "Y" and k != S[i][1]-1:
                for l in range(N):
                    if ans[k][l] == "Y":
                        tmp[l] = "Y"
                    else:
                        pass

        for m in range(N):
            if tmp[m] == "Y":
                ans[S[i][1] - 1][m] = "Y"
            else:
                pass
for o in range(N):
    ans[o][o] = "N"

for n in range(N):
    ans_n = "".join(ans[n])
    print(ans_n)"""






"""#D - 重複検査 / Duplicated?
N = int(input())
A = [int(input()) for i in range(N)]
count = 0
ans1 = 0
ans2 = 0
B = sorted(A)
for i in range(1, N + 1):
    if B[i - 1] == i:
        pass
    elif B[i-1] < i:
        ans1 = B[i-1]
        count = 1
        break
    else:
        ans2 = i
        count = 2
        break

if count == 1:
    for j in range(i, N + 1):
        if B[j - 1] == j:
            ans2 = j - 1
            break
        else:
            ans2 = N


elif count == 2:
    for j in range(i , N+1):
        if B[j-1] == j:
            ans1 = j
            break
        else:
            ans1 = N
if count != 0:
    print(ans1, ans2)
else:
    print("Correct")"""


"""# C - 3 番目 / The Third
A = list(map(int, input().split()))
B = sorted(A, reverse=True)

print(B[2])
"""

"""#B - 増減管理 / Up and Down
N = int(input())
A = [int(input()) for i in range(N)]
ans1 = 0
ans2 = 0
for i in range(N-1):
    if A[i] < A[i+1]:
        ans1 = A[i+1]-A[i]
        print("up " + str(ans1))
    elif A[i] > A[i+1]:
        ans2 = A[i]-A[i+1]
        print("down "+ str(ans2))
    else:
        print("stay")"""

"""# A - 2 倍チェック / Is It a Number?
S = input()
if S.isdecimal() == True:
    print(int(S)*2)
else:
    print("error")"""

