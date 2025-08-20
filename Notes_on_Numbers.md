# WORKING WTIH NUMBERS
- A floating-pointnumber is an approximate value that can yield unexpected results knows as floating-point errors.
- Examples of floating-point numbers:
    12.5
    -124.82
    -3.7e-9   # -0.000000037
- Examples of Scientic notation
    2.38E+5     # 2.38 x 10^5
    3.25E-8     # 3.25 x 10^-8


### Formatting Numbers
- The format() method of a string is used to format a single value or a series of vaues by converting them into strings.
- Syntax:
    "...{:format_specification}...".format(data_items)

- Syntax for the *format_specification*:
    [field_width][comma][.deci_places][type_code]

- Common type codes:
    1. d Integer
        Decimal positions can't be specified.
    2. f Floating-point number
        Decimal postions can be specified.
    3. % Percent
        Multiplies the value by 100 and puts a percent sign after it.
    4. e Scientific notation
        Converts the number to scientific notation.

- To align a formatted value use:
    < for left-alignment
    > for right-alignment
    ^ for center-alignment


### Working with Decimal Numbers
- Use the `decimal` module to create decimal numbers that are exact when and don't yield unexpected results.
- when we work with decimal numbers, we usually import the `Decimal` class and any rounding constants we need from the `decimal` module.
- To create a Decimal object that stores a decimal number, pass a string for the decimal number to the constructor of the Decimal class.

- We can use most arithmetic operators with Decimal object.
- In addition, it's legal to code expressions that mix Decimal objects with int objects. However, its illegal to code expressions that mix Decimal objects with float objects.


