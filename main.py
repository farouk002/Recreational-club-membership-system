#Farouk Kotob - Group Project 406
"""
main():
    1.creates a new StoreUsers instance (storeUsers = StoreUsers)
    2.prompts the user with an interface to either Login or Register, both these functions take storeUsers as a parameter
      i.e: login(storeUsers)    or     register(storeUser)

register(storeUsers):
    1.prompts the user for; userType, username, password
    2.creates a new User instance i.e: newUserObject = userType(userType, username, password)
    3.newUser is added to storeUsers.userDictionary
        key = username
        value = newUserObject

login(storeUsers):
    1.prompts the user for; username, password
    2.checks if storeUsers.userDictionary matches the given username/password
      if so, main() will update and show a different interface

main():
    1.Note: this section will only appear with the user has successfully logged in
    2.Depending on the userType, printAvailableActions(userType) will print a different action list
    3.A constant while loop with prompt the user of an input
    4.Given an input, main will call useInput(input)
    5.useInput is a case/switch. i.e: given an input it will do something
"""

from StoreUsers import StoreUsers
from getpass import getpass
from Member import Member
from Coach import Coach
from Treasurer import Treasurer
from Practice import Practice
from DemoVersion import DemoVersion
import time
import os

def clearScreen(message="", sleepTime=0, lines=0):
    clearLines(lines)
    print(message)
    time.sleep(sleepTime)
    os.system('clear')


def clearLines(numberOfLines):
    for x in range(numberOfLines):
        print("\033[A                                                        \033[A")


def login(storeUsers):
    clearScreen()
    userDictionary = storeUsers.userDictionary
    print("Login Screen")
    username = input("Enter Username: ")
    password = getpass()

    if username in userDictionary and userDictionary[username].getPassword() == password:
        clearScreen("Logged in successfully!", 2, 2)
        return userDictionary[username]
    else:
        clearScreen("Invalid Username/Password", 2, 2)
        return False

def getUserType():
    type = ""
    userTypes = ["Member", "Coach", "Treasurer"]
    type = input("Enter User Type (Member, Coach, Treasurer): ")
    while not (type in userTypes):
        clearScreen("Please enter a valid user type!", 2.7, 1)
        print("Registration Screen")
        type = input("Enter User Type (Member, Coach, Treasurer): ")
    return type

def createNewUserObject(username,password,type,phoneNumber,storeUsers):
    if type == "Member":
        newObject = Member(username,password,"member", phoneNumber)
        storeUsers.allMembers[username] = newObject
    if type == "Coach":
        newObject = Coach(username, password,"coach", phoneNumber)
        storeUsers.allCoaches[username] = newObject
    if type == "Treasurer":
        newObject = Treasurer(username, password,"treasurer", phoneNumber)
    return newObject

def register(storeUsers):
    clearScreen()
    print("Registration Screen")
    type = getUserType()
    phoneNumber = input("Enter Phone Number: ")
    username = input("Enter Username: ")
    password1 = getpass()
    password2 = getpass("Confirm Password: ")

    while (password1 != password2):
        clearScreen()
        print("Registration Screen\nPasswords do not match!")
        password1 = getpass()
        password2 = getpass("Confirm Password: ")

    if username in storeUsers.userDictionary:
        clearScreen("Username already exists!", 2, 4)
        return False
    else:
        newUserObject = createNewUserObject(username,password1,type, phoneNumber, storeUsers)
        storeUsers.userDictionary[username] = newUserObject
        clearScreen("Registered successfully!",2,5)
        return True


def printAvailableActions(userType):
    memberActions = ["Pay for Practice", "Schedule Practice", "View Notifications", "Exit"]
    coachActions = ["Manage Members", "Post Announcement", "View Notifications", "Exit"]
    treasurerActions = ["Manage Practices", "Manage Members","View Profits", "View Unpaid Debts", "View Current Month Payables", "View Notifications", "Exit"]

    lst = []
    if userType == "member": lst = memberActions
    if userType == "coach": lst = coachActions
    if userType == "treasurer": lst = treasurerActions

    for action in lst:
        print("\t" + action)



def main():
    loggedIn = False
    storeUsers = StoreUsers()
    demo = DemoVersion()
    demo.demoVersion(storeUsers)
    currentUser = False                      #currentUser is the object of the user logged in

    while True:
        while not loggedIn:
            clearScreen()
            print("Recreation Club MemberShip\nAvailable Actions:\n\tLogin\n\tRegister\n")
            userInput = input("Enter Action: ")
            if userInput == "Register": register(storeUsers)
            if userInput == "Login":
                currentUser = login(storeUsers)
                if(currentUser != False): loggedIn = True

        while loggedIn:
            clearScreen()
            print("Main Menu\nWelcome, " + currentUser.getUserType() + " " + currentUser.getName() + "!" + "\n\nNotifications: 0\n\nAvailable Actions:\n")
            printAvailableActions(currentUser.getUserType())
            userInput = input("\nEnter Action: ")
            if (useInput(userInput, storeUsers, currentUser) == False): loggedIn = False


def useInput(userInput, storeUsers, currentUser):
    match userInput:
        case "Exit": return False    #Logs the user outs
        case "View Notifications": currentUser.viewNotifications()

        #Member Functions
        case "Pay for Practice": currentUser.payForPractice(storeUsers)
        case "Schedule Practice": currentUser.schedulePractice(storeUsers)

        #Coach Functions
        case "Manage Members": currentUser.manageMembers(storeUsers)
        case "Post Announcement": currentUser.postAnnouncement(storeUsers)

        #Treasurer Functions
        case "Manage Practices": currentUser.managePractices(storeUsers)
        case "View Profits": currentUser.viewProfits(storeUsers)
        case "View Unpaid Debts": currentUser.viewUnpaidDebts(storeUsers)
        case "View Current Month Payables": currentUser.viewMonthPayables(storeUsers)
        case "Manage Members": currentUser.manageMembers(storeUsers)


        case _:
            clearScreen("Invalid Input.\nInput is Case Sensative!",2.7,1)   #"_" Catches all other inputs


main()
