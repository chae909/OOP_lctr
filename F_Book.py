class Book:
    def __init__(self, title, pages, *authors):
        self.title = title
        self.pages = pages
        self.authors = authors

    def __contains__(self, title):
        return title in self.title

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other.title


if __name__ == "__main__":
    books = [Book("한국근현대사", 472, "한국근현대사학회"),
             Book("한국근현대사", 649, "김행선"),
             Book("역사책에없는조선사", 376, "이상호", "이정철")]
    print(books[0] == books[1])

    for book in books:
        if "사" in book:
            print(f'{book.title}, {len(book)}쪽 by {book.authors}')