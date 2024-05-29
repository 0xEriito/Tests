import random

while True:
    
    words = ["apple", "tea", "italy", "monalisa", "sushi", "car", "table", "water"]
    
    pc = random.choice(words)
    
    print("\n(type Q/q to Quit)\n")
    
    if pc == words[0]:
        try:
            print ("I'm a fruit, people love me in pies! Who Am I ?\n")
            answer = input("Enter Your Answer: ")
            if answer.lower() == 'apple':
                print("\nYou're Correct! I'm An Apple! A Delicious Red One :D\n")
                stov = input("Do You Want To Start Over? (y/n):  ")
                if stov.lower() == 'n':
                    print("See You Later!")
                    break
                elif stov.lower() == 'y':
                    continue
                else:
                    print("Unavailable Option!")
                    break
            elif answer.lower() == 'q':
                print("See You Later!")
                break
            else:
                print("Wrong Answer Or Typo, Try Again :)")
        except ValueError:
            print("The Answer Should Be A Word!")
        
            
    
    elif pc == words[1]:
        try:
            print ("I'm a word, but also a letter, Who Am I ?\n")
            answer = input("Enter Your Answer: ")
            if answer.lower() == 'tea':
                print("\nYou're Correct! I'm Tea! :D\n")
                stov = input("Do You Want To Start Over? (y/n):  ")
                if stov.lower() == 'n':
                    print("See You Later!")
                    break
                elif stov.lower() == 'y':
                    continue
                else:
                    print("Unavailable Option!")
                    break
            elif answer.lower() == 'q':
                print("See You Later!")
                break
            else:
                print("Wrong Answer Or Typo, Try Again :)")
        except ValueError:
            print("The Answer Should Be A Word!")
        
            
            
    elif pc == words[2]:
        try:
            print ("I'm a country, famous for food and a video game character, Who Am I ?\n")
            answer = input("Enter Your Answer: ")
            if answer.lower() == 'italy':
                print("\nYou're Correct! I'm Italy! Mamma Mia! :D\n")
                stov = input("Do You Want To Start Over? (y/n):  ")
                if stov.lower() == 'n':
                    print("See You Later!")
                    break
                elif stov.lower() == 'y':
                    continue
                else:
                    print("Unavailable Option!")
                    break
            elif answer.lower() == 'q':
                print("See You Later!")
                break
            else:
                print("Wrong Answer Or Typo, Try Again :)")
        except ValueError:
            print("The Answer Should Be A Word!")
        
            
            
    elif pc == words[3]:
        try:
            print ("I'm a famous drawing done by DaVinci! Who Am I ?\n")
            answer = input("Enter Your Answer: ")
            if answer.lower() == 'monalisa':
                print("\nYou're Correct! I'm The Monalisa! :D\n")
                stov = input("Do You Want To Start Over? (y/n):  ")
                if stov.lower() == 'n':
                    print("See You Later!")
                    break
                elif stov.lower() == 'y':
                    continue
                else:
                    print("Unavailable Option!")
                    break
            elif answer.lower() == 'q':
                print("See You Later!")
                break
            else:
                print("Wrong Answer Or Typo, Try Again :)")
        except ValueError:
            print("The Answer Should Be A Word!")
        
            
            
    elif pc == words[4]:
        try:
            print ("I'm a famous japanese dish, probably the most famous! Who Am I ?\n")
            answer = input("Enter Your Answer: ")
            if answer.lower() == 'sushi':
                print("\nYou're Correct! I'm Sushi! :D\n")
                stov = input("Do You Want To Start Over? (y/n):  ")
                if stov.lower() == 'n':
                    print("See You Later!")
                    break
                elif stov.lower() == 'y':
                    continue
                else:
                    print("Unavailable Option!")
                    break
            elif answer.lower() == 'q':
                print("See You Later!")
                break
            else:
                print("Wrong Answer Or Typo, Try Again :)")
        except ValueError:
            print("The Answer Should Be A Word!")
        
            
            
    elif pc == words[5]:
        try:
            print ("I can take you wherever you want in a short time! Who Am I ?\n")
            answer = input("Enter Your Answer: ")
            if answer.lower() == 'car':
                print("\nYou're Correct! I'm A Car ! :D\n")
                stov = input("Do You Want To Start Over? (y/n):  ")
                if stov.lower() == 'n':
                    print("See You Later!")
                    break
                elif stov.lower() == 'y':
                    continue
                else:
                    print("Unavailable Option!")
                    break
            elif answer.lower() == 'q':
                print("See You Later!")
                break
            else:
                print("Wrong Answer, Try Again :)")
        except ValueError:
            print("The Answer Should Be A Word!")
        
            
            
    elif pc == words[6]:
        try:
            print ("You put your stuff on me all day and I'm never tired, Who I'm I ?\n")
            answer = input("Enter Your Answer: ")
            if answer.lower() == 'table':
                print("\nYou're Correct! I'm The Table! :D\n")
                stov = input("Do You Want To Start Over? (y/n):  ")
                if stov.lower() == 'n':
                    print("See You Later!")
                    break
                elif stov.lower() == 'y':
                    continue
                else:
                    print("Unavailable Option!")
                    break
            elif answer.lower() == 'q':
                print("See You Later!")
                break
            else:
                print("Wrong Answer, Try Again :)")
        except ValueError:
            print("The Answer Should Be A Word!")
        
            
            
    elif pc == words[7]:
        try:
            print ("I'm the most famous drink in the world! Who Am I ?\n")
            answer = input("Enter Your Answer: ")
            if answer.lower() == 'water':
                print("\nYou're Correct! I'm Water! :D\n")
                stov = input("Do You Want To Start Over? (y/n):  ")
                if stov.lower() == 'n':
                    print("See You Later!")
                    break
                elif stov.lower() == 'y':
                    continue
                else:
                    print("Unavailable Option!")
                    break
            elif answer.lower() == 'q':
                print("See You Later!")
                break
            else:
                print("Wrong Answer, Try Again :)")
        except ValueError:
            print("The Answer Should Be A Word!")