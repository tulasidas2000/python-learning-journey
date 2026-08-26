# Leap Year Checker

This is a simple Python project that lets you enter a year and quickly find out whether it is a **Leap Year** or a **Non-Leap Year**. It’s a good beginner project for practicing `if`, `elif`, `else`, and the modulus operator.

## How It Works

A year is a leap year when:

* It is divisible by **400**, or
* It is divisible by **4** but **not divisible by 100**.

## Code

```python
year = int(input('Enter year'))

if year % 100 == 0:
    if year % 400 == 0:
        print('Leap Year')
    else:
        print('Not a Leap Year')
elif year % 4 == 0:
    print('Leap Year')
else:
    print('Not a Leap Year')
```

## Example

```text
Enter year: 2024
Leap Year
```

```text
Enter year: 2025
Not a Leap Year
```

## Requirements

* Python 3.x

## Run the Program

Save the file as `leap_year.py`, then run:

```bash
python leap_year.py
```

## About This Project

You can use this small project to practice:

* Conditional statements
* Nested `if` statements
* The modulus operator (`%`)
* Taking user input in Python

It’s suitable as a simple beginner Python project for your GitHub repository.