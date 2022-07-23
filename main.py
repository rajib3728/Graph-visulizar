
from tkinter import *
from matplotlib import pyplot as plt
from matplotlib import style
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import socket
import webbrowser
def grp():
    l=t1.get(1.0, "end-1c")
    if l=="":
        messagebox.showinfo("info","Please write code then click view")
    else:
        s=l.split()
        a=len(s)
        #print(a)
        m=clicked.get()
        
        #print(m)
        if a==4  and  m!="Pie plot":
            b=s[1]
            c=s[3]
            #print(type(b))
            #print(c[0])
            #print(b[len(b)-1])
            #print(c[len(c)-1])
            if b[0]=="[" and c[0]=="[" and b[len(b)-1]=="]" and c[len(c)-1]=="]":
                style.use("ggplot")
                b1=b.replace("[","")
                b2=b1.replace("]","")
                b3=b2.split(",")
                c1=c.replace("[","")
                c2=c1.replace("]","")
                c3=c2.split(",")
                m1=[]
                m2=[]
                for i in b3:
                    if i!="[" and i!="]" and i!=",":
                        m1.append(int(i))
                for i in c3:
                    if i!="[" and i!="]" and i!=",":
                        m2.append(int(i))
                if clicked.get()=="Line plot":
                    plt.plot(m1,m2)
                    plt.title("Line plot")
                    plt.xlabel(s[0])
                    plt.ylabel(s[2])
                    plt.show()
                elif clicked.get()=="Bar plot":
                    plt.bar(m1,m2)
                    plt.title("Bar plot")
                    plt.xlabel(s[0])
                    plt.ylabel(s[2])
                    plt.show()
                elif clicked.get()=="Scatter plot":
                    plt.scatter(m1,m2)
                    plt.title("Scatter plot")
                    plt.xlabel(s[0])
                    plt.ylabel(s[2])
                    plt.show()
                elif clicked.get()=="Histogram plot":
                    plt.hist(m1,m2)
                    plt.title("Histogram plot")
                    plt.xlabel(s[0])
                    plt.ylabel(s[2])
                    plt.show()
            else:
                messagebox.showerror("error","Wrong syntax or wrong select")
        elif a==2 and m=="Pie plot":
            p1=s[1].replace("[","")
            p2=p1.replace("]","")
            d=p2.split(",")
            #print(d)
            e=len(s[1])
            m3=[]
            #p=list(d)
            for i in d:
                
                m3.append(int(i))
            #print(m3)
            if clicked.get()=="Pie plot" and s[1][0]=="[" and s[1][len(s[1])-1]=="]":
                plt.style.use("fivethirtyeight")
                if sum(m3)==100:
                    plt.pie(m3)
                    plt.title("Pie plot")
                    #plt.tight_layout()
                    plt.show()
                else:
                        messagebox.showinfo("info","All the number sum should be 100")
            else:
                    messagebox.showerror("error","wrong syntax or wrong select")
         
        elif clicked.get()=="Stack plot" and a>4 and a%2!=0 and s[a-1]=="stack":
                if a==5:
                    q1=s[1].replace("[","")
                    
                    q2=q1.replace("]","")
                    q3=q2.split(",")
                    
                    q4=[]
                    for i in q3:
                        q4.append(int(i))
                    
                    q5=s[3].replace("[","")
                    q6=q5.replace("]","")
                    q7=q6.split(",")
                    q8=[]
                    for i in q7:
                        q8.append(int(i))
                    li1=[]
                    li2=[]

                    for i in range(len(s)):
                        if i%2==0:
                            li1.append(s[i])
                        else:
                            li2.append(s[i])
                    labels=[]       
                    for i in range(len(li1)):
                        if i!=1:
                            labels.append(li1[i])
                    plt.style.use("fivethirtyeight")
               
                    plt.stackplot(q4,q8,labels=labels)
                    plt.legend()
                    plt.show()   
                elif a==7: 
                    q1=s[1].replace("[","")
                    
                    q2=q1.replace("]","")
                    q3=q2.split(",")
                    
                    q4=[]
                    for i in q3:
                        q4.append(int(i))
                    
                    q5=s[3].replace("[","")
                    q6=q5.replace("]","")
                    q7=q6.split(",")
                    q8=[]
                    for i in q7:
                        q8.append(int(i))

                    q9=s[5].replace("[","")
                    q10=q9.replace("]","")
                    q11=q10.split(",")
                    q12=[]
                    for i in q11:
                        q12.append(int(i))
                    li1=[]
                    li2=[]

                    for i in range(len(s)):
                        if i%2==0:
                            li1.append(s[i])
                        else:
                            li2.append(s[i])
                    labels=[]       
                    for i in range(len(li1)):
                        if i!=1:
                            labels.append(li1[i])
                    plt.style.use("fivethirtyeight")
               
                    plt.stackplot(q4,q8,q12,labels=labels)
                    plt.legend()
                    plt.show() 
                elif a==9:
                    q1=s[1].replace("[","")
                    print(q1)
                    q2=q1.replace("]","")
                    q3=q2.split(",")
                    print(q3)
                    q4=[]
                    for i in q3:
                        q4.append(int(i))
                    
                    q5=s[3].replace("[","")
                    q6=q5.replace("]","")
                    q7=q6.split(",")
                    q8=[]
                    for i in q7:
                        q8.append(int(i))

                    q9=s[5].replace("[","")
                    q10=q9.replace("]","")
                    q11=q10.split(",")
                    q12=[]
                    for i in q11:
                        q12.append(int(i))

                    q13=s[7].replace("[","")
                    q14=q13.replace("]","")
                    q15=q14.split(",")
                    q16=[]
                    for i in q15:
                        q16.append(int(i))
                    li1=[]
                    li2=[]

                    for i in range(len(s)):
                        if i%2==0:
                            li1.append(s[i])
                        else:
                            li2.append(s[i])
                    labels=[]       
                    for i in range(len(li1)):
                        if i!=1:
                            labels.append(li1[i])
                    plt.style.use("fivethirtyeight")
               
                    plt.stackplot(q4,q8,q12,q16,labels=labels)
                    plt.legend()
                    plt.show()
                elif a==11:
                    q1=s[1].replace("[","")
                    print(q1)
                    q2=q1.replace("]","")
                    q3=q2.split(",")
                    print(q3)
                    q4=[]
                    for i in q3:
                        q4.append(int(i))
                    
                    q5=s[3].replace("[","")
                    q6=q5.replace("]","")
                    q7=q6.split(",")
                    q8=[]
                    for i in q7:
                        q8.append(int(i))

                    q9=s[5].replace("[","")
                    q10=q9.replace("]","")
                    q11=q10.split(",")
                    q12=[]
                    for i in q11:
                        q12.append(int(i))

                    q13=s[7].replace("[","")
                    q14=q13.replace("]","")
                    q15=q14.split(",")
                    q16=[]
                    for i in q15:
                        q16.append(int(i))

                    q17=s[9].replace("[","")
                    q18=q17.replace("]","")
                    q19=q18.split(",")
                    q20=[]
                    for i in q19:
                        q20.append(int(i))
                    li1=[]
                    li2=[]

                    for i in range(len(s)):
                        if i%2==0:
                            li1.append(s[i])
                        else:
                            li2.append(s[i])
                    labels=[]       
                    for i in range(len(li1)):
                        if i!=1:
                            labels.append(li1[i])
                    plt.style.use("fivethirtyeight")
               
                    plt.stackplot(q4,q8,q12,q16,q20,labels=labels)
                    plt.legend()
                    plt.show()
                else:
                    messagebox.showinfo("Info"," sorry! You can plot upto 4 for now")
         
        else:
            messagebox.showerror("error","wrong syntax!")
          
def help():
    messagebox.showinfo("Info",'''Here various type of plot are present ,you have to select the type then you have to click the view button.NOTE:
    if you take screen shot it will go to E drive''')
def ss():
    import pyautogui
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('E:\your_screenshot.png')  
    messagebox.showinfo("info","screen shot ✔ check e drive")
def tutorial():
    def test():
        try:
            socket.create_connection(("google.com",80))
            return True
        except OSError:
            return False
    k=test()
    if k:
        webbrowser.open("index.html")
    else:
        messagebox.showerror("error","Please check internet connection!")
def clr():
    t1.delete("1.0","end")
    
root=Tk()
photo = ImageTk.PhotoImage(file = "./Pic/logo.jpg")
root.iconphoto(False, photo)
root.geometry("1600x900")
root.configure(bg="grey")
root.title("Graph Visulizar")

btn1=Button(root,text="View",command=grp,bg="lightgreen")
btn1.place(x=1470,y=10)
btn2=Button(root,text="help",command=help,padx=18,bg="grey")
btn2.place(x=120,y=40)
btn3=Button(root,text="screenshot",command=ss,bg="grey")
btn3.place(x=200,y=40)
btn4=Button(root,text="click",bg="grey",command=tutorial,padx=5)
btn4.place(x=280,y=40)
btn5=Button(root,text="Clear",bg="grey",command=clr)
btn5.place(x=333,y=40)
l1=Label(root,text="Select plot",fg="black",bg="grey")
l1.place(x=10,y=10)
l2=Label(root,text="Need help",bg="grey",fg="black")
l2.place(x=120,y=10)
l3=Label(root,text="Take snapshot" ,fg="black",bg="grey")
l3.place(x=200,y=10)
l4=Label(root,text="Tutorial",bg="grey")
l4.place(x=280,y=10)
l5=Label(root,text="Clear screen",fg="black",bg="grey")
l5.place(x=333,y=10)
options = [
    "Line plot",
    "Bar plot",
    "Scatter plot",
    "Pie plot",
    "Histogram plot",
    "Stack plot",
] 
# datatype of menu text
clicked =StringVar()
# initial menu text
clicked.set( "Line plot" )
drop =OptionMenu( root , clicked ,*options )
drop.place(x=10,y=40)
f1=Frame(root,width=1500,height=650,bg="grey")
f1.place(x=20,y=100)
t1=Text(f1,width=1000,height=100)
t1.place(x=0,y=0)
root.mainloop()