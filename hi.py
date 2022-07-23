from matplotlib import pyplot as plt
from tkinter import *
def hi():

    l="x [10,20] y [10,20]"
    s=l.split()
    print(len(s))
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
root=Tk()
btn=Button(root,text="hi",command=hi)
btn.pack()
root.mainloop()