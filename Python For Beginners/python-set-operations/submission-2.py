from typing import List

def count_unique_words(words: List[str]) -> int:
    # checking if length of list is 0, return 0
    if len(words) == 0:
        return 0
        
    # use method to convert the list into having all duplicates/repeats
    new_set = set(words)
    set_without_duplicates = list(new_set)    

    # return length of the new list 
    num = len(set_without_duplicates)
    return num

print(count_unique_words(["hello", "world", "hello", "goodbye"])) # hello, world, goodbye
print(count_unique_words(["hello", "world", "i", "am", "world"])) # hello, world, i, am
print(count_unique_words(["hello", "hello", "hello"])) # hello
print(count_unique_words([])) # 


'''
Implement the function count_unique_words(words: List[str]) -> int which 
accepts a list of strings words 
returns the number of unique words in the list.
 It's possible the list may be empty, in which case the function should return 0.
Hint: You can call the len() function on a set to get the number of elements in the set.
'''