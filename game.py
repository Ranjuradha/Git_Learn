import random
def handcricket():
    print("handcricket game"
          "welcome to the game")
    print("1.rock")
    print("2.paper")
    print("3.scissors")
    print("4.lizard")
    print("5.spock")
    print("choose your option")
    a = int(input())
    if a == 1:
        print("you chose rock")
    elif a == 2:
        print("you chose paper")
    elif a == 3:
        print("you chose scissors")
    elif a == 4:
        print("you chose lizard")
    elif a == 5:
        print("you chose spock")
    else:
        print("invalid option")
    print("computer chose")
    b = random.randint(1, 5)
    if b == 1:
        print("rock")
    elif b == 2:
        print("paper")
    elif b == 3:
        print("scissors")
    elif b == 4:
        print("lizard")
    elif b == 5:
        print("spock")
    else:
        print("invalid option")
    if a == b:
        print("tie")
    elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 4) or (a == 4 and b == 5) or (a == 5 and b == 1):
        print("computer wins")
    else:
        print("you win")

