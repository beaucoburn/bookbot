import sys
from stats import get_num_words
from stats import count_char
from stats import sort_char_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path, 'r') as f:
        book_text = f.read()
        return book_text

def main(file_path):
    book_text = get_book_text(file_path)

    print("\n============ BOOKBOT ============")
    print("Analyzing book found at {file_path}...")
    print("\n----------- Word Count -----------")
    print(f"Found {get_num_words(book_text)} total words")
    char_counts = count_char(book_text)
    sorted_char_list = sort_char_count(char_counts)
    
    print("\n---------Character Count---------")
    for new_dict in sorted_char_list:
        char = new_dict["char"]
        count = new_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")

main(sys.argv[1])
