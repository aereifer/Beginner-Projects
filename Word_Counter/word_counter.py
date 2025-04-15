#The Word Counter Challenge
"""
Analyzes a text file and outputs a new file containing a frequency list of all the unique words and their counts
"""

def remove_punc(text):
    punc_list = [".", ",", "!", "?","'",'"',"(", ")", ":", ";"]
    
    for punc in punc_list:
        text = text.replace(punc, "")
        
    return text

word_dict = {}

with open("file path", "r") as text_file:
    contents = text_file.read()

new_contents = remove_punc(contents).lower().split(" ")

for word in new_contents:
    if word in word_dict.keys():
        word_dict[word] += 1
    else:
        word_dict[word] = 1

for word, num in word_dict.items():
    print(f"{word}: {num}")