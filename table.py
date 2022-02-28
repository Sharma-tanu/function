# Python Multiplication Table of Number by Function Program

# def print_table(num): 
#     for i in range(1,11): 
#         print(num,' x ', i, ' = ',num*i) 
# n = int(input("Please Enter a number table:"))
# print_table(n)

# What is the output of the following code snippet?
# num = 1
# def func():
#     global num
#     num = num + 3
#     print(num)
# func()
# print(num)


# print("\U0001F600")
# print("\U0001F600")
# print("\U0002F600")





Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). 



def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l[:5])
	print(l[-5:])

printValues()
