import random
from fdrawhand import drawhand
from fdictsearch import dictwrite,elimwords
from fgamecreate import *
from fFixDictionary import fixdict
hand = []
bag = ["A","A","A","A","A","A","A","A","A","B","B","C","C","D","D","D","D","E","E","E","E","E","E","E","E","E","E","E","E","F","F","G","G","G","H","H","I","I","I","I","I","I","I","I","I","J","K","L","L","L","L","M","M","N","N","N","N","N","N","O","O","O","O","O","O","O","O","P","P","Q","R","R","R","R","R","R","S","S","S","S","T","T","T","T","T","T","U","U","U","U","V","V","W","W","X","Y","Y","Z","*","*"]
[b1,w1,t1] = gstart()
d1 = dictwrite("dictionary.txt")
#addword(w1,"SMART",[7,7],"a",d1)
w1[7][7] = "S"
w1[12][7] = "A"
w1[7][12] = "M"
#printwords(w1)
#d2 = fixdict("dictionary.txt")
for i in range(15):
    temp=[]
    temp2=[]
    c=0
    f=0
    for j in range(15):
        if w1[i][j] != 0:
            temp.append(f)
            temp.append(w1[i][j])
            f=0
        else:
            f+=1
    temp.append(f)
    print(temp)