#ASSIGNMENT 1
#1question
a=int(input("enter first no"))
b=int(input("enter the second no"))
c=int(input("enter the third no"))
print("average of three no",(a+b+c)/3)

#2 question
gr=int(input("enter the gross income"))
dp=int(input("enter the no of dependents"))
tax=gr-10000-(3000*dp)
taxp=tax*0.20
print(taxp)

#3 question
sec=int(input("enter the seconds to convert"))
m=sec//60
r=sec%60
print("no. of minutes =",m)
print("no. of seconds=",r)

#4 question
h=[25,'25',25.0]
p=[]
su=0
for i in h:
    con=int(i)    
    p.append(con)
for j in p:
    su=su+j
v=str(su)
print(v)
print(type(v))

#5 question
import math as m
for i in range(0,346,15):
    s=m.radians(i)
    print(round(m.sin(s),4),"     ",round(m.cos(s),4))


