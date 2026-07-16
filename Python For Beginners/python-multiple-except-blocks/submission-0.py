def divide_numbers(a: str, b: str) -> None:
    try:
        a = int(a)
        b = int(b)
        answer = a/b
        print(answer)
    except ValueError:
        print("Error: Invalid value!")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except Except as error:
        print("An error occured:", error)



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
