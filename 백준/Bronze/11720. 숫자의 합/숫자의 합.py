lenth = int(input())
user_input = input()

data = []
for x in range(0,lenth):
    data.append(user_input[x])
#print(data)
total = 0
for x in data:
    total += int(x)
print(total)
#print(data)