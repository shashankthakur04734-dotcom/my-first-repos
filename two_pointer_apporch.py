# def palindrome(arr):
#     left=0
#     right=len(arr)-1
#     while left<right:
#         if arr[left]!=arr[right]:
#             return "not palindrome"
#         left+=1
#         right+=1
#         return "palindrome"
# arr=[1,2,4,4,2,1]
# print(palindrome(arr))
def soul(arr):
    left=0
    right=len(arr)-1
    tar=11
    while left<right:
        s=arr[left]+arr[right]
        if s==tar:
            return [left,right]
        elif s<tar:
            left+=1
        else :
            right-=1
    return[None]
arr=[-2,3,4,7,5,12]
print(soul(arr))
           
     

        





