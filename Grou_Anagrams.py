import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_t = collections.defaultdict(list)

        for st in strs:
            sort_st = tuple(sorted(st))
            hash_t[sort_st].append(st)
    
        
        return list(hash_t.values())

        

solution = Solution()
res = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])

print(res)


