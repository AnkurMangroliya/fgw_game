class Emplooyee:
    no_of_leaves=8
    def __init__(self,aname,aage,aschool):
        self.name = aname
        self.age = aage
        self.school = aschool
    def printd(self):
        return f"name is {self.name} age is {self.age} and school is {self.school}"


# ankur=Emplooyee()
harry=Emplooyee("Harry",23,"pps")
#
# harry.name="Harry"
# harry.age="23"
# harry.school="pps"
print(harry.printd())