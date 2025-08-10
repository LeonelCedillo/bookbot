from stats import get_num_words, count_character_frequencies, sort_char_counts
from typing import Union
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    num_words = get_num_words(book)
    char_dict = count_character_frequencies(book)
    sorted_chars_list = sort_char_counts(char_dict)
    print_report(book_path, num_words, sorted_chars_list)

    
def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


# list[dict[str, Union[str, int]]]
# means: 
# all keys are strings, and values can be either string or int.
def print_report(book_path: str, num_words: int, sorted_chars_list: list[dict[str, Union[str, int]]]) -> None: 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars_list:
        if char_dict["char"].isalpha(): 
            print(f"{char_dict["char"]}: {char_dict["num"]}")
    print()
    print("============= END ===============")


main()