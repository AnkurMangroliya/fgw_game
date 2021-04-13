class Emplooyee:
    no_of_leaves=8
    def __init__(self,aname,aage,aschool):
        self.name = aname
        self.age = aage
        self.school = aschool
    def printd(self):
        return f"name is {self.name} age is {self.age} and school is {self.school}"
    @classmethod
    def dash(cls,string):
        return cls(*string.split("-"))
    def __add__(self, other):
        return self.age + other.age
    def __truediv__(self, other):
        return self.age / other.age
    def __repr__(self):
        return f"my name is {self.name}"
    def __str__(self):
        return f"name is {self.name} age is {self.age} and school is {self.school}"
emp1 = Emplooyee("ankur",454,"pps")
# emp2 = Emplooyee("vishal",454,"pts")
# print(emp1+emp2)
# print(emp1/emp2)
print(str(emp1))
