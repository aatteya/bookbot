from stats import get_book_words, get_char_dict, get_sorted_dict_list
import sys

def get_book_text(filepath):
    file_str = ""
    with open(filepath) as f:
        file_str = f.read()
    return file_str

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    file_str = get_book_text(file_path)
    num_words = get_book_words(file_str)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    char_dict = get_char_dict(file_str)
    sorted_list_chars = get_sorted_dict_list(char_dict)
    for entry in sorted_list_chars:
        char = entry["char"]
        if not char.isalpha():
            continue
        print(f"{char}: {entry['num']}")

if __name__ == "__main__":
    main()
 