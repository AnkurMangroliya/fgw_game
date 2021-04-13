from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class rectangle(shape):
    type = "rectangle"
    def __init__(self):
        self.length = 4
        self.breath = 7
    def printarea(self):
        return self.length * self.breath
emp1 = rectangle()
print(emp1.printarea())