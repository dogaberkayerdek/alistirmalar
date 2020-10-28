
sayi =int(input("3 ya da 4 basamaklı bir sayı yazınız: "))

sayi=str(sayi)

if len(sayi) == 3:
    if sayi[0] == sayi[2]:
        print("Girilen 3 basamaklı sayı palindromik sayıdır")
    else:
            print("Girilen 3 basamaklı sayı palindromik sayı değildir")

if len(sayi) == 4:
    if sayi[0] == sayi[3] and sayi[1] ==sayi[2]:
        print("Girilen 4 basamaklı sayı palindromik sayıdır")
    else:
            print("Girilen 4 basamaklı sayı palindromik sayı değildir")
