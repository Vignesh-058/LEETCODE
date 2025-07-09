from itertools import chain

# 1. Using custom loop with modulo
def method_1_loop_mod(nums):
    """
    Repeat list using a loop and modulo.
    Example: [1, 2, 1] → [1, 2, 1, 1, 2, 1]
    """
    ans = []
    a = len(nums)
    for i in range(2 * a):
        ans.append(nums[i % a])
    return ans

# 2. Using list addition
def method_2_list_addition(nums):
    """
    Repeat list using list addition.
    Example: [1, 2, 1] + [1, 2, 1]
    """
    return nums + nums

# 3. Using list multiplication
def method_3_list_multiplication(nums):
    """
    Repeat list using multiplication.
    Example: [1, 2, 1] * 2
    """
    return nums * 2

# 4. Using list comprehension with modulo
def method_4_list_comprehension(nums):
    """
    Repeat list using list comprehension and modulo.
    """
    return [nums[i % len(nums)] for i in range(2 * len(nums))]

# 5. Using itertools.chain
def method_5_itertools_chain(nums):
    """
    Repeat list using itertools.chain.
    """
    return list(chain(nums, nums))

# Example usage
# Given a list of integers, repeat it twice using different methods
# Example: [1, 2, 1] → [1, 2, 1, 1, 2, 1]
nums = [1, 2, 1]
result1 = method_1_loop_mod(nums)
result2 = method_2_list_addition(nums)
result3 = method_3_list_multiplication(nums)
result4 = method_4_list_comprehension(nums)
result5 = method_5_itertools_chain(nums)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)