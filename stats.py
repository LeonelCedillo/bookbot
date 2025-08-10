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


def sort_char_counts(char_counts: dict[str, int]) -> list[dict[str, int]]:
    list_dicts = []
    for key, value in char_counts.items():
        list_dicts.append({"char": key, "num": value})

    def sort_on(items: list[dict[str, int]]) -> int:
        return items["num"]

    list_dicts.sort(reverse=True, key=sort_on)
    return list_dicts
