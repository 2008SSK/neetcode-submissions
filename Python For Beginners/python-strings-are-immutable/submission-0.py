def remove_fourth_character(word: str) -> str:
    # 4th character is the [3]
    # split up to before & after [3]
    firstfewchars = word[0:3]
    secondfewchars = word[4:]

    updatedchars = firstfewchars + secondfewchars
    return updatedchars



# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
