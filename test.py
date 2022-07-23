from matplotlib import pyplot as plt
x="height [10,20] weight [30,40] strength [50,60]"
#y=len(x)
#print(y)
s=x.split()
print(len(s))
l1=[]
l2=[]
for i in range(len(s)):
    if i%2==0:
        l1.append(s[i])
    else:
        l2.append(s[i])
print(l1)
print(l2)
bye=[]
for i in range(len(l2)):
    a=l2[i]
    m=a.replace("[","")
    n=m.replace("]","")
    l=n.split(",")
    print(l)
    hi=[]
    for i in l:
        hi.append(int(i))
    bye.append(hi)
    print(hi)
print(bye)
labels=[]
for i in range(len(l1)):
    if i!=1:
        labels.append(l1[i])
print(labels)
plt.style.use("fivethirtyeight")

li1=[10, 20]
li2=[10, 20]
plt.stackplot(li1,li2,labels=labels)
plt.legend()
plt.show()
