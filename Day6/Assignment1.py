#1
for i in range(11): #mac dinh bat dau tu 0, kthuc o 11
    print(i)
print('\n')
i = 0                                  
while i <= 10:
    print(i)
    i = i + 1
del i

#2
print('\n')
for i in range(10,-1,-1): #bat dau tu 10, ket thuc o -1, moi lan -1
    print(i)
print('\n')
i = 10
while i >= 0:
    print(i)
    i = i - 1
del i

#3
print('\n')
for i in range(1,8):
    print('#'*i) #nhan hoat dong cho str x int smh

#4
print('\n')
for hang_ngang in range(7): #print 7 # trong mot hang ngang tu 0 -> 6
    for hang_doc in range(7): #nested loop
        print('#',end=' ') #phai cho end=' ' khong thi python tu cach dong xuong buc ca minh
    print() #dinh newline o day nhung quen mat no tu cach dong xuong #new line 7 lan

#5
print('\n')
for i in range(11):
    print(i,"x",i,"=",i**2)

#6
print('\n')
list=['Python','Numpy','Pandas','Django','Flask']
for i in list:
    print(i)
del list

#7
print('\n')
for i in range(101):
    if i%2 == 0:
        print(i)

#8
print('\n')
for i in range(101):
    if 0 != i%2:
        print(i)

