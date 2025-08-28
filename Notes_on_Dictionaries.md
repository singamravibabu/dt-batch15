- Unlike a list, which is an ordered collection of items, a dictionary is an unordered collection of items.
- There's no gurantee that the items in a dictionary remain in the same order.

- In a dictionary, each item consists of a key/value pair where each value in the dictionary is indexed by a unique key.
- Syntax:
    dictionary_name = {key1:value1, key2:value2, key3:value3, ...}
    - The key can be any immutable data type, but its usually a string.

##### Getting an item from a dictionary
- Syntax:
    dictionary_name[key]

##### Setting an item in a dictionary
- Syntax:
    dictionary_name[key] = newValue

#### Adding an item to a dictionary
- Syntax:
    dictionary_name[newKey] = newValue

#### Checking Whether a Key is in the Dictionary
- Syntax:
    key in dictionary_name
    - If key is in dictionary_name it returns True; otherwise False.

#### The get() method of a dictionary
- Syntax:
    dictionary_name.get(key[, default_value])
- To prevent a KeyError from occuring, we can use te get() method of a dictionary.

#### Delete items from a dictionary
- We can delete item from a dictionary using:
    1. del keyword
    2. pop() method
    3. clear() method

- Syntax for del keyword
    del dictionary_name[key]
- Syntax for pop() method
    dictionary_name.pop(key[, default_value])
- Syntax for clear() method
    dictionary_name.clear()
