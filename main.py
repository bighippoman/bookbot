import sys
from stats import num_words
from stats import count_characters
from stats import sorted_character_count


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    book_length = num_words(book_text)
    characters = count_characters(book_text)
    sorted_chars = sorted_character_count(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_length} total words")
    print("--------- Character Count -------")

    for char in sorted_chars:
        print(f"{char['char']}: {char['num']} ")
    print("============= END ===============")


if __name__ == "__main__":
    main()
