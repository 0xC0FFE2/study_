import sys
input = sys.stdin.read

def process_commands(commands):
    stack = []
    results = []
    
    for command in commands:
        if command[0] == "1":  # Push X
            _, x = command.split()
            stack.append(int(x))
        elif command[0] == "2":  # Pop and print
            if stack:
                results.append(stack.pop())
            else:
                results.append(-1)
        elif command[0] == "3":  # Print size
            results.append(len(stack))
        elif command[0] == "4":  # Check if empty
            results.append(1 if not stack else 0)
        elif command[0] == "5":  # Print top
            if stack:
                results.append(stack[-1])
            else:
                results.append(-1)
    
    return results

if __name__ == "__main__":
    input_data = input().splitlines()
    n = int(input_data[0])  # Number of commands
    commands = input_data[1:]
    output = process_commands(commands)
    sys.stdout.write("\n".join(map(str, output)) + "\n")