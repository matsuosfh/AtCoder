# A - Table Tennis Training
N,A,B = map(int, input().split())

if (B-A) % 2 == 0:
    ans = int((B-A)/2)
else:
    # ansB1 = A-1
    # ansB2 = int((B - A-1) / 2)
    # ansB = A-1 +1+ ansB2

    ansC2 = int((B - A-1) // 2)
    ans = min(N-B,A-1) +1+ ansC2

print(int(ans))