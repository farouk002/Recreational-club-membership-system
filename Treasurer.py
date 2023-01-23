#Farouk Kotob - Group Project 406
from User import User
from Practice import Practice
import operator
import time
import os

class Treasurer(User):

    def clearScreen(self, message="", sleepTime=0, lines=0):
        self.clearLines(lines)
        print(message)
        time.sleep(sleepTime)
        os.system('clear')

    def clearLines(self, numberOfLines):
        for x in range(numberOfLines):
            print("\033[A                                                        \033[A")

    def managePractices(self, storeUsers):

        def addPractice(storeUsers):
            self.clearLines(1)
            practiceID = input("Enter Practice ID: ")
            if not storeUsers.validPracticeID(practiceID):
                self.clearScreen("Practice ID already Exists!", 2.7, 1)
                return
            coach = input("Enter Coach: ")
            try:
                coach1 = storeUsers.allCoaches[coach]
                newPractice = Practice(practiceID, coach, 10, )
                storeUsers.listPractices.append(newPractice)
                coach1.notifications.append("You have been assigned to practice ID: " + practiceID)
                self.clearScreen("Successfully created new practice!", 2.7, 2)
                return
            except KeyError:
                self.clearScreen("No such coach exists!", 2.7, 2)
                return

        def switchCoach(storeUsers):
            self.clearLines(1)
            practiceID = input("Enter practice ID: ")
            if storeUsers.validPracticeID(practiceID):
                self.clearScreen("Practice ID does not exist!", 2.7, 1)
                return
            practice = storeUsers.getPractice(practiceID)
            coach = input("Who would you like to replace coach " + practice.getCoach() + " with: ")
            if coach == practice.getCoach():
                self.clearScreen("He is already the coach of this Practice.", 2.7, 1)
                return

            try:
                storeUsers.getCoach(practice.getCoach()).notifications.append("You have been removed from practice ID: " + practiceID)
                practice.changeCoach(storeUsers.getCoach(coach).getName())
                storeUsers.getCoach(coach).notifications.append("You have been assigned to practice ID: " + practiceID)
                self.clearScreen("Coach changed successfully!", 2.7, 1)
                return
            except KeyError:
                self.clearScreen("Coach does not exist!", 2.7, 1)
                return

        userInput = ""
        while not (userInput == "Return"):
            os.system('clear')
            string = ""
            print("Manage Practices\n")
            print("Practices:\nID\t Coach\t\t Members")

            for practice in storeUsers.listPractices:
                for member in practice.getMemberList():
                    string = string + member.getName() + ", "
                print(practice.getID(),"\t",practice.getCoach(),"     \t", string[:-2])
                string = ""

            print("\nAvailable Actions:\n   Switch Coach\n   Add Practice\n   Return\n")
            userInput = input("Enter Action: ")
            if userInput == "Add Practice":
                addPractice(storeUsers)
            if userInput == "Switch Coach":
                switchCoach(storeUsers)

    def viewProfits(self, storeUsers):

        def printMemberRevenue(storeUsers):
            Revenue = 0
            for user in storeUsers.allMembers:
                member = storeUsers.allMembers[user]
                if member.classesAttended > 0:
                    classesAttended = member.classesAttended
                    price = classesAttended * 10
                    Revenue += price
                    print("\t", member.getName(), "attending", classesAttended, "classes\t\t$", price)
            return Revenue

        def printCoachExpenses(storeUsers):
            Expenses = 0
            for practice in storeUsers.listPractices:
                Expenses += 10
                print("\t Coach", practice.getCoach(), "hosting", practice.getID(), "          \t$ 10")
            return Expenses

        def viewYearlyProfit(NetIncome):
            userInput = ""
            string = "Unpaid March Debt has been paid."
            months = {'January': "200", 'February': "180", 'March\t': "230", 'April\t': str(NetIncome), 'May\t': "Pending",
                      'June\t': "Pending", 'July\t': "Pending", 'August\t': "Pending", 'September': "Pending",
                      'October': "Pending", 'November': "Pending", 'December': "Pending"}
            if string in self.notifications:
                months['March\t'] = "0"

            while not (userInput == "Return"):
                os.system('clear')
                print("Monthly Income Spreadsheet:\n\tMonth\t\t\tNet Income")
                for month in months:
                    print("\t", month, "\t\t $", months[month])
                userInput = input("\nEnter \"Return\" to exit: ")

        userInput = ""
        while not (userInput == "Return"):
            os.system('clear')
            print("Viewing Profits\n\nRevenue:\n\tSource\t\t\t\t\tAmount")
            Revenue = printMemberRevenue(storeUsers)
            print("\nTotal Revenue: $", Revenue, "\n\nExpenses:\n\tSource\t\t\t\t\tAmount")
            print("\t Monthly Hall Expense\t\t\t$ 30")
            Expenses = printCoachExpenses(storeUsers) + 30
            NetIncome = Revenue - Expenses
            print("\nTotal Expenses: $", Expenses, "\nNet Income: $", NetIncome)
            print("\nAvailable Actions:\n\n\tView Current Yearly Profit\n\tReturn\n")
            userInput = input("Enter Action: ")
            if userInput == "View Current Yearly Profit": viewYearlyProfit(NetIncome)

    def viewUnpaidDebts(self,storeUsers):
        userInput = ""
        while not (userInput == "Return"):
            os.system('clear')
            string = "Unpaid March Debt has been paid."
            print("Viewing Unpaid Debts\n Month\t\tItem\t\tStatus\t\tAmount\t\tUrgency")
            if not string in self.notifications:
                print("  March\t\t Hall Rent\t Unpaid\t\t $30\t\t High")
            print("\nAvailable Actions:\n\n\tPay Debts\n\tReturn\n")
            userInput = input("Enter Action: ")
            if userInput == "Pay Debts": self.notifications.append(string)
        return True

    def viewMonthPayables(self, storeUsers):
        userInput = ""
        while not (userInput == "Return"):
            os.system('clear')
            print("Current Monthly Payables\nViewing Members with advanced payments:\n\tMember\t\tBalance")
            for user in storeUsers.allMembers:
                member = storeUsers.allMembers[user]
                if member.getAccountBalance() > 0:
                    print("\t" + member.getName() + "\t\t$" + str(member.getAccountBalance()))
            userInput = input("\nEnter \"Return\" to exit: ")



    def manageMembers(self, storeUsers):
        userInput = ""

        def printGeneralInformation(storeUsers):
            index = 1
            print("Member General Information\n")
            print("  Name\t\tPhone Number\t\tAccount Balance\t\tClasses Attended\tClasses Paid\tUnpaid Classes")
            for user in storeUsers.allMembers:
                member = storeUsers.allMembers[user]
                print(index,member.getName(),"  \t",member.getPhoneNumber(),"\t\t$",member.getAccountBalance(),
                      "\t\t\t",member.getClassesAttended(),"Classes\t\t",member.getClassesPaidFor(), "Classes",
                        "\t",member.getClassesAttended()-member.getClassesPaidFor())
                index +=1

        def notifyUnpaid(storeUsers):
            for user in storeUsers.allMembers:
                member = storeUsers.allMembers[user]
                if member.getClassesAttended()-member.getClassesPaidFor() > 0:
                    string = "Warning: You have an outstanding balance."
                    member.notifications.append(string)
            self.clearScreen("Messages Sent Successfully!", 2, 1)

        def sortByAttendance(storeUsers):
            tempLst = []
            newDict = {}
            for user in storeUsers.allMembers:
                member = storeUsers.allMembers[user]
                tempLst.append(member)
            tempLst = sorted(tempLst, key=lambda x: x.classesAttended,reverse=True)
            for member in tempLst:
                newDict[member.getName()] = member
            storeUsers.allMembers = newDict
            return tempLst[0]

        def sortByUnpaidUsers(storeUsers):
            tempLst = []
            newDict = {}
            for user in storeUsers.allMembers:
                member = storeUsers.allMembers[user]
                tempLst.append(member)
            tempLst = sorted(tempLst, key=lambda x: x.classesAttended-x.classesPaidFor, reverse=True)
            for member in tempLst:
                newDict[member.getName()] = member
            storeUsers.allMembers = newDict

        def loyaltyDiscount(storeUsers):
            user = sortByAttendance(storeUsers)
            user.accountBalance += 10
            string = "Congrats, due to having the highest attendance you have been given a $10 credit!"
            user.notifications.append(string)
            self.clearScreen((user.getName() + " was given a loyalty discount."), 2, 1)


        while not (userInput == "Return"):
            os.system('clear')
            printGeneralInformation(storeUsers)
            print("\nAvailable Actions:\n\tSort By Attendance\n\t"
                  "Sort By Unpaid Users\n\tNotify Unpaid Users\n\t"
                  "Loyalty Discount\n\t"
                  " -(Member with most attended classes gets $10 credit)\n\tReturn")
            userInput = input("\nEnter Action: ")
            if userInput == "Notify Unpaid Users": notifyUnpaid(storeUsers)
            if userInput == "Sort By Attendance": sortByAttendance(storeUsers)
            if userInput == "Sort By Unpaid Users": sortByUnpaidUsers(storeUsers)
            if userInput == "Loyalty Discount": loyaltyDiscount(storeUsers)



        return True