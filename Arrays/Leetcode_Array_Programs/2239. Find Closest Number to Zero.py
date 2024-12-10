class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        x = nums[0]
        for i in range(len(nums)):
            if abs(nums[i])<abs(x):
                x = nums[i]
        if x < 0:
            for i in range(len(nums)):
                if nums[i]+x==0:
                    x = nums[i]        
        return x