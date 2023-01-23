#Farouk Kotob - Group Project 406
from User import User
from Coach import Coach
from Treasurer import Treasurer
from Member import Member
from Practice import Practice


class StoreUsers:

    userDictionary = {}
    allMembers = {}
    allCoaches = {}
    listPractices = []


    def getUser(self, name):
        u = self.userDictionary[name]
        return u

    """If you want, you can transfer user objects from userDictionary, that have usertype "member" to allMembers dictionary,
       and usertype "coach" to allCoaches dictionary
    """
    def addUsertoMemCoach(self):

        for i in self.userDictionary.keys():
            u = self.userDictionary[i]

            if u.userType == "member":
                self.allMembers[i] = u
            if u.userType == "coach":
                self.allCoaches[i] = u

    def getMembers(self):
        listmembers = []
        for i in self.allMembers.keys():
            listmembers.append(i)

        return listmembers

    def getPractice(self, ID):
        for i in self.listPractices:
            if i.getID() == ID:
                return i

    def getCoach(self, name):
        c = self.allCoaches[name]
        return c

    def validPracticeID(self, ID):
        for i in self.listPractices:
            if i.getID() == ID:
                return False
        return True

    def getName(self, name):
        u = self.userDictionary[name]
        return u.getName()

    def getUserType(self, name):
        u = self.userDictionary[name]
        return u.getName()

    def getNumber(self, name):
        u = self.userDictionary[name]
        return u.getPhoneNumber()

    def getPassword(self, name):
        u = self.userDictionary[name]
        return u.getPassword()

    def addUser(self, user):
        name = user.getName()

        for i in self.userDictionary.keys():
            u = self.userDictionary[i]
            if i == name:
                print("User already exists")
                return

            elif u.userType != "member" or u.userType != "coach" or u.userType != "treasurer":
                print("Cannot add user due to invalid usertype")
                return
            elif user.phoneNumber == u.getPhoneNumber:
                print("Cannot add this user.  An existing user already has this phone number")
                return

        if user.userType == "coach":
            self.addCoach(user)
        elif user.userType == "member":
            self.addMember(user)

        self.userDictionary[name] = user

    def addMember(self, member):
        name = member.getName()

        for i in self.allMembers.keys():
            m = self.allMembers[i]
            if i == name:
                print("This member already exists")
                return
            elif member.userType != "member":
                print("Usertype is not member")
                return

            elif member.phoneNumber == m.getPhoneNumber():
                print("Cannot add this member.  An existing member already has this phone number")
                return

        self.allMembers[name] = member

    'Add practice object to listPractices list'
    def addPractice(self, ID, coach, price):
        if self.validPracticeID(ID):
            for i in self.allCoaches.keys():
                if i != coach:
                    print("This coach does not exist")
                    return

            self.listPractices.append(Practice(ID, coach, price))

    'Add coach object to allCoaches dictionary'
    def addCoach(self, coach):
        name = coach.getName()
        for i in self.allCoaches.keys():
            c = self.allMembers[i]
            if i == name:
                print("This coach already exists")
                return

            elif coach.userType != "coach":
                print("Usertype is not coach")
                return

            elif coach.phoneNumber == c.getPhoneNumber():
                print("Cannot add this member.  An existing member already has this phone number")
                return

        self.allCoaches[name] = coach


    def removeUser(self, name):

        for i in self.userDictionary.keys():
            if i == name:
                del self.userDictionary[name]
                return

        print("Cannot remove a non-existent user")

    def removeMember(self, name):

        for i in self.allMembers.keys():
            if i == name:
                del self.allMembers[name]
                return

        print("Cannot remove a non-existent member")

    'Change the name of a particular user from userDictionary'
    def changeName(self, oldname, newname):

        for i in self.userDictionary.keys():
            if i == oldname:
                self.userDictionary[newname] = self.userDictionary[oldname]

                del self.userDictionary[oldname]
                return

        print(oldname, "not found")

    'Change the password of a particular user from userDictionary'
    def changePassword(self, name, currentP, newP):

        for i in self.userDictionary.keys():
            u = self.userDictionary[i]

            if i == name and u.getPassword() == currentP:
                if u.getUserType() == "member":
                    modifieduser = Member(u.getName(), newP, "member", u.getPhoneNumber())
                    del self.userDictionary[name]
                    self.userDictionary[name] = modifieduser
                    return

                elif u.getUserType() == "coach":
                    modifieduser = Coach(u.getName(), newP, "coach", u.getPhoneNumber())
                    del self.userDictionary[name]
                    self.userDictionary[name] = modifieduser
                    return

                elif u.getUserType() == "treasurer":
                    modifieduser = Treasurer(u.getName(), newP, "treasurer", u.getPhoneNumber())
                    del self.userDictionary[name]
                    self.userDictionary[name] = modifieduser
                    return
            else:
                print("Please enter the correct current password for user ", u.getName())
                return

        print(name, "not found")

    def printPractices(self):
        print("Practices: ")
        for i in range(len(self.listPractices)):
            print(self.listPractices[i].getString())


    def printCoaches(self):
        print("Coaches: ")
        for i in self.allCoaches.keys():
            print(i)