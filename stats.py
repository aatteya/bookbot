def get_book_words(file_str):
    file_words = file_str.split()
    return len(file_words)

def get_char_dict(text):
    lower_text = text.lower()
    char_dict = {}
    for c in lower_text:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def get_sorted_dict_list(char_dict):
    dict_list = []
    for char in char_dict:
        char_entry = {"char" : char, "num" : char_dict[char]}
        dict_list.append(char_entry)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

