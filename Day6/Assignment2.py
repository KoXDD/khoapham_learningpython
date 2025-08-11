#1
a = 0
for i in range(101):
    a += i
print("Tong tat ca cac so tu 0 toi 100 la",a) #neu de cung hang thi no loop chu ko chi in ra 5050
del a

#2
a = 0
b = 0
for i in range(101):
    if i % 2 == 0:
        a += i
    elif i % 2 != 0:
        b += i
print("Tong tat ca cac so chan tu 0 toi 100 la",a)
print("Tong tat ca cac so chan tu 0 toi 100 la",b)

