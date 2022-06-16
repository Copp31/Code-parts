# This program will give you the occurrence of each word in your text. 
# Put all the text you want to analyze in the same folder and name it sample.txt.

# run in your powershell :           py recurrenceMots.py

import string 
  
text = open("sample.txt", "r") 
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
