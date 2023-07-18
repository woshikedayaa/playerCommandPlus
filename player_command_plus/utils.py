def CheckBrackets(str:str):
    stack = []
    for i in range(len(str)):
        if str[i]=="[":
            stack.append(i)
            continue
        elif str[i]=="]":
            if not stack:
                return False
            else:
                stack.pop()
                continue
    return len(stack) == 0

        