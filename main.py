import time


print('Hello and welcome to the Study Pomodoro Timer! How long are you studying for?')  #This is placed out here so the welcome message is not reused upon restarting

def timer():
    print(timeTotal)
    print(testValue)
    while (studyTimeSeconds != 0 and studyTimeMinutes != 0 and studyTimeHours != 0):
        print(studyTimeSeconds, ":", studyTimeMinutes, ":", studyTimeHours)
        studyTimeSeconds = secostudyTimeSeconds - 1
        time.sleep(1)
        
        if (studyTimeSeconds == 0):
            studyTimeSeconds = 59
            time.sleep(1)
    
def start():
    start = input("")                   #having no characters as an input ensures that user can just press enter.
    if (start == "" or start == " "):   
        timer()
    else:
        print("Please press enter to start.")       #gives a little bit for interactivity to the user, allowing them to choose when to start. 
        start()   

def breakCalc():
    #print(timeTotal)
    breakAmt = int(timeTotal / 30)              #calculates the amount of total breaks
    longBreakAmt = int(breakAmt / 4)            #calculates the amount of long breaks
    #print(breakAmt)
    if (breakAmt >= 4):                         #checks if the user gets a long break or not
        print("You will have", breakAmt, "breaks every twenty-five minutes, where", longBreakAmt, "of them is a 15 minute break, and the rest are five.")
        print("Press enter to start the timer")
        start()                                #calls the function that starts the timer
    elif (breakAmt < 4):
        print("You will have", breakAmt, "five minute breaks every 25 minutes.")
        print("Press enter to start the timer")
        start()                                #calls the function that starts the timer

def setup():
    global studyTimeHours
    studyTimeHours = int(input("Hours: ")) #asks user for how many hours they want to study for.
    hours = studyTimeHours
    if (studyTimeHours == 1):
        plural = 'hour'                     #checks for proper grammar
    else:
        plural = 'hours'                    #checks for proper grammar

    print(studyTimeHours, plural, 'huh? And how many minutes?') #asks user for how many minutes to study
    
    global studyTimeMinutes
    studyTimeMinutes = int(input('Minutes: '))
    if (studyTimeMinutes == 1):
     plural2 = 'minute'                         #checks for proper grammar
    else:
     plural2 = 'minutes'                        #checks for proper grammar

    if (studyTimeMinutes >= 60):                #if the amount of minutes is over 60, it adds 1 hour.
        hours = int(studyTimeMinutes / 60)
        remainder = (studyTimeMinutes % 60)
        studyTimeHours = (studyTimeHours + hours)
        studyTimeMinutes = 0 + remainder
        if (studyTimeHours == 1):
            plural = "hour"              #checks for proper grammar
        else:
            plural = "hours"             #checks for proper grammar
    

    print(studyTimeMinutes, plural2, "? Alright! And how many seconds?") #asks for how many seconds to stud
    global studyTimeSeconds
    studyTimeSeconds = int(input("Seconds: "))
    if (studyTimeSeconds == 1):
        plural3 = "second"              #checks for proper grammar
    else:
        plural3 = "seconds"             #checks for proper grammar
              
    
    
    if (studyTimeSeconds >= 60):            #if the amount of seconds is over 60, it adds one minute
        minutes = int(studyTimeSeconds / 60)
        remainder = (studyTimeSeconds % 60)
        studyTimeMinutes = (studyTimeMinutes + minutes)
        studyTimeSeconds = 0 + remainder
        if (studyTimeMinutes == 1):
            plural2 = "minute"              #checks for proper grammar
        else:
            plural2 = "minutes"             #checks for proper grammar
    
    global timeTotal                    #for some reason my code only works if this is called here. Sorry!
    timeTotal = studyTimeMinutes  + (studyTimeHours * 60)   #Adds the total time studied in minutes
    global testValue
    testValue = int(input("test:"))
    
    print("Okay! You want to study for ", studyTimeHours, plural, ",", studyTimeMinutes, plural2, ", and", studyTimeSeconds, plural3, "right?")
    confirmation = input("Yes or No? ").lower()#asks for user confirmation, in case they messed up a step. ensures input is not case sensitive
    if confirmation in ["yes", "y"]:          
        breakCalc()                          #calls the function which calculates how many breaks user will get
    elif confirmation in ["no", "n"]:
        print("Alright then, let's do this again. How many hours would you like to study for?")
        setup()                                #calls back to the start of this function, in case user wants to start over.


setup()                                         #starts the code



    