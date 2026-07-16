from typing import List

def read_integers() -> List[int]:
    finalized_list_of_ints = []
    line = input()
    new_numbers_in_string_list = line.split(",")
    for number in new_numbers_in_string_list:
        new_number = int(number)
        finalized_list_of_ints.append(new_number)
    return finalized_list_of_ints

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
