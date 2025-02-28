def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    characters = {}
    for character in text.lower():
        if character.isalpha() is False:
            pass
        elif character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters

def get_sorted_dict(char_count):
    sorted_items = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    sorted_list_of_dicts = [{key: value} for key, value in sorted_items]
    return sorted_list_of_dicts