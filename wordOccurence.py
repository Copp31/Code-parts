# This program will give you the number of times each word is in your text. 
# Drag the text you want to analyze in this folder and name it yourtxt.txt.

# run in your powershell : py wordOccurence.py

import string 
  
text = open("yourtxt.txt", "r") 
d = dict() 
  
for line in text: 
    
    line = line.strip() 
    line = line.lower() 
    line = line.translate(line.maketrans("", "", string.punctuation)) 
  
    words = line.split(" ") 
  
    for word in words: 
        if word in d: 
            d[word] = d[word] + 1
        else: 
            d[word] = 1
  
    for key in list(d.keys()): 
        print(key, ":", d[key]) 

for k, v in sorted(d.items(), key=lambda x: x[1]):
    print("%s: %s" % (k, v))
