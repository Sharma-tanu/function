# reverse_list=["1234abcd"]
# def reverse(string):
#     i=1
#     while i<=len(string):
#         print(string[-1],end=" ")
#         i=i+1
#     print()
# reverse("1234abcd")


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("Input a number to compute the factiorial : "))
# print(factorial(n))


def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))
