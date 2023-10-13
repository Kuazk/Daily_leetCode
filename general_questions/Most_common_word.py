

from collections import Counter

def mostCommonWord(paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        normalized = ''.join([ch.lower() if ch.isalnum() else ' ' for ch in paragraph])

        normalized = normalized.split()
        count = Counter(normalized)

        for i in banned:
            if i in count:
                count.pop(i)
        res = '' 
        max_n = 0  

        for key in count:
            
            if count[key] > max_n:
                res = key 
                max_n = count[key]
        return res



paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]

print(mostCommonWord(paragraph, banned))
