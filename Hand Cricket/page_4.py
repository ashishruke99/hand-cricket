import page_3
import page_2
from tkinter import *
zzz=page_2.tnv1.get()
           
team = Tk()
team.title("----------CRICKET 🏏❤----------")
team.maxsize(width=950,height=700)
team.minsize(width=950,height=700)
leftList = Listbox(team, width=40, height=70, bg="skyblue",borderwidth=10,font=("CUTE",12))
rightList = Listbox(team, width=40, height=70, bg="skyblue",borderwidth=10,font=("bold",12))
leftList.pack()

mi = ["Rohit Sharma(C) ,", "Ramandeep Singh ,", "Rahul Buddhi ,", "Tilak Varma ,", "Aryan Juyal ,",
      "Ishan Kishan ,", "Tristan Stubbs ,", "Tim David ,", "Sanjay Yadav ,", "Akash Madhwal ,", "Riley Meredith ,",
      "Jofra Archer ,", "Daniel Sams ,", "Mayank Markande ,", "Jaydev Unadkat ,"]
DC=["David Warner", "Sarfaraz Khan", "Mitchell Marsh", "Rishabh Pant (c & wk)", "Lalit Yadav", "Rovman Powell", "Axar Patel", "Shardul Thakur", "Kuldeep Yadav", "Anrich Nortje", "Khaleel Ahmed","Srikar Bharat", "Chetan Sakariya", "Mandeep Singh", "Tim Seifert", "Lungi Ngidi", "Ripal Patel", "Yash Dhull", "Mustafizur Rahman", "Ashwin Hebbar", "Praveen Dubey", "Kamlesh Nagarkoti", "Vicky Ostwal"]
SRH=["Abhishek Sharma", "Priyam Garg", "Kane Williamson (c)", "Rahul Tripathi", "Aiden Markram", "Nicholas Pooran (wk)", "Washington Sundar", "Bhuvneshwar Kumar", "Fazalhaq Farooqi", "Umran Malik", "T Natarajan","Sean Abbott", "Ravikumar Samarth"," Shreyas Gopal", "Jagadeesha Suchith", "Glenn Phillips", "Vishnu Vinod", "Kartik Tyagi", "Romario Shepherd", "Abdul Samad", "Sushant Mishra", "Shashank Singh","Marco Jansen"]
KKR=["Venkatesh Iyer", "Ajinkya Rahane", "Shreyas Iyer (c)", "Nitish Rana", "Sam Billings", "Andre Russell", "Sunil Narine", "Sheldon Jackson (wk)", "Umesh Yadav", "Shivam Mavi", "Varun Chakaravarthy", "Chamika Karunaratne", "Rasikh Salam", "Mohammad Nabi", "Baba Indrajith", "Rinku Singh", "Tim Southee", "Anukul Roy", "Pratham Singh", "Abhijeet Tomar", "Aman Hakim Khan", "Ashok Sharma", "Ramesh Kumar"]
PBKS=["Mayank Agarwal (c)", "Shikhar Dhawan", "Bhanuka Rajapaksa", "Liam Livingstone", "Shahrukh Khan", "Jitesh Sharma (wk)", "Odean Smith", "Arshdeep Singh", "Kagiso Rabada", "Rahul Chahar", "Vaibhav Arora", "Benny Howell", "Sandeep Sharma", "Rishi Dhawan", "Baltej Singh", "Writtick Chatterjee", "Prerak Mankad", "Ishan Porel", "Atharva Taide", "Jonny Bairstow", "Prabhsimran Singh", "Ansh Patel", "Raj Bawa", "Harpreet Brar"]
RCB = ["Faf Du Plessis", "Akash Deep", "Aneeshwar Gautam", "Anuj Rawat", "Chama Milind", "David Willey", "Dinesh Karthik", "Finn Allen", "Glenn Maxwell", "Harshal Patel", "Jason Behrendorff", "Josh Hazlewood", "Karn Sharma",  "Luvnith Sisodia", "Mahipal Lomror", "Mohammed Siraj", "Rajat Patidar", "Shahbaz Ahmed", "Sherfane Rutherford", "Siddhart Kaul", "Suyash Prabhudedssai", "Virat Kohli", "Wanindu Hasaranga"]
LSG = ["Lokesh Rahul", "Ankit Rajpoot", "Avesh Khan", "Ayush Badoni", "Dushmantha Chameera", "Evin Lewis", "Jason Holder", "Karan Sharma", "Krishnappa Gowtham", "Krunal Pandya", "Kyle Mayers", "Manan Vohra", "Manish Pandey", "Marcus Stoinis", "Mark Wood", "Mayank Yadav", "Mohsin Khan", "Quinton de Kock", "Ravi Bishnoi", "Shahbaz Nadeem"]
GT = ["Hardik Pandya", "Abhinav Manohar", "Alzarri Joseph", "B Sai Sudarshan", "Darshan Nalkande", "David Miller", "Dominic Drakes", "Gurkeerat Singh Mann", "Jayant Yadav", "Lockie Ferguson", "Matthew Wade", "Mohammed Shami", "Noor Ahmad", "Pradeep Sangwan", "Rahul Tewatiya", "Rashid Khan", "Ravisrinivasan Sai Kishore", "Shubman Gill", "Varun Aaron", "Vijay Shankar", "Wriddhiman Saha", "Yash Dayal"]
RR = ["Sanju Samson", "Anunay Singh", "Corbin Bosch", "Daryl Mitchell", "Devdutt Padikkal", "Dhruv Chand Jurel", "Jimmy Neesham", "Jos Buttler", "Karun Nair", "KC Cariappa", "Kuldeep Sen", "Kuldip Yadav", "Nathan Courtlernile", "Navdeep Saini", "Obed McCoy", "Prasidh Krishna", "Rassie Van der Dussen", "Ravichandran Ashwin", "Riyan Prayag", "Shimron Hetmyer", "Shubham Garhwal", "Tejas Baroka", "Trent Boult", "Yashasvi Jaiswal", "Yuzendra Chahal"]
CSK = ["Ravindra Jadeja", "MS Dhoni", "Moeen Ali", "Ruturaj Gaikwad", "Dwayne Bravo" , "Ambati Rayudu", "Dwaine Pretorius", "Mitchell Santner" , "Subhranshu Senapati", "Adam Milne", "Mukesh Choudhary", "Prashant Solanki", "C Hari Nishaanth", "N Jagadeesan", "Chris Jordan", "K Bhagath Varma", "Robin Uthappa", "Deepak Chahar", "KM Asif", "Tushar Deshpande", "KM Asif", "Shivam Dube", "Maheesh Theekshana", "Rajvardhan Hangargekar", "Samarjeet Singh", "Devon Conway" ]
if zzz =="MI":
    for i in mi:
        leftList.insert(END,i)
elif zzz =="DC":
    for i in DC:
        leftList.insert(END,i)
elif zzz =="SRH":
    for i in SRH:
        leftList.insert(END,i)
elif zzz =="KKR":
    for i in KKR:
        leftList.insert(END,i)
elif zzz =="PK":
    for i in PBKS:
        leftList.insert(END,i)
elif zzz =="RCB":
    for i in RCB:
        leftList.insert(END,i)
elif zzz =="LSG":
    for i in LSG:
        leftList.insert(END,i)
elif zzz =="GT":
    for i in GT:
        leftList.insert(END,i)
elif zzz =="CSK":
    for i in CSK:
        leftList.insert(END,i)
elif zzz =="RR":
    for i in RR:
        leftList.insert(END,i)

def moveTo(fromList, toList):
    indexList = fromList.curselection()
    if indexList:
        index = indexList[0]
        val = fromList.get(index)
        fromList.delete(index)
        toList.insert(END, val)
      

frame = Frame(team)
button1= Button (frame, text="Playing", command= lambda: moveTo(leftList, rightList),bg="green",fg="red",borderwidth=5,border=10,font="BOLD",anchor=E)
button2= Button (frame, text="Reverse", command= lambda: moveTo(rightList, leftList),bg="red",fg="green",borderwidth=5,border=10,font="BOLD",anchor=E)

button1.pack(side="top")
button2.pack(side="bottom")

leftList.pack(side="left")
frame.pack(side="left")
rightList.pack(side="right")
QuitButton=Button(team,text="ok",command=quit,width=8,borderwidth=5,bg="black",fg="white",border=10,font="BOLD",anchor=W)
QuitButton.pack()
                                                                     
team.mainloop()

