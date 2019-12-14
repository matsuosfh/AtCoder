#D - 重複検査 / Duplicated?
N = int(input())
A = [int(input()) for i in range(N)]
count = 0
A.sort()
for i in range(1,N+1):
    if A[i-1] == i:
        pass
    else:
        ans1 = A[i]
        count += 1
        break

if count == 1:
    for j in range(ans1+1, N+1):
        if A[j-1] == j:
            pass
        else:
            ans2 = j
            break

    print(ans2,ans1)


else:
    print("Correct")


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

