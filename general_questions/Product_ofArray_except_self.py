






class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_arr = [1]   # left
        right_arr = [1] # right

        for i in range(len(nums)-1):
            left_arr.append(left_arr[i]*nums[i])
        for i in range(len(nums)-1):
            right_arr.append(right_arr[i]*nums[-i-1])
        right_arr.reverse()

        res = list(map(self.muitiply,left_arr,right_arr))
        return res
    def muitiply(self,n1,n2):
        return n1*n2    

solution = Solution()
num=[-1,1,0,-3,3]

res = solution.productExceptSelf(num)
print(res)