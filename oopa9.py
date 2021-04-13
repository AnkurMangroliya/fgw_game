class a:
    classver1 = "i am a devil"
    def __init__(self):
        self.var = 2
        self.classver1 = "i am in class a"
        self.special = 34
class b(a):
    def __init__(self):

        self.var = 4
        self.classver1 = "i am in class 2"
        super().__init__()

a= a()
b = b()
print(b.classver1,b.special)