#Farouk Kotob - Group Project 406
from Member import Member
from Practice import Practice
from Treasurer import Treasurer
from Coach import Coach
import random


class DemoVersion():
    def demoVersion(self, storeUsers):
        #This function will populate our program, its messy and long but it works

        #Creating Coaches and Practices
        coach1 = Coach("Peter", "asd", "coach", "416")
        coach2 = Coach("Raul", "asd", "coach", "416")
        coach3 = Coach("Ryan", "asd", "coach", "416")
        coach4 = Coach("Chris", "asd", "coach", "416")
        coach5 = Coach("John", "asd", "coach", "416")
        practice1 = Practice("1237", "Peter", 10)
        practice2 = Practice("5551", "Ryan", 10)
        practice3 = Practice("6325", "Chris", 10)
        practice4 = Practice("8923", "John", 10)
        practice5 = Practice("9123", "Raul", 10)

        #Creating Members
        member1 = Member("Will", "asd", "member", "705-9345333")
        member2 = Member("Matthew", "asd", "member", "403-7599519")
        member3 = Member("Liam", "asd", "member", "250-7165990")
        member4 = Member("Oliver", "asd", "member", "506-5086531")
        member5 = Member("Lucas", "asd", "member", "514-4899253")
        member6 = Member("Emma", "asd", "member", "416-2245269")
        member7 = Member("Char", "asd", "member", "416-8529865")
        member8 = Member("Mia", "asd", "member", "604-4399036")
        member9 = Member("Evelyn", "asd", "member", "647-5034067")
        member10 = Member("Harper", "asd", "member", "250-2036776")
        member11 = Member("Sophia", "asd", "member", "403-3393020")
        member12 = Member("Isabel", "asd", "member", "418-9535536")


        #Populating Practices
        practice1.memberList.append(member1)
        practice1.memberList.append(member12)
        practice1.memberList.append(member9)
        practice1.memberList.append(member5)

        practice5.memberList.append(member12)
        practice5.memberList.append(member11)
        practice5.memberList.append(member7)
        practice5.memberList.append(member1)
        practice5.memberList.append(member4)
        practice5.memberList.append(member8)

        practice3.memberList.append(member11)
        practice3.memberList.append(member6)
        practice3.memberList.append(member1)
        practice3.memberList.append(member10)
        practice3.memberList.append(member3)
        practice3.memberList.append(member2)
        practice3.memberList.append(member5)

        practice2.memberList.append(member8)
        practice2.memberList.append(member10)
        practice2.memberList.append(member7)

        practice4.memberList.append(member8)
        practice4.memberList.append(member3)
        practice4.memberList.append(member12)
        practice4.memberList.append(member2)
        practice4.memberList.append(member1)
        practice4.memberList.append(member5)
        practice4.memberList.append(member7)
        practice4.memberList.append(member9)
        practice4.memberList.append(member11)
        practice4.memberList.append(member4)

        # Storing Practices
        storeUsers.listPractices.append(practice1)
        storeUsers.listPractices.append(practice2)
        storeUsers.listPractices.append(practice3)
        storeUsers.listPractices.append(practice4)
        storeUsers.listPractices.append(practice5)

        #Updating Members
        for practice in storeUsers.listPractices:
            for member in practice.memberList:
                member.attendClass()
                member.classesPaidFor += 1
                member.accountBalance = random.randint(50,120)
                storeUsers.allMembers[member.getName()] = member
                storeUsers.userDictionary[member.getName()] = member

        storeUsers.allMembers["Will"].classesPaidFor = 2
        storeUsers.allMembers["Lucas"].classesPaidFor = 2
        storeUsers.allMembers["Isabel"].classesPaidFor = 1
        storeUsers.allMembers["Emma"].classesPaidFor = 0


        #Storing Coaches
        storeUsers.allCoaches["Peter"] = coach1
        storeUsers.allCoaches["Raul"] = coach2
        storeUsers.allCoaches["Ryan"] = coach3
        storeUsers.allCoaches["Chris"] = coach4
        storeUsers.allCoaches["John"] = coach5

        for user in storeUsers.allCoaches:
            coach = storeUsers.allCoaches[user]
            storeUsers.userDictionary[coach.getName()] = coach

