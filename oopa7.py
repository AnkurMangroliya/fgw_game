class dad():
    basketball =1
class son(dad):
    dance=1
    def isdance(self):
        return f"he is {self.dance} no of type dance"
class grandson(son):
    dance=6
harry = dad
carry = son
ankur = grandson
print(son.dance)