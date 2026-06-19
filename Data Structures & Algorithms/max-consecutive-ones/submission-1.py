class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_val = 0
        temp_val = 0
        for num in nums:
            if num == 1:
                temp_val += 1
                if temp_val > max_val:
                    max_val = temp_val
            else:
                temp_val = 0
        return max_val
        