#E - スプリンクラー
#隣接リストでの解法
N,M,Q = map(int,input().split())

#FalseのN*Nの２次元配列を作る
graph = []
for i in range(0,N):
    # 長さ0の１次元配列を作る
    row = []
    graph.append(row)

# M 本の辺を受け取る
for i in range(0,M):
    u,v = map(int,input().split())

    # 頂点番号は全て-1とする
    u -= 1
    v -= 1

    #頂点uからvへ辺がある
    graph[u].append(v)
    # 頂点vからuへ辺がある
    graph[v].append(u)


# 頂点の色のリストを受け取る
C = list(map(int,input().split()))

# Qこのクエリを受け取る
for i in range(0,Q):
    query = list(map(int,input().split()))

    #スプリンクラーを起動するクエリの場合
    if query[0] == 1:
        x = query[1]

        # 頂点番号は全て-1
        x -= 1

        #頂点xの色を出力する
        print(C[x])

        #頂点xに隣接する頂点の色を頂点xと同じ色にする
        for i in graph[x]:
            C[i] = C[x]

    #スプリンクラーを起動しない場合、
    if query[0] == 2:
        x = query[1]
        y = query[2]

        #頂点番号は-1
        x -= 1

        #頂点xの色を出力する
        print(C[x])

        #頂点xの色をyに書き換える
        C[x] = y


"""
#隣接行列での解法
N,M,Q = map(int,input().split())

#FalseのN*Nの２次元配列を作る
graph = []
for i in range(0,N):
    # 長さNのFalseの１次元配列を作る
    row = []
    for j in range(0,N):
        row.append(False)

    # 長さNのFalseの1次元配列をgraphに追加する
    graph.append(row)

# M 本の辺を受け取る
for i in range(0,M):
    u,v = map(int,input().split())

    # 頂点番号は全て-1とする
    u -= 1
    v -= 1

    #uとvの間には辺があるためTrueにする
    graph[u][v] = True
    graph[v][u] = True

# 頂点の色のリストを受け取る
C = list(map(int,input().split()))

# Qこのクエリを受け取る
for i in range(0,Q):
    query = list(map(int,input().split()))

    #スプリンクラーを起動するクエリの場合
    if query[0] == 1:
        x = query[1]

        # 頂点番号は全て-1
        x -= 1

        #頂点xの色を出力する
        print(C[x])

        #全ての頂点を順番に見る
        for i in range(0,N):

            #頂点iが頂点xに隣接している時、すなわち頂点xと頂点iの間に変がある時
            if graph[x][i]:
                #頂点iの色をC[x]に書き換える
                C[i] = C[x]

    #スプリンクラーを起動しない場合、
    if query[0] == 2:
        x = query[1]
        y = query[2]

        #頂点番号は-1
        x -= 1

        #頂点xの色を出力する
        print(C[x])

        #頂点xの色をyに書き換える
        C[x] = y


"""