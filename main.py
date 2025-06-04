from stats import get_num_words

def get_book_text(file_path):
    with open(file_path, 'r') as f:
        book_text = f.read()
        return book_text

def main(file_path):
    book_text = get_book_text(file_path)
    num_words = get_num_words()
    print(f"{num_words} words found in the document.")

main("books/frankenstein.txt")
