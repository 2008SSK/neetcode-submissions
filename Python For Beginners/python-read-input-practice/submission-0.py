def add_two_numbers() -> int:
    total = 0 
    numbers = input()
    numbers_list = numbers.split(",")
    for i in range(len(numbers_list)):
        numbers_list[i] = int(numbers_list[i])
        total += numbers_list[i]
    return total



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
