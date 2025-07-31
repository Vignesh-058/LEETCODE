def Two_sum_2(nums, target):
    l = 0
    r = len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == target:
            return [l + 1, r + 1]
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            r -= 1
    return []

nums = [2, 7, 11, 15]
target = 9
result = Two_sum_2(nums, target)
print(result)