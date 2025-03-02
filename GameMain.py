import random
from fdrawhand import drawhand
from fgamecreate import gstart,printwords,addword,scoreletter,scoreword
from fdictsearch import dictwrite
d1 = dictwrite("dictionary.txt")
b1,w1,t1 = gstart()
bag = ["A","A","A","A","A","A","A","A","A","B","B","C","C","D","D","D","D","E","E","E","E","E","E","E","E","E","E","E","E","F","F","G","G","G","H","H","I","I","I","I","I","I","I","I","I","J","K","L","L","L","L","M","M","N","N","N","N","N","N","O","O","O","O","O","O","O","O","P","P","Q","R","R","R","R","R","R","S","S","S","S","T","T","T","T","T","T","U","U","U","U","V","V","W","W","X","Y","Y","Z","*","*"]
h1 = []
h2 = []
i = 0
s1 = 0
s2 = 0
while bag!= []:
    print("input 1,2,3,4,5")
    print("1=printwords")
    print("2=addword")
    print("3=scoreword")
    print("4=drawhand")
    print("5=playmove")
    print("----------")
    a= input()
    if a == "1":
        printwords(w1)
    elif a == "2":
        print("input word")
        b = input()
        print("input pos")
        c1 = input()
        c2 = input()
        print("input direction")
        d=input()
        c = [int(c1),int(c2)]
        addword(w1,b,c,d,d1)
    elif a == "3":
        print("input word")
        b = input()
        print("input pos")
        c1 = input()
        c2 = input()
        print("input direction")
        d=input()
        c = [int(c1),int(c2)]
        e = scoreword(w1,b,c,d,b1,t1)
        print(e)
    elif a == "4":
        if i%2==0:
            h1 = drawhand(h1,bag)
            print(h1)
        if i%2==1:
            h2 = drawhand(h2,bag)
            print(h2)
    elif a == "5":
        print("input word")
        b = input()
        print("input pos")
        c1 = input()
        c2 = input()
        print("input direction")
        d=input()
        c = [int(c1),int(c2)]
        e = scoreword(w1,b,c,d,b1,t1)
        print(e)
        addword(w1,b,c,d,d1)
        for i in range(len(b)):
            if i%2==0:
                h1.pop(b[-1])
            elif i%2==1:
                h2.pop(b[-1])
        if i%2==0:
            s1+= e
            print(s1)
        elif i%2==1:
            s2+=e
            print(s2)
        printwords(w1)
        i +=1
    elif a == "6":
        i+=1
    elif a == "7":
        bag = []