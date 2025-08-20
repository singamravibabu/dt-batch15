import pickle

books = [
    ["Attitude", 150.00, 130],
    ["One Minute Manager", 200.00, 100],
    ["The Power of Now", 250.00, 80],
    ["The 7 Habits of Highly Effective People", 300.00, 50],
    ["Think and Grow Rich", 350.00, 30],
    ["The Alchemist", 400.00, 20],
    ["Rich Dad Poor Dad", 450.00, 10]
]

with open("books.bin", "wb") as file:
    pickle.dump(books, file)