# WORKING WITH STRINGS

- Python uses Unicode to store the characters in strings.
- Unicode maps each character to an integer (oridinal) value.

###### Two built-in functions
1. ord(char)
    Returns an integer (ordinal) value for the given Unicode character.
2. chr(ordinal)
    Returns the character for the given Unicode integer.
3. len(str)
    Returns an integer for the length of the specified string.

##### Index to access a character in a string
```
str1 = value
str1[index]
```

##### Strings are immutable
- A string is immutable, which means that we can't change its characters.
- If we attempt to do that, Python raises a TypeError.

##### Slicing a string
- Slicing a string works the same as slicing a list.
- Syntax:
    my_string[start:end:step]

##### Duplicating a string
- Duplicating a string works same way as duplicating a list.
-  Use the repeatition operator (*).
- Syntax:
    str * int

##### Triple Quotes
- Triple quotes are used for strings that are used within programs, not for displays.
- Use the triple quotes to create a multiline string.

##### Searching a String
- Syntax:
    term in string
- Searches for term in string
    - If the term in string it returns True; otherwise False.
Syntax:
    term not in string
    - If the term not in string it returns True; otherwise False.

##### Using an 'if' statement to check a search
```
if term in string:
    block
```

##### Looping over each character of a string
```
for char in string:
    block
```

#### Basic String Methods
1. isalpha()
    Returns True if all the characters are alphabetic letters; otherwise False.
2. islower()
    Returns True if all the characters are lowercase letters; otherwise False.
3. isupper()
    Returns True if all the characters are uppercase letters; otherwise False.
4. isdigit()
    Returns True if all the characters are digits; otherwise False.
5. startswith(str)
    Returns True if the string starts with str; otherwise False.
6. endswith(str)
    Returns True if the string ends with str; otherwise False.
7. lower()
    Converts a string to lowercase and returns it.
8. upper()
    Converts a string to uppercase and returns it.
9. title()
    Converts a string to title case and returns it.
10. lstrip()
    Strips the whitspaces from the left and returns the string.
11. rstrip()
    Strips the whitspaces from the right and returns the string.
12. strip()
    Strips the whitspaces from both sides and returns the string.
13. ljust(width)
    Returns a left-justified string with spaces add to fill the width
14. rjust(width)
    Returns a right-justified string with spaces add to fill the width
15. center(width)
    Returns a centered string with spaces add to fill the width


##### Finding a substring index (position) in a larger string
```
find(str[, strat][, end])
```
- Searches for the specified str and returns the index of the first occurances or -1 if te str isn't found.
- The optiona start and end parameters let us set the staring and ending indexes for the search.

##### Replace old string with new string
```
replace(old, new[, num])
```

- Returns a new string with occurances of the old substring replaced by the new substring.
- The optiona third parameter allows us to specify the number of occurances to replace.


#### Splitting the string
- A delimiter is a character that's used to divide a string into multiple parts.
```
slit([delimiter][, num])
```
- Uses a delimiter to split a string into substrings.
- By default, the delimier is any whitespace.
- The second parameter lets us specify the number of occurances to replace.
- Returns a list of substrings.


##### Joining Strings
- Lists and strings are sequences.
- A string is a sequence of characters.
- We can join a string using join() method.
```
str.join(sequence)
```
Joins the elements of a sequence into a string that uses the current string as a delimitter.

