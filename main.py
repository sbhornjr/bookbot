from stats import get_word_count, get_letter_counts, sort_letter_counts
import sys

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    word_count = get_word_count(text)
    letter_counts = get_letter_counts(text)
    sorted_letter_counts = sort_letter_counts(letter_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count ---------")
    for d in sorted_letter_counts:
        if d["letter"].isalpha():
            print(f"{d['letter']}: {d['count']}")
    print("============= END =============")

main()