import sys
from stats import count_words, count_chars,sorted_counts
def getbook_text(path) :
    with open(path) as f:
        return f.read()     

def main():
    if len(sys.argv) !=2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = getbook_text(path)
    num_words = count_words(text)
    
    # Fix the spelling of 'sorted' here:
    sorted_list = sorted_counts(text) 
    
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")

    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")

    print("--- End report ---")
main()    