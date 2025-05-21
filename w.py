def f_to_c(f):
    c= (f-32)*5/9
    return c

def c_to_f(c):
    f= (c*9/5)+32
    return f

f= float(input("enter farenheit:"))
c= float(input("enter celsius:"))
cho= int(input("enter 1 for finding celsius\n enter 2 for finding farhenheit"))

if(cho==1):
    print("celsius=",f_to_c(f))
if(cho==2):
    print("farenheit=",c_to_f(c))


