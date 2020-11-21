#çarpımları 12121 olacak. a*b=12121 ve mutlak değer a-b minimum olacak ,o zaman mesela 3 basamak ve 2 basamaklı sayılara bakalım
xler=[]
yler=[]
farklar=[]
for x in range(10,1000):
    for y in range(10,1000):
        if x*y == 121212:
            xler.append(x)
            yler.append(y)
            farklar.append(abs(x-y))
            m=farklar.index(min(farklar))
print(xler[m],yler[m])

            


            
            
            
           
            



