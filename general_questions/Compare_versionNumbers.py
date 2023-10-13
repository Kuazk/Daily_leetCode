

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        v1 = [int(num) for num in version1.split(".")]
        v2 = [int(num) for num in version2.split(".")]
        l1,l2 = len(v1),len(v2)
        
        pointer= 0
        res = 0
        while pointer < l1 and pointer < l2:

            if v1[pointer] > v2[pointer]:
                res = 1
                break
            elif v1[pointer] < v2[pointer]:
                res = -1
                break
            pointer +=1
        if res == 0:
            if l1 > l2:
                while pointer < l1:
                    if v1[pointer] > 0:
                        res = 1
                    pointer +=1
            else:
                while pointer < l2:
                    if v2[pointer] > 0:
                        res = -1
                    pointer +=1
        return res

                    




solution = Solution()
version1 ="1.01"
version2 = "1.001"
res = solution.compareVersion(version1, version2)

print(res)