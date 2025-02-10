while True:
    input_ = input()
    temp = []
    status = False
    error= False
    if (input_ == "."):
        break
    else:
        for x in range(0,len(input_)):
            if input_[x] == "[" or input_[x] == "(":
                temp.append(input_[x])
            elif input_[x] == ")" or input_[x] == "]":
                if (len(temp)==0):
                    error=True
                    break
                elif (temp[-1]!="[") and (input_[x] == "]"):
                    break
                elif (temp[-1]!="(") and (input_[x] == ")"):
                    break
                else:
                    temp.pop()
        if (len(temp) == 0) and error==False:
            status = True
    if(status):
        print("yes")
    else:
        print("no")