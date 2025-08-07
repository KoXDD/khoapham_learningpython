#first part


a=str('Thirty') 
b=str('Days')                         #1
c=str('Of') 
d=str('Python')
e='%s %s %s %s' %(a,b,c,d)

del a,b,c,d,e


a='Coding'
b='For'                    #2
c='All'
d='%s %s %s' %(a,b,c)
print(d)

company=d  #3
print(company)      #4
print(len(company)) #5
print(company.upper()+"\n"+company.lower()) #6&7

print(d.capitalize())
print(d.title())              #8
print(d.swapcase())


print(d[0:7]) #9

res=d.find("Coding")              #10
if res != -1:
    print("\"coding\" da duoc tim thay trong",res)
else:
    print('ko tim thay tu \"coding\"')
del res,company,a,b,c,d

#second part

list_empt=list()            #1

list1=[ 'item1' , 12, True, 'aaaa', 'bbb' ]               #2

print(len(list1))       #3

print(list1[0])        #4
print(list1[2])
print(list1[4])

mixed_data_types = ['name', 'age', 'height', 'marital', 'status', 'address']  #5

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"] #6

print(it_companies) #7


print(len(it_companies)) #8


tdgiua= len(it_companies) // 2            #9
print(it_companies[0], it_companies[tdgiua], it_companies[-1])

it_companies[0]="Electronic Art"
print(it_companies)  #10

it_companies.append("ContyCoPhanDienTuNinjaForSale")   #11

it_companies.insert(tdgiua,"CongtyITnuquyenvaunghonguoidothai")  #12

print(it_companies[0].upper)    #13

"#;&nbsp; ".join(it_companies)    #14

if "Ebisoft" in it_companies:    #15
    print("Cong ty Ebisoft co a trong cac tap toan tren")
else:
    print("Ebisoft khong co o trong cac tap doan tren")

it_companies.sort()      #16
print(it_companies)

it_companies.reverse()    #17
print(it_companies)

one = it_companies[:3]    #18
print(one)

two= it_companies[-3:]    #19
print(two)

abc=(len(it_companies))    #20
if abc % 2 != 0:
    m=it_companies[tdgiua+1]
else:
    m=it_companies[tdgiua]
print(m)
del m, it_companies, tdgiua, one, two, abc


#21
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = min(ages)
max_age = max(ages)
print("age dc sort", ages)
print("age min", min_age)
print("age max", max_age)
ages.append(max_age)
ages.append(min_age)
ages.sort()
n=len(ages)
if n%2 == 0:
    median = (ages[n//2-1] + ages[n//2])/2
else:
    median = ages[n//2]
print('median age la',median)

average=sum(ages)/len(ages)
print("do tuoi trung binh",average)

rangeage=max_age-min_age
print("age range la",rangeage)

qwe = abs(min_age - average)
asd = abs(max_age - average)
print("abs min toi average:", qwe)
print("abs max toi average:", asd)
if qwe >= asd:
    print("gia tri min-a lon hon gia tri max-a")
elif qwe == asd:
    print("ca hai gia tri co khoang cach bang nhau")
else:
    print("gia tri max-a lon hon gia tri min-a")
del ages, average, asd, qwe, rangeage, min_age, max_age, median, n

#third part
dog={}         #1

dog['name']='Buddy'            #2
dog['color']='Brown'
dog['breed']='Labrador'
dog['legs']=4
dog['age']=5

student = {                    #3
    'first_name': 'Khoa',
    'last_name': 'Pham',
    'gender': 'Nam',
    'age': 69,
    'marital_status': 'Polyamory',
    'skills': ['being bullied', 'self-harm'],
    'country': 'VN',
    'city': 'TP Cao Bang',
    'address': '123 Doi Mat'
}

print("Do dai cua tu dien:", len(student))        #4

sksk = student['skills']
print("Skills:",sksk)
print("kieu du lieu cua skills", type(sksk))          #5

student['skills'].extend(['an', 'luoi'])          #6

values = list(student.values())        #8
print("gia tri dict:", values)


items=list(student.items())       #9

del student['marital_status']       #10

del dog           #11
