#Farouk Kotob - Group Project 406
from User import User
import time
import os

class Member(User):

    """
    Let me know if you spot an error, or if you would like me to add a new feature or function to this class
    -hameedah
    """
    accountBalance = 0
    classesAttended = 0
    classesPaidFor = 0
    listPractices = []

    def clearScreen(self, message="", sleepTime=0, lines=0):
        self.clearLines(lines)
        print(message)
        time.sleep(sleepTime)
        os.system('clear')

    def clearLines(self, numberOfLines):
        for x in range(numberOfLines):
            print("\033[A                                                       \033[A")

    def getAccountBalance(self):
        """
        For userType = member
        Returns the users account balance (int)
        """
        return self.accountBalance

    def getClassesAttended(self):
        """
        For userType = member
        Returns the number of classes the user has attended (int)
        """
        return self.classesAttended

    def getClassesPaidFor(self):
        """
        For userType = member
        Returns the number of classes the user has paid for (int)
        """
        return self.classesPaidFor

    def attendClass(self):
        """
         For userType = member
         Increments the number of classes the member has attended
         Returns the updated number of classes attended (int)
         """
        self.classesAttended += 1
        return self.classesAttended

    def payReminder(self):
        """
         For userType = member
         Prints a reminder to pay outstanding fees if outstanding fees exist
         Returns 1 always
         """
        if self.classesAttended > self.classesPaidFor:
            print("You need to pay for ", (self.classesAttended - self.classesPaidFor), " outstanding classes")
        return 1


    def depositMoney(self):
        """
         For userType = member
         Returns updated accountBalance

         Increments accountBalance accordingly

         Parameters:
             int amount: amount of money to be added to member account
         """
        try:
            amount = input("Enter the amount you would like to deposit: ")
            self.accountBalance += int(amount)
            return self.accountBalance
        except ValueError:
            self.clearScreen("Invalid Amount", 2.7, 1)


    def schedulePractice(self, info):

        """
        schedules the practice specified by the user

        Parameters:
             info: a StoreUser object

        Returns void

        Side Effects:
          - increments the classesAttended variable
          - adds the member to the list of members signed up for the practice
        """

        exitLoop = 0
        while exitLoop == 0:
            os.system('clear')
            info.printPractices()
            practice = input("\n\"Exit\" to exit.\nEnter ID of Practice You Would Like to Schedule: ")
            if practice == "Exit" or practice == "exit":
                exitLoop += 1
                return

            if info.validPracticeID(practice):
                self.clearScreen("Invalid ID", 3, 2)
                return

            if practice in self.listPractices:
                string = ("Error: You have already paid for this practice")
                self.clearScreen(string, 3, 2)
                return


            self.classesAttended += 1
            self.listPractices.append(practice)
            practiceObj = info.getPractice(practice)
            practiceObj.addPracticeMember(self)
            string = ("Practice " + practice + " booked successfully")
            self.clearScreen(string, 3, 2)


    def payForPractice(self, storeUsers):
        def payBalance(self, bal):
            if bal == 0:
                self.clearScreen("No balance to pay!", 2.7, 1)
                return
            if bal <= self.accountBalance:
                self.accountBalance -= bal
                self.classesPaidFor += (bal//10)
                return

        userInput = ""
        while not (userInput == "Return"):
            unpaid = str(self.classesAttended - self.classesPaidFor)
            outStandBal = str((self.classesAttended - self.classesPaidFor) * 10)
            os.system('clear')
            print("Viewing Financial Status\n")
            print("  Unpaid Classes\t ",unpaid,"\n  Paid Classes\t\t ",str(self.classesPaidFor),
                  "\n\n  OutStanding Balance\t$",outStandBal,"\n  Account Balance\t$",str(self.accountBalance))

            print("\nAvalible Actions:\n\tDeposit Money\n\tPay Balance\n\tReturn")
            userInput = input("\nEnter Action: ")

            if userInput == "Deposit Money": self.depositMoney()
            if userInput == "Pay Balance": payBalance(self, int(outStandBal))






