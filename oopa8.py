class Emplooyee:
    _pri =9
    __private = 100
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
ankur = Emplooyee("ankur",546,"pps")
print(ankur._Emplooyee__private)