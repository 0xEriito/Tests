import random
import string

while True:
    passkeys = string.ascii_letters+string.digits+string.punctuation
    
    print("(type 999 to quit)")
    passlenth = int(input("Enter The Number Of Characters You Want: "))

    if passlenth < 6 :
        print("It Should Be 6 Characters At Least. Try Again")

    elif passlenth >= 6 and not 999 :
        password = ''.join(random.choices(passkeys, k=passlenth))
        print("The Password Is :  ", password)
    elif passlenth == 999 :
        print("See You Later!")
        break
