from stats import get_num_words
from stats import count_char

def get_book_text(file_path):
    with open(file_path, 'r') as f:
        book_text = f.read()
        return book_text

def main(file_path):
    book_text = get_book_text(file_path)
    print(f"{get_num_words(book_text)} words found in the document.")
    print(f"{count_char(book_text)}")

main("books/frankenstein.txt")
