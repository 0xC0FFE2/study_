filecnt = input()
string = input()

for x in range(1,int(filecnt)):
    target = input()
    temp = []
    for x in range(0,len(string)):
        if (x != '?') and (target[x] != string[x]):
            temp.append('?')
        else:
            temp.append(target[x])
    tempstr = ""
    for x in temp:
        tempstr = tempstr + str(x)
    string = tempstr
print(string)