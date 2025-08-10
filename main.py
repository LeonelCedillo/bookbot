from stats import get_num_words, count_character_frequencies, sort_char_counts


def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    num_words = get_num_words(book)
    char_dict = count_character_frequencies(book)
    sorted_chars_list = sort_char_counts(char_dict)

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


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


main()