max_ = 0
current = 0
while True:
    input_ = input()
    out_cnt = int(input_.split(" ")[0])
    in_cnt = int(input_.split(" ")[1])

    current += in_cnt
    current -= out_cnt
    
    if (max_ < current):
        max_ = current
    if (in_cnt == 0):
        break
    
print(max_)