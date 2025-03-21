def check_mirror(text):
    return text == text[::-1]

user_string = input().strip()

longest_suffix = ""
suffix_start = len(user_string)

for i in range(len(user_string)):
    suffix = user_string[i:]
    if check_mirror(suffix) and len(suffix) > len(longest_suffix):
        longest_suffix = suffix
        suffix_start = i

prefix = user_string[:suffix_start]
result = user_string + prefix[::-1]

print(len(result))