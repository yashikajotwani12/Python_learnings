class Employee:
    company="google"
    def getsalary(self):
          print(f"no salary { self.salary}")
    @staticmethod
    def greet():
       print("helloo!!!!")
    def __init__(self):
        print(f"{self}employee is created")

yashika=Employee()
kajal= Employee()
yashika.salary=22000
# kajal.salary=10

print(yashika.company)
print(kajal.company)


Employee.company="youtube"
print(yashika.company)
print(yashika.salary)

yashika.getsalary()
yashika.greet()
