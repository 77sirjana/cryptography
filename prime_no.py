def check_prime(num):
    if(num>1):
        for i in range(2,int(num/2)+1):
            if(num%i==0):
                return False
        return True
print(check_prime(11))