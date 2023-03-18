# Data Types

## Strings

Create a string of "Hello World"
```python
message = "Hello World"
```

pulling out a specific element form a string is called *Subscripting*

Examples:

Print the first character of a string

```python
print("Hello"[0])
```

Output
```
H
```

Print the last character of the string

```python
print("Hello"[4])
```

Output

```
o
```

What happen if the we set a index that not in the string, for example 5

```python
print("Hello"[5])
```

Output

Program throw a Index out of range error

```
IndexError: string index out of range
```

Note : A value inside a single / double quote is a string even you type number inside it like "123"

```python
print("123" + "456")
```

Output

The strings concatenate together.

```
123456
```

## Integer

Hole numbers without any decimal places. Example 4 , 55, 295.

The number 43.24 ❌ is not an integer

Example :

```python
age = 25
```


```python
print(123+456)
```

Output:
```
468
```

Large number can written with underscores

Example:

Consider the number 123,456,789

```python
print(123_456_789)
```

Output
```
123456789
```

## Float

Floats are numbers having decimal places. Example 3.14


## Boolean

Boolean has only two value `True` and `False`.

## Concatenate Strings with Numbers

If we try to concatenate strings with numbers in the following way our program throws a TypeError

```python
num_char = len(input("What is your name?"))
print("Your name has " + num_char + " characters.")
```

Output:
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

## type()

type function provide the type of a data

Example:

```python
num_char = len(input("What is your name?"))
print(type(num_char))
```

Output:

```
<class 'int'>
```

## Typecasting

This is called converting one data type to a another data type, a example would be converting a integer to a string

## str()

The str function covert a number to a string

Example

```python
num_char = len(input("What is your name?"))
print("Your name has " + str(num_char) + " characters.")
```

Output
```
What is your name?
Sam
Your name has 3 characters.
```

Converting a string to float
```python
print(70 + float("100.5"))
```
Output
```
170.5
```

Coverting a number to string

```python
print(str(70) + str(100))
```

Output
```
70100
```

## Mathematical Operations in Python

```python
print(3 + 5)
print(7 - 4)
print(3 * 2)
print(6 / 3)
print(2 ** 3)
```

Output:
```
8
2
6
2.0
8
```

When there are multiple operations the in the same line the following order take in place.

### PEMDAS Left to Right
1. Parentheses ()
2. Exponents **
3. Multiplication *
4. Division /
5. Addition +
6. Subtraction -

Example:

```python
print(3 * 3 + 3 / 3 - 3)
```

Output
```
7.0
```

```python
print(3 * (3 + 3) / 3 - 3)
```

Output
```
3.0
```

## round()

round function round a value

```python
print(round(8 / 3))
```

Output:
```
3
```
Round to 2 decimal places

```python
print(round(2.66666666666,2))
```

Output
```
2.67
```
Output without the floating point number
```python
print(type(8 // 3))
```

Output
```
2
```

## Manipulate the previous value

```
score = 4 + 5
score =+ 1
print(score)
```

## f'string
```python
score = 0
height = 1.8
isWinning = True

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
```

Output
```
your score is 0, your height is 1.8, you are winning is True
```
