class Employee:
    company="yamaha"
    salary=1000
    bonus=500


    @property
    def totalsalary(self):
        return self.salary+self.bonus

e=Employee()
print(e.totalsalary)