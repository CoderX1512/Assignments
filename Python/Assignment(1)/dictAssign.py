books = {
    "book1": {
        "name": "Atomic Habits",
        "author": "James Clear"

    },
    "book2": {
        "name": "Pride and Prejudice",
        "author": "Jane Austen"

    },
    "book3": {
        "name": "Anna Karenina",
        "author": "J.K Rowling"
    },
    "book4": {
        "name": "The Alchemist",
        "author": "Paulo Coelho"

    },
    "book5": {}

}
books["book3"]["author"] = "Leo Tolstoy"
print(books["book3"]["author"])

new_book = {
    "book5": {
        "name": "Murder on the orient express",
        "author": "Agatha Christie"
    }
}

books.update(new_book)

# for i in books:
#    print(books[i])
for key, value in books.items():
    print(key, ":", value)
