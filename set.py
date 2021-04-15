# a={1,2,3,4,5,2} 
# # sets dont have repetetive
# print(type(a))
# print(a)
a={}
# empty dictionary
print(type(a))
a=set()
print(type(a))
# set methods
a.add(2)
a.add(6)
print(a)
print(len(a))
a.remove(6)
print(a)
a.pop()
print(a)