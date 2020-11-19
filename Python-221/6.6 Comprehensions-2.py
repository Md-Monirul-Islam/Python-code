numbers = [1, 5, 2, 12, 14, 7, 18]
doubles_generator = (2 * number for number in numbers)
print(doubles_generator)
doubles_set = {2 * number for number in numbers}
print(doubles_set)
doubles_dict = {number: 2 * number for number in numbers}
print(doubles_dict)