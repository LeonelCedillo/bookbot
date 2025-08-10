from typing import Union

def get_num_words(text: str) -> int:
    count = text.split()
    return len(count)


def count_character_frequencies(text: str) -> dict[str, int]:
    counts = {}
    for character in text:
        char = character.lower()
        if char in counts:
            counts[char] += 1 
        else:
            counts[char] = 1
    return counts


def sort_on(items: list[dict[str, int]]) -> int:
        return items["num"]

def sort_char_counts(char_counts: dict[str, int]) -> list[dict[str, Union[str, int]]]:
    sorted_list = []
    for key, value in char_counts.items():
        sorted_list.append({"char": key, "num": value})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    # list[dict[str, Union[str, int]]]
    # means: 
    # all keys are strings, and values can be either string or int.
