def eucledian(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def extended_eucledian (a,b):
    a,b,t1,t2=a,b,0,1
    while b!=0:
        q,r=a//b,a%b
        t1,t2=t2,t1-4*t2
        a,b=b,r
    return a
x=eucledian(2,5)
y=extended_eucledian(2,5)
print(f"the gcd of 2 and 5 using eucledian is {x} and gcd using extended eucledian is {y}")
        