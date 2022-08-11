




from collections import Counter

def firstUniqChar(s):
        
    hash_t = Counter(s)

    for index, ch in enumerate(s):

        if hash_t[ch] == 1:
            return index
    return -1


s = "aabb"

print(firstUniqChar(s))



