import unidecode
  
text = open("./text.txt", "r") 
textData = open('./textData.txt', 'w')
d = dict() 
  
for line in text: 
    
    line = line.strip() 
    line = line.lower() 
    line = unidecode.unidecode(line)

    specialChars = "!#$%^&?*():;/><." 

    for specialChar in specialChars:
        line = line.replace(specialChar, '')

    line = line.replace(',', ' ')
    line = line.replace('\'', '\' ')

    words = line.split(" ") 
  
    for word in words: 
        if word in d: 
            d[word] = d[word] + 1
        else: 
            d[word] = 1
  

for k, v in sorted(d.items(), key=lambda x: x[1]):
    print("%s: %s" % (k, v))
    data = "%s: %s" % (k, v)

    textData.write(data + '\n')


