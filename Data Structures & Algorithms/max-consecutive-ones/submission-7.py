class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    # define a number count 
    # go through the list
    # if the number is 1
    # append to a pre-defined # count 
    # if the instance is not 1
    # reset the count 
    # output the result aftera ll of this is done 

        current_consecutive = 0
        max_consecutive = 0

        for num in nums:
            if num == 1:
                current_consecutive += 1
                max_consecutive = max(max_consecutive, current_consecutive)
            if num == 0:
                current_consecutive = 0
        return max_consecutive


