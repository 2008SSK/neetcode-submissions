from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    length = len(nums)
    total = 0
    for i in range(length):
        total += nums[i]
    return total 

def get_min(nums: List[int]) -> int:
    number = nums[0] 
    number += 1 
    length = len(nums) 
    for i in range(length): 
        if nums[i] < number: 
            number = nums[i]
    return number



def get_max(nums: List[int]) -> int:
    number = nums[0] # 4
    number -= 1 # 3
    length = len(nums)
    for i in range(length):
        if nums[i] > number:
            number = nums[i]
    return number


# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
