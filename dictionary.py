import json
from difflib import get_close_matches

source = json.load(open("data.json"))


def meaning(word):
    word = word.lower()
    if word in source:
        return source[word]
    elif word.title() in source: #if user entered "delhi" this will check for "Delhi" as well.
        return source[word.title()]
    elif word.upper() in source:    #if user entered acronyms like USA this program checks that as well
        return source[word.upper()]
    elif len(get_close_matches(word,source.keys()))>0:
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

op = meaning(find_word)
if type(op) == list:
    for i in op:
        print(i)
else:
    print(op)

    
