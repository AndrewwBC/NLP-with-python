from nltk.book import *

# Shows when these words are in commom contexts
print(text2.common_contexts(["monstrous", "very"]))
# Shows similar words used in the text based on the input
print(text1.similar("good"))
print(text2.common_contexts(["good", "pretty"]))

def lexical_diversity(text):
    return len(text) / len(set(text))

def percentage(text, wordToCount): 
    return 100 * text.count(wordToCount) / len(text)
