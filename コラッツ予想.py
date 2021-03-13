def kora(N):
    count: int = 0
    while N != 1:
        if N % 2 == 0:
            N = N // 2
            count += 1
        else:
            N = 3 * N + 1
            count += 1

    return(count)

N = int(input())
max_count =[]

max_a = 0
for i in range(N):
    count = kora(i+1)
    if max_a < count:
        max_count.append((i+1,count))
        max_a = count

# ko =[]
# for i in range(N):
#     ko.append(kora(i+1))

print(max_count)