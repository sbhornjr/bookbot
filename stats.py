def get_word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count

def get_letter_counts(text):
    letter_counts = {}
    for letter in text:
        letter = letter.lower()
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts

def sort_on(dict):
    return dict["count"]

def sort_letter_counts(letter_counts):
    list_of_dicts = []
    for letter in letter_counts:
        dict = {}
        dict["letter"] = letter
        dict["count"] = letter_counts[letter]
        list_of_dicts.append(dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
