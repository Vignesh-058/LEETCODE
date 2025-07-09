
import time
from itertools import chain
from Concatenationarray import Solution  # Import your class from Concatenationarray.py

def test_performance():
    nums = list(range(100000))  # Large test input

    print("Testing custom loop method...")
    s = Solution()
    start = time.time()
    result = s.getConcatenation(nums)
    end = time.time()
    print("→ Custom loop: {:.6f} seconds | Length: {}".format(end - start, len(result)))

    print("\nTesting list addition (nums + nums)...")
    start = time.time()
    result = nums + nums
    end = time.time()
    print("→ List addition: {:.6f} seconds | Length: {}".format(end - start, len(result)))

    print("\nTesting list multiplication (nums * 2)...")
    start = time.time()
    result = nums * 2
    end = time.time()
    print("→ List multiply: {:.6f} seconds | Length: {}".format(end - start, len(result)))

    print("\nTesting list comprehension...")
    start = time.time()
    result = [nums[i % len(nums)] for i in range(2 * len(nums))]
    end = time.time()
    print("→ List comprehension: {:.6f} seconds | Length: {}".format(end - start, len(result)))

    print("\nTesting itertools.chain...")
    start = time.time()
    result = list(chain(nums, nums))
    end = time.time()
    print("→ Chain: {:.6f} seconds | Length: {}".format(end - start, len(result)))

if __name__ == "__main__":
    test_performance()