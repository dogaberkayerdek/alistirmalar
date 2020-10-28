#çarpımları 12121 olacak. a*b=12121 ve mutlak değer a-b minimum olacak ,o zaman mesela 3 basamak ve 2 basamaklı sayılara bakalım
sayilar=[]
for x in range(10,1000):
    for y in range(10,1000):
        if x*y == 12121:
            sayilar.append(abs(x-y))

print(min(sayilar))
                    
            



