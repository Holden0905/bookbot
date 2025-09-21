def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    text = text.lower()
    chars = {}
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_char_counts(char_counts):
    sorted_list = []
    for char, count in char_counts.items():
        if char.isalpha():  # skip spaces, punctuation, etc.
            sorted_list.append({"char": char, "num": count})

    def sort_on(item):
        return item["num"]

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list





