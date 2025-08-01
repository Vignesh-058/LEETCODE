#Brute Force Solution
def twonums(nums, target):
    a = len(nums)
    for i in range(a):
        for j in range(i+1,a):
            if nums[i] + nums[j] == target:
                return [i, j]

#Hash Map Solution
def hashmap(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i

#Input Parameters
nums=[2, 7, 11, 15]
target=9
solution=twonums(nums,target)
solution1=hashmap(nums,target)
print(solution)
print(solution1)