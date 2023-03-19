# Conditional Operators

```python
if condition:
	do this
else:
	do this
```

In python we can add certain conditions check and execute different pice of code.

Example:

Imagine you need to write a program to check a person can ride in rollercoaster or not based on their height. A person need to have minimum of 120cm to ride on the rollercoaster

```python
print("Welcome to the rollercoaster")
height =int(input("What is your height in cm? "))

if height > 120:
	print("You can ride in the rollercoaster")
else
	print("Sorry, you can not ride in rollercoaster")
```

Output:
```
Welcome to the rollercoaster
What is your height in cm? 100
Sorry, you can not ride in rollercoaster
```

Output:
```
Welcome to the rollercoaster
What is your height in cm? 130
You can ride in the rollercoaster
```

```
Welcome to the rollercoaster
What is your height in cm? 120
Sorry, you can not ride in rollercoaster
```

## Operators

\>	: Greater than

\>=	: Greater than and equal to

\< : Less than

\<= : Less than and equal to

\== : Equal to

\!= : Not equal to

## Nested Conditions

Nested conditions are conditions under a another condition.

```python
if condition:
	if another condition:
		do this
	else:
		do this
else:
	do this
```

Consider the previous example and about the rollercoaster and now there is additional condition to check the age if the person can ride.

```python
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height > 120:
	print("You can ride in the rollercoaster")
	age = int(input ("What is your age? "))
	if age <= 18:
		print("Please pay $7.00")
	else:
		print("Please pay $12.00")
else
	print("Sorry, you can not ride in rollercoaster")
```

## Nested if else conditions

Consider the previous example and about the rollercoaster and now there is additional more condition to check the age if the person can ride display different prices.

```python
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height > 120:
	print("You can ride in the rollercoaster")
	age = int(input("What is your age? "))
	if age < 12:
		print("Please pay $5.00")
	elif <= 18:
		print("Please pay $7.00")
	else:
		print("Please pay $12.00")
else:
	print("Sorry, you can not ride in rollercoaster")
```

## Multiple if Statements in Succession

Let check if the person want to photo in the rollercoaster and want to add it to bill.

```python
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
	print("You can ride in the rollercoaster")
	age = int(input("What is your age? "))
	if age < 12:
		bill = 5
		print("Your ticket price is $5.00")
	elif <= 18:
		bill = 7
		print("Your ticket price is $7.00")
	else:
		bill = 12
		print("Your ticket price is $12.00")

	wants_a_photo = input("Do you want a photo taken? Y or N.")

	if wants_a_photo == 'Y':
		bill += 3

	print(f"Your total bill is $ {bill}")
else:
	print("Sorry, you can not ride in rollercoaster")
```

## Logical Operator

There are three logical operators `and` , `or` and `not`

A and B : Both conditions need to be True

C or D : One condition need to be True

not E

Add midlife condition to the above code

```python
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
	print("You can ride in the rollercoaster")
	age = int(input("What is your age? "))
	if age < 12:
		bill = 5
		print("Your ticket price is $5.00")
	elif <= 18:
		bill = 7
		print("Your ticket price is $7.00")
		if age >= 45 and age <= 55:
			print("Everything is okay. Have a free ride.")
	else:
		bill = 12
		print("Your ticket price is $12.00")

	wants_a_photo = input("Do you want a photo taken? Y or N.")

	if wants_a_photo == 'Y':
		bill += 3

	print(f"Your total bill is $ {bill}")
else:
	print("Sorry, you can not ride in rollercoaster")
```