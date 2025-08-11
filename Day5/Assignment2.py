while True:                                                     #1
    score = int(input("Hay nhap diem so cua ban"))
   
    a = 80 <= score <= 100    #may cai nay boolean het
    b = 70 <= score <= 79
    c = 60 <= score <= 69
    d = 50 <= score <= 59
    f = 0 <= score <= 49
   
    if a == True:
        print("Ban duoc diem A")
        break
    elif b == True:
        print("Ban duoc diem B")
        break
    elif c == True:
        print("Ban duoc diem C")
        break
    elif d == True:
        print("Ban duoc diem D")
        break
    elif f == True:
        print("Ban duoc diem F")
        break
    elif score < 0 or score > 100:
        print("So diem ban nhap khong hop le, vui long nhap lai")
print('\n')


while True:                                                    #2
    Month = input("Hay nhap mot thang")
    Season = {
        "Thu": ["September", "October", "November"],
        "Dong": ["December", "January", "February"],
        "Xuan": ["March", "April", "May"],
        "He": ["June", "July", "August"]
    } #tao dictionary mua va list item cua no
    tenseasontimthay = False #cai value boolean nay sau nay thay doi dc khi condition va loop gop phan
    #va neu gan cho no gia tri True thi no tuong la tim thay roi va ke ca ko nhap dung season thi no van skibidi
    for mua, thang in Season.items():  #loop ben trong
        if Month in thang:
            print(f"Mua hien tai la mua {mua.lower()}")
            tenseasontimthay = True #tim thay roii
            break #pha loop cua for .. in ..
    if tenseasontimthay: #neu tim thay (timthay = true) thi break, ko thi print else
        break
    else:
        print("Thang ban nhap khong hop le, vui long nhap lai.")


print('\n')
fruits=['banana','orange','mango','lemon']          #3
print('List hoa qua hien tai la',fruits)
while True:
    addfruit = input("Hay nhap mot loai qua")
    timthayqua = False
    for qua in fruits:
        if addfruit == qua: 
#ko dung addfruit in qua dc vi neu the ke ca chi ghi a ko thi no van cho a = banana
                print("Qua da ton tai trong list roi, vui long nhap lai")
                timthayqua = True
    if timthayqua is False:
        print("Qua khong duoc cho truoc, da them qua vao list")
        print("\n")
        print("List moi la")
        fruits.append(addfruit)
        print(fruits)
        tieptuc=int(input('Ban co muon tiep tuc them qua khong? Nhan 1 de ket thuc hoac bat ki so nao khac de tiep thuc them'))
        if tieptuc == 1:
            break
        else:
            continue

        
        