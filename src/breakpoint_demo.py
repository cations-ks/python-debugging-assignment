def calculate_average(numbers):
    total = sum(numbers)

    breakpoint()

    average = total / len(numbers)
    return average


def calculate_result(numbers):
    average = calculate_average(numbers)

    if average >= 50:
        return "Pass"
    else:
        return "Fail"


numbers = [60, 70, 80, 90]

result = calculate_result(numbers)

print("Numbers:", numbers)
print("Result:", result)