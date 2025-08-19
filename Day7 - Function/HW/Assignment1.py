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
        break
    except ValueError as loi: #store cai valueerror message thanh variable loi
        print("Chuong trinh da bi loi do:", loi)    
    #raise ValueError("So khong the chia cho 0") = da thay cai message valueerror kia thanh nhu print trong hinh
    #except ValueError as loi:
        #print("Chuong trinh da bi loi do:", loi) do loi o day no la cai minh da raise nen no tra ve message ko chia dc cho 0