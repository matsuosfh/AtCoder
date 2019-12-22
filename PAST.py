# F - DoubleCamelCase Sort
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
print(ans)

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

