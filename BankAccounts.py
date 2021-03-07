# Kit Bower-Morris
# Student Number: 201532917
# COMP517 - CA4 - Bank Accounts

#Import random and datetime modules. These are used in the Issue Card Number function.
import random
import datetime

#Basic Account Class - for Accounts with no overdraft. 
class BasicAccount:
    #cardNum set records all Card Numbers issued. Checking against this stops the issueNewCard function from issuing an already used card number. 
    #serial dictionary records the account name (self.name) as the key and the acNum associated with that account as the value. 
    #acNum int is a counter, the __init__ function adds 1 to it. This serialises the account numbers associated with each account. 
    cardNum = {0}
    serial = {}
    acNum = 0

    #__init__ function. Tests if values are correct format. Rounding any numbers to 2 decimal places. 
    def __init__(self, acName, openingBalance):
        self.name = str(acName)
        try:
            float(openingBalance)
        except ValueError:
            print("Invalid Opening Balance entered. \nOpening Balance for {self.name} set to £0.00".format(self=self))
            openingBalance = 0.00
        else:
            openingBalance = float(openingBalance)
            openingBalance = round(openingBalance, 2)
        finally:
            if(openingBalance < 0):
                print("Invalid Opening Balance entered. \nOpening Balance for {self.name} set to £0.00".format(self=self))
                openingBalance = 0.0                
            self.balance = openingBalance 
            print("Thank you for setting up an Account {self.name}. Your Opening Balance is £{self.balance}".format(self=self))
            BasicAccount.acNum +=1
            self.acNum = BasicAccount.acNum
            BasicAccount.serial[BasicAccount.acNum] = self.name
    
    #Creates new print function. Printing the Account Name and Current Balance. 
    def __str__(self):
        return "Account Name: {self.name} \nAvailable Balance: {self.balance}".format(self=self)
        
    #Tests that amount entered is a number. If not deposits £0.00 into account. Also makes sure amount is positive.
    #If all is right format and within the right range, this adds amount to the current value of the account.     
    def deposit(self, amount):
        try:
            float(amount)
        except ValueError:
            print("Invalid deposit value entered. \nDeposit for {self.name} set to £0.00".format(self=self))
            amount = 0.00
        else:
            amount = float(amount)
            amount = round(amount, 2)
        finally:        
            if(amount < 0):
                print("Can not deposit negative amount. \nDeposit for {self.name} set to £0.00".format(self=self))
                amount = 0.00 
            self.balance += amount
            print("£",amount, " deposited into {self.name}'s account. \nNew balance - £{self.balance}".format(self=self))
            return self.balance 
    
    #Tests that amount entered is a number. If not withdraws £0.00 from account. Also makes sure amount is positive.
    #If all is right format and within the right range, this minuses amount to the current value of the account.
    def withdraw(self, amount):
        try:
            float(amount)
        except ValueError:
            print("Invalid withdrawal value entered. \nWithdrawal for {self.name} set to £0.00".format(self=self))
            amount = 0.00
        else:
            amount = float(amount)
            amount = round(amount, 2)
        finally:  
            if(amount < 0):
                print("Can not withdraw negative amount. \nWithdrawal for {self.name} set to £0.00".format(self=self)) 
                amount = 0.0     
            if (amount <= self.balance):
                self.balance -= amount
                self.balance = round(self.balance, 2)
                print(self.name," has withdrew £", amount, "\nNew balance is £{self.balance}".format(self=self))
            else:
                print(self.name, " can not withdraw £", amount)

    #Prints Available Balance and returns this as a float.
    def getAvailableBalance(self):
        print("{self.name}'s Available Balance - £{self.balance}".format(self=self))
        return float(self.balance)

    #Prints Available Balance and returns this as a float.
    def getBalance(self):
        print("{self.name}'s Balance - £{self.balance}".format(self=self))
        return float(self.balance)

    #Prints Balance.    
    def printBalance(self):
       print("{self.name} - Account Balance: £{self.balance}".format(self=self))

    #Prints Name, and returns as string. 
    def getName(self):
        print("Account Name is {self.name}.".format(self=self))
        return str(self.name)

    #Returns Account number.
    def getAcNum(self):
        return str(self.acNum)
        
    #Issues new card number, using the random function. Records card number in set cardnum, and checks that the new card number hasn't already been used.
    #Expiry date is created by taking the current year, adding 3 to it and then removing the first two digits. This is then added to a list along with the current month.
    def issueNewCard(self):
        newCardNum = ""
        cardExp = []
        currentYear = []
        newYear = ""
        today = datetime.datetime.now()
        
        for i in range(0,16):
            x = random.randint(0,9)
            x = str(x)
            newCardNum += x
        if(newCardNum in BasicAccount.cardNum):
            print("Card Number already in use, issuing new Card Number...")
            BasicAccount.issueNewCard(self)
        else:
            (BasicAccount.cardNum).add(newCardNum)
            print("{self.name}'s New Card Number: ".format(self=self), newCardNum)

            newMonth = today.month
            cardExp.append(newMonth)
            now = today.year
            now += 3
            now = str(now)
            for i in (now):
                currentYear.append(i)
            del currentYear[0:2]
            for i in currentYear:
                newYear += i
            newYear = int(newYear)
            cardExp.append(newYear)
            cardExp = tuple(cardExp)
            print("New Expiry Date:", cardExp)

    #Closes Account. Removed name (value) from the Account Number (key) in the serial dict. 
    #Withdraws all money from account and returns True.
    def closeAccount(self):
        BasicAccount.withdraw(self, self.balance)
        BasicAccount.serial[self.acNum] = ""
        print("Closing {self.name}'s Account. Good Bye!".format(self=self))
        return True
        
class PremiumAccount(BasicAccount):
    #Overdraft dictionary, records which premium accounts have an overdraft and which don't.
    overdraft = {}
      
    #__init__ function. Tests if values are correct format. Rounding any numbers to 2 decimal places.
    #If Initial Overdraft is <= 0, overdraft is disabled. Otherwise, overdraft is enabled.
    def __init__(self, acName, openingBalance, initialOverdraft):       
        super().__init__(acName, openingBalance)
        try:
            float(initialOverdraft)
        except ValueError:
            print("Invalid Initial Overdraft entered. \nInitial Overdraft for {self.name} set to £0.00".format(self=self))
            initialOverdraft = 0.00
        else:
            initialOverdraft = float(initialOverdraft)
            initialOverdraft = round(initialOverdraft, 2)
        finally:        
            if(initialOverdraft < 0):
                print("Can not set Initial Overdradt Limit to a negative amount. \nOverdraft for {self.name} is disabled for now".format(self=self)) 
                initialOverdraft = 0.0            
            self.overdraftLimit = initialOverdraft
            if (self.overdraftLimit != 0.0):
                PremiumAccount.overdraft[BasicAccount.getAcNum(self)] = True
                print("Thank you for setting up a Premium account {self.name}. \nYour overdraft limit is £{self.overdraftLimit}".format(self=self))
            else:
                PremiumAccount.overdraft[BasicAccount.getAcNum(self)] = False
                print("Thank you for setting up a Premium account {self.name}.".format(self=self))   

    #Prints values. Including overdraft information if overdraft is active. 
    def __str__(self):
        if(PremiumAccount.overdraft[BasicAccount.getAcNum(self)]):
            return "Account Name: {self.name} \nAvailable Balance: £{self.balance} \nOverdraft Limit: £{self.overdraftLimit}".format(self=self)
        else:
             return "Account Name: {self.name} \nAvailable Balance: £{self.balance} \nOverdraft Disabled.".format(self=self)

    #Tests that amount entered is a number. If not withdraws £0.00 from account. Also makes sure amount is positive.
    #If all is right format and within the right range, this minuses amount to the current value of the account.
    #Takes into account overdraft, testing to see if there is enough balance. 
    def withdraw(self, amount):
        try:
            float(amount)
        except ValueError:
            print("Invalid withdrawal value entered. \nWithdrawal for {self.name} set to £0.00".format(self=self))
            amount = 0.00
        else:
            amount = float(amount)
            amount = round(amount, 2)
        finally: 
            if(amount < 0):
                print("Can not withdraw negative amount. \nWithdrawal for {self.name} set to £0.00".format(self=self))
                amount = 0.0
            if(PremiumAccount.overdraft[BasicAccount.getAcNum(self)] == True):
                if (-(self.balance - amount) > self.overdraftLimit):
                    print(self.name, "can not withdraw £", amount)
                else:
                    self.balance = self.balance - amount
                    self.balance = round(self.balance, 2)
                    print(self.name,"has withdrew £", amount, "\nNew balance is £{self.balance}".format(self=self))

    #Sets new overdraft limit. 
    #Ensures right data type is used. And ensures new overdraft limit is not less than how much they are in debt.
    def setOverdraftLimit(self, newLimit):
        try:
            float(newLimit)
        except ValueError:
            print("Invalid Overdraft Limit entered. \nOverdraft Limit change for {self.name} is denied at this time".format(self=self))
        else:
            newLimit = float(newLimit)
            newLimit = round(newLimit, 2)
            if(newLimit < 0):
                print("Can not set new Overdraft Limit to a negative amount. \nOverdraft Limit change for {self.name} is denied at this time.".format(self=self))  
            if newLimit < -self.balance:
                print("Can not set new overdraft limit to £",newLimit)
            else:
                if newLimit == 0:
                    PremiumAccount.overdraft[BasicAccount.getAcNum(self)] = False
                    print("Overdraft has been disabled.")    
                else:
                    PremiumAccount.overdraft[BasicAccount.getAcNum(self)] = True
                    self.overdraftLimit = newLimit

    #Prints available balance. Checking for and account for overdrafts. 
    def getAvailableBalance(self):
        if(PremiumAccount.overdraft[BasicAccount.getAcNum(self)] == True):
            availableBalance = self.balance + self.overdraftLimit
            print("{self.name}'s Available Balance - £".format(self=self), availableBalance)
            return availableBalance
        else:
            return BasicAccount.getAvailableBalance(self)

    #Prints available balance. Checking for and account for overdrafts. 
    def printBalance(self):
        print("{self.name} - Account Balance: £{self.balance}".format(self=self))
        if(PremiumAccount.overdraft[BasicAccount.getAcNum(self)] == True):
            print(self.name, " - Overdraft Limit: £", self.overdraftLimit)
            if (self.balance < 0):
                print(self.name, " - Remaining Overdraft: £", (self.overdraftLimit+self.balance))
            else:
                print(self.name, " - Remaining Overdraft: £", self.overdraftLimit)

    #Closes Account. Removed name (value) from the Account Number (key) in the serial dict. 
    #Deletes entry in overdraft dictionary.
    #Withdraws all money from account and returns True.    
    def closeAccount(self):
        if(PremiumAccount.overdraft[BasicAccount.getAcNum(self)] == False):
            return super().closeAccount()
        else:
            if(self.balance < 0):
                print("Can not close account due to customer being overdrawn by £", -(self.balance))
                return False
            else:
                self.setOverdraftLimit(0)
                del PremiumAccount.overdraft[BasicAccount.getAcNum(self)]
                return super().closeAccount()

