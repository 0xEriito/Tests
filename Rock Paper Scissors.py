import random
while True:
    print("Type (Q/q) to quit")
    choices = ['rock', 'paper', 'scissors']
    choices2 = ['r', 'p', 's']
    player = input("Start First : (Rock/r), (Paper/p), (Scissors/s))\n")
    if player in choices :
        pc = random.choice(choices)
        print(pc)

        if pc == 'rock' and player == 'paper':
            print("You Won!")
        elif pc  == 'rock' and player == 'scissors' :
            print("I Won! Good Luck Next Time.")
        elif pc  == 'rock' and player == 'rock' :
            print("It's a draw!")
    
        elif pc  == 'paper' and player  == 'rock' :
            print("I Won! Good Luck Next Time.")
        elif pc  == 'paper' and player  == 'scissors' :
            print("You Won!")
        elif pc  == 'paper' and player  == 'paper' :
            print("It's a draw!")

        elif pc  == 'scissors' and player  == 'rock' :
            print("You Won!")
        elif pc  == 'scissors' and player  == 'scissors' :
            print("It's a draw!")
        elif pc  == 'scissors' and player  == 'paper' :
            print("I Won! Good luck next time.")
        elif player == 'Q' or 'q':
            break
        else:
            pass
    

    elif player in choices2:
        pc = random.choice(choices2)
        print(pc)    
        if pc  == 'r' and player  == 's' :
            print("I Won! Good Luck Next Time.")
        elif pc  == 'r' and player  == 'p' :
            print("You Won!")
        elif pc  == 'r' and player  == 'r' :
            print("It's a draw!")
    
    
        elif pc  == 'p' and player  == 'r' :
            print("I Won! Good Luck Next Time.")
        elif pc  == 'p' and player  == 's' :
            print("You Won!")
        elif pc  == 'p' and player  == 'p' :
            print("It's a draw!")
    
    
        elif pc  == 's' and player  == 'p' :
            print("I Won! Good Luck Next Time.")
        elif pc  == 's' and player  == 'r' :
            print("You Won!")
        elif pc  == 's' and player  == 's' :
            print("It's a draw!")
        elif player == 'Q' or 'q' :
            break
        else :
            pass

    else:
        print("Thanks For Playing, See You Soon!")
        break       