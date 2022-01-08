def kora(N):
    count: int = 0
    maxN = 0
    while N != 1:
        if N % 2 == 0:
            N = N // 2
            count += 1
        else:
            N = 3 * N + 1
            count += 1
        if maxN < N:
            maxN = N

    return(count,maxN)

N = int(input())
max_count =[]
max_N = []
max_Nw = [] #初期値Nと最大値の比較

max_a = 0
max_b = 0
max_c = 0
for i in range(N):
    count = kora(i+1)[0]
    maxN = kora(i+1)[1]
    maxNw = kora(i + 1)[1]/(i+1)
    if max_a < count:
        max_count.append((i+1,count))
        max_a = count
    if max_b < maxN:
        max_N.append((i+1,maxN))
        max_b = maxN
    if max_c < maxNw:
        max_Nw.append((i+1,int(maxNw)))
        max_c = maxNw
#
# ko =[]
# for i in range(N):
#     ko.append(kora(i+1))

print(max_count,len(max_count))
print(max_N,len(max_N))
print(max_Nw,len(max_Nw))

