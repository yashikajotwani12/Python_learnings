# x=10
# print("X is of type:",type((x)))

# y=10.88
# print("y is of type:",type((y)))


# x=x+y


# print("X is of type:",type((x)))

#operator overloading
print(1+2)
print("yashika "+" jotwani")
print(3*4)
print("yashika"*5)



# complex numbers using operator overloading

'''class complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def _add_(self,other):
        return self.a + other.a , self.b + other.b 

    def __str__(self):
        return self.a, self.b

obj1= complex(1,2)
obj2= complex(3,4)
obj3= obj1 + obj2
print(obj3)
'''
class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
  
     # adding two objects 
    def __add__(self, other):
        return self.a + other.a, self.b + other.b
  
    def __str__(self):
        return self.a, self.b
  
Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)