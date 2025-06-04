def get_book_text(file_path):
    with open(file_path, 'r') as f:
        book_text = f.read()
        return book_text

num_words = 0
def word_count(book_text):
    num_words = book_text.split()
    print(f"{num_words} words found in the document")


def main(file_path):
    book_text = get_book_text(file_path)
    print(book_text)

main("books/frankenstein.txt")
