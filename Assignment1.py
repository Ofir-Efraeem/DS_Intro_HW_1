#Task A
def my_func(x1=None, x2=None, x3=None ):
    if(not type(x1) == float) or (not type(x2) == float) or (not type(x1) == float):
        return "Error: parameters should be float"
    if(x1+x2+x3 == 0):
        return "Not a number – denominator equals zero"

    num= ((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
    return num


#print(my_func(1.0,2.0,-3.0))

#Task B
def convert(hours=0,minutes=0):
    if(hours<0) or (minutes<0):
        return "Input error!"
    num= hours*3600+minutes*60
    return num

#print(convert(-1,3))
