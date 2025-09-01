import sys

filename = input("Enter filename: ")
books = []
try:
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            books.append(line)
        print(books)
except FileNotFoundError as e:
    print("FileNotFoundError:", e)
    sys.exit()
except OSError as e:
    print("OSError:", e)
    sys.exit()
except Exception as e:
    print(type(e), e)
    sys.exit()
