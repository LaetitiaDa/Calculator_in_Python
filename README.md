# Calculator_in_Python
Calculator in Python 

First project in Python in 1 day. In this exercise we were not allowed to use some functions such as eval.

This code will display a simple calculator in tkinter.

This is a simple calculator on the same model as the iphone one but it also supports priorities in the calculation (ex: 2+5x6).

The principle behind: It takes the string written in the input and decompose it to find the * and / before the + and -. Then it finds the floats around and does the operation before finally recompose the string with the result.
These operations loop until there is no more *, /, -, + and gives the result.
