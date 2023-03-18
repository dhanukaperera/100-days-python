# Day 01 Notes

### Function Name:

`print()`

### Description:

The `print()` function is a built-in function in Python that is used to display output on the console. It takes one or more arguments and prints them to the console. The arguments can be of any data type, such as a string, integer, or float.

### Syntax:

```python
print(value1, value2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```

### Parameters:

The `print()` function takes several optional parameters:

* value1, value2, ...: One or more values that need to be printed. These values can be of any data type.
* sep: Specifies the separator between the values. By default, it is a space character.
* end: Specifies the end character that will be printed after the values. By default, it is a newline character.
* file: Specifies the output file where the output will be printed. By default, it is sys.stdout, which prints to the console.
* flush: Specifies whether to flush the output buffer or not. By default, it is Fals

### Example:

Here is an example that uses the print() function to print a string:

```python
print("Day 1 - Python Print Function")
```

Output:

The output of the above code will be:

```
Day 1 - Python Print Function
```

### Note:

* The print() function is often used for debugging, testing, and displaying information to the user.

* If you want to print a string that contains quotes, you can use either single quotes or escape the quotes with a backslash (").

* You can also use the + operator to concatenate multiple values or strings that need to be printed.

* You can use the format() method or f-strings to format the output in a specific way.

___

## Function Name:

`input()`

### Description:

The `input()` function is a built-in function in Python that allows the user to enter a value or string from the console. It takes an optional prompt argument as a string that is displayed to the user before taking input.

### Syntax:

```python
input([prompt])
```

### Parameters:

The `input()` function takes an optional prompt argument:

prompt: A string that is displayed to the user before taking input. This argument is optional.

### Return Value:

The `input()` function returns a string that is entered by the user.

### Example:

Here is an example that uses the input() function to get the user's age:

```python
age = input("What is your age?")
print("Your age is: " + age)
```

Using sep parameter:

In this example, we use the sep parameter to change the separator between the values from the default space character to a hyphen.

```python
name = "John"
age = 25
print(name, age, sep="-")
```

Output:

```
John-25
```

Using end parameter:

In this example, we use the end parameter to change the end character from the default newline character to a space character.

```python
name = "John"
age = 25
print(name, age , end=" ")
print("is a programmer")
```

Output:
```
John 25 is a programmer.
```

Using file parameter:

In this example, we use the file parameter to redirect the output to a file named "output.txt" instead of printing it to the console.

```python
name = "John"
age = 25
with open("output.txt", "w") as f:
    print(name, age, file=f)

```

Output:

This will create a new file named "output.txt" in the current working directory with the following content:

```
John 25
```

Using flush parameter:

In this example, we use the flush parameter to immediately flush the output buffer, which means that the output is immediately printed to the console instead of waiting for the buffer to fill up.

```python
import time

for i in range(5):
	print(i, end=" ")
	time.sleep(1)
	print("seconds elapsed", flush=True)
```

Output:

This will print the numbers from 0 to 4 with the message "seconds elapsed" after each number. The flush parameter ensures that the output is immediately printed to the console.

### Output:

The output of the above code will be:
```
What is your age? 27
Your age is: 27
```

### Note:

* The `input()` function always returns a string, so if you need to use the input as an integer or a float, you need to convert it using the `int()` or `float()` functions.

* The `input()` function can be used for a wide range of input types such as strings, numbers, and other data types.