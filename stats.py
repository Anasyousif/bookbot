def count_words(text) :
    num_words = text.split()
    return len(num_words)   

def count_chars(text): 
    counts = {}
    letter_count = text.lower()
    for letter in letter_count:
        if letter in counts:
            counts[letter] += 1
        else :
            counts[letter] = 1
    return counts
