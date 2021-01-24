# Operator precedence

## PEMDASLR

(Parenthesis, Exponent, Multiply+Divide, Add+Subtract, Left to Right)

# Numbers

## Rounding

```python
round(num, decimals)
round(2.6666, 2) # => 2.67
```

# Conditions

## Chained comparsion

A more readable conditional statement is possible in Python

Instead of
```python
if x >= 40 and x <= 50: 
```

**use**

```python
if 40 <= x <= 50:
```

# Loops

## Password generator

Good passwords contains numbers, uppercase and lowercase letters 
(and probably extra characters like '!#_' or something like this). 
By the end of the day 5 we will create a strong password generator.

# Math functions

- round up:
  ```python
  import math
  math.ceil(x)
  ```
-