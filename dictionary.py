import json

source = json.load(open("data.json"))

def meaning(word):
    word = word.lower()
    if word in source:
        return source[word]
    else:
        return "The Word is not defined; or perhaps you must be joking(Nice One!!^_^)"

find_word = input("Enter the word you want meaning for : ")
print(meaning(find_word))
