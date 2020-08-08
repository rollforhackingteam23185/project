#step one: produce an easily computable format (i.e. RPN)

def d():

def parse(string):
    #...
    # sample 1d20;
    ret = {}
    for i in range(1,21): # range is not inclusive at both ends??
        print i
        if i in ret:
            ret[i]=ret[i]+1
        else:
            ret[i]=1
    return ret
