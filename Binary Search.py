def Binary_Search(nums,target):
    l = 0
    r = len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l += 1
        else:
            r =- 1
    return -1

nums = [1,0,3,5,9,12]
target = 12
result = Binary_Search(nums,target)
print(result)