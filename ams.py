def ams(s,b):
    from math import sqrt,log
    if b==0:
        return 0
    return sqrt(2*((s+b+10)*log(1+float(s)/(b+10))-s))