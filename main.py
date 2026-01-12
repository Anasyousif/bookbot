from stats import count_words
def getbook_text(path) :
    with open(path) as f:
        return f.read()     

def main (): 
    path = "books/frankenstein.txt"
    text = getbook_text(path)
    num_words = count_words(text)
    print(f"Found {num_words} total words")

main()