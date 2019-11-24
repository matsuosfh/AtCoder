count = 0

for x in range(2021,2041):
    print(x)
count += 1

print('ループ回数：{}'.format(count))

# # Some Sums
# N, A, B = map(int, input().split())
# ans = 0
# for i in N :
#     if A <= sum(list)
# N = 100
# A = 4
# B = 16
# N, A, B = map(int, input().split())
#
# ans = 0
# ans_0 = [] # 足し算対象数値
# ans_1 = 0 # 桁足し算
#
# for i in range(1,N+1): # Nまでの全ての数値確認
#     ans_n = i
#     s = str(i)
#     ans_1 = 0
#     print(i)
#     print('桁数：' + str(len(s)))
#     # for i in range(len(s)):
#     #     print('文字：' + str(s[i]))
#     ans_1 = sum(int(j) for j in s)
#     # for j in range(0, len(s)): # 桁足し算
#     #         ans_1 = ans_1+int(s[j])
#     print('足し算：' + str(ans_1))
#     if A <= ans_1 <= B: # 計算対象抽出
#         ans_0.append(ans_n)
#         print('ans_0：' + str(ans_0))
#     else:
#         pass
#
# for k in range(len(ans_0)): # 各数値の和を取り解答
#     ans = ans + ans_0[k]
#
# print(ans)
#
#
#
# print(N,ans)

# N



"""
A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0

for nA in range(A + 1):
    for nB in range(B + 1):
        for nC in range(C + 1):
            if nA * 500 + nB * 100 + nC * 50 == X:
                ans += 1

print(ans)
"""
"""
ans = 10**9
N = int(input())
A = list(map(int,input().split()))
for i in A:
    p = 0
    while i % 2 == 0:
        i //= 2
        p += 1
    if p < ans:
        ans = p
print(ans)
"""