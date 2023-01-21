from tkinter import *
import datetime
import time
import winsound
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d:%m:%Y")
        print("The set date is: ",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to wake up!")
            path = r"C:\Users\marjan\Downloads\mixkit-scanning-sci-fi-alarm-905.wav"
            winsound.PlaySound(path,winsound.SND_ASYNC)
            break
            
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
    
#creating GUI using Tkinter
clock = Tk()  #initialize Tkinter
clock.title("Pincer Alarm Clock")
clock.geometry('400x400+20+20')
time_format=Label(clock, text="Enter time in 24hour format: ",fg="red",bg="blue",font="Ariel").place(x=60,y=120)
addtime = Label(clock, text="Hour Min Sec",font=60,).place(x=110)
SetYourAlarm = Label(clock,text="When to wake you up", fg='blue',relief='solid', font=('Helevitica',7,'bold')).place(x=0,y=29)
#variables required to set alarm
hour = StringVar()
min = StringVar()
sec = StringVar()
#Time required to set the alarm clock
hourTime= Entry(clock,textvariable = hour,bg = "grey",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "grey",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "grey",width = 15).place(x=200,y=30)
#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)
clock.mainloop()