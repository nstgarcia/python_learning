# define a function 
#def isPrime2(num):
#
#    if num > 1:
#      
#       # check for factors
#       for i in range(2,num):
#           if (num % i) == 0:
#               return False
#
#       else:
#           return True
#           
#    # if input number is less than
#    # or equal to 1, it is not prime
#    else:
#       return False;


def isPrime(n):    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

