from typing import Dict, List # this adds type hints for List and Dict

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    name = [] 
    for key in age_dict: 
        name.append(key)
    return name

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    # create an empty list to represent the ages
    ages = []

    # go through the dictionary's keys
    for key in age_dict:

    # for each key, index the corresponding value 
      val = age_dict[key]

    # append these values to the string
      ages.append(val)

    # ultimately, return the list
    return ages

# do not modify below this line
dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))

'''
get_dict_keys(age_dict: Dict[str, int]) -> List[str] should take a dictionary of names and ages and return a list of the names.
get_dict_values(age_dict: Dict[str, int]) -> List[int] should take a dictionary of names and ages and return a list of the ages.
'''