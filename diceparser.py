#step one: produce an easily computable format (i.e. RPN)

def parse(string):
    #assuming all tokens seperated by whitespace
    tokens = string.split()
    print(tokens)
    precedences = {"+": 10,"-":9, "*":7, "^":5, "d": 0}
    #turn into rpn
    stack = [];
    result = [];
    for a in tokens:
        a=a.strip()
        if a.isdigit():
            result.append(a)
        elif a in precedences: #a is an operator
            print(len(stack))
            while len(stack)!=0 and stack[-1] in precedences \
                    and precedences[stack[-1]]<precedences[a] \
                    or precedences[stack[-1]]==precedences[a] and a!="d":
                        result.append(stack[-1])
                        stack.pop()
            stack.append(a)
        elif a=="(":
            stack.append(a)
        elif a==")":
            while stack[-1]!="(":
                result.append(stack[-1])
                stack.pop()
            stack.pop()
    result.append(stack[-1])
    stack.pop()

def main():
    print (parse("1 d 6"))

if __name__ == "__main__":
    main()
