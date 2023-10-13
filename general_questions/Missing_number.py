





class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0  

        missing_sum = 0  

        for num in nums:
            missing_sum += num  
            if num > max_num:
                max_num = num
        total_sum = int(max_num*(max_num+1) /2)
        if missing_sum == total_sum:
            return total_sum +1
        return (total_sum - missing_sum)

solution = Solution()
nums = [3,0,1]
res = solution.missingNumber(nums)
print(res)
