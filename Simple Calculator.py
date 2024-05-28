def sum(a,b):
    print(f"The Sum Of {a} And {b} Is: ", a+b)

def sub(a,b):
    print(f"The Result Of Substracting {b} From {a} Is: ", a-b)

def mult(a,b):
    print(f"The Result Of MUltiplying {a} By {b} Is: ", a*b)

def div(a,b):
    print(f"The Result Of Deviding {a} Over {b} Is: ", a/b)

while True:
    print(f"\n*****PYTHON SIMPLE CALCULATOR*****\n       (type Q/q to quit)\n")
    choice = input("Enter An Operator (+|-|*|/) Or Type (Q/q) To Quit:  ")
    qu = ["Q", "q"]
    operators = ["+", "-", "*", "/"]

    if choice in qu:
        print("See You Later!")
        break
    else:
        if choice not in operators:
            print("Wrong Input, No Operator Or Quit Detected!")
            break
        try:
            a = float(input("Type The First Number:  "))
            b = float(input("Type The Second Number:  "))
        except ValueError:
            print("The Input Should Be A Number!")
            break

        if choice == operators[0]:
            sum(a,b)
            restart = input("Do You Want To Calculate Something Else? (Y/N):  ")
            no = ["n","N"]
            if restart in no:
                print("See You Later!")
                break
            else:
                continue
        
        elif choice == operators[1]:
            sub(a,b)
            restart = input("Do You Want To Calculate Something Else? (Y/N):  ")
            no = ["n","N"]
            if restart in no:
                print("See You Later!")
                break
            else:
                continue
            
        elif choice == operators[2]:
            mult(a,b)
            restart = input("Do You Want To Calculate Something Else? (Y/N):  ")
            no = ["n","N"]
            if restart in no:
                print("See You Later!")
                break
            else:
                continue
            
        elif choice == operators[3]:
            div(a,b)
            restart = input("Do You Want To Calculate Something Else? (Y/N):  ")
            no = ["n","N"]
            if restart in no:
                print("See You Later!")
                break
            else:
                continue