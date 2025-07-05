## Finding Words Containing Characters
# This code finds the indices of words in a list that contain a specific character.
# It provides two functions: one using a simple loop and another using list comprehension with enumeration.
# The first function iterates through the list and checks if the character is in each word,
# while the second function uses `enumerate` to achieve the same result in a more concise way.
def findingwordscontaining(words,x):
    ans = []
    for i in range(len(words)):
        word = words [i ]
        if x in word:
            ans.append(i)
    return ans

# This function uses list comprehension with enumeration to find indices of words containing a specific character.
# It iterates through the list of words and checks if the character is present in each word
# while keeping track of the index using `enumerate`.
def usingenumeratedfind(words, x):
    return[i for i,word in enumerate(words) if x in word]

# Example usage of the functions
# The following code demonstrates how to use the two functions defined above.
# It initializes a list of words and a character to search for,
# then calls both functions to find the indices of words containing that character.
words = ["leet", "leetcode", "leet", "code"]
x= "e"
result = findingwordscontaining(words,x)
result2 = usingenumeratedfind(words, x)
print(result)
print(result2)