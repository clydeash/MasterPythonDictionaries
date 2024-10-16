book_object1 = {
    "title": "The Lord of the Rings",
    "author": "J.R.R. Tolkien"
}
book_object2 = {
    "title": "Harry Potter and the Sorcerer's Stone",
    "author": "J.K. Rowling"
}
book_object3 = {
    "title": "The Hitchhiker's Guide to the Galaxy",
    "author": "Douglas Adams"
}
book_object4 = {
    "title": "Pride and Prejudice",
    "author": "Jane Austen"
}
book_object5 = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee"
}

books = [book_object1, book_object2, book_object3, book_object4, book_object5]

for book in books:
    print(f"Book Title: {book['title']}, Author: {book['author']}")
