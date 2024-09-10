from playsound import playsound
import time #to calculate using time
CLEAR = "\033[2J" #clear terminal for better view
CLEAR_AND_RETURN = "\033[H"#return cursor to home position and print

def alarm(seconds): #defining a alarm variable
    time_elapsed = 0 #set it to 0
    print(CLEAR) #clear the terminal and print
    while time_elapsed < seconds:
        time.sleep(1) #wait for 1 second 
        time_elapsed +=1
        time_left = seconds - time_elapsed #create a variable time left so that we can display it(time left = second - time elapsed)
        minuts_left = time_left //60 # convert to minuts 
        seconds_left = time_left %60 #for seconds
        print(f"{CLEAR_AND_RETURN}TIME REMAINING = {minuts_left:02d}:{seconds_left:02d}") #02d to makeit 2 digits. (clear and return means to make it write in the same place by clearing the previous value)
    playsound("C:\VSC\Projects\PYTHON projects\Alarm clock project\alarm.mp3")
minuts = int(input("How many minuts do you want to wait: "))
seconds = int(input("How many seconds do you want to wait: "))
total_seconds= minuts*60+seconds #convert to same value
alarm(total_seconds)

