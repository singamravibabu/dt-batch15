import csv

def read_books(filename):
    try:
        file = open(filename, newline="")
        try:
            books = []
            reader = csv.reader(file)
            for row in reader:
                books.append(row)
            return books
        except Exception as e:
            print(type(e), e)
        finally:
            file.close()
    except FileNotFoundError as fnfe:
        print("File not found:", fnfe)
    except Exception as e:
        print("An error occurred:", e)
