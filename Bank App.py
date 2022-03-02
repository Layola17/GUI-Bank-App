files = open("Transaction Log.txt", "w")

yes = "1"
no = "2"
bal = 10000

print("Would you like to make a transaction?\n 1. Yes\n 2. No")

transaction = int(input())
if transaction == 1:
    print("Would you like to make a Deposit, Withdrawal, or Check balance \n 1. Deposit\n 2. Withdrawal \n 3. Check Balance")

    option = float(input())

    if option == 1:
        print("Enter the amount to Deposit: ")
        deposit = float(input("R"))
        new_bal = bal + deposit
            
        files.write("Money In:\t" + str(deposit)+"\n");            
        files.write("Balance:\t" + str(new_bal)+"\n")
            
        print("Your Deposit succesful and your Current Balance is: ", new_bal)

    elif option == 2:
        print("Enter the amount to withdraw: ")
        withdraw = float(input("R"))
        new_bal = bal - withdraw
            
        files.write("Money Out:\t" + str(withdraw)+"\n")
        files.write("Balance:\t" + str(new_bal))
            
        print("\n""R",-withdraw, "has been deducted from your account!\nAnd your Current Balance is: ", round(new_bal, 2))

    elif option == 3:
        print("Your Current Balance: \n", bal)

    elif option > 3:
        print("Sorry, you've entered an invalid number!")
        files.write("You provided an invalid input")    
    else:            
        print("\n You provided an invalid input")
        files.write("You provided an invalid input")
            
else:
    print("Thank you for your time, please take your card!")
    files.write("The transactions were cancelled")
 
files.close()