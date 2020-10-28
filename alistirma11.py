a=125
b=200
c=350
sayilar=[]
for x in range (1,125):
    if a%x == b%x and a%x == c%x:
        sayilar.append(x)

print(max(sayilar))
        
    
        
        
        
