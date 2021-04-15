# def increment(num):
#     try:
#         return int(num)+1
#     except:
#         raise ValueError("This is not good")

# a=increment('deewdf')
# print(a)

# try:
#     i=int(input("enter a number"))
#     c=1/i
# except Exception as e:
#     print(e)
# else:
#     print("we Are successful")


try:
    i=int(input("enter a number"))
    c=1/i
except Exception as e:
    print(e)
finally:
    print("great success")
