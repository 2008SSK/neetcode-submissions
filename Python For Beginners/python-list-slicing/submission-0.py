from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:

    # get the length of my_list 
    length = len(my_list)
    
    # reverse the string 
    reversedList = my_list[::-1]

    # remainder the len(my_list) - 3
    remainder = length - 3

    # if this remaining number is = 0:
    if remainder == 0:
    # reverse list 
        secondReversed = reversedList[::-1]
    # print list
        return secondReversed

    # if the remaining number is > 0:
    if remainder > 0:
    # cut out the indexes that is :3
        newReversedList = reversedList[:3]
    # reverse the list
        secondReversed = newReversedList[::-1]
    # print the new list
        return secondReversed


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
