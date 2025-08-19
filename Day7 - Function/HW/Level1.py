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
    try: #try voi except nhu if vs else, nhung khi dung except value error thi no ko crash luon chuong trinh ma
        #bao loi nhu o duoi #try la thu chay code
        a=float(input('Nhap so thu 1:'))
        b=float(input('Nhap so thu 2:'))
        c=float(input('Nhap so thu 3:'))
        d=float(input('Nhap so thu 4:')) #dung int hoac float luon
        def add_all_sum(a,b,c,d):
            sum = a + b + c + d
            return sum
        print("Tong cac so da cho la:",add_all_sum(a,b,c,d))
        break
    except ValueError: #try and except nhu if v else nhung thay vi handle condition thi handle error
        print("Cac so da nhap khong phai la cac con so, ban co muon nhap lai khong? (1 de xac nhan)")
        confirm = input()
        if confirm != 1:
            break

#4 Temperature in °C can be converted to °F using this formula:
# °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
while True:
    a = float(input("Hay nhap nhiet do hien tai (C)"))
    try:
        def convert():
            fahrenheit = a * (9/5)
            return fahrenheit
        print("Khi doi sang do F, nhiet do la",convert())
        break
    except ValueError:
        print("So khong hop le, ban co muon nhap lai khong? (1 de tiep tuc)")
        confirm = input()
        if confirm == 1:
            continue
        else:
            break

#5 Write a function called check-season, 
# it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
while True:
    try:
        #12, 1, 2 win 345 spring 678summer 91011 autumn
        month_lst = [1,2,3,4,5,6,7,8,9,10,11,12]
        a = int(input("Nhap thang tu 1 toi 12:"))
        if a in month_lst:
            def check_season(month):
                Winter = (12,1,2)
                Spring = (3,4,5)
                Summer = (6,7,8)
                Autumn = (9,10,11)
                if month in Winter:
                    return "winter"
                elif month in Spring:
                    return "spring"
                elif month in Summer:
                    return "summer"
                elif month in Autumn:
                    return "autumn"
            print ("Thang tren thuoc mua",check_season(a))
            break
        else:
            print("Thang ko hop le, vui long nhap so thang tu 1 toi 12. Ban co muon nhap lai khong (1 de dong y)")
            confirm = input()
            if confirm != "1":
                break
    except ValueError:
        print("Thang ko hop le, vui long nhap so thang tu 1 toi 12. Ban co muon nhap lai khong (1 de dong y)")
        confirm = input()
        if confirm != "1":
            break


#6 Write a function called calculate_slope which return the slope of a linear equation (m=y2-y1/x2-x1)
while True:
    x1=float(input("Nhap x1"))
    x2=float(input("Nhap x2"))
    y1=float(input("Nhap y1"))
    y2=float(input("Nhap y2"))
    def calculate_slope(x1,x2,y1,y2):
        if x2-x1==0:
            raise ValueError("So khong the chia cho 0")
        return (y2-y1)/(x2-x1)
    try:
        print("Slope co gia tri la", calculate_slope(x1,x2,y1,y2))
        break #trying to break 
    except ValueError as loi: #store cai valueerror message thanh variable loi
        print("Chuong trinh da bi loi do:", loi)    #neu loi thi lap lai loop
    #raise ValueError("So khong the chia cho 0") = da thay cai message valueerror kia thanh nhu print trong hinh
    #except ValueError as loi:
        #print("Chuong trinh da bi loi do:", loi) do loi o day no la cai minh da raise nen no tra ve message ko chia dc cho 0


#7 Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
while True:
    import math
    a = float(input("Nhap so a:"))
    b = float(input("Nhap so b:"))
    c = float(input("Nhap so c:"))
    if a == 0:
            print("Phuong trinh bac hai khong ton tai voi a = 0")
            continue
    else:
        def solve_quaratic_eqn(a,b,c):
            delta = b**2-4*a*c
            #Nếu Δ > 0: Phương trình có hai nghiệm phân biệt (khác nhau).
                #cong thuc x = (-b ± √(b² - 4ac)) / 2a.
            #Nếu Δ = 0: Phương trình có một nghiệm kép (hai nghiệm bằng nhau).
            #   Khi delta (Δ) bằng 0, phương trình bậc hai có một nghiệm kép. Nghiệm kép này được tính bằng công thức:
            #   x = -b / 2a, 
            #   trong đó a và b là các hệ số của phương trình bậc hai. 
            #Nếu Δ < 0: Phương trình vô nghiệm (không có nghiệm thực).
            if delta > 0:
                x1 = (-b + math.sqrt(delta))/(2*a)
                x2 = (-b - math.sqrt(delta))/(2*a)
                return(x1,x2)
            elif delta == 0:
                x = -b / (2*a) 
                return(x,) #the nay thi luc nao no cung sex return la tuple chu luc thi tuple luc thi float luc thi none no messy
            elif delta < 0:
                print("Phuong trinh vo nghiem")
                return()
        ketqua=solve_quaratic_eqn(a,b,c)
        if ketqua: #o day do tuple co gia tri nen no la true
            print("Tap nghiem da cho la", ketqua)
        else: #khi xet den phuong trinh vo nghiem thi no da return mot tuple empty r "()", va empty tuple thi la False mac dinh
            print("Vo nghiem")
        break

#8 Declare a function named print_list. 
# It takes a list as a parameter and it iprints out each element of the list.


def print_list(list):
    for cacitem in list:
        print(cacitem)
print_list([1, 2, 3, 4])


#9 Declare a function named reverse_list. 
#It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(array):
    ketqua = [] #ket qua la tap rong
    for i in range(len(array)-1,-1,-1):
        ketqua.append(array[i]) #lay gia tri o index i va cho items vao list ketqua
    return ketqua
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]

#10 Declare a function named capitalize_list_items.
#  It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(list):
    ketqua = []
    for i in list:
        ketqua.append(i.capitalize())
    return ketqua
print(capitalize_list_items(["a","afw","decusnegus"]))

#11 Declare a function named add_item. It takes a list and an item parameters.
#  It returns a list with the item added at the end.
def add_item(lst,item):
    lst.append(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat')) 
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5)) 
del food_staff, numbers
#12 Declare a function named remove_item. It takes a list and an item parameters.
#  It returns a list with the item removed from it.

def remove_item(lst, item):
    lst.remove(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

#13 Declare a function named sum_of_numbers.
#  It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(number):
    sums = 0
    for i in range(number+1):
        sums += i
    return sums
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

#14 Declare a function named sum_of_odds. 
# It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(number):
    sums = 0
    for i in range(number + 1):  # co n
        if i % 2 != 0:      # check if i is odd
            sums += i
    return sums

#15 even
def sum_of_even(number):
    sums = 0
    for i in range(number + 1):  
        if i % 2 == 0:      
            sums += i
    return sums
