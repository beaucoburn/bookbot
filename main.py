file_path = input("books/frankenstein.txt")
def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
        return book_text
