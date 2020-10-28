
for x in range(10000,100000):
    for y in range(2,x):

        if x%y == 0:
            break

    else:
        print(x, end=" ")
