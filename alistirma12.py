for x in range(1900,2005):
    x=str(x)
    if int(x[0]) + int(x[1]) + int(x[2]) + int(x[3]) == 2005 - int(x):
        print(int(x))
