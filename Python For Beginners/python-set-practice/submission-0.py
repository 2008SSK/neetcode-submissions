from typing import List

def contains_duplicate(words: List[str]) -> bool:
    # convert the list of words into a set, save to a var 
    # if length of list of words is greater than the set of words
    # return True
    # else:
    # return False

    setofwords = set(words)
    if len(words) > len(setofwords):
        return True
    else:
        return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"])) # true 
print(contains_duplicate(["hello", "world", "i", "am", "great"])) # false
print(contains_duplicate(["hello", "hello", "hello"])) # true
print(contains_duplicate(["Hello", "hellooo", "hello"])) # false
