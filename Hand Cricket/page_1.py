
from tkinter import *
from tkinter import ttk
from webbrowser import get
from PIL import ImageTk,Image
import pyttsx3


root=Tk()
root.title("selection buttion")
root.geometry("1150x600+60+50")
root.configure(bg='blue')

def ok():
        if(p.get()==0):
               print("You have selected Green Pitch")
               print("This Pitch Contain Good covering of tall grass")
               print("Moisture in it is good for fast bowler especially on grassy area")
               print("Ball Doesn,t grip surface and also doesn,t acid spin\n")
        elif(p.get()==1):
               print("You have Selected Dusty Pitch")
               print("This Pitch contain Soft Track")
               print("Turns of ball are mostly unrolled which is good for spinnners")
               print("If ball grip,s the surface unbelievable turn can be see\n")
        elif(p.get()==2):
               print("You have Selected Dead Pitch\n")
               print("This pitch is even for both batsmen and bowler")   
               print("This is average scoring pitch")   
        
        
        if(m.get()==0):
               print("you have selected playing in evening")
        
        elif(m.get()==1):
               print("you have selected playing in Afternoom")
        elif(m.get()==2):  
               print("you have selected playing in  Night")

        if(b.get()==0):
               print("Today wheater is clear")
        
        elif(b.get()==1):
               print("Today wheater is cloudy") 
               print("it might rain")

    
        


def select():            
       num = Stadium.get() 
       if num == "DY Patil Stadium":
          i.config(image=DY_Patil_Stadium)
       elif num=="eden gardens stadium":
            i.config(image=eden_gardens_stadium)
       elif num=="Narendra Modi Stadium":
            i.config(image=Narendra_Modi_Stadium) 
       elif num=="Shaheed Veer Narayan Singh International Cricket Stadium":
            i.config(image=Shaheed_Veer_Stadium)           
       elif num=="Feroz Shah Kotla Stadium":
            i.config(image=Feroz_Shah_Kotla_Stadium)           
       elif num=="MCAS":
            i.config(image=MCAS)
       elif num=="Holkar Stadium":
            i.config(image=Holkar_Stadium)           
       elif num=="HPCA Stadium":
            i.config(image=HPCA_Stadium)
       elif num=="M. Chinnaswamy Stadium":
            i.config(image=M_Chinnaswamy_Stadium)    
       elif num=="Raipur International Cricket Stadium":
            i.config(image=Raipur_International_Cricket_Stadium)    
       elif num=="Rajiv Gandhi International Cricket Stadium":
            i.config(image=Rajiv_Gandhi_Stadium)       
       elif num=="Wankhede Stadium":
            i.config(image=Wankhede_Stadium)
     


#Raipur International Cricket Stadium
load = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\Python\\Stadium\\Raipur International Cricket Stadium.jpg")
load = load.resize((500, 250))
Raipur_International_Cricket_Stadium = ImageTk.PhotoImage(load)


#Wankhede Stadium
load = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\python\\Stadium\\Wankhede Stadium.jpg")
load = load.resize((550, 270))
Wankhede_Stadium= ImageTk.PhotoImage(load)

#Rajiv Gandhi International Cricket Stadium
load = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\python\\Stadium\\Rajiv Gandhi International Cricket Stadium.jpg")
load = load.resize((550, 270))
Rajiv_Gandhi_Stadium= ImageTk.PhotoImage(load)

#M. Chinnaswamy Stadium
load = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\python\\Stadium\\M. Chinnaswamy Stadium.jpg")
load = load.resize((550, 270))
M_Chinnaswamy_Stadium= ImageTk.PhotoImage(load)

#HPCA Stadium
load = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\python\\Stadium\\HPCA Stadium.jpg")
load = load.resize((550, 270))
HPCA_Stadium = ImageTk.PhotoImage(load)


#Holkar Stadium
load = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\python\\Stadium\\Holkar Stadium.jpg")
load = load.resize((550, 270))
Holkar_Stadium= ImageTk.PhotoImage(load)

#MCAS
load = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\python\\Stadium\\MCAS.jpg")
load = load.resize((550, 270))
MCAS = ImageTk.PhotoImage(load)
#Feroz Shah Kotla Stadium
load = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\python\\Stadium\\Feroz Shah Kotla Stadium.jpg")
load = load.resize((550, 270))
Feroz_Shah_Kotla_Stadium = ImageTk.PhotoImage(load)


#Shaheed Veer Narayan Singh International Cricket Stadium
load = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\python\\Stadium\\Shaheed Veer Narayan Singh International Cricket Stadium.jpg")
load = load.resize((550, 270))
Narendra_Modi_Stadium = ImageTk.PhotoImage(load)


#Narendra Modi Stadium
load = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\python\\Stadium\\Narendra Modi Stadium.jpg")
load = load.resize((550, 270))
Shaheed_Veer_Stadium = ImageTk.PhotoImage(load)

 
#DY_Patil_Stadium 
load = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\python\\Stadium\\DY Patil Stadium.jpg")
load = load.resize((550, 270))
DY_Patil_Stadium = ImageTk.PhotoImage(load)
 
#eden_gardens_stadium
load = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\python\\Stadium\\eden gardens stadium.jpg")
load = load.resize((550, 270))
eden_gardens_stadium = ImageTk.PhotoImage(load)

a = Image.open("C:\\Users\\Ashish Ruke\\OneDrive\\Desktop\\python\\basic image\\22.jpg")
a = a.resize((1100, 350))
coin = ImageTk.PhotoImage(a)
i = Label(root, image=coin)
i.config(bg='blue',fg='white')
i.place(x=22,y=0,width=1100,height=400)    

st=Button(root,text="select",command=select)
st.config(bg='red',fg='blue')
st.place(x=490,y=340,width= 140,height=30)

Stadium=ttk.Combobox(root,value=("DY Patil Stadium","eden gardens stadium","Narendra Modi Stadium","Shaheed Veer Narayan Singh International Cricket Stadium","Feroz Shah Kotla Stadium","MCAS","Holkar Stadium","HPCA Stadium","M. Chinnaswamy Stadium","Raipur International Cricket Stadium","Rajiv Gandhi International Cricket Stadium","Wankhede Stadium" ),font=("time new roman",10,"bold"),justify=CENTER,state='readonly')
Stadium.place(x=480,y=32,width= 200,height=30)
Stadium.set("select your Stadium")

p=IntVar()
r=Label(root,text="Choose your Pitch")
r.config(bg='red',fg='white',font=("time new roman",11,"bold"))
r1= Radiobutton(root, text="Green Pitch",value=0,variable = p)
r2= Radiobutton(root, text="Dusty Pitch",value=1,variable = p)
r3= Radiobutton(root, text="Dead Pitch",value=2,variable = p)
r1.config(bg='yellow',fg='green',font=("time new roman",12,"bold"))
r2.config(bg='yellow',fg='green',font=("time new roman",12,"bold"))
r3.config(bg='yellow',fg='green',font=("time new roman",12,"bold"))
r1.place(x=170,y=500,width= 140,height=30)
r3.place(x=458,y=500,width= 140,height=30)
r2.place(x=315,y=500,width= 140,height=30)
r.place(x=0,y=500,width= 169,height=30)

m=IntVar()
n=Label(root,text="Choose the playing time")
n.config(bg='red',fg='white',font=("time new roman",11,"bold"))
n1= Radiobutton(root, text="Evening",value=0,variable = m)
n2= Radiobutton(root, text="Afternoon",value=1,variable = m)
n3= Radiobutton(root, text="Night",value=2,variable = m)
n1.config(bg='yellow',fg='green',font=("time new roman",12,"bold"))
n2.config(bg='yellow',fg='green',font=("time new roman",12,"bold"))
n3.config(bg='yellow',fg='green',font=("time new roman",12,"bold"))
n1.place(x=170,y=420,width= 140,height=30)
n2.place(x=290,y=420,width= 140,height=30)
n3.place(x=430,y=420,width= 140,height=30)
n.place(x=0,y=420,width= 169,height=30)

b=IntVar()
v=Label(root,text="Choose weather")
v1= Radiobutton(root, text="Clear",value=0,variable = b)
v2= Radiobutton(root, text="Cloudy",value=1,variable = b)
v1.config(bg='yellow',fg='green',font=("time new roman",12,"bold"))
v2.config(bg='yellow',fg='green',font=("time new roman",12,"bold"))
v.config(bg='red',fg='white',font=("time new roman",11,"bold"))
v1.place(x=170,y=462,width= 140,height=30)
v2.place(x=290,y=462,width= 140,height=30)
v.place(x=0,y=462,width= 169,height=30)

btn=Button(root,text="confirm",command=ok)
btn.place(x=440,y=552,width= 140,height=30)



root.mainloop()

