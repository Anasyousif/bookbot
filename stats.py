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

def sort_on(dict):
    return dict["num"]

def sorted_counts(text): 
    a = []
    counts = count_chars(text)
    for count in counts: 
        if count.isalpha(): 
            a.append({"char": count, "num": counts[count]})
    a.sort(reverse=True,key=sort_on)
    return a