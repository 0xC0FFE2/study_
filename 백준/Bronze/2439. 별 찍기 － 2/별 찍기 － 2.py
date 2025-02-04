cnt = int(input())

for x in range(0,cnt):
    printstr = " "*(cnt-x-1)
    printstr = printstr + "*"*(x+1)
    print(printstr)