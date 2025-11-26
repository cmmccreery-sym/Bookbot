import sys
from stats import count_words, get_character_count, sort_dict

def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as fp:
        contents: str = fp.read()
        return contents


def main() -> None:
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath: str = sys.argv[1]

    content: str = get_book_text(filepath)
    num_words: int = count_words(content)
    char_dict: dict[str, int] = get_character_count(content)
    sorted_char_dict = sort_dict(char_dict)

    
    print("============= BOOKBOT ================")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ---------------")
    print(f"Found {num_words} total words")
    print("---------Character Count -------------")

    for pair in sorted_char_dict:
        if pair['char'].isalpha():
            print(f"{pair['char']}: {pair['num']}")

    print("================ END =================")


if __name__ == "__main__":
    main()

