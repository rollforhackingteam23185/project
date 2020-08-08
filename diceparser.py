#step one: produce an easily computable format (i.e. RPN)

def parse(string):
    #assuming all tokens seperated by whitespace
    tokens = string.split()
    #print(tokens)
    precedences = {"+": 10,"-":9, "*":7, "^":5, "d": 0}
    #turn into rpn
    stack = [];
    result = [];
    for a in tokens:
        a=a.strip()
        if a.isdigit():
            result.append(a)
        elif a in precedences: #a is an operator
            #print(len(stack))
            while len(stack)!=0 and (stack[-1] in precedences \
                    and (precedences[stack[-1]]<precedences[a] \
                    or (precedences[stack[-1]]==precedences[a] and a!="d"))):
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
    while len(stack)!=0:
        result.append(stack[-1])
        stack.pop()
    queue=[]
    queue.append(result);
    calculate = True;
    #print(queue)
    while calculate:
        calculate=False
        stack=[]
        queue2=[]
        for q in queue:
            if len(q) > 1:
                calculate=True
            else:
                queue2.append(q.copy())
                continue
            i=0
            while not q[i] in precedences:
                i+=1
            if q[i] == "d":
                if(int(q[i-2]) != 1):
                    r=q[:i-2]
                    r.append("1")
                    r.append(q[i-1])
                    r.append("d")
                    for _ in range(1,int(q[i-2])):
                        r.append("1")
                        r.append(q[i-1])
                        r.append("d")
                        r.append("+")
                    r=r+q[i+1:]
                    queue2.append(r.copy())
                    #print(r)
                else:
                    r=q[:i-2]
                    r.append(1)
                    j=i-2
                    r=r+q[i+1:]
                    for j in range(1,int(q[i-1])+1):
                        r[i-2]=str(j)
                        queue2.append(r.copy())
                        #print(r)
            elif q[i] == "+":
                r=q[:i-2]
                r.append(str(int(q[i-2])+int(q[i-1])))
                r=r+q[i+1:]
                queue2.append(r.copy())
                #print(r)
            elif q[i] == "-":
                r=q[:i-2]
                r.append(str(int(q[i-2])-int(q[i-1])))
                r=r+q[i+1:]
                queue2.append(r.copy())
                #print(r)
            elif q[i] == "*":
                r=q[:i-2]
                r.append(str(int(q[i-2])*int(q[i-1])))
                r=r+q[i+1:]
                queue2.append(r.copy())
                #print(r)
            elif q[i] == "^":
                r=q[:i-2]
                r.append(str(int(q[i-2])**int(q[i-1])))
                r=r+q[i+1:]
                queue2.append(r.copy())
                #print(r)
        queue=queue2.copy()
#        print(queue)
    result={}
    for q in queue:
        for r in q:
            if r in result:
                result[r]+=1
            else:
                result[r]=1
    return result

def main():
    print(parse("6 d 6"))

if __name__ == "__main__":
    main()
