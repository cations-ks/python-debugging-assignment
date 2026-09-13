import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)


def calculate(a, b):
    logging.debug("Starting calculation")
    logging.debug("a = %s", a)
    logging.debug("b = %s", b)

    result = a + b

    logging.info("Calculation completed")

    return result


print(calculate(10, 20))