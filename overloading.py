class Number:
    def __init__(self, number):
        self.number=number
    def __add__(self,number2):
        print("adding")
        return self.number +number2.number
    def __mul__(self,number2):
        print("adding")
        return self.number *number2.number

n1=Number(5)
n2=Number(6)
sum=n1+n2
mult=n1*n2
print(sum)
print(mult)


