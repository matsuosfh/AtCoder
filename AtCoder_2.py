# Card Game for Two
N = int(input())
A = list(map(int,input().split()))

# N = 4
# A = [20, 18, 2, 18]
Alice = []
Bob = []
# 降順にソートする
A.sort(reverse=True)
# for i in range(N):
#     if i % 2 == 0 :
#         Alice.append(A[i])
#     else:
#         Bob.append(A[i])

Alice = A[::2]
Bob = A[1::2]

# それぞれ合計し引く
Alice_sum = sum(int(j) for j in Alice)
Bob_sum = sum(int(j) for j in Bob)

print(Alice_sum, Bob_sum)

ans = Alice_sum - Bob_sum

print(A, Alice, Bob, ans)
