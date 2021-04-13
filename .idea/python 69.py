class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def explain(self):
        return f"this is employee {self.fname} . {self.lname}"
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "email is not set please using setter"
        return f"{self.fname}.{self.lname}@codewithharrygmail.com"
    @email.setter
    def email(self,string):
        print("setting now...")
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

n1 = Employee("ankur","patel")
n2 = Employee("vishal","patel")
# n2.fname = "kali"
# print(n2.email)
n2.email = "this.that@codewithharrygmail.com"
print(n2.email)
del n2.email
print(n2.email)
