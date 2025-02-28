N, L = map(int, input().split())

for length in range(L, 101):  # L부터 100까지
    temp = (N - (length * (length - 1) // 2)) 
    if temp % length == 0:
        x = temp // length
        if x >= 0:  # x가 0 이상이어야 함
            print(" ".join(map(str, range(x, x + length))))
            break
else:
    print(-1)
