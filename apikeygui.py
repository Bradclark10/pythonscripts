from datetime import datetime
from tkinter import *
from tkinter import messagebox   
import datetime
  
top = Tk()  
  
top.geometry("200x100")  

current_time = datetime.datetime.now(datetime.timezone.utc)
current_time = current_time.timestamp() # works if Python >= 3.3
threemonths = current_time + (43800*3* 60)  # 5 min * 60 seconds
twomonths = current_time + (43800*2* 60)  # 5 min * 60 seconds
onemonth = current_time + (43800*1* 60)  # 5 min * 60 seconds


  
def threemonth():  
    messagebox.showinfo("Hello", threemonths)  

def twomonth():  
    messagebox.showinfo("Hello", twomonths)  

def onemonths():  
    messagebox.showinfo("Hello", onemonth)  
  
  
  
b1 = Button(top,text = "three months",command = threemonth,activeforeground = "red",activebackground = "pink",pady=10)  
  
b2 = Button(top,text = "two months",command = twomonth,activeforeground = "red",activebackground = "pink",pady=10)    
  
b3 = Button(top,text = "one months",command = onemonths,activeforeground = "red",activebackground = "pink",pady=10)  
    
  
b1.pack(side = BOTTOM)  
  
b2.pack(side = RIGHT)  
  
b3.pack(side = TOP)  
  

  
top.mainloop()  