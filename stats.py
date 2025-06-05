def get_num_words(book_text):
    return len(book_text.split())

def count_char(book_text):
    new_dict = {}
    text = book_text.lower()
    for t in text:
        if t not in new_dict:
            new_dict[t] = 1
        else:
            new_dict[t] += 1
    return new_dict

def sort_char_count(new_dict):
    """
    Takes a dictionary of characters and their counts and returns a sorted list of dictionaries.
    Each dictionary contains 'char' and 'num' keys.
    Sorted from greatest to least by count.
    """
    # Convert dictionary to list of dictionaries
    char_list = []
    for char, count in new_dict.items():
        char_list.append({"char": char, "num": count})
    
    # Sort by count in descending order (greatest to least)
    char_list.sort(key=lambda x: x["num"], reverse=True)
    
    return char_list
