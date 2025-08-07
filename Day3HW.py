#Day 3 Homework


age=int(15) #1
height=float(165) #2
co_numb = 1j #3
print("complex number: ",co_numb)


print("Nhap chieu dai base cua hinh tam giac: ") #4
a = int(input())
print("Nhap chieu dai height cua hinh tam giac: ")
b = int(input())
dt=a*b*0.5
print("dien tich tam giac da cho la:", dt)
del a,b,dt

print("Nhap chieu dai canh a: ") #5
a = int(input())
print("Nhap chieu dai canh b: ")
b = int(input())
print("Nhap chieu dai canh c: ")
c = int(input())
cv = a+b+c
qwe="Chu vi tam giac da cho"
print(qwe,"la",cv)
del a,b,c,cv,qwe

print("length: ")              #6
a = int(input())
print("width: ")
b = int(input())
perimeter=2*(a+b)
area=a*b
print("chu vi la",perimeter)
print("dien tich la",area)
del a,b,perimeter,area

pi=float(3.14)
print("radius: ")                #7
r = float(input())
area = float(r**2*pi)
dgtron = float(2*pi*r)
print("dien tich bang",area)
print("chu vi duong tron bang",dgtron)
del pi,r,area,dgtron

print("x=")                #8
x=float(input())
y=float(2*x-2)
slope1 = y
print('slope=',y)
del x,y

import math #import tv math       #9
x1=2
y1=2
x2=6
y2=10
m=(y2-y1)/(x2-x1)
slope2=m
kcach=math.sqrt((x2-x1)**2 + (y2-y1)**2)
print('Slope=',m)
print('Kcach euclid=',kcach)
del x1,y1,x2,y2,m,kcach

if slope1==slope2:
    print('slope tai 2 task bang nhau')                #10
else:
    if slope1>=slope2:
        print('slope o task 8 lon hon slope o task 9')
    else:
        print('slope o task 9 lon hon slope o task 8')
del slope1, slope2


print('Nhap gia tri x')            #11
while True:
    x=float(input())
    y = x**2 + 6*x +9
    print('''Voi y = x^2 + 6x +9.
        Ta co y la:''',y)
    while True:
        if y == 0:
            print("Voi gia tri",x,'''
            Ta co y=''',0)
            break
        else:
            print('Voi x =',x,'''
            y se la mot so /= 0
                hay thu mot so khac''')
            ans=input("muon thu so khac ko? (y/n)")
            if ans=="n":
                break
            else:  
                continue
    break

a=len("python")    #12
b=len("dragon")
print('python co nhieu ki tu hon dragon khong?',a>b)

if "on" in "python" and "dragon":                          #13
    print('tu (on) co o trong python va dragon')
else:
    print('tu (on) khong co trong ca hai tu')              #15
del a,b

c='I hope this course is not full of jargon'      #14
if "jargon" in c:
    print ("jargon co o trong", c)

del c

a="python"
print("So ki trong python la", float(len(a)), "va", str(len(a)))      #16
del a

a=input("Chon mot so bat ki:") #17
print(float(a))
if float(a) % 2 == 0:
    print ("so da cho la so chan")
else:
    print ("so da cho la so le") 
del a

a = 7 / 3             #18
b = 2.7
b1 = int(b)
print(a, "=", b, "la", a is b1)
del a,b,b1

a='10'                       #19
b=10
print(a,'va',b,'la',type(a) is type(b))
del a,b

a=9.8
a1=int(a)
b=10
print(a,"=",b,"is",a1 is b) #20
del a, a1, b

print('Enter hours')
a=input()
print('Enter rate per hour')            #21
b=input()
mul=int(a)*int(b)
print('Your weekly earning is:',mul)
del mul,a,b

print('The number of year you have live is')
a=int(input())                                         #22
b= a * (3153600000/100)
print('You have lived for',b,'seconds')
del a,b

print('''               
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
      ''')               #23


