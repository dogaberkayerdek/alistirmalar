
sayi = int(input("Bir sayı yazınız: "))


if sayi < 0:
    print("Pozitif bir sayı yazınız")
    sayi = int(input("Bir sayi yazınız: "))

if sayi == 0 or sayi == 1:
    print("Yazılan sayi asal sayi değildir")

if sayi == 2:
    print("Yazılan sayi asal sayidir")

for x in range(2,sayi):
        if sayi % x == 0:
            print("asal sayı değildir")
            break
        else:
            print("asal sayıdır")
            break
        
