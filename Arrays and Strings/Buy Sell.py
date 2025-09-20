#brute force approach  #)Time complexity: O(n^2)  #)space complexity: O(1)
def Max_profit_brute(arr):
    m = 0 # max profit
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                profit = arr[j] - arr[i]
                if m < profit:
                    m = profit # update max profit
    return m

#optimized approach
#)Single Forloop #)Time complexity: O(n)  #)space complexity: O(1)
def Max_profit_optimized(arr):
    maxPro = 0 # max profit
    minPrice = float('inf') # initialize min price to infinity
    for i in range(len(arr)):
                minPrice = min(minPrice, arr[i])
                maxPro = max(maxPro, arr[i] - minPrice)
    return maxPro

# further optimized approach
#)Two pointer approach  #)Time complexity: O(n)  #)space complexity: O(1)
def Max_profit(arr):
    l = 0
    r = 1
    m = 0 # max profit
    while r < len(arr):
        if arr[l] < arr[r]:
            profit = arr[r] - arr[l]
            if m < profit:
                m = profit # update max profit
        else:
            l = r
        r+=1
    return m


# Calling the function
arr = [7,1,5,3,6,4]
result1 = Max_profit(arr)
result2 = Max_profit_optimized(arr)
result3 = Max_profit_brute(arr)
print("Bruteforce Approch:",result1)
print("Optimized approach:",result2)
print("Two pointer approach:",result3)