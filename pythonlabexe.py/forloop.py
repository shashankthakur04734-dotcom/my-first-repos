# s=int(input())
# sum=0
# for i in range(1,s):
#     if s%i==0:
#         sum+=i
#     if sum==s:
#         print("perfect:",s)
# else:
#     print("not a perfect number")
# s=4
# sum=0
# for i in range(1,s+1):
#     if s%i==0:
#         sum+=i
#     elif sum>s:
#         print("abundant :",s)
# else:
#     print(" not abundant :", s)
n1=6
n2=28
sum1=0
sum2=0
for  i in range(1,29):
    if n1%i==0:
        sum1+=i
        print(sum1)
    elif n2%i==0:
        sum2+=i
    print(sum2)
if sum1/n1==sum2/n2:
        print("friendly pair")
else:
        print(" not friendly pair")

 





