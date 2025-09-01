filename = input("Enter filename: ")
books = []
try:
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            books.append(line)
        print(books)
except FileNotFoundError:
    print("Cound not find the file named: " + filename)
except OSError:
    print("Could not open the file named: " + filename)
except Exception:
    print("An unexpected error occured")
