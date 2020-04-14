import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def reply(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8))>0:
        yn=input( "Did you mean -> %s <- instead , if 'YES' type Y else N?" % get_close_matches(word,data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return "The word does not exist. Please double check it."
    else:
        return "The word does not exist. Please double check it."


    
word=input("Enter the word :").lower()
ans=reply(word)

if(type(ans)==list):
    for item in ans:
        print(item)
else:
    print(ans)