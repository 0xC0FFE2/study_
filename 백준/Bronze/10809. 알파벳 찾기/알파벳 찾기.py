alpha = [chr(c) for c in range(97,123)]
target = input()
targetlen = len(target)


for y in alpha:
    times = 0
    
    for x in range(0,targetlen):
        if (target[x] == y):
            break;
        times += 1
    if (times == targetlen):
        print("-1 ", end="")
    else:
        print(str(times) + " ", end="")