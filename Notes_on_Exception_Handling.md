# EXCEPTION HANDLING
- When an error occurs at runtime, it can be referred as throwing an exception.
- When an excpetion occurs, Python ends the program and prints information about the exception.
- Some exceptions occur due to programming errors. We need to fix those errors before the program is ready for use.
- Some exceptions occur due to causes outside of the program.
    - These exceptions need to be handled by our Python code so the program doesn't crash when they occur.

- Two functinos that can cause a ValueError exception.
    int(data)
        - When it can't convert the data argument to an integer
    float(data)
        - When it can't convert the data argument to a floating-point number

#### A `try` statement to handle one type of exception
- Syntax:
    try:
        block   # it may throw an exception
    except [ExceptionName]:
        block   # handle the exception
    
    - If we don't code teh name of an exception type in the `except` clause handles all types of exceptions that can occur.

#### Handling multiple exceptions
- The hierarchy of five common excetions
    Exception
        OSError
            FileExistsError
            FileNotFoundError
        ValueError

**Note:**  The `except` clause must be coded in sequence starting with the most specific exception and ending with the most general exception.

#### A `try` statement to handle multiple exceptions
- Syntax:
    try:
        block   # it may throw an exception
    except [ExceptionName1]:
        block   # handle the exception
    except [ExceptionName2]:
        block   # handle the exception
    except [ExceptionName3]:
        block   # handle the exception
    except [ExceptionName4]:
        block   # handle the exception
    except [ExceptionName5]:
        block

#### The complete `except` clause syntax
- Syntax:
    except [ExceptionName] [as variable]:
        block

- Later we can inspect the variable to which Exception is assigned.

#### The `exit()` function
- The exit() function from the `sys` module exits the Python program.

#### Complete `try` statement with `finally` clause
- Syntax:
    try:
        block
    except [ExceptionName] [as variable]:
        block
    [except [ExceptionName] [as variable]:
        block]...
    finally:
        block

- A `finally` clause is always executed, even if an exception occurs or a retuen statement is executed in the `try` clause.

- Generally, the `finally` clause is defined for clean-up actions manually.

#### Rasing an Exception
- To raise an exception, we can use a `raise` statement that creates an exception object.
- Syntax:
    raise ExceptionName("Error Message")