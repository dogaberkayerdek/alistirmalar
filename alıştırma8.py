k=0
for x in range(100,1000,2):
        x=str(x)
        if x[0] == x[1] or x[0] == x[2] or x[1] == x[2]:
            k+=1
print(k)
            
