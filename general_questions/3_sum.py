



class Solution:
    def threeSum(self, nums):
        

        res = []

        nums = sorted(nums)
        for index, num in enumerate(nums):

            target = 0 - num 
            table = {}


            for j in nums[index+1:]:
                if j in table:
                    suM = [num, table[j],j]
                    if suM not in res:
                        res.append(suM)
                        print(f'append on num {num}')
                    
                    table.pop(j)
                else:
                    table[target - j] = j
                print(f'current num is {num},current table is {table}')
            



        return res


solution = Solution()
res = solution.threeSum([1,2,-2,-1])
print(res)