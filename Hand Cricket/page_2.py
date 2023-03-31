from tkinter import *
from tkinter import ttk
from tkinter import font
import page_1
from playsound import playsound
import random
import tkinter as tk
from tkVideoPlayer import TkinterVideo
from PIL import ImageTk,Image

root = Tk()
root.title("Coin Flipping Game")
root.geometry('1200x650')
root.configure(bg='black')

#vs
def V():
    gtt=tnv1.get()
    if gtt=="CSK":
        a1.config(image=csk)
    if gtt=="MI":
        a1.config(image=mi)
    if gtt=="RCB":
        a1.config(image=rcb)
    if gtt=="DC":
        a1.config(image=dc)
    if gtt=="RR":
        a1.config(image=rr)
    if gtt=="KKR":
        a1.config(image=kkr)    
    if gtt=="LSG":
        a1.config(image=lsg)  
    if gtt=="GT":
        a1.config(image=gt)     
    if gtt=="PK":
        a1.config(image=pk)  
    if gtt=="SRH":
        a1.config(image=srh)     

    gtts=tnv2.get()   
    if gtts=="CSK":
        a2.config(image=csk)
    if gtts=="MI":
        a2.config(image=mi)
    if gtts=="RCB":
        a2.config(image=rcb)
    if gtts=="DC":
        a2.config(image=dc)
    if gtts=="RR":
        a2.config(image=rr)
    if gtts=="KKR":
        a2.config(image=kkr)    
    if gtts=="LSG":
        a2.config(image=lsg)  
    if gtts=="GT":
        a2.config(image=gt)     
    if gtts=="PK":
        a2.config(image=pk)  
    if gtts=="SRH":
        a2.config(image=srh)     
    videoplayer = TkinterVideo(master=root, scaled=True)
    videoplayer.load("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\Python\\Video\\toss.mp4")
    videoplayer.place(x=422,y=80,width=410,height=150)    
    videoplayer.play() # play the video
def bating():
    bat1=Label(text="You will bat first")
    bat1.config(font=("bold",20))
    bat1.place(x=440,y=500)
def bowling():
    bat1=Label(text="You will bowl first")
    bat1.config(font=("bold",20))
    bat1.place(x=440,y=500)
        
 
def choose():
    if(g.get()==0):
        print("you choose head")    
    elif(g.get()==1):     
         print("you choose tails")

def flip():
    
    if num == 0:
        i.config(image=heads)
    elif num==1:
        i.config(image=tails)
        
    
    if g.get()== num:
        print("you won the toss")
        print(g.get())
        print(num)   
        qq=Label(root,text="congrulation you have won the toss")
        qq.config(font=("bold",22))
        qq.place(x=400,y=350)
        bat=Button(root, text="bat",command=bating)
        bowl=Button(root, text="bowl",command=bowling)
        bowl.config(font=("bold"))
        bowl.place(x=620,y=400)
        bat.config(font=("bold"))
        bat.place(x=420,y=400)
    

    else:
        print("you lost")
        print(g.get())
        print(num)
        a=random.randint(0,1)
        if a=="0":
           bat1=Label(text="Opponent has choosen to bowl ")
           batw=Label(text="You will bat first")
           bat1.config(font=("bold"))
           bat1.place(x=420,y=400)
           batw.place(x=420,y=440) 
           batw.config(font=("bold"))
        else:
           bat1=Label(text="Opponent has choosen to bat ")
           batw=Label(text="You will bowl first") 
           bat1.config(font=("bold"))
           bat1.place(x=420,y=400)
           batw.place(x=420,y=440) 
           batw.config(font=("bold"))   
        qq=Label(root,text="opps you lost the toss")
        a7.config(image=h)
        qq.config(font=("bold",22))
        qq.place(x=400,y=350)


g=IntVar()
r1= Radiobutton(root, text="head",value=0,variable = g)
r2= Radiobutton(root, text="tails",value=1,variable = g)
r1.config(font=("bold",18))
r2.config(font=("bold",18))
r1.place(x=600,y=290,width=85,height=20,)
r2.place(x=700,y=290,width=85,height=20,)
button=Button(root,text="choose",command=choose)
button.config(bg="gold",font=("bold",18))
button.place(x=500,y=290,width=85,height=25)

l = Label(root, text="WELCOME TO TOSS OF VIIT IPL")
l.config(font=("Courier", 14),bg="yellow")
t = Text(root, width=20, height=1, )
t.insert(INSERT, "Whoose head or tails")
t.config(font=("Courier", 19))
z=Button(root,text="Vs",command=V)
z.config(font=("Courier", 14),bg="red")
z.place(x=620,y=130)
l.pack()
t.place(x=500,y=230)

import random
num = random.randint(0,1) 

from PIL import Image, ImageTk
#rr                 
load = Image.open('C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\Python\\logo1\\RR.jpg')
load = load.resize((150, 150))
rr= ImageTk.PhotoImage(load)

#rcb
load = Image.open('C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\Python\\logo1\\RCB.jpg')
load = load.resize((150, 150))
rcb= ImageTk.PhotoImage(load)
#kkr
load = Image.open('C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\Python\\logo1\\KKR.jpg')
load = load.resize((150, 150))
kkr= ImageTk.PhotoImage(load)
#mi
load = Image.open('C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\Python\\logo1\\MI.jpg')
load = load.resize((150, 150))
mi= ImageTk.PhotoImage(load)

#dc
load = Image.open('C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\Python\\logo1\\DC.jpg')
load = load.resize((150, 150))
dc= ImageTk.PhotoImage(load)
#csk                
load = Image.open('C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\Python\\logo1\\CSK.jpg')
load = load.resize((150, 150))
csk= ImageTk.PhotoImage(load)

#gt
load = Image.open('C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\Python\\logo1\\GT.jpg')
load = load.resize((150, 150))
gt= ImageTk.PhotoImage(load)

#SRH
load = Image.open('C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\Python\\logo1\\SRH.jpg')
load = load.resize((150, 150))
srh= ImageTk.PhotoImage(load)

#PK
load = Image.open('C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\Python\\logo1\\PK.jpg')
load = load.resize((150, 150))
pk= ImageTk.PhotoImage(load)

#LSG
load = Image.open('C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\Python\\logo1\\LSG.jpg')
load = load.resize((150, 150))
lsg= ImageTk.PhotoImage(load)
#team 1          
T1 = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\python\\basic image\\bowl.jpg")
T1 = T1.resize((150, 150))
logo = ImageTk.PhotoImage(T1)
a1 = Label(root, image=logo)
a1.place(x=200,y=65) 

#team 2
T2 = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\python\\basic image\\bat.jpg")
T2 = T2.resize((150, 150))
logo2 = ImageTk.PhotoImage(T2)
a2 = Label(root, image=logo2)
a2.place(x=900,y=65) 

#load heads
load = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\python\\basic image\\heads.jpg")
load = load.resize((150, 150))
heads = ImageTk.PhotoImage(load)
#load tails
load = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\python\\basic image\\tails.jpg")
load = load.resize((150, 150))
tails = ImageTk.PhotoImage(load)
a = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\python\\basic image\\coin.jpg")
a = a.resize((150, 150))
coin = ImageTk.PhotoImage(a)
i = Label(root, image=coin)
i.place(x=195,y=450)

l = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\python\\basic image\\heads.jpg")
l = l.resize((150, 150))
h = ImageTk.PhotoImage(l)
a7 = Label(root, image=h)
a7.place(x=1000,y=665) 

tnv1=StringVar()
team1name=ttk.Combobox(root,value=("MI","CSK","RCB","DC","GT","RR","LSG","KKR","SRH","PK"),font=("time new roman",10,"bold"),justify=CENTER,state='readonly',textvariable = tnv1)
team1name.place(x=205,y=30,width= 140,height=30)
team1name.set("select your team ")

tnv2=StringVar()
team2name=ttk.Combobox(root,value=("MI","CSK","RCB","DC","GT","RR","LSG","KKR","SRH","PK"),font=("time new roman",10,"bold"),justify=CENTER,state='readonly',textvariable = tnv2)
team2name.place(x=888,y=30,width= 180,height=30)
team2name.set("select your oppiste team ")


b = Button(root, text="Flip Coin", bg='lightblue', fg='green', activebackground="lightgray", padx=10, pady=10, command=flip)
b.config(font=("bold",18))
b.place(x=210,y=230)

root.mainloop()

if g.get()== num:
    print("you won the toss")
    print(g.get())
    print(num)   

else:
    print("you lost")
    print(g.get())
    print(num)
    
    
   
    
    