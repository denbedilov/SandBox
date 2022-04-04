"""
call function generically
"""
import generic_functions

func = 's1'

print(getattr(generic_functions, func)(1))
func = 's2'
print(getattr(generic_functions, func)(2))
func = 's3'
print(getattr(generic_functions, func)(3))
