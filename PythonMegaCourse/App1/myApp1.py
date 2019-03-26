#!/Volumes/MacintoshSSD/anaconda3/bin/python

import os, time
import json
from difflib import get_close_matches

# first load the data
data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word does not exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist.  Please double check it."

print("Warning!!! If you want to exit from dictionary please write 'exitfrom' to the enter word area")
word = ''
while word != 'exitfrom':
    word = input("Enter word: ")
    if word != 'exitfrom':
        output = translate(word)
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)
    else:
        print("Goodbye my friend! \nThe Program will be shut down in 5 seconds...")
        time.sleep(5)
