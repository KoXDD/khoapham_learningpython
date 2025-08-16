#1
a=float(input('Nhap so thu 1:'))
b=float(input('Nhap so thu 2:'))
def add_two_numbers():
    c = a + b
    return int(c)
print("Tong hai so la",add_two_numbers())
del a,b
#2
r=float(input('Nhap ban kinh hinh tron:'))
pi=3.14
def area():
    dien_tich=r*r*pi
    return dien_tich
print("Dien tich hinh tron la:",area())
del r,pi
#3
# Write a function called add_all_nums which takes arbitrary 
# number of arguments and sums all the arguments.
#  Check if all the list items are number types. If not do give a reasonable feedback.
while True:
    a=input('Nhap so thu 1:')
    b=input('Nhap so thu 2:')
    c=input('Nhap so thu 3:')
    d=input('Nhap so thu 4:')
    if a and b and c and d == type(float) or type(int):
        def add_all_sum(a,b,c,d):
            sum = a + b + c + d
            return sum
        print("Tong cac so da cho la:",add_all_sum(a,b,c,d))
        break
    else:
        print("Cac so da nhap khong phai la cac con so, ban co muon nhap lai khong? (1 de xac nhan)")
        confirm = input()
        if confirm == 1:
            print()
        else:
            break

#4 Temperature in °C can be converted to °F using this formula:
# °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
while True:
    a = input("Hay nhap nhiet do hien tai (C)")
    if a == type(int) or a == type(float):
        def convert():
            fahrenheit = a * (9/5)
            return fahrenheit
        print("Khi doi sang do F, nhiet do la",convert())
        break
    else:
        print("So khong hop le, ban co muon nhap lai khong? (1 de tiep tuc)")
        confirm = input()
        if confirm == 1:
            continue
        else:
            break

#5 Write a function called check-season, 
# it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
while True:
    #12, 1, 2 win 345 spring 678summer 91011 autumn
    month_lst = [1,2,3,4,5,6,7,8,9,10,11,12]
    a = input()
    if a == month_lst:
        def check_season(a):
            Winter = 12,1,2
            Spring = 3,4,5
            Summer = 6,7,8
            Autumn = 9,10,11
            if a == Winter:
                return Winter
            elif a == Spring:
                return Spring
            elif a == Summer:
                return Summer
            elif a == Autumn:
                return Autumn
        print (check_season(a))
        break
    else:
        print("Thang ko hop le, vui long nhap so thang tu 1 toi 12. Ban co muon nhap lai khong (1 de dong y)")
        confirm = input()
        if confirm == 1:
            continue
        else:
            break
                