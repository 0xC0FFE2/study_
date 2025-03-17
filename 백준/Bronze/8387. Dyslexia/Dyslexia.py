length = int(input())

original = input()
user = input()

count = 0

for x in range(0,length):
    if (original[x]== user[x]):
        count += 1

print(count)