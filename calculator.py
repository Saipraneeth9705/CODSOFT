def add(a,b):
    return a+b 
def sub(a,b):
    return a-b 
def mul(a,b):
    return a*b 
def div(a,b):
    return a/b 
def mdiv(a,b):
    return a%b
print("please selct the operation\n" "1.add\n","2.sub\n","3.mul\n","4.div\n","5.mdiv\n")
select=int(input("select operations from 1,2,3,4,5:"))
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
if select==1:
   print(add(a,b))
elif select==2:
    print(sub(a,b))
elif select==3:
    print(mul(a,b))
elif select==4:
    print(div(a,b))
elif select==5:
    print(mdiv(a,b))
else:
    print("invalid input")
