def missingAndRepeating(arr, n):
    # Write your code here
    a,b = 0,0
    nums = {i for i in range(1,n+1)}
    for i in arr:
        if i in nums:
            nums.remove(i)
        
        elif i not in nums:
            a = i
    
    for i in nums:
        b = i
    
    return (b,a)
