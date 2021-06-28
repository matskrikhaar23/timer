import time
longBreaksHad = 0
breaksHad = 0
timerBool = False

print('Hello and welcome to the Study Pomodoro Timer! How long are you studying for?')  #This is placed out here so the welcome message is not reused upon restarting

def timer():
    longBreaksHad = 0
    
    def stop():
        timerBool = False
        print("The timer is over! Good Job!")

    def timeRemaining():
        global minutes
        minutes == (timeTotal - (5 * breaksHad) - (25 * studyHad ) - (15 * longBreaksHad))
        seconds = studyTimeSeconds
        timerBool = True
        while (timerBool == True):
            if (seconds == 0):
                print("Study Time:", hours, ":", minutes, ":", seconds)
                time.sleep(1)
                seconds = 59
                minutes = minutes - 1   
            else:
                print("Study Time:", hours, ":", minutes, ":", seconds)
                seconds -= 1
                time.sleep(1)

            if (seconds) == 0:
                if (minutes == 0):
                    if (hours == 0):
                        timerBool == False
                    else:
                        print(hours, ":", minutes, ":", seconds)
                        time.sleep(1)
                        minutes = 59
                        hours = hours - 1
                
    def longBreak():
        timerBool = True
        global longBreaksHad
        seconds = 0
        minutes = 15
        hours = 0

        while (timerBool == True):
            if (seconds == 0):
                print("Break Time:", hours, ":", minutes, ":", seconds)
                time.sleep(1)
                seconds = 59
                minutes = minutes - 1   
            else:
                print("Break Time:", hours, ":", minutes, ":", seconds)
                seconds -= 1
                time.sleep(1)

            if (minutes == 0):
                if (seconds == 0):
                    if (hours == 0):
                        timerBool = False
                        breaksHad = breaksHad + 1

                        if (breaksHad == breakAmt):
                            timeRemaining()
                        else:
                            twentyFiveMinTimer()
                    
                    print("Break Time:", hours, ":", minutes, ":", seconds)
                    time.sleep(1)
                    minutes = 59
                    hours = hours - 1
        
    def shortBreak():
        seconds = 0
        minutes = 5
        hours = 0
        timerBool = True
        global breaksHad

        while (timerBool == True):
            if (seconds == 0):
                print("Break Time:", hours, ":", minutes, ":", seconds)
                time.sleep(1)
                seconds = 59
                minutes = minutes - 1   
            else:
                print("Break Time:", hours, ":", minutes, ":", seconds)
                seconds -= 1
                time.sleep(1)

            if (minutes == 0):
                if (seconds == 0):
                    if (hours == 0):
                        timerBool = False
                        breaksHad = breaksHad + 1

                        if (breaksHad == breakAmt):
                            timeRemaining()
                        else:
                            twentyFiveMinTimer()
                    print("Break Time:", hours, ":", minutes, ":", seconds)
                    time.sleep(1)
                    minutes = 59
                    hours = hours - 1  
    
    def setMinTimer():
        seconds = studyTimeSeconds
        minutes = studyTimeMinutes
        hours = studyTimeHours
        timerBool = True
        
        while(timerBool == True):
            if (seconds == 0):
                    if (minutes == 0):
                        if (hours == 0):
                            seconds = seconds - 1
                            print("Time's up! Great job!")
                            break
                            timerBool == False 
                    elif (seconds == 0 and minutes !=0):
                        print("Study Time:", hours, ":", minutes, ":", seconds)
                        time.sleep(1)
                        seconds = 59
                        minutes = minutes - 1   
            elif (seconds != 0):
                print("Study Time:", hours, ":", minutes, ":", seconds)
                seconds -= 1
                time.sleep(1)
            elif(hours != 0):
                print(hours, ":", minutes, ":", seconds)
                time.sleep(1)
                minutes = 59
                hours = hours - 1
                            
    def twentyFiveMinTimer():
        global studyHad
        global seconds
        global minutes
        global hours
        timerBool = True
        seconds = 0
        minutes = 25
        hours = 0
        studyHad = 0
        while (timerBool == True):
            if (seconds == 0):
                print("Study Time:", hours, ":", minutes, ":", seconds)
                time.sleep(1)
                seconds = 59
                minutes = minutes - 1   
            else:
                print("Study Time:", hours, ":", minutes, ":", seconds)
                seconds -= 1
                time.sleep(1)

            if (minutes == 0):
                if (seconds == 0):
                    if (hours == 0):
                        studyHad += 1
                        timerBool = False
                        if (breaksHad > 0):
                            if (breaksHad % 4 == 0):
                                seconds = 0
                                minutes = 15
                                hours = 0
                                longBreak()
                            elif (breaksHad == breakAmt):
                                timeRemaining()
                        else:
                            seconds = 0
                            minutes = 5
                            hours = 0
                            shortBreak()
                    
                        
                    print(hours, ":", minutes, ":", seconds)
                    time.sleep(1)
                    minutes = 59
                    hours = hours - 1  

    if (breakAmt == 0):
        setMinTimer()
    elif (breakAmt < 4 and breakAmt != 0):
        twentyFiveMinTimer()

                   
def start():
    start = input("")                   #having no characters as an input ensures that user can just press enter.
    if (start == "" or start == " "):   
        timer()
    else:
        print("Please press enter to start.")       #gives a little bit for interactivity to the user, allowing them to choose when to start. 
        start()   

def breakCalc():
    #print(timeTotal)
    global breakAmt
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

            
    global timeTotal        #for some reason my code only works if this is called here. Sorry!
    timeTotal = studyTimeMinutes  + (studyTimeHours * 60)   #Adds the total time studied in minutes
    
    
    print("Okay! You want to study for ", studyTimeHours, plural, ",", studyTimeMinutes, plural2, ", and", studyTimeSeconds, plural3, "right?")
    confirmation = input("Yes or No? ").lower()#asks for user confirmation, in case they messed up a step. ensures input is not case sensitive
    if confirmation in ["yes", "y"]:          
        breakCalc()                          #calls the function which calculates how many breaks user will get
    elif confirmation in ["no", "n"]:
        print("Alright then, let's do this again. How many hours would you like to study for?")
        setup()                                #calls back to the start of this function, in case user wants to start over.

setup()                                         #starts the code



