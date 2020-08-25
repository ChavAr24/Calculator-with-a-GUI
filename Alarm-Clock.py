# ||------------------------
# An alarm Clock with a GUI 
# would recommend turning this code file to a exe file
# I have a Alarm tone as per my taste but you can always use a different one
# By: Aryan Chavan
# ||------------------------

#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
import winsound

# printing the current time 
current_time1 = datetime.datetime.now()
now1 = current_time1.strftime("%H:%M:%S")
date1 = current_time1.strftime("%d/%m/%Y")
print(date1)
print(now1)



def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound('sound.wav',winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Alarm Clock")
# clock.iconbitmap(r"dataflair-logo.ico")
clock.geometry("400x225")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=150)
addTime = Label(clock,text = "Hour     Min      Sec",font=60).place(x = 100, y = 30)
setYourAlarm = Label(clock,text = "What time do you want the alarm to be",fg="black",font=("Arial",15,"bold")).place(x=0, y=0)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "grey",width = 15).place(x=100,y=60)
minTime= Entry(clock,textvariable = min,bg = "grey",width = 15).place(x=150,y=60)
secTime = Entry(clock,textvariable = sec,bg = "grey",width = 15).place(x=200,y=60)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=100)

Author =  Label(clock,text = "Aryan Chavan",fg="black",font=("Arial",3,"bold")).place(x=370, y=215)

clock.mainloop()
#Execution of the window.

