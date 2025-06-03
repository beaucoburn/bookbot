def get_book_text(file_path):
    with open(file_path, 'r') as f:
        book_text = f.read()
        return book_text

def main(file_path):
    book_text = get_book_text(file_path)
    print(book_text)

main("books/frankenstein.txt")
