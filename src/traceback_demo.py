import traceback


def divide(a, b):
    return a / b


try:
    result = divide(10, 0)
    print(result)

except Exception:
    print("An error occurred:")
    traceback.print_exc()