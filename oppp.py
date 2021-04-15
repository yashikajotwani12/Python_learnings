class Employee:
    def __init__(self,name,salary,company):
        self.name=name
        self.salary=salary
        self.company=company
        print("good morningg!!!")
    def getdetails(self):
        print(f"the name of the employee is {self.name}")
        print(f"the salary of the employee is {self.salary}")
        print(f"the company of the employee is {self.company}")

yashika=Employee("yashika",100000000000000000000000000000000000000,"youthubbeee")

yashika.getdetails()

