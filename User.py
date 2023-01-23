#Farouk Kotob - Group Project 406
import time
import os
class User:

    """
    Let me know if you spot an error, or if you would like me to add a new feature or function to this class
    -hameedah
    """

    def __init__(self, name, password, usertype, phoneNumber):
        # make sure that when we ask the user how to enter their user type, we give them three options
        # coach, treasurer, member and that they enter it in all lowercase
        # if it doesn't contain this criteria, then we tell them to enter it again until it does
        self.name = name
        self.password = password
        self.userType = usertype
        self.phoneNumber = phoneNumber
        self.notifications = []

    def getName(self):
        """ Returns the users name (string)"""
        return self.name

    def getPassword(self):
        """ Returns the uncensored version of the users password """
        return self.password

    def getCensoredPassword(self): #Not sure if this function is necessary but I put it here just in case
        """ Returns a string of eight (8) '*' characters """
        censoredPass = "********"
        return censoredPass

    def getUserType(self):
        """ Returns the users type (string)"""
        return self.userType

    def getPhoneNumber(self):
        """ Returns the users phone number (string)"""
        return self.phoneNumber

    def changeName(self, newName):
        """Returns the updated name

        Parameters:
          string newName: the name that will replace the old one
        """
        self.name = newName
        return self.name

    def changePassword(self, currentPass, newPass):
        """Returns 0 if password could not be changed because the current Password entered was incorrect
           Returns 1 if password was changed successfully

        Parameters:
          string currentPass: old password
          string newPass: new password that will replace old password
        """
        if currentPass != self.password:
            print("Password Incorrect: Cannot Change Password")
            return 0
        self.password = newPass
        print("Password Change Successful")
        return 1

    def changeUserType(self, newUserType):
        """Returns the updated userType

        Parameters:
          string newUserType: the usertype that will replace the old one
        """
        self.userType = newUserType
        return self.userType

    def viewNotifications(self):

        def printNotifications(self):
            index = 1
            for message in self.notifications:
                print("\t" + str(index) + ": " + message)
                index += 1

        userInput = ""
        while not (userInput == "Exit"):
            os.system('clear')
            print("Notifications:\n")
            printNotifications(self)
            print("\nAvalible Actions:\n\tDelete Message\n\tExit\n")
            userInput = input("Enter Action: ")
            if userInput[-1].isdigit():
                try:
                    del self.notifications[int(userInput[-1]) - 1]
                except IndexError:
                    print("\033[A                                                        \033[A")
                    print("Invalid Index")
                    time.sleep(2.5)
