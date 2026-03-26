def divide_numbers(numbers):
    result = []
    for i in range(len(numbers)):
        res = 100 / numbers[i]
        result.append(res)
    return result

print(divide_numbers([10, 5, 0]))