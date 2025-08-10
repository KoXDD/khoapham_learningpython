a=int(input("Nhap tuoi ban:"))        #1
if a >= 18:
    print("Ban da du tuoi hoc lai xe")
else:
    b = float(18 - a)
    print("Ban can doi",b,"nam nua de hoc lai xe")


tuoi_cua_minh = 15                            #2
if a > tuoi_cua_minh:
    minus = int(a - tuoi_cua_minh)
    print("Ban hon minh",minus,"tuoi")
elif a < tuoi_cua_minh:
    minus = int(tuoi_cua_minh - a)
    print("Ban kem minh",minus,"tuoi")
else:
    print("Minh va ban bang tuoi nhau")


so1=float(input("Nhap so thu nhat"))            #3
hon= "lon hon"
so2=float(input("Nhap so thu hai"))
if so1 > so2:
    print(so1, hon, so2)
elif so2 > so1:
    print(so2, hon, so1)
else:
    print("so",so1,"va","so",so2,"bang nhau")
