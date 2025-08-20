import pickle

with open("books.bin", "rb") as f:
    books = pickle.load(f)
    for book in books:
       print(book)
