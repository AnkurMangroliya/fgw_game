import random
l=["s","w","g"]
choice=0
number_choice=0
human_p=0
computer_p=0
while(choice<10):
    i=input("s for snake g for gun w for water:")
    a=random.choice(l)
    if i==a:
        print("tai")
    elif i=="s" and a=="g":
        computer_p+=1
        print(f"you guess {i} and computer guess {a}")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_p} and your point is {human_p} \n")
    elif i == "s" and a == "w":
        human_p += 1
        print(f"you guess {i} and computer guess {a}")
        print("human wins 1 point \n")
        print(f"computer_point is {computer_p} and your point is {human_p} \n")
    elif i=="w" and a=="s":
        computer_p+=1
        print(f"you guess {i} and computer guess {a}")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_p} and your point is {human_p} \n")
    elif i == "w" and a == "g":
        human_p += 1
        print(f"you guess {i} and computer guess {a}")
        print("human wins 1 point \n")
        print(f"computer_point is {computer_p} and your point is {human_p} \n")
    elif i=="g" and a=="w":
        computer_p+=1
        print(f"you guess {i} and computer guess {a}")
        print("comouter wins 1 point \n")
        print(f"computer_point is {computer_p} and your point is {human_p} \n")
    elif i == "g" and a == "s":
        human_p += 1
        print(f"you guess {i} and computer guess {a}")
        print("human wins 1 point \n")
        print(f"computer_point is {computer_p} and your point is {human_p} \n")
    else:
        print("invalid choice")
    choice+=1
if human_p == computer_p:
    print("tie")
elif human_p<computer_p:
    print("computer won the match")
elif human_p>computer_p:
    print("human won the match")