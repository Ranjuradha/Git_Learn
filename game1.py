import random
def rock_paper_scissors():
    print("Rock, Paper, Scissors, Lizard, Spock")
    print("Welcome to the game")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Lizard")
    print("5. Spock")
    print("Choose your option")
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