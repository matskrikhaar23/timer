#study pomodoro
#get input as to how long user needs to study
#based on that numeric value
#convert hours, minutes, seconds
#Compute how many breaks, and how long they will study
import time

def timer():
    print("You will get a 5 minute break every 25 minutes, with a 15 minute break every hour.")
    print(timeTotal)
    breakAmt = int(timeTotal / 30)
    longBreakAmt = int(breakAmt / 4)
    print(breakAmt)
    if (breakAmt >= 4):
        print("You will have", breakAmt, "breaks every twenty-five minutes, where", longBreakAmt, "of them is a 15 minute break, and the rest are five.")
    elif (breakAmt < 4):
        print("You will have", breakAmt, "five minute breaks every 25 minutes.")
def setup():
    print('Hello and welcome to the Study Pomodoro Timer! How long are you studying for?')
    studyTimeHours = int(input("Hours: ")) 
    if (studyTimeHours == 1):
        plural = 'hour'
    else:
        plural = 'hours'

    print(studyTimeHours, plural, 'huh? And how many minutes?')
    studyTimeMinutes = int(input('Minutes: '))
    if (studyTimeMinutes == 1):
     plural2 = 'minute'
    else:
     plural2 = 'minutes'

    print(studyTimeMinutes, plural2, "? Alright! And how many seconds?")
    studyTimeSeconds = int(input("Seconds: "))
    if (studyTimeSeconds == 1):
        plural3 = "second"
    else:
        plural3 = "seconds"
    global timeTotal
    timeTotal = studyTimeMinutes  + (studyTimeHours * 60)
    
    print("Okay! You want to study for ", studyTimeHours, plural, ",", studyTimeMinutes, plural2, ", and", studyTimeSeconds, plural3, "right?")
    confirmation = input("Yes or No?").lower()
    if confirmation in ["yes", "y"]: 
        timer()
    elif confirmation in ["no", "n"]:
        print("Alright then, let's do this again.")
        setup()
 
setup()

