"""
Comparison Operators
== Equal
!= NotEqual
>  Greater than
<  Less than
>= Greater than or equal to
<= Less than or equal to

<<<<<<< HEAD
comparison operator always return True of False
"""
a, b = 10,20
=======
comparison operator always return True or False.
"""
a, b = 20, 20
>>>>>>> 8f44d62b34f61f413ac87cfa479badc149f47826
flag=(a>=b) # comparison operator has higher priority than assignment operator
print(flag)