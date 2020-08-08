#step one: produce an easily computable format (i.e. RPN)

def parse(string):
    #...
    # sample 1d20;
    ret = {}
    for i in range(1,20):
        print i
        if i in ret:
            ret[i]=ret[i]+1
        else:
            ret[i]=1
    return ret
