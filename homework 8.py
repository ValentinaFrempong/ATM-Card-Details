ServerName = "Valentina Frempong"
severCardNumber = "12345678910"
serverPin="1654"
balance = 50000
balance = int(balance)


print('''
WELCOME TO THE BANK OF ENGLAND
-----------------------------------------------
THANK YOU FOR CHOSING THIS ATM MACHINE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
NOW PLEASE ENTER YOUR DETAILS!
''')

print("\n")

card = input("Please enter your card numbers right hereeeee:")

if card == severCardNumber:
    print("Welcome Back! " + ServerName)
    pin = input("Please enter your pin here:")

    if pin == serverPin:
        print("Welcome Back, Login Successful!")


    else:
         print("Wrong Pin, get out the way")

else:
    print("Sorry we do not recognize youuuuu!!!!")
    print("See you later......never liked you anyways!!!!!!")



if pin == serverPin:
    print("Login Successful!")
    amount = input("Please enter the amount you want to withdraw:")
    amount = int(amount)

    if amount > balance:
        print("Sorry you don't have enough funds, now go up and away!")


    else:
        balance = balance - amount
        print("PROCESSING....")
        print("Transaction Complete")
        print("Remaining Balance: " + str(balance))

        rc = input("Do you want to print your bank details? (yes/no):")

        if rc == "yes":
            print("Name: " + ServerName)
            print("--------------------------------------------------")
            print("Card Number: " + severCardNumber)
            print("---------------------------------------------------")
            print("Remaing Balance: " + str(balance))
            print("----------------------------------------------------")
            print("Amount Withdrawn: " +str(amount))
            print("------------------------------------------------------")
            print("Have a lovely day")


        else:
            print("F**k off")


    

else:
    print("Sorry we don't recognize you!")
    print("See you later!")
