
for x in range(1,10):
    x=str(x)
    if int(x[0]) < 9:
        print(int(x),end=" ")

for x in range(10,100):
    x=str(x)
    if int(x[0]) + int(x[1]) < 9:
        print(int(x),end=" ")
for x in range(100,1000):
    x=str(x)
    if int(x[0]) + int(x[1]) + int(x[2]) < 9:
        print(int(x),end=" ")
