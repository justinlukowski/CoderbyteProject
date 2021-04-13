class User:
    def __init__(self, cardNum, PIN, checkBal, savBal):
        self.cardNumber = cardNum
        self.pin = PIN
        self.checkings = Account(checkBal)
        self.savings = Account(savBal)
        self.locked = 0

class Account:
    def __init__(self, bal):
        self.balance = bal

#Tests the card inserted
def cardTest(userList):
    cardNum = int(input("Insert card (enter a number to simulate card number, -1 to shut down program): "))
    userValid = 0
    currentUser = None
    if cardNum == -1:
        return 1, None
    for i in userList:
        if cardNum == i.cardNumber:
            currentUser = i
            userValid = 1
    if userValid == 0:
        print("Invalid card")
    return userValid, currentUser

#tests the PIN entered
def pinTest(currentUser):
    pinNum = -1
    wrong = 0
    while pinNum != currentUser.pin:
        if wrong != 0:
            print("Incorrect PIN")
        if currentUser.locked != 1:
            if wrong >= 3:
                print("Your account has been locked due to too many failed logins")
                currentUser.locked = 1
                return 0
            pinNum = int(input("Enter PIN: "))
            wrong += 1
    return 1

#selects type of account
def selectAccount(currentUser):
    accountValid = 0
    while(accountValid == 0):
        bankAccount = int(input("Press 1 for Checking, 2 for Savings, 3 to Logout: "))
        if bankAccount == 1:
            accountValid = 1
            account = currentUser.checkings
        elif bankAccount == 2:
            accountValid = 1
            account = currentUser.savings
        elif bankAccount == 3:
            accountValid = 1
            account = None
        else:
            print("Invalid account")
    return accountValid, account

#selects whether to deposit or withdraw
def choice(account):
    choiceValid = 0
    logout = 0
    back = 0
    while choiceValid == 0:
        choice = int(input("Select 1 for Deposit, 2 for Withdraw, 3 to go back, 4 to Logout: "))
        if choice == 1:
            choiceValid = 1
            amount = int(input("Deposit money (enter amount to deposit): "))
            account.balance += amount
            print("New balance: ", account.balance)
        elif choice == 2:
            choiceValid = 1
            insufficient = 0
            while insufficient == 0:
                amount = int(input("Enter amount to withdraw: "))
                if amount > account.balance:
                    print("Insufficient funds")
                else:
                    insufficient = 1
                    account.balance -= amount
                    print("New balance: ", account.balance)
        elif choice == 3:
            choiceValid = 1
            back = 1
        elif choice == 4:
            choiceValid = 1
            logout = 1
        else:
            print("Invalid choice")
        return choiceValid, back, logout

if __name__ == "__main__":
    userList = []
    userList.append(User(1, 1234, 10, 100))         #test user
    userList.append(User(2, 9210, 32, 414))         #test user
    userList.append(User(8932, 3413, 2134, 3124))   #test user

    finish = 0
    while finish == 0:
        #Uses user's card (number) to access their account
        userValid = 0
        currentUser = None
        while(userValid == 0):
            userValid, currentUser = cardTest(userList)
        if currentUser == None:
            finish = 1
            break
        if currentUser.locked == 1:
            print("Your account is locked, visit the bank for more details")

        #Uses user's PIN to login
        if currentUser.locked != 1:
            pinValid = 0
            while(pinValid == 0 | currentUser.locked == 0):
                pinValid = pinTest(currentUser)

        #Allows user to select bank account
        logout = 0
        if currentUser.locked == 0:
            while logout == 0:
                accountValid = 0
                while(accountValid == 0):
                    accountValid, account = selectAccount(currentUser)

                if account == None:
                    logout = 1
                else:
                    #Displays balance
                    print("Balance:", account.balance)
                    # Deposit/withdraw
                    exit = 0
                    back = 0
                    while logout != 1:
                        choiceValid = 0
                        while choiceValid == 0:
                            choiceValid, back, logout = choice(account)
                        if back == 1:
                            back = 0
                            accountValid = 0
                            while (accountValid == 0):
                                accountValid, account = selectAccount(currentUser)
                            print("Balance:", account.balance)
        else:
            pass
        if logout == 1:
            print("Logged out")
    print("Program shut down")





