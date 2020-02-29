# B053:表の自動生成
H, W = map(int, input().split())
a = [list(map(int, input().split())) for i in range(2)]
ans = [[0 for i in range(W)] for j in range(H)]
ans[0][0] = a[0][0]
ans[0][1] = a[0][1]
ans[1][0] = a[1][0]
ans[1][1] = a[1][1]

sa_H = ans[1][0] - ans[0][0]
sa_H2 = ans[1][1] - ans[0][1]
sa_W = ans[0][1] - ans[0][0]
sa_W2 = ans[1][1] - ans[1][0]
#print(a)
#print(ans)
for i in range(2,H):
    ans[i][0] = ans[i-1][0] + sa_H
    ans[i][1] = ans[i-1][1] + sa_H

for i in range(H):
    for j in range(2,W):
        ans[i][j] = ans[i][j-1] + sa_W

#print(ans)

for l in range(H):
    for k in range(W):
        if k == W-1:
            print(ans[l][k])
        else:
            print(ans[l][k],end=" ")




"""#C056:テストの採点
N, M = map(int, input().split())
a = [list(map(int, input().split())) for i in range(N)]
ans = []
for i in range(N):
    if a[i][0]-5*a[i][1] >= 0:
        tmp = a[i][0]-5*a[i][1]
    else:
        tmp = 0
    if tmp >= M:
        ans.append(i+1)

for j in range(len(ans)):
    print(ans[j])"""


"""#C051:カード並べ
a = list(map(int, input().split()))

a.sort(reverse = True)
ans = int(str(a[0])+str(a[2]))+int(str(a[1])+str(a[3]))
print(ans)"""



"""# B075:商品の表示
N, M = map(int, input().split())
a = [list(map(int, input().split())) for i in range(N)]
a_sub = a[:]
ans_sub = []
ans_b = []
ans = []

DP = [[0 for l in range(M)] for m in range(N)]
# DP = [[1000]*M]*N
# print(a, DP)

for k in range(M):
    a_sub.sort(key=lambda x: x[k], reverse=True)
    for i in range(N):
        tmp = 1
        for j in range(N):
            if a[i][k] == a_sub[j][k]:
                DP[i][k] = j + 1
                break
#             if a[i][k] != a_sub[j][k]:
#                 if j >= 1 and a_sub[j][k] == a_sub[j-1][k]:
#                     pass
#                 else:
#                     tmp += 1
#             else:
#                 DP[i][k] = tmp
#                 break
for n in range(N):
    ans_a = 0
    for m in range(M):
        ans_a += N - DP[n][m]
    ans_b.append(ans_a)

ans_sub = sorted(ans_b, reverse=True)

for o in range(N):
    for p in range(N):
        if ans_b[o] == ans_sub[p]:
            ans.append(p+1)
            break
#print(ans)
for q in range(N):
    if ans.index(ans[q]) < q :
        ans[q] += 1


# print(a_sub, a)
# print(DP)
# print(ans_b, ans_sub)
# print(ans)

for q in range(len(ans)):
    print(ans[q])"""


# for i in range(N):
#     for j in range(M):
#         for k in range(k+1,N):
#             if a[i][j] > a[k][j]:
#                 DP[i][0]


"""#C019:完全数とほぼ完全数
Q = int(input())
S = [int(input()) for i in range(Q)]
P = [0]*Q
ans =[""]*Q
for i in range(Q):
    for j in range(int(S[i]/2)+1,0,-1):
        tmp = S[i]
        if tmp % j == 0:
            tmp = int(tmp/j)
            P[i] += j
        else:
            pass
    if P[i] == S[i]:
        ans[i] = "perfect"
    elif abs(P[i] -S[i]) == 1:
        ans[i] = "nearly"
    else:
        ans[i] = "neither"
for l in range(len(ans)):
    print(ans[l])"""

"""#C075:ポイント払い
N,M = map(int, input().split())
f = [int(input()) for i in range(M)]
P = [0]
C = [N]
c = N
p = 0
for i in range(M):
    if P[i] >= f[i]:
        p = P[i] - f[i]

    else:
        c = C[i] - f[i]
        p += f[i] * 0.1


    C.append(c)
    P.append(p)

for l in range(1,M+1):
    print(C[l],int(P[l]))"""

"""#B021:複数形への変換
N = int(input())
S = [str(input()) for i in range(N)]

for i in range(N):
    if S[i][-1] == "s" or S[i][-1] == "o" or S[i][-1] == "x" or S[i][-2]+S[i][-1] == "sh" or S[i][-2]+S[i][-1] == "ch":
        S[i] = S[i]+"es"
    elif S[i][-1] == "f":
        S[i] = S[i].rstrip("f")
        S[i] = S[i]+"ves"

    elif S[i][-2]+S[i][-1] == "fe":
        S[i] = S[i].rstrip("fe")
        S[i] = S[i] + "ves"

    elif S[i][-1] == "y":
        if S[i][-2] == "a" or S[i][-2] == "i" or S[i][-2] == "u" or S[i][-2] == "e" or S[i][-2] == "o":
            S[i] = S[i] + "s"
        else:
            S[i] = S[i].rstrip("y")
            S[i] = S[i] + "ies"
    else:
        S[i] = S[i] +"s"

for l in range(len(S)):
    print(S[l])"""

"""#B055:タクシー料金
N,M = map(int, input().split())
a = [list(map(int, input().split())) for i in range(N)]
value = []

for i in range(N):
    if  M < a[i][0]:
        value.append(a[i][1])
    else:
        add_n = (M-a[i][0]) // a[i][2] +1
        add_v = a[i][1]+a[i][3]*add_n
        value.append(add_v)

print(min(value),max(value))"""

"""# B013:最遅出社時刻
a,b,c = map(int, input().split())
N = int(input())
h = []
m = []
for i in range(N):
    h1,m1 = [int(i) for i in input().split()]
    h.append(h1)
    m.append(m1)

train_m = c + b
if train_m > 59:
    train_m -= 60
    train_h = 8 - int(train_m / 60)
elif train_m > 59:
    train_h = 8
    train_m = 59 - train_m

print(train_h,train_m)
for j in range(N-1,0,-1):
    if h[j] <= train_h and m[j] <= train_m:
        train_tmp_h = h[j]
        train_tmp_m = m[j]
        break
    else:
        pass

ans_m = train_tmp_m - a
if ans_m < 0:
    ans_m += 60
    ans_h = train_tmp_h - 1
else:
    ans_h = train_tmp_h

ans_h = "0" + str(ans_h)
if ans_m <= 10:
    ans_m = "0" + str(ans_m)
else:
    ans_m = str(ans_m)
print(ans_h+":"+ans_m)"""

"""M,N,K = map(int, input().split())
a = [int(input()) for i in range(K)]
ans_0 = [0]*(M+1)
ans_0[0] = N
for i in range(K):
    tmp = 0
    for j in range(M+1):
        if j != a[i]:
            if ans_0[j] > 0:
                tmp += 1
                ans_0[j] += -1
            else:
                pass
        else:
            pass
    ans_0[a[i]] += tmp

print(ans_0)

ans_1 =[]
for k in range(1,len(ans_0)):
    ans_1.append(ans_0[k])
print(ans_1)

ans = [l+1 for l, v in enumerate(ans_1) if v == max(ans_1)]

for l in range(len(ans)):
    print(ans[l])"""
# for k in range(2,len(ans_0)):
#     if ans_0[k] > ans[0]:
#         ans = []
#         ans[0] = k
#     elif ans_0[k] == ans[0]:
#         ans.append(k)
#     else:
#         pass
# print(ans)
