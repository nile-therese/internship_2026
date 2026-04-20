def max_average_subarray(nums,k):
    window_sum=sum(nums[:k])
    max_sum=window_sum
    for i in range(k,len(nums)):
        window_sum=window_sum-nums[i-k]+nums[i]
        max_sum=max(max_sum,window_sum)
    return max_sum/k
nums=[1,12,-5,-6,50,3]
k=4
result=max_average_subarray(nums,k)
print(result)