import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()
def main():
    # require exactly one argument: the path to the book file
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    text = get_book_text(path)

    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("------- Character Count ---------")

    char_counts = get_char_counts(text)
    sorted_chars = sort_char_counts(char_counts)
    for item in sorted_chars:
        char = item["char"]
        count = item["num"]
        print(f"{char}: {count}")

    print("============= END ===============")


main()