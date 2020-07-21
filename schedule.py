import sys
from datetime import date
import time
import random


class Objective:
    def __init__(self,obj):
        self.obj = obj
        self.my_rank = 0
        self.subject = ""
        self.assignment = ""
        self.due_date_str = ""
        self.due_date = 0
        self.difficulty = 0
        self.importance = 0
        self.total_due_date = 0
        self.total_difficulty = 0
        self.total_importance = 0
        self.per_due_date = 0
        self.per_difficulty =0
        self.per_importance =0
        self.my_total = 0
        self.per_hour = 0
        self.all_total = 0
        self.my_mins = 0
        self.rank_info = ""
        self.all_info = ""



    def datecheck(self,datate):
        # Here we try to validate
        # the date

        self.due_date_str = datate
        catchslash = 0
        datlen = len(datate)
        while catchslash < datlen:
            if datate[catchslash] == "/":
                datlen = -1
            catchslash +=1

        if catchslash == 0 or catchslash == len(datate):
            return 2

        to_month = int(datate[:catchslash-1])
        to_day = int(datate[catchslash:])

        if to_month >12 or to_month < 1:
            return 2
        if to_day >31 or to_day < 1:
            return 2

        today = str(date.today())
        from_day = int(today[8] + today[9])
        from_month = int(today[5] + today[6])
        if to_month - from_month < 0 or to_month - from_month > 2: return 2
        if to_day - from_day < 0 and to_month - from_month == 0: return 2
        daycrease = 0
        daycrease += 30 *(to_month - from_month)
        if to_day < from_day:
            daycrease += 30 - from_day
        else:
            daycrease += to_day - from_day
        self.due_date = daycrease
        return 0




    def oneten(self,intensity,typee):

        inten = int(intensity)
        if inten < 1 or inten >10:
            if typee == 3:
                return typee
            if typee == 4:
                return typee
        if typee == 3:
            self.difficulty = inten
        if typee == 4:
            self.importance = inten
        return 0

    def validate(self):
        # space_count keeps track of the
        # spaces that are in the string
        space_count = 0

        # space_back stays back and encapsulates
        # a word with slicing
        space_back = 0

        # st_loop stops the loop
        st_loop = 1

        # schelisto sticks all the strings into
        # a list
        schelisto = []

        while space_count < len(self.obj):
            if self.obj[space_count] == ' ':
                schelisto.append(self.obj[space_back:space_count])
                space_back = space_count+1
            space_count+=1
        schelisto.append(self.obj[space_count-1:])
        print(schelisto)

        # This returns the status of the schedule
        # 0 is everything is fine
        # 1 is that the wrong size of input
        # 2 is that the date is wrong
        # 3 is that the difficult is wrong
        # 4 is that the importance is wrong
        listostatus = 0
        # This is to check for the right input
        # 5 of size is for normal input
        # 6 is for percentage completed
        if len(schelisto) == 5 or len(schelisto) == 6:

            self.subject = schelisto[0]
            self.assingment = schelisto[1]
            listostatus = self.datecheck(schelisto[2])
            listostatus = self.oneten(schelisto[3],3)
            listostatus = self.oneten(schelisto[4],4)
        else:
            listostatus = 1
        return listostatus

    def my_objective(self):
        return self.obj
    def my_subject(self):
        return self.subject
    def my_assignment(self):
        return self.assignment
    def my_due_date(self):
        return self.due_date
    def my_difficulty(self):
        return self.difficulty
    def my_importance(self):
        return self.importance
    def my_total(self):
        return self.my_total

    def calcu(self,due,difi,imp):
        self.my_total = 0
        self.total_due_date = due
        self.total_difficulty = difi
        self.total_importance = imp
        dudu = float(due - self.due_date)
        self.per_due_date = dudu/due
        self.per_difficulty = float(self.difficulty)/difi
        self.per_importance = float(self.importance)/imp
        self.my_total += (due * self.per_due_date)*1.5
        self.my_total += (difi * self.per_difficulty)*1.2
        self.my_total += (imp * self.per_importance)*1.3
        return self.my_total


    def alto(self,alto):
        self.all_total = alto
        self.per_hour = float(self.my_total)/alto
        return self.per_hour

    def ranki(self,rank,mins):
        self.my_rank = rank
        self.rank_info += str(rank) + " "
        self.rank_info += self.subject + " "
        self.rank_info += self.assignment + " "
        self.rank_info += self.due_date_str + " "
        self.rank_info += str(int(mins*60)) + " " + "out of 60 minutes"
        self.my_mins = mins

        self.all_info += str(rank) + " "
        self.all_info += self.subject + " "
        self.all_info += self.assignment + " "
        self.all_info += self.due_date_str + " "
        self.all_info += str(self.due_date) + " "
        self.all_info += str(self.difficulty) + " "
        self.all_info += str(self.importance) + " "
        self.all_info += str(self.total_due_date) + " "
        self.all_info += str(self.total_difficulty) + " "
        self.all_info += str(self.total_importance) + " "
        self.all_info += str(self.per_due_date) + " "
        self.all_info += str(self.per_difficulty) + " "
        self.all_info += str(self.importance) + " "
        self.all_info += str(self.my_total) + " "
        self.all_info += str(self.per_hour) + " "
        self.all_info += str(self.all_total) + " "
        self.all_info += str(self.my_mins) + " "
        return self.rank_info

class Schedular:
    def __init__(self):
        self.subject = []
        self.assignment = []
        self.due_date = []
        self.difficulty = []
        self.importance = []
        self.objectives = []
        self.sorted_obj = []
        self.pers = []
        self.tutor()

    def tutor(self):
        # We ask if they are first time users or not
        yes_response = ["Yes","y","yes"]
        no_response = ["No","n","no"]
        tutosponse = input("Is this your first time using schedular?\n")
        if tutosponse in no_response:
            return 0
        else:
            #return 0
            self.main_tutor()

    def printi(self,pp):
        for i in pp:
            sys.stdout.write(i)
            sys.stdout.flush()
            if i == '\n':
                time.sleep(random.uniform(1,1.5))
            else:
                time.sleep(random.uniform(0,0.1))



    def main_tutor(self):
        self.printi("Welcome to The Schedular!\n\nIn this program you will create an optimal schedule for your deadlined objectives or assignments.\n\nYou will need to enter 5 things about each of your objectives\n\nThe format for each variable is as follows\n\nFormat = Subject || Type of Assignment || Due Date || Difficulty ||  Importance\n\nSubject Format = String\n\nType of Assignment Format = String\n\nDate Format = mm/dd or m/d or m/dd or mm/d\n\nDifficulty = Difficulty of Work\nDifficulty Range = 1-10\n\nImportance = Importance of Work\nImportance Range = 1-10\n\n\n\nHere is an example of an input:\nObjective : CSE1000 HW1 3/9 4 9\n\nWhen all objectives have been added press 'q' to procedd to the next step\n\nNow it is time to enter your objectives\nFormat = Subject || Type of Assignment || Due Date || Difficulty ||  Importance\n\n")

    def good_schedule(self, schedule):
        self.objectives.append(schedule)
        return 0


    def all_schedules(self):
        toto_due = -1
        toto_difi = 0
        toto_imp = 0
        self.printi("\n\nSo far your schedule looks like:\n\n")
        for i in self.objectives:
            #print(i.my_objective())
            self.assignment.append(i.my_assignment())
            self.subject.append(i.my_subject())
            self.due_date.append(i.my_due_date())
            if toto_due <= i.my_due_date():
                toto_due = i.my_due_date()
            self.difficulty.append(i.my_difficulty())
            toto_difi += i.my_difficulty()
            self.importance.append(i.my_importance())
            toto_imp += i.my_importance()
        alto = 0
        for i in self.objectives:
            alto += i.calcu(toto_due,toto_difi,toto_imp)

        self.sorted_obj = []
        ii = 0
        for i in self.objectives:
            self.sorted_obj.append([i.alto(alto),ii])
            self.pers.append(60 * self.sorted_obj[ii][0])
            ii+=1
        self.sorted_obj = self.swaps(self.sorted_obj)
        self.sorted_obj.reverse()
        #print(self.objectives)
        self.the_schedule()
        return 0

    def the_schedule(self):
        ii = 0
        ilen = len(self.sorted_obj)
        stri = ""
        while ii < ilen:
            #stri += self.subject[self.sorted_obj[ii][1]].ranki(ii+1,self.sorted_obj[ii][0])
            stri += self.objectives[self.sorted_obj[ii][1]].ranki(ii+1,self.sorted_obj[ii][0])
            stri += "\n\n"
            print(stri)
            stri = ""
            ii +=1
        return 0


    def swaps(self,l):
        # In the dictiionary  we store the following
        # 'lst' to store the list
        # 'swaps' will store the number of swaps
        # 'lt' will be the left of the list
        # 'rt' will be the right of the list
        swapcheck = {'lst':l,'swaps':0, 'lt': None, 'rt' : None}

        # Call the function to perform swap counting
        swapresults = self.mergeswap(swapcheck)
        return swapresults['lst']


    def mergeswap(self,swapcheck):
        # If the amount of objects in the list is less
        # than 2 then there is nothing to check
        if len(swapcheck['lst']) < 2:
            return swapcheck

        # Other wise start dividing list into two
        # begin by putting the list into a new list
        lst = swapcheck['lst']

        # Find the median
        mid = len(swapcheck['lst']) // 2

        # The left
        lt = lst[:mid]

        # The right
        rt = lst[mid:]

        # assign the left to the list as new
        swapcheck['lst'] = lt

        # Use swapmerge function to check for swaps
        self.mergeswap(swapcheck)

        # assign the right to the list as new
        swapcheck['lst'] = rt

        # Use swapmerge function to check for swaps
        self.mergeswap(swapcheck)

        # Assign a new list to dictionary
        swapcheck['lst'] = lst

        # Assign a new left to the dictionary
        swapcheck['lt'] = lt

        # Assign a new right to the dictionary
        swapcheck['rt'] = rt

        # Now do the counting
        return self.swapcounter(swapcheck)




    def swapcounter(self,swapcheck):
        # i and j to keep track of the indices
        i = 0
        j = 0

        # Assign a new left, right, key and list
        a = swapcheck['lt']
        b = swapcheck['rt']
        L = swapcheck['lst']


        # Now use mergesorts merging to check for the number of swaps
        while i <len(a) and j < len(b):
            if a[i][0] <= b[j][0]:
                L[i+j] = a[i]
                i += 1
            else:
                L[i+j] = b[j]
                j += 1
                swapcheck['swaps'] += len(a[i:])
            L[i+j:] = a[i:] + b[j:]
            swapcheck['lst'] = L
        return swapcheck



def main():
    validators = ["","\n\nWrong Input\nTry Again","\n\nWrong Date\nTry Again","\n\nWrong Difficulty\n\nDifficulty should be between 1-10\nTry Again","\n\nWrong Importance\n\nImportance should be between 1-10\nTry Again\n"]
    mys = Schedular()
    objs = ""
    while objs != "q":
        objs = input("Enter Objective = ")
        obj = Objective(objs)
        vali = obj.validate()
        if vali == 0:
            mys.good_schedule(obj)
        else:
            if objs != "q":
                print(validators[vali])

    mys.all_schedules()

def maine_justice():
    mys = Schedular()
    objs = "CSE1000 HW1 7/25 4 9"
    obj = Objective(objs)
    vali = obj.validate()
    mys.good_schedule(obj)

    objs = "CSE100 HW1 7/25 8 9"
    obj = Objective(objs)
    vali = obj.validate()
    mys.good_schedule(obj)

    objs = "CSE10 HW1 7/25 7 9"
    obj = Objective(objs)
    vali = obj.validate()
    mys.good_schedule(obj)

    mys.all_schedules()





    return 0

if __name__ == '__main__':
    maine_justice()
    #main()
