#Horizontal  Scanning
def lcp_h(strs):
    if len(strs) == 0:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[0:len(prefix)-1]  # Fixed assignment
            if prefix == "":
                return ""
    return prefix

#Vertical Scanning
def lcp_v(strs):
    if strs is None or len(strs) == 0:
        return ""
    for i in range(len(strs[0])):  # Fixed range
        c = strs[0][i]  # Fixed variable name
        for j in range(1, len(strs)):  # Start from 1
            if i >= len(strs[j]) or strs[j][i] != c:
                return strs[0][0:i]
    return strs[0]

#Divide and Conquer
def LCP_DC(strs):
    if strs is None or len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    mid = len(strs) // 2
    left = LCP_DC(strs[:mid])
    right = LCP_DC(strs[mid:])
    i = 0
    while i < min(len(left), len(right)) and left[i] == right[i]:
        i += 1
    return left[:i]

#inputs
strs = ["flower", "flow", "flight"]
Result1 = lcp_h(strs)
Result2 = lcp_v(strs)
Result3 = LCP_DC(strs)
print("Horizontal Scanning:", Result1)
print("Vertical Scanning:", Result2)
print("Divide and Conquer:", Result3)