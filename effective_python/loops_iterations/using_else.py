

a =4
b=9

for i in range(2, min(a,b)+1):
    print("testing",i)
    if a % i==0 and b % i ==0:
        print("not coprime")
        break
else:
    print("coprime")