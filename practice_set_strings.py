# name=input("enter your name\n")
# print("good afternoon, ", name)


letter ='''
Dear <|NAME|>,
You are selected!

Date:<|DATE|>'''
name=input("enter your name\n")
date=input("enter date\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)