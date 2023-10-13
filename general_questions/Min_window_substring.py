
from collections import Counter




class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if not t or not s:
            return ""
        min_count = Counter(t)
        table = {}

        required = len(min_count)
        formed = 0
        filter_s = []  # filtel
        l,r = 0 ,0
        min_len = float("inf"), None, None
        for index,ch in enumerate(s):
            if ch in min_count:
                filter_s.append((index,ch))
        
        for index, ch in filter_s:
            
            table[ch] = table.get(ch,0) +1

            if table[ch] == min_count[ch]:
                formed +=1

            while l <= r and formed == required:
                l_ch = filter_s[l][1]
                start = filter_s[l][0]
                end = filter_s[r][0]
                if end -start +1 < min_len[0]:
                    min_len = (end -start +1, start, end)
                
                table[l_ch] -= 1
                if table[l_ch] < min_count[l_ch]:
                    formed -=1
                l +=1
            r +=1
        return "" if min_len[0] == float("inf") else s[min_len[1]:min_len[2]+1]




            

       
        
        
    



solution = Solution()
s = "AA"
t = "AA"
res = solution.minWindow(s,t)
print(res)