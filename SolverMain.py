import random
from functions.fdrawhand import drawhand
from functions.fdictsearch import dictwrite,elimwords
from functions.fgamecreate import *
from functions.fFixDictionary import fixdict
hand = []
bag = ["A","A","A","A","A","A","A","A","A","B","B","C","C","D","D","D","D","E","E","E","E","E","E","E","E","E","E","E","E","F","F","G","G","G","H","H","I","I","I","I","I","I","I","I","I","J","K","L","L","L","L","M","M","N","N","N","N","N","N","O","O","O","O","O","O","O","O","P","P","Q","R","R","R","R","R","R","S","S","S","S","T","T","T","T","T","T","U","U","U","U","V","V","W","W","X","Y","Y","Z","*","*"]
[b1,w1,t1] = gstart()
d1 = dictwrite("dictionary.txt")
print(len(d1))
#addword(w1,"SMART",[7,7],"a",d1)
w1[7][7] = "S"
w1[12][7] = "A"
w1[7][12] = "M"
#printwords(w1)
d2 = fixdict("dictionary.txt")
#print()
#print()
rows = []
collumns = []
drawhand(hand,bag)
print(hand)
for i in range(15):#this currates each row of words to search for the words that fit there
    temp=[]
    f=0
    for j in range(15):#rows
        if w1[i][j] != 0:
            temp.append(f)
            temp.append(w1[i][j])
            f=0
        else:
            f+=1
    temp.append(f)
    rows.append(temp)
    #print(temp)
    temp=[]
    f=0
    for j in range(15):#collumns
        if w1[j][i] != 0:
            temp.append(f)
            temp.append(w1[j][i])
            f=0
        else:
            f+=1
    temp.append(f)
    collumns.append(temp)
    #print(temp)
list_hands_r = {}
list_hands_c = {}
#print(rows,collumns)
for i in range(15):#currating an effective hand to look for candidate words
    temphand = []
    if rows[i] != [15]:
        temphand = []
        for j in range(len(rows[i])):
            if type(rows[i][j]) == str:
                temphand+=rows[i][j]
            #print(hand+temphand)
    if temphand != []:
        list_hands_r[i] = hand+temphand
    else: 
        list_hands_r[i] = 0

    temphand = []
    if collumns[i] != [15]:
        temphand = []
        for j in range(len(collumns[i])):
            if type(collumns[i][j]) == str:
                temphand+=collumns[i][j]
            #print(hand+temphand)
    if temphand != []:
        list_hands_c[i] = hand+temphand
    else: 
        list_hands_c[i] = 0
#print(list_hands_r,list_hands_c)
#print()
#print()
#print(d1[100000])
#print(d2[100000])
starcount = 0
for i in range(len(hand)):
    if hand[i] == "*":
        starcount+=1
print(starcount)
#sorting for possible plays based only on letter
dictionaries = []
tempd=[]
for j in range(15): #for each row
    if list_hands_c[j]!=0:#making sure that we dont loop over the hands that are just hand
        for i in range(len(d2)):#looping over dictionary
            c = starcount
            tempd=d1.copy()
            #print(tempd[1000])
            #print(d1[1000])
            for k in range(len(list_hands_c[j])):#for each in effective hand
                if list_hands_c[j][k] not in d2[i] and starcount == 0 :
                    tempd.remove(d1[i])
                    break
                elif list_hands_c[j][k] not in d2[i]:
                    c-=1
                else:
                    1
            if i%1000 ==0:
                print(i)
    dictionaries.append(tempd)
    print(1)
print(c)
print(dictionaries)
    #calculates for just hand from last dictionary
#ummmm this is taking way to long but ill figure it out later... maybe
#this is a big problem