def linear_secarch():
    for i in  range (0,n):
        if arr[i]==search:
            return i
    return -1
n=int(input("enter the size of list:"))
arr=list(map(int,input().split()))
search=int(input("enter search element:"))
result=linear_secarch()
if result!=-1:
    print("element found at:",result)
else:
    print("elememt not found:")
