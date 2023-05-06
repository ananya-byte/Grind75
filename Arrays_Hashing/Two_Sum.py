class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst = []
        for x in range(0,len(nums)):
            for y in range(x+1,len(nums)):
                if (nums[x]+nums[y]==target):
                    lst.append(x)
                    lst.append(y)
                    return lst
