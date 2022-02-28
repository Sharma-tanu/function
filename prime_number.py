
num=int(input("enter a number: "))

def prime(num):
    c=0
    if num==1 or num==0:
        print(num, "is a prime number")
    for i in range(2,num+1):
        if num%i==0:
            c=c+1
    if c==1:
         print(num,"is a prime number")    
    else:   
        print(num,"is not a prime number")
prime(num)