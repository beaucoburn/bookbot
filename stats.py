def get_num_words(book_text):
    return len(book_text.split())

def count_char(book_text):
    dict = {}
    text = book_text.lower()
    for t in text:
        if t not in dict:
            dict[t] = 1
        else:
            dict[t] += 1
    return dict

