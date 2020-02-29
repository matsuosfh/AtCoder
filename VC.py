"""# 高橋君とお肉
N = int(input())
S = [int(input()) for i in range(N)]

S.sort()
if N == 1:
    print(S[0])
elif N == 2:
    print(max(S))
elif N == 3:
    print(max(S[0]+S[1],S[2]))
else:
    print(min(max(S[0] + S[3], S[1] + S[2]),max(S[0]+S[1]+S[2],S[3])))"""


"""#B - Exponential
X = int(input())
for i in range(X,0,-1):
    X_1 = i**0.5
    if X_1.is_integer():
        print(i)
        exit()
    else:
        pass"""

"""#B - Different Distribution
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
A.sort(key=lambda x: x[1])

print((A[0][0])+A[0][1])"""