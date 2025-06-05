from stats import get_num_words
from stats import count_char
from stats import sort_char_count

def get_book_text(file_path):
    with open(file_path, 'r') as f:
        book_text = f.read()
        return book_text

def main(file_path):
    book_text = get_book_text(file_path)
    print(f"Found {get_num_words(book_text)} total words")
    char_counts = count_char(book_text)
    sorted_char_list = sort_char_count(char_counts)
    
    print("\n---Character Report---")
    for new_dict in sorted_char_list:
        char = new_dict["char"]
        count = new_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")

main("books/frankenstein.txt")
