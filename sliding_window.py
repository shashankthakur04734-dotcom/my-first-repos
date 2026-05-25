def sliding_window_sum(arr,k):
    max_sum=0
    curr_sum=0
    for i in range(0,k):
        curr_sum=curr_sum+arr[i]
        max_sum=curr_sum
    for j in range(k,len(arr)):
        curr_sum=curr_sum+arr[j]-arr[j-k]
        max_sum=max(max_sum,curr_sum)
    return max_sum
arr=[1,2,3,-4,6,8]
k=3
print(sliding_window_sum(arr,k))