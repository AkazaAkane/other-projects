#from collections import Counter
text = "jia you, ao li gei"


def count_words(text):

    text = text.lower()
    skips = [".",".",";",":","'",'"']
    for ch in skips:
        text = text.replace(ch,"")

    #word_counts = Counter(text.split(""))
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

print(count_words(text))

def read_book(title_path):

    with open(title_path, "r", encoding = "uft8") as current_file:
        text = current_file.read()
        text = text.replace("\n",".").replace("\r","")
    return text

def word_stats(word_counts):
    """
    return number of unique words and word frequencies
    """
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique,counts)
