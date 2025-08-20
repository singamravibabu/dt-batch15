# WORKING WITH FILES

##### Two types of files
1. Text
    - Contains one or more lines that contain text characters.
    - In a text file, each line end with a newline character `\n`.
    - On Windows, the newline character is sometimes preceded by a carriage return `\r`: `\r\n`.
    - Common Types:
        - .txt files
        - .csv files
        - .json files
        - .xml files
        - .html files
        - .md files
2. Binary
    - Any file that isn't a text file.
    - Many binary file formats contain parts that can be interperted as text.
    - However, binary files typically contain a sequence of bytes that are intended to be interpreted as something other than text characters.
    - Common types:
        - Compiles program files
        - Image files
        - audio files
        - video files
        - database files
        - compressed files

##### Sequence of file operations
1. Open the file: open()
2. Write data to a file or read data from a file: write(), read(), readlines(), or readline()
3. Close the file: close()


##### Opening a file
- When we open a file we create a file object.
- Then, we can use the methods of the file object to work with the file.

##### The built-in open() function
```
open(file_name, mode)
```
- Returns a file object for the specified file with the specified mode.

###### Modes of the open() function
1. r - Read
    - If the file doesn't exist, this mode causes a file not found error.
2. w - Write
    - If the file doesn't exist, this mode creates a new file.
    - If the file exists, this mode overwrites the existing file.
3. a - Append
    - If the file doesn't exist, this mode creates a new file.
    - If the file exists, this mode appends to the existing file.
4. b - Binary
    - Use for binary files along with "r" or "w" mode.

##### 'with' to close files automatically
- Every file that we open must be closed.
- When we use with statement to open a file, it automatically closes when the block ends.
```
with open(file_name, mode) as file:
    block
```

##### The 'write' method
```
file_object.write(str)
```

##### Reading a file
1. Use `for` loop to read line by line.
2. read() - reads entire file as one string.
3. readlines() - reads a file into a list, where each item is a line of the file.
4. readline() - reads a single line from the file.

### Working with CSV files
- A comma-separated values (CSV) file stores tabular data in a text form.
- Within CSV file, each line is a row that ends with a new line character, and each row contains one or more columns that are typically separated by a comma.
- Rows are records, and columns are fields.
- To work with CSV files, we use the `csv` module.

#### Writing data to a CSV file
- To write data to a csv file we have to use `writer()` function of the csv module to get writer object.
```
csv.writer(file_object)
```
- This writer object converts the data into comma-separated values.
- After creating writer object we use writerows() method of the csv writer object to write to file_object.
- **Note**: When we open a CSV file for reading or writing, we typically specify an argument name 'newline' with a value of an empty string. This enables universal newlines mode, so the reading and writing operations work correctly for all operating systems.

#### Reading data from a CSV file
- Use reader() function from the csv module to get reader object.
```
csv.reader(file_object)
```
- Then use `for` statement with the reader object to read the data in the file.


#### CSV format specification
- Optional arguments with reader() and writer() functions
    - quotechar='"' -> specifies the character that's used to quote columsn\
    - delimiter=',' -> specifies the character that's used to separate fields
    - quoting=csv.QUOTE_MINIMAL -> specifies the quoting policy


### Working with Binary files
- Use `pickle` module to work with binary files.
- The `pickle` module can be used to dump (write) an object like a list to a file, and to load (read) an object from a binary file.
- The dump and load pickle methods
    dump(object, bfile)
    - Writes the specified object to the binary file.
    load(bfile)
    - Reads an object from the binary file.