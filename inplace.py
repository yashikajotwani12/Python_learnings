import operator

x= operator.iadd(2,3)
print(" The value after adding and assigning : ", end=" ")
print(x)


y="yashika"
z=" jotwani"

y = operator.iconcat(y,z)
print(" my name is : ", end="")
print(y)

##loops

for key ,value in enumerate(['the ','big','bang','theory']):
    print(key,value)
    print(value, end=" ")






questions=['name','color','shape']
answere=['apple','red','a circle']

for questions, answere in zip(questions,answere):
    print("What is your {0}? I am {1}.".format(questions,answere))



lis=[1,2,3,33,4,45,55,56,666,7,2,11,2,2,3333,33,0]
print(" The list is reversed in the order :")

for i in reversed(lis):
    print(i,end=" ")
print("\n")

for i in sorted(lis):
    print(i, end=" ")



# def pypart(n):

#     for i in range(0,n):


#         for j in range(0,i+1):


#             print("* ", end="")


#     print("\r")

# n=5
# pypart(n)

# Function to demonstrate printing pattern
def pypart(n):
     
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ",end="")
      
        # ending line after each row
        print("\r")
 
# Driver Code
n = 5
pypart(n)