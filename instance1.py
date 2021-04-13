class Emplooyee:
    no_of_leaves=8
    pass
ankur=Emplooyee()
harry=Emplooyee()

harry.name="Harry"
harry.age="23"
harry.school="pps"
print(Emplooyee.no_of_leaves)
print(harry.__dict__)
harry.no_of_leaves=9
print(harry.__dict__)
print(harry.age)