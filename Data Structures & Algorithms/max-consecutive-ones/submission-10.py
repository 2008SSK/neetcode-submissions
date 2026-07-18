class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_array = 0
        maximum_array = 0

        for num in nums:
            if num == 1:
                current_array += 1
                maximum_array = max(maximum_array, current_array)
            else:
                current_array = 0
        return maximum_array