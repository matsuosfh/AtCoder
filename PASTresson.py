

"""#E - スプリンクラー
#隣接リスト
N,M,Q = map(int,input().split())
graph = []

for i in range(0,N):
    row =[]
    graph.append(row)
#辺を受け取る
for i in range(0,M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    #頂点u,vからv,uへ辺
    graph[u].append(v)
    graph[v].append(u)

#頂点の色を受け取る
C = list(map(int,input().split()))

#クエリを受け取る
for i in range(0,Q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        x = query[1]
        x -= 1
        print(C[x])
        #全ての頂点を見る
        for i in graph[x]:
            C[i] = C[x]
    if query[0] == 2:
        x = query[1]
        y = query[2]
        x -= 1
        print(C[x])
        C[x] = y"""


#隣接行列
"""N,M,Q = map(int,input().split())

graph = []
#N*Nの行列(false)
for i in range(0,N):
    row = []
    for j in range(0,N):
        row.append(False)
    graph.append(row)

#辺の情報書き込む
for i in range(0,M):
    u,v = map(int,input().split())
    #頂点番号は-1
    u -= 1
    v -= 1

    graph[u][v] =True
    graph[v][u] =True

#頂点の色を受け取る
C = list(map(int,input().split()))

#クエリを受け取る
for i in range(0,Q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        x = query[1]
        x -= 1
        print(C[x])
        #全ての頂点を見る
        for i in range(0,N):
            if graph[x][i]:
                C[i] = C[x]
    if query[0] == 2:
        x = query[1]
        y = query[2]
        x -= 1
        print(C[x])
        C[x] = y

"""


"""#隣接行列
graph = [
    [False,True,True]
    [True,False,True]
    [True,True,False]
]
"""
"""#D - パターンマッチ
S = input()

def is_match(T,S):

    for i in range(0,len(S)-len(T)+1):
        ok = True
        for j in range(0,len(T)):
            if S[i+j] != T[j] and T[j] != ".":
                ok = False
        if ok:
            return True
    return False

#使える文字の一覧
C = "abcdefghijklmnopqrstuvwxyz."
M =[]
#1文字
for T in C:
    if is_match(T,S):
        M.append(T)
#2文字
for c1 in C:
    for c2 in C:
        T = c1 + c2
        if is_match(T,S):
            M.append(T)
#3文字
for c1 in C:
    for c2 in C:
        for c3 in C:
            T = c1 + c2 +c3
            if is_match(T,S):
                M.append(T)

print(len(M))"""


"""#A - We Love Golf
N = int(input())
A,B = map(int, input().split())
ans = False
for i in range(A,B+1):
    if i % N == 0:
        ans = True

if ans:
    print("OK")
else:
    print("NG")"""

"""#A - ゾロ目数
N = int(input())
ans = 0
for i in range(1,555555+1):
    a = str(i)
    ok = True

    for s in a:
        if s != a[0]:
            ok = False
    if ok:
        ans += 1

    if ok and ans == N:
        ans2 = i
print(ans2)"""


"""#C - 山崩し
N = int(input())
S = []

for i in range(0,N):
    si = input()
    si = list(si) #文字列を文字のリストに変換する
    S.append(si)


for i in range(N-2,-1,-1):
    for j in range(1,2*N-1):
        if S[i][j] == '#':
            if S[i+1][j-1] == 'X':
                S[i][j] = 'X'
            if S[i+1][j] == 'X':
                S[i][j] = 'X'
            if S[i+1][j+1] == 'X':
                S[i][j] = 'X'

for i in range(N):
    S[i] = ''.join(S[i])
    print(S[i])
"""

"""#C - Takahashi's Information
C = []
for _ in range(0,3):
    row = list(map(int,input().split()))
    C.append(row)

ok = True
#print(C)

#1列目と２列目
if C[0][0]-C[0][1] != C[1][0]-C[1][1] or C[1][0]-C[1][1] != C[2][0]-C[2][1]:
    ok = False
#2列目と3列目
if C[0][1]-C[0][2] != C[1][1]-C[1][2] or C[1][1]-C[1][2] != C[2][1]-C[2][2]:
    ok = False
#1行目と2行目

if C[0][0]-C[1][0] != C[0][1]-C[1][1] or C[0][1]-C[1][1] != C[0][2]-C[1][2]:
    ok = False
#2行目と3行目
if C[1][0]-C[2][0] != C[1][1]-C[2][1] or C[1][1]-C[2][1] != C[1][2]-C[2][2]:
    ok = False
if ok:
    print("Yes")
else:
    print("No")"""

"""#B - Bingo
A =[]
for _ in range(0,3):
    row = list(map(int,input().split()))
    A.append(row)
M = []
for _ in range(0,3):
    row = []
    for _ in range(0,3):
        row.append(False)
    M.append(row)

N = int(input())
for i in range(N):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if A[j][k] == b:
                M[j][k] = True

bingo = False
for i in range(0,3):
    if M[i][0] and M[i][1] and M[i][2]:
        bingo = True

for i in range(0,3):
    if M[0][i] and M[1][i] and M[2][i]:
        bingo = True

if M[0][0] and M[1][1] and M[2][2]:
    bingo = True

if M[0][2] and M[1][1] and M[2][0]:
    bingo = True

if bingo:
    print("Yes")
else:
    print("No")"""



"""#C - 3 番目
a= list(map(int,input().split()))
a.sort(reverse=True)
print(a[2])"""

"""#B - 多数決
S = input()
na = S.count("a")
nb = S.count("b")
nc = S.count("c")

mx = max(na,nb,nc)
if mx == na:
    print("a")
elif mx == nb:
    print("b")
else:
    print("c")

# a = 0
# b = 0
# c = 0
# for i in range(len(S)):
#     if S[i] == "a":
#         a += 1
#     elif S[i] == "b":
#         b += 1
#     else:
#         c += 1
#
# if max(a,b,c) == a:
#     print("a")
# elif max(a,b,c) == b:
#     print("b")
# else:
#     print("c")
"""
"""#C - 3 番目
a= list(map(int,input().split()))
a.sort()
print(a[3])"""