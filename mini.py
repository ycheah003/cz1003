#Import all relevant modules and packages
from tkinter import *
import functools
from datetime import datetime

#All relevant datasets
daysinweek = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
menu, price, operatinghrs = {}, {}, {}
operatinghrs["Mini Wok"] = ["1000 to 1900", "1000 to 1900", "1100 to 1900", "1100 to 2000", "1100 to 1500"]
operatinghrs["Yong Tau Fu"] = ["1000 to 2000", "1000 to 2000", "1100 to 1800", "1000 to 1800", "1100 to 1500"]
operatinghrs["Chicken Rice"] = ["1100 to 1700", "1100 to 2000", "1000 to 1600", "1000 to 1800", "1100 to 1900"]
menu["Mini Wok"], price["Mini Wok"]= ["Fried Rice", "Fried Hor Fun", "Fried Bee Hoon"], \
                                     ["$4.00", "$5.00", "$5.50"]
menu["Yong Tau Fu"], price["Yong Tau Fu"] = ["Bak Chor Mee", "Laksa Soup"], \
                                            ["$4.00", "$4.50"]
menu["Chicken Rice"], price ["Chicken Rice"] = ["Chicken Rice", "Chicken Hor Fun"], \
                                               ["$3.00", "$3.00"]


#Setting interface size and name
window = Tk()
window.title("CZ1003 Mini Project")
window.geometry("500x400")

#Welcome banner showing current date and time
time, mainpage = StringVar(), StringVar()
Mainpage = Label(window, textvariable=mainpage, font = ("arial 15 bold italic"), relief=RAISED)
mainpage.set("Welcome to NTU NorthSpine Food Section")
logo = PhotoImage(file= "canteen.ppm")
currenttime = Label(window, textvariable=time, font = ("arial 10 bold italic"))
time.set(datetime.now().strftime("%a, %d %b %Y %H:%M:%S"))

def viewtdy():
    top = Toplevel()
    top.title("Choose a Store")

def viewother():
    top = Toplevel()
    top.title("Select Query Date and Time")

buttontoday = Button(window, text="View Today's Menu", command=viewtdy).pack()
buttonother = Button(window, text="View Other Day's Menu", command=viewother).pack()

Mainpage.pack()
currenttime.pack()


frame = Frame(window, width = 400,height = 300)
frame.pack_propagate(0)
frame.pack()
Label(frame, image = logo) .pack(fill=BOTH)   #logo

window.mainloop()
