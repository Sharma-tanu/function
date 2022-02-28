# def sorting(li):
#     for i in range(len(li)):
#         for j in range(len(li)):
#             if li[i] < li[j]:
#                 li[j],li[i] = li[i],li[j]
#     return li

# listToSort = [22,11,23,1,100,24,3,101,2,4]
# print(sorting(listToSort)) 


#  Q3. Aapko sort function ka use kr ke di hue list ko sort krna hai.
# unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]          

# def sort(a):
#     for i in range(len(a)):
#         for j in range(len(a)):
#             if a[i] < a[j]:
#                 a[j],a[i] = a[i],a[j]
#     return a
# unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15] 
# print(sort(unorder_list))

# def sort(a):
#     i=0
#     while i<len(a):
#         j=0
#         while j<len(a)-i-1:
#             if a[j]>a[j+1]:
#                 temp=a[j]
#                 a[j]=a[j+1]
#                 a[j+1]=temp
#             j=j+1
#         i=i+1
#     print(a)
# sort([6, 8, 4, 3, 9, 56, 0, 34, 7, 15])
