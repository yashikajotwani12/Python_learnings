# name=input("Enter your name")
# surname = raw_input("Enter Your surname")
# inputs for competetive programming

# import sys
# def get_ints():return map(int,sys.stdin.readline().strip().split())
# a,b,c,d = get_ints()
# print(get_ints())

# print("Welcome to Python world ", end=" ")
# print("Geeks for geeks" , end=" ")

# print('9','0','9','888','9','7',sep='@')

# basic calc using python
def add(num1,num2):
    return num1+num2

def substract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

division=lambda num1,num2:num1/num2


print('''Please Select one option:
        1.Add
        2.Substract
        3.Multiply
        4.Divide

       ''')
select=int(input("Enter your Choice from 1,2,3,4:  "))
number_1=int(input("Enter First number"))
number_2=int(input("Enter Second number"))

if select==1:
    print(number_1 ,"+",number_2,"=", add(number_1,number_2))
      
elif select==2:
    print(number_1 ,"-",number_2,"=" ,substract(number_1,number_2))
      
elif select==3:
    print(number_1 ,"*",number_2,"=" ,multiply(number_1,number_2))
      
elif select==4:
    print(number_1 ,"/",number_2,"=", division(number_1,number_2))

else:
    print("Invalid Input")
      
       