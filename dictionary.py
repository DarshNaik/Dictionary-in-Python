import json
from difflib import get_close_matches

source = json.load(open("data.json"))

def meaning(word):
    word = word.lower()
    if word in source:
        return source[word]
    elif len(get_close_matches(word,source.keys(),cutoff=0.8))>0:
        ans = input("Did you mean %s instead?(Y/n) : " % get_close_matches(word,source.keys())[0])
        if ans.lower() == "y":
            return source[get_close_matches(word,source.keys())[0]]
        elif ans.lower() == 'n':
            return "The Word is not defined; or perhaps you must be joking(Nice One!!^_^)"
        else:
            return "You are Stupid!!"
    else:
        return "The Word is not defined; or perhaps you must be joking(Nice One!!^_^)"

find_word = input("Enter the word you want meaning for : ")
print(meaning(find_word))
