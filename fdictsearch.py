def dictwrite(filename):#creates oxford dictionary (180,000 words)
    #newdict = # Open the file in read mode
    with open(filename, 'r') as file:
        # Read the contents of the file
        newdict = file.readlines()
    "for i in range(len(newdict)):"
    for i in range(len(newdict)):
        newdict[i] = newdict[i].strip()
    #    newdict[i].removesuffix("n")
    #    #newdict[i].remove("\\n")
    #    #print(newdict[i])
    return newdict

newdict = dictwrite('dictionary.txt')

def elimwords(hand,dictionary):#eliminates all words that are not possible on any board
    if '*' in hand:
        dictionary2 = dictionary
    else:
        dictionary2=[]
        for j in range(len(dictionary)):
            counter = 0
            for k in range(len(dictionary[j])):
                if dictionary[j][k] in hand:
                    counter+=1
            if counter > 0:
                dictionary2.append(dictionary[j])
    return dictionary2
#print(i)
#def collectingletters