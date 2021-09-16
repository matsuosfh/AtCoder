# Daydream

S = "erasedream"

add_d = ['dream', 'dreamer', 'erase', 'eraser']

T = []

# Sからadd_dを確認し
# add_dに該当した場合、文字数分Sから削除する
# 文字数が減ったSについて再度 add_dに該当するか確認する。

for i in range(len(S)):
    if S[-3] == add_d[i][-3]:
        T.insert(0, add_d[i])
        if len(S) == len(T):
            print('YES')
            exit()
        elif len(S) < len(T):
            print('NO')
            exit()
        else:
            T.insert(0, add_d[i])
            if S[-len(T)-3] == T[-len(T)-3]:
                if len(S) == len(T):
                    print('YES')
                    exit()
                elif len(S) < len(T):
                    print('NO')
                    exit()
                else:
                    T.insert(0, add_d[i])
            else:
                print('NO')

        # T = T + add_d[i]

    else:
        pass


# Tにadd_dを任意の順で結合させる
print(len(S))


# for i in range(4):
#     T = T + add_d[i]
#     if S == T :
#         print('YES')
#         exit()
#     else:
#         pass
# print('NO')

# 文字数がS<Tなら　一致しないので確認を止まる
len(S) < len(T)
print(len(T))
print(T)

# if S == T :
#     print(YES)
# else:
#     print(NO)
# print(add_d)