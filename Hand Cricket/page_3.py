
from tkinter import*
from tkinter import ttk
import webbrowser

import page_2

root=Tk()
root.title("selection buttion")
root.geometry("220x90")
root.configure(bg='black')

def select2():
    root.quit()



def select1():
    qa=page_2.tnv1.get()
    if qa=="MI":
       
       webbrowser.open('https://www.mykhel.com/cricket/ipl-2022-mumbai-squad-tp62-s4/')

    elif qa=="RCB":
         webbrowser.open('https://www.mykhel.com/cricket/ipl-2022-bangalore-squad-tp57-s4/')

    elif qa=="RR":
         webbrowser.open('https://www.mykhel.com/cricket/ipl-2022-rajasthan-squad-tp64-s4/')     

    elif qa=="KKR":
         webbrowser.open('https://www.mykhel.com/cricket/ipl-2022-kolkata-squad-tp61-s4/')      
   
    elif qa=="CSK":
         webbrowser.open('https://www.mykhel.com/cricket/ipl-2022-chennai-squad-tp58-s4/')

    elif qa=="DC":
         webbrowser.open('https://www.mykhel.com/cricket/ipl-2022-delhi-squad-tp64-s4/')
    
    elif qa=="SRH":
         webbrowser.open('https://www.mykhel.com/cricket/ipl-2022-hyderabad-squad-tp64-s4/')
    
    elif qa=="PBK":
         webbrowser.open('https://www.mykhel.com/cricket/ipl-2022-punjab-squad-tp64-s4/')
    
    elif qa=="GT":
         webbrowser.open('https://www.mykhel.com/cricket/ipl-2022-gujarat-squad-tp64-s4/')

    elif qa=="LSG":
         webbrowser.open('https://www.mykhel.com/cricket/ipl-2022-lucknow-squad-tp64-s4/')

st=Button(root,text="yes",command=select1)
st.config(bg='red',fg='blue')
st.place(x=20,y=32,width= 80,height=30)

wt=Button(root,text="no",command=select2)
wt.config(bg='red',fg='blue')
wt.place(x=90,y=32,width= 80,height=30)

label=Label(root,text="Do you want analysis of the team")
label.config(bg='black',fg='white',font=("Courier", 7))
label.place(x=10,y=0)
qa=page_2.tnv1.get()

root.mainloop()
