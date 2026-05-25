#DIRECT METHOD #COMPILE TIME INIT
"""matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)"""
#run time
#user input
# matrix=[]
# for i in range(3):
#     row=list(map(int,input("enter list:").split(",")))
#     matrix.append(row)
# print("3x3 matrix is:")
# for row in matrix:
#     print(row)
#Nested list
# matrix=[[int(input("enter element:")) for col in range(3)] for row in range(3)]
# for row in matrix:
#     print(row)



#access a specific element
# matrix=[
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]
# ]
# print("element at 0 0 is:",matrix[0][0])
# print("element at 1 2 is:",matrix[1][2])


#tarversing a 2d array
# arr=[
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]
# ]
# rows=len(arr)
# cols=len(arr[0])

# print("row-wise tar:")
# for i in range(rows):
#     for j in range(cols):
#         print(arr[i][j],end=" ")
#     print()



# #tarversing a 2d array colume
# arr=[
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]
# ]
# rows=len(arr)
# cols=len(arr[0])

# print("col-wise tar:")
# for j in range(rows):
#     for i in range(cols):
#         print(arr[i][j],end=" ")
#     print()



# #secring in a 2d array
# arr=[
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]
# ]
# key=int(input("enter element to search:"))
# found=False

# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         if arr[i][j]==key:
#             print("element found at position",i,j)
#             found=True
#             break
#     if found:
#         break
#     if not found:
#         print("element not found")


def max_num(arr):
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
        return arr
print(max_num([3,7,2,9,4]))
    



    




