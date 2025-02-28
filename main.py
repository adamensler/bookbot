from stats import get_num_words, get_char_count, get_sorted_dict
import sys



def main():
    # book_path = sys.argv[0]
    try:
        text = get_book_text(sys.argv[1])
        num_words = get_num_words(text)
        char_count = get_char_count(text)
        sorted_dict = get_sorted_dict(char_count)
        print(f"Found {num_words} total words")
        for entry in sorted_dict:
            for key, value in entry.items():
                print(f"'{key}: {value}'")
    except:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()