from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    dictionary = {}
    dictionary[name] = age
    return dictionary


def list_to_dict(words: List[str]) -> Dict[str, int]:
# define empty dictionary {}
# go thorugh the list of words
# for each word, find its according index
# turn this into a pair ex. 'my_dict["Alice"] = 25'
# ultimately, retunr the dicitonary once looped through everything!

    dictionary = {}
    for word in words:
        exactindex = words.index(word) # finds index position
        dictionary[word] = exactindex
    return dictionary



# don't modify code below this line

print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))


print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))