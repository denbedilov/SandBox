import generic_functions


def check_type(type, value):
    try:
        value = eval(type)(value)
        return isinstance(value, eval(type))
    except ValueError:
        return False


print(check_type('int', '33'))
# print(check_type('str', 'str'))
# print(check_type('str', 44))

# print(getattr(generic_functions, 's1')(1))
# print(getattr(generic_functions, 's2')(2))
# print(getattr(generic_functions, 's3')(3))

