def num_words(text):
    return len(text.split())


def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


def sort_on(item):
    return item["num"]  # item is a dict, "num" is the string key


def sorted_character_count(character_dict):
    character_list = []
    for char, count in character_dict.items():
        character_list.append({"char": char, "num": count})
    character_list.sort(key=sort_on, reverse=True)
    return character_list
