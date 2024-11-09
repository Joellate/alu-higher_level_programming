>>> BaseGeometry = _import_('7-base_geometry').BaseGeometry
>>> bg = BaseGeometry()

>>> bg.area()
Traceback (most recent call last):
    ...
Exception: area() is not implemented

>>> bg.integer_validator("my_int", 10)

>>> bg.integer_validator("my_int", -5)
Traceback (most recent call last):
    ...
ValueError: my_int must be greater than 0

>>> bg.integer_validator("my_int", "abc")
Traceback (most recent call last):
    ...
TypeError: my_int must be an integer

>>> bg.integer_validator()
Traceback (most recent call last):
    ...
TypeError: integer_validator() missing 2 required positional arguments: 'name' and 'value'

>>> bg.integer_validator("age")
Traceback (most recent call last):
    ...
TypeError: integer_validator() missing 1 required positional argument: 'value'

>>> bg.integer_validator("age", 0)
Traceback (most recent call last):
    ...
ValueError: age must be greater than 0

>>> bg.integer_validator("age", (4,))
Traceback (most recent call last):
    ...
TypeError: age must be an integer

>>> bg.integer_validator("age", [3])
Traceback (most recent call last):
    ...
TypeError: age must be an integer

>>> bg.integer_validator("age", True)
Traceback (most recent call last):
    ...
TypeError: age must be an integer

>>> bg.integer_validator("age", {3, 4})
Traceback (most recent call last):
    ...
TypeError: age must be an integer

>>> bg.integer_validator("age", None)
Traceback (most recent call last):
    ...
TypeError: age must be an integer
