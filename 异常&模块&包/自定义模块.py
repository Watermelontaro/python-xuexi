__all__ = ["te", "teb"]


def te(a, b):
    print(a + b)


def teb(a: object, b: object) -> object:
    print(a / b)


def tec(a, b):
    print(a * b)


te(1, 2)
