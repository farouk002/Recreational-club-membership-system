#Farouk Kotob - Group Project 406
from Coach import Coach
from Member import Member


class Practice:

    def __init__(self, ID, coach, price):
        #id must be a string
        self.ID = ID
        self.coach = coach
        self.price = price
        self.memberList = []

    def getID(self):
        return self.ID

    def getMemberList(self):
        return self.memberList

    def getCoach(self):
        return self.coach

    def getPrice(self):
        return self.price

    def changePrice(self, newPrice):
        self.price = newPrice
        return self.price

    def changeCoach(self, newCoach):
        self.coach = newCoach

    def changeID(self, newID):
        self.ID = newID

    def clearMemberList(self):
        self.memberList = []

    def addPracticeMember(self, member):
        if member in self.memberList:
            return False
        else:
            self.memberList.append(member)
            return True

    def removePracticeMember(self, member):
        if member in self.memberList:
            self.memberList.remove(member)
            return True
        else:
            return False

    def getString(self):
        '''
        returns a string of the general information in practice

        Example:    "ID:" self.ID,    hosted by: Coach self.coach.    self.getPrice()     Attending Members: [member.getName() for all members]
        Returns:    ID: Practice 1, hosted by: Coach Curtis. Price: $10 Attending Members: Jax, Yuno, Hoza
        '''

        string = "ID: " + self.ID + ", hosted by: Coach " + self.coach + ". Price: $" + str(
            self.getPrice()) + ". Attending Members: "
        memberName = []
        for member in self.memberList:
            memberName.append(member.getName())

        for member in memberName:
            string = string + member + ", "

        return string[:-2]
