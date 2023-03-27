## PYTHON EXCEPTIONS
Learn what are exceptions, how to use and handle them.

Each file will demonstrate a concept on exceptions.

## LEARNING OBJECTIVES

* Difference between errors and exceptions
* What are exceptions & how to use them
* When should we use exceptions
* How to correctly handle an exception
* Purpose of catching an exception
* How to raise a builtin exception
* When do we need to implement a clean up action after an exception

All the files will be excecutable.

[0-safe\_print\_list.py](https://github.com/Mosesbwire/alx-higher_level_programming/blob/main/0x05-python-exceptions/0-safe_print_list.py)

The function prints a specified number of items from a list. The items in the list can be of any type(integer, string, e.t.c).

The `x` parameter represents the number of items to be printed and it can be lager than the length of `my_list`.

The function returns the number of elements printed.

No module can be imported

The len function cannot be used.

[1-safe\_print\_integer.py](https://github.com/Mosesbwire/alx-higher_level_programming/blob/main/0x05-python-exceptions/1-safe_print_integer.py)

Prints an integer

prototype: `def safe_print_integer(value):`

Return `True` if value is an integer otherwise `False`

Don't import any module

Don't use `type`

[2-safe\_print\_list\_integers.py](https://github.com/Mosesbwire/alx-higher_level_programming/blob/main/0x05-python-exceptions/2-safe_print_list_integers.py)

prints only integers from the given list

non-integers are skipped silently

`x` represents the number of items to print from the list

`x` can be lager than the length of the list. This should throw an exception

Function returns the number of integers printed

[3-safe\_print\_division.py](https://github.com/Mosesbwire/alx-higher_level_programming/blob/main/0x05-python-exceptions/2-safe_print_division.py)

Returns result of the division otherwise `None`

Assumption is made that the arguments given are always integers

Exceptions should be well handled

`finally` block will always print the results of the division

[5-raise\_exception.py](https://github.com/Mosesbwire/alx-higher_level_programming/blob/main/0x05-python-exceptions/5-raise_exception.py)

Function raise TypeError Exception

