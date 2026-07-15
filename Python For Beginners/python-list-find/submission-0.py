from typing import List # this is used to add type hints for List type

def find_index(nums: List[int], target: int) -> int:
    # return the index of the first occurence of the target number. target number will always be present
    if target in nums:
        return nums.index(target)

# don't modify code below this line
print(find_index([1, 2, 3, 4, 5], 3)) # returns 2
print(find_index([1, 2, 3, 4, 5, 3], 3)) # returns 2
print(find_index([1, 2, 3, 4], 1)) # returns 0
print(find_index([1, 3, 4, 2], 2)) # returns 3