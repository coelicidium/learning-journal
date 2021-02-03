>>> print 'Hello, World!'

# In the IDLE shell (Python 3.9.1) entering this statement results in a syntax error. This is because the statement lacks parentheses. 
# in order to be valid. However, it is a perfectly legal token in version 2.7.12 where Hello World! is printed right away.
# Quite evidently, at some point between these two versions the syntax of the language has changed.

>>> 1/2

# This is expression returns 0.5 as a result. The interpreter when in its default state - the interactive mode - displays the result. 
# The opposite is true in script mode, where unless stated otherwise by means of a print function or something equivalent serving the same purpose,
# the operation remains a valid token and thus evaluated, but with its result not displayed on screen. 

>>> type(1/2)

# The type function returns the class (the category) of its argument. Since 1/2 is written as an expression, it goes on to be evaluated and the shell returns
# us 'float' - which is indeed the data type (to be less confusing, the category of data types) where 0.5 belongs. 

>>> print(01)

# SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers.
# Well... this is self-explaining, isn't it? Typing print(0o01) give us 1, which is a perfectly fine number in the octal system.
# Warning: the print statement returns automatically the output in decimal base, so (0o200) produces 128 as a result.
# And 8 is definitely not a valid octal number. 

>>> 1/(2/3) 

# This is a valid expression in the most recent version of Python, but not in its former one, that returns us the following:
# ZeroDivisionError: integer division or modulo by zero
# This can only mean that Python 2.7.12 has the operator / as integer division only, and gives us the error 
# because 2/3 would be 0.666666666 and this is NOT an integer; only the integer part gets in, leading to zero.
# Suddenly we have a division by zero, which is known to be undefined. A modulo by zero is undefined as well.
# Why? Because you get the modulo through a division. 
# Type 2//3, where // is the floor division operator, rounding the result to the nearest integer if you want to verify by yourselves.

