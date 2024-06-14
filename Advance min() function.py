Exceptions while using min()

    ValueError Exception

If you pass min() an empty iterable as an argument, it will throw a ValueError. The arguments to min() cannot be null.

Example

Copy Code

                    
cars = []
print('Smallest string is:', min(cars))

Output

                    
Traceback (most recent call last):
File "", line 2, in 
ValueError: min() arg is an empty sequence

To avoid this error, Python min() accepts the default parameter. Even if the list is empty, min() returns the default value.

    TypeError Exception

When we do not pass anything to the min() function, which requires at least one argument, we get a TypeError. OR when two different types of data are compared.

Example 1
Copy Code

                    
a = min()
print('Least value:', a)

Output

                    
Traceback (most recent call last):
File "", line 1, in 
TypeError: min expected 1 argument, got 0

Example 2
Copy Code

                    
a = min(20, 43, 5, 'Hello', 'John', 'Jack')
print("Minimum value is : ", a)

Output

                    
Traceback (most recent call last):
File "", line 1, in 
TypeError: '<' not supported between instances of 'str' and 'int'

    NameError Exception

The NameError exception occurs if the iterable or the argument passed to the min() function is not been defined before.

Example

Copy Code

                    
