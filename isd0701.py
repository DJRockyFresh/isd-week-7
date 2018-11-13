pi = 0
n = 0

while n < 1000:
    pi = pi + ((-1)**n * 4)/(2*n+1)
    print ("n: ", n, ";pi: ", pi)
    n = n + 1
print (pi)

