#Farouk Kotob - Group Project 406
from User import User
import time
import os

class Coach(User):

    practiceSchedule = []

    def temp(self):
        return True

    def addMember(self, name, data, practiceID):
        """
         Returns nothing

         Adds member to membersList in practice class
         Increments member classesAttended

         Parameters:
             string name: name of member
             storeUser data: a store user object
             string practiceID: the identification number of a practice object
         """

        if(data.getPractice(practiceID)): iD = data.getPractice(practiceID)
        else:
            return "Invalid Id!"

        if name in data.userDictionary: member = data.userDictionary[name]
        else:
            return "No such member exists!"

        if member in iD.memberList: return "Member already in Practice!"

        if iD.getCoach() != self.getName():
            return ("Coach does not have permission to add member to this practice.")

        else:
            iD.addPracticeMember(member)
            member.notifications.append("You have been added to practice ID:" + practiceID +
                                        " by coach " + self.getName())
            member.classesAttended +=1
            return "Member added successfully!"


    def removeMember(self, name, data, practiceID):
        """
         Returns nothing

         removes member from membersList in practice class
         decrements member classesAttended

         Parameters:
             string name: name of member
             storeUser data: a store user object
             string practiceID: the identification number of a practice object
         """

        if (data.getPractice(practiceID)):
            iD = data.getPractice(practiceID)
        else:
            return "Invalid Id!"

        if name in data.userDictionary:
            member = data.userDictionary[name]
        else:
            return "No such member exists!"

        if not (member in iD.memberList): return "Member is not in practice!"

        if iD.getCoach() != self.getName():
            return ("Coach does not have permission to add member to this practice.")

        else:
            iD.removePracticeMember(member)
            member.notifications.append("You have been removed from practice ID:" + practiceID +
                                    " by coach " + self.getName())
            member.classesAttended -= 1
            return "Member removed successfully!"

    def addPractice(self, practiceObj):
        self.practiceSchedule.append(practiceObj)
        return

    def removePractice(self, practiceObj):
        self.practiceSchedule.remove(practiceObj)
        return


    def clearScreen(self, message="", sleepTime=0, lines=0):
        self.clearLines(lines)
        print(message)
        time.sleep(sleepTime)
        os.system('clear')

    def clearLines(self, numberOfLines):
        for x in range(numberOfLines):
            print("\033[A                                                        "
                  "                   "
                  "                                                             \033[A")

    def postAnnouncement(self,storeUsers):
        self.clearLines(1)
        string = input("Enter Announcement (\"Return\" to cancel): ")
        if string == "Return": return
        else:
            for user in storeUsers.userDictionary:
                member = storeUsers.userDictionary[user]
                member.notifications.append("From: Coach " + self.getName() + ", " + string)
            self.clearScreen("Announcement sent!",2.7,1)
            return

    def manageMembers(self,storeUsers):
        userInput = ""
        while not (userInput=="Return"):
            os.system('clear')
            print("Manage Members\n Your Practices:")
            for practice in storeUsers.listPractices:
                if practice.getCoach() == self.getName():
                    print(" ",practice.getString())
            print("\nAvailable Actions:\n\tRemove Member\n\tAdd Member\n\tReturn")
            userInput = input("\nEnter Action: ")

            if userInput == "Remove Member":
                id = input("Enter Practice ID: ")
                member = input("Enter Member Name: ")
                string = self.removeMember(member, storeUsers, id)
                self.clearScreen(string, 2.7, 1)

            if userInput == "Add Member":
                id = input("Enter Practice ID: ")
                member = input("Enter Member Name: ")
                string = self.addMember(member, storeUsers, id)
                self.clearScreen(string, 2.7, 1)