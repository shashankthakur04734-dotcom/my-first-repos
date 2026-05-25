def max_sum(arr,k):
    max_sum=float("-inf")
    for i in range(0,len(arr)-k+1):
        curr_sum=0
        for j in range(i,i+k):
            curr_sum=curr_sum+arr[j]
            max_sum=max(max_sum,curr_sum)
        return max_sum
arr=[11,2,-3,4,5,-6]
k=3
print(max_sum(arr,k))