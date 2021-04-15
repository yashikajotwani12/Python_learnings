# swap two variables
# x=int(input("enter num1 \n"))
# y=int(input("enter num2 \n"))
# x,y=y,x
# print("After Swapping :",x,y)

# private Variables

# class Map:
#     def __init__(self,iterate):
#                                  self.list=[]
#                                  self.__geek(iterate)

#     def geek(self, iterate):
#         for item in iterate:
#             self.list.append(item)
a =  not True
b =  not False
print(a)
print(b)
# teranary operator
a,b = 10,8

min = a if a < b else b
print(min)

a,b=10,20

print((b,a)[a<b])
print({True :a , False: b}[a<b])

print((lambda :b , lambda :a)[a<b]())

