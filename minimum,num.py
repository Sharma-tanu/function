list= [8, 6, 4, 8, 4, 50, 2, 7]
def minimum(numbers):
    i=0
    a=list[0]
    while i< len(numbers):
        if numbers[i]<a:
            a=numbers[i]
        i=i+1
    print(a)
minimum([8, 6, 4, 8, 4, 50, 2, 7])