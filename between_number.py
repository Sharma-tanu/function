# Write a Python program to generate and print a list of first and last 5
# elements where the values are square of numbers between 1 and 30 (both included). 



# def printValues():
# 	l = list()
# 	for i in range(1,21):
# 		l.append(i**2)
# 	print(l[:5])
# 	print(l[-5:])

# printValues()


# def square(a,b): 
#     l=[] 
#     for i in range(a,b+1): 
#         l.append(i*i) 
#         return(l) 
#         print(square(1,30)) 

# a="navgurukul"
# print("gu"in a)
# i=0
# while 


def values():
    list1=[]
    i=1
    while i<=30:
        if i<=5:
            a=i*i
            list1.append(a)
        if i>=26:
            a=i*i
            list1.append(a)
        i+=1
    print(list1)
values()
