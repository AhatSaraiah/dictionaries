
# exercise 14:
#count_words(text) that gets a text, and prints the list of words in the text with the number of occurrences of each word

def count_words(text):
    list_text=text.split()

    return {word : list_text.count(word) for word in list_text}


