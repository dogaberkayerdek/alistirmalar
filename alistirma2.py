
say=0
n=1
while True :
     say = say + 1/n**2
     n=n+1

     if n == 100000 :
           pi = (6*say)**0.5
           print(pi)
           break
           
