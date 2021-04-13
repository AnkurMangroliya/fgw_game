class Library:
    def __init__(self,list,name):
        self.booklist= list
        self.name=name
        self.lendDict = {}

    def displayBooks(self):
        print(f"we have following book in our Library : {self.name}")
        for book in self.booklist:
            print(book)
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("lender-book databse has been updated.")
        else:
            print(f"book is already being used by {self.lendDict[book]}")
    def addBook(self,book):
        self.booklist.append(book)
        print("book has been added to the book list")

    def returnBook(self,book):
        self.booklist.remove(book)

if __name__ == '__main__':
    harry = Library(["python","harry potter","c++","ankur","lakj"],"codewithharry")

    while(True):

        print(f"welcome to the {harry.name} library. enter your cjoice to continue")
        print("1 for display book")
        print("2 for lend a book")
        print("3 for add a book")
        print("4 for return book")
        user_choice = int(input())

        if user_choice == 1:
            harry.displayBooks()

        elif user_choice == 2:
            book = input("enter the nameof the book you want to lend")
            user= input("enter your name")
            harry.lendBook(user,book)
        elif user_choice == 3:
            book = input("enter the nameof the book you want to add")
            harry.addBook(book)


        elif user_choice == 4:
            book = input("enter the nameof the book you want to return")
            harry.returnBook(book)
        else :
            print("not a vlaid option")
        print("press q to quite and c to continue")
        user_choice2=""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2=="q":
                exit()
            if user_choice2=="c":
                continue