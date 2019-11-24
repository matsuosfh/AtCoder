# Otoshidama
N, Y = list(map(int,input().split()))

# N = [2000, 20000000]
# ans_OK = 0
# 各札で探索

for x in range(N+1):
    for y in range(N+1-x):
        z = N-x-y
        if x + y + z == N and 10000 * x + 5000 * y + 1000 * z == Y:
            print(x, y, z)
            exit()
        else:
            pass

print(-1, -1, -1)
        # for z in range(N[0]+1-x+y):
        #     if x + y + z == N[0] and 10000 * x + 5000 * y + 1000 * z == N[1]:
        #         ans_OK = (x, y, z)
        #     else:
        #         pass

# else:
#     print(ans_OK[0], ans_OK[1], ans_OK[2])