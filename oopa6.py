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

class player:
    def __init__(self,name,play):
        self.name = name
        self.play = play
    def printy(self):
        return f"name is {self.name} paly is {self.play}"
class goodprog(Emplooyee,player):
    language = "cpp"
    def printn(self,language):
        self.language = language
ankur=Emplooyee("ankur",25,"abs")
harry=Emplooyee("Harry",23,"pps")
karan = goodprog("karan",4567,"laa")
print(karan.language)