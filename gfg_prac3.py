# x=10
# print(type(x))
# x=10000000000000000000000000000000000000000000
# print(type(x))

#packing and unpacking 
def fun(a,b,c,d):
   print(a,b,c,d)
list=[1,2,3,4]

fun(*list)

def fun1(a,b,c,d):
    return a+b+c+d
list1=[1,2,3,4]

fun1(*list1)


# packing
def sum(*arg):
    return sum(arg)


    
print(sum(1,3,4,5))
