class employee:
    def __init__(self, fname, lname, gender, email):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.email = email

    def Newly_Onboarded_Employee(self):
        print(self.fname, self.lname, self.gender, self.email)



emp1=employee('Dushyant', 'Singh', 'Male', 'dushyant.singh@xyz.com')
emp2=employee('Aditya', 'Singh', 'Male', 'aditya.singh@gmail.com')
print(emp1.fname)
print(emp2.fname)

emp1.Newly_Onboarded_Employee()
emp2.Newly_Onboarded_Employee()