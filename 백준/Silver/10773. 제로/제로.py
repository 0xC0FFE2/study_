import sys
input = sys.stdin.read

k, *numbers = map(int, input().split())
stack = []

for num in numbers:
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
