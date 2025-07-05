# loop + append method
# This method iterates through the input list and appends the value at the index specified by each element.
# It has a time complexity of O(n) and a space complexity of O(n).
def buildArray(nums):
    answer = []
    for i in range(len(nums)):
        answer.append(nums[nums[i]])
    return answer

# List comprehension method
# This method is more concise and often faster than the loop + append method.
# It uses list comprehension to achieve the same result in a single line.
# It also has a time complexity of O(n) and a space complexity of O(n).
def listcomprehension(nums):
    ans = len(nums)
    return[nums[nums[i]]for i in range(ans)]

# In-place method
# This method modifies the original array to avoid using extra space.
# It uses the fact that the values in nums are within the range of indices of nums.
def inplace(nums):
    n = len(nums)
    for i in range(n):
        nums[i]=nums[i] + n* ( nums[nums[i]] % n )
    for i in range(n):
        nums[i] = nums[i] // n
    return nums

# Example usage of the functions
# The input is a list of integers where each integer is an index to another integer in the list.
# The output is a new list where each element is the value at the index specified
# corresponding element in the input list.
nums = [0,2,1,5,3,4]
result  = buildArray(nums)
result2 = listcomprehension(nums)
result3 = inplace(nums)
print("loop + append method => ", result)
print("listcomprehension    => ", result2)
print("inplace              => ", result3)