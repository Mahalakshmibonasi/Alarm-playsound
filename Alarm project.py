import datetime
from playsound import playsound
# from tkinter import*
# from tkinter.ttk import Combobox



hour=int(input("enter the hour:"))
minute=int(input("enter the minit:"))
AmPm=input(" am / pm : ")
ampm=AmPm.lower()

if ampm=="pm":
    hour+=12
elif ampm=="am":
    hour-=12

i=1
while i<=3:
    if (hour==datetime.datetime.now().hour and minute==datetime.datetime.now().minute):
        print(f"wake up it's {hour}:{minute}")
        playsound("/home/b/Downloads/")
        i=i+1
print("good morning")