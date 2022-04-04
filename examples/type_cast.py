"""
generic type check function
"""


def check_type(type, value):
    try:
        value = eval(type)(value)
        return isinstance(value, eval(type))
    except ValueError:
        return False


print(check_type('int', '33'))
print(check_type('str', 'str'))
print(check_type('str', 44))
