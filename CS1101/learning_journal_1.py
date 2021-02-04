# 1. In a print statement, what happens if you leave out one of the parentheses, or both?

# A syntax error is displayed as in the following examples (it's worth nothing how putting only one parentheses
# on the left leads to having the prompt allowing us to further introduce another token).

SyntaxError: invalid syntax
>>> Print(4
      4
      
SyntaxError: invalid syntax
>>> print(4
      )
4
>>> print(5
      3
      
SyntaxError: invalid syntax
>>> print(5
      3)
SyntaxError: invalid syntax
>>> 
 
# If missing both parentheses, the syntax error specifies that the parentheses are missing:

SyntaxError: invalid syntax
>>> print 59
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(59)?
>>> 

# 2. If you are trying to print a string, what happens if you leave out one of the quotation marks, or both? #
# It depends. With one quotation mark, the interpreter  gives an EOL (end of line) error. 

>>> print ("dog
  File "<stdin>", line 1
    print ("dog
              ^
SyntaxError: EOL while scanning string literal

# In other cases, though, while a generic syntax error is displayed, the shell tells us something interesting:

>>> print dog 
  File "<stdin>", line 1
    print dog 
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(dog)?
>>> print(dog)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dog' is not defined
>>> 

# My educated guess is that here 'dog' is treated as a variable that, as prompt suggests us,
# it's undefined and thus meaningless.

 

#3. You can use a minus sign to make a negative number like -2. 
# What happens if you put a plus sign before a number? What about 2++2?

>>> 2++2
4
>>> 2+-2
0

# An expression happens. One that gets parsed correctly, and gives a correct arithmetical result. The signs specify if
# the number is negative or positive. A plus, I immagine, makes it so that you can force the "positiveness" of the number.
# Who knows? Maybe for some reason you want Python to compute a number without a positive sign a negative number by default,
# and this would be a godsend to avoid the pains of reimplementing positive integers somehow. In alternative, Python has reached the singularity
# only in order to know only Siths deals in absolutes, and decided to have its opinions on absolute values as well.


# 4. In math notation, leading zeros are ok, as in 02. What happens if you try this in Python? 

>>> 02
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

# It's because a numerical value inputted with a leading zero is assumed to be an octal number, not one in base ten.
# A precise syntax has to be followed when inputting an octal, see above.  


# 5. What happens if you have two values with no operator between them? 

SyntaxError: invalid syntax

# This. Only numbers and no operators whatsoever? Nothingness. Darkness. Oblivion. Invalid syntax. Different names for the same fate.



# If you are trying to print a string, what happens if you leave out one of the quotation marks or both and why?
# You can use a minus sign to make a negative number like -2. What happens for each of the following and why?

>>> 2++2
4
>>> 2--2
4
>>> 2+-2
0
>>> 2-+2
0

# The addition of two positive integers (one implied by default, the other specified) leads to a positive integer.
# For the rest of the results: these are algebraic expressions, parsed and solved as such. This explains the change of sign in 2--2 that might as well
# have been 2-(-2) in another context. This occurs to me as the only reason that makes sense.  

	
# Next, describe at least three additional Python experiments that you tried while learning Chapter 1. 
# Show the Python inputs and their outputs, and explain what you learned from the results of each example.

>>> 2^2
0

# I learned that ^ is not the exponential operator, mostly. My spider sense tell me it might have something to do with logic gates, though.
# Or the mysterious bitwise operations the first chapter doesn't elaborate on. Perhaps both. 

>>> remainder = 11 % 3
print(remainder)
SyntaxError: multiple statements found while compiling a single statement
>>> 

# I learned that I a self aware idiot that just remembered that the python *SHELL* is not supposed to handle multiple statements at once.
# This stuff needs the script mode. 

>>> 
= RESTART: C:/Users/Denys/Documents/GitHub/learning-logs/CS1101/lj1_exercise.py
2

# This is the result I have in script mode, with the same text. It works!
# Always in script mode:

>>> import math
>>> int(math.pi)
3

# Forgive me Father, for I have sinned, but a bit less than usual, because now I know how to import a library.





 

