from stats import get_num_words, character_count, letter_count, sort_on
import sys

def get_book_text(path_to_file):
    with open (path_to_file) as f:
        file_contents = f.read()
        return file_contents
   
def main(path_to_file):
    text = get_book_text (path_to_file)
    words = get_num_words(text)
    characters = character_count(text)
    total = letter_count(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(words)
    print("--------- Character Count -------")
    for item in total:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    print("============= END ===============")

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    main(sys.argv[1])