>>> print 'Hello, World!'

# In the IDLE shell (Python 3.9.1) entering this statement results in a syntax error. This is because the statement lacks parenthesis 
# in order to be valid. However, it is a perfectly legal token in version 2.7.12. Quite evidently, at some point between these two versions
# the syntax of the language has changed. 

>>> 1/2

# This is expression returns 0.5 as a result. The interpreter when in its default state - the interactive mode - displays the result. 
# The opposite is true in script mode, where unless stated otherwise by means of a print function or something equivalent serving the same purpose,
# the operation remains a valid token and thus evaluated, but with its result not displayed on screen. 

>>> type(1/2)

## The type 

>>> print(01)

##

>>> 1/(2/3) 

## 