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
    @staticmethod
    def printm(string):
        print("this is a "+string)


class programmer(Emplooyee):
    def __init__(self,aname,aage,aschool,language):
        self.name = aname
        self.age = aage
        self.school = aschool
        self.language = language
    def printprog(self):
        return f"name is {self.name} age is {self.age} and school is {self.school} and language is {self.language}"

ankur=Emplooyee("ankur",25,"abs")
harry=Emplooyee("Harry",23,"pps")
karan = programmer ("karan",354,"kks",["python"])
print(karan.printprog())
