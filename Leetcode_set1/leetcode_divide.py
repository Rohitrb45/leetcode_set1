def divide(divisor,dividend):
    output=0 
    tmp=0
    d=abs(divisor)
    dv=abs(dividend)
    while d-dv>=0:
        tmp=dv
        mul=1
        while d>=tmp:
            d=d-tmp
            output+=mul
            mul+=mul
            tmp+=tmp 

    if (divisor>0 and dividend<0) or (divisor<0 and dividend>0):
        output=-output
    return output


out=divide(10000000,1)
print(out)