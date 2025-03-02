def printwords(words):
    for i in range(15):
        print(words[i])
#creates board position
def gstart(): #creates board where 
    board = [[3,0,0,1.2,0,0,0,3,0,0,0,1.2,0,0,3],[0,2,0,0,0,1.3,0,0,0,1.3,0,0,0,2,0],[0,0,2,0,0,0,1.2,0,1.2,0,0,0,2,0,0],[1.2,0,0,2,0,0,0,1.2,0,0,0,2,0,0,1.2],
             [0,0,0,0,2,0,0,0,0,0,2,0,0,0,0],[0,1.3,0,0,0,1.3,0,0,0,1.3,0,0,0,1.3,0],[0,0,1.2,0,0,0,1.2,0,1.2,0,0,0,1.2,0,0],[3,0,0,1.2,0,0,0,2,0,0,0,1.2,0,0,3],
             [0,0,1.2,0,0,0,1.2,0,1.2,0,0,0,1.2,0,0],[0,1.3,0,0,0,1.3,0,0,0,1.3,0,0,0,1.3,0],[0,0,0,0,2,0,0,0,0,0,2,0,0,0,0],
             [1.2,0,0,2,0,0,0,1.2,0,0,0,2,0,0,1.2],[0,0,2,0,0,0,1.2,0,1.2,0,0,0,2,0,0],[0,2,0,0,0,1.3,0,0,0,1.3,0,0,0,2,0],[3,0,0,1.2,0,0,0,3,0,0,0,1.2,0,0,3]]
    words = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    tilepoints = {'E': 1, 'A': 1, 'I': 1, 'O': 1, 'N': 1, 'R': 1, 'T': 1, 'L': 1, 'S': 1, 'U': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10, '*':0}
    print("game start")
    return(board, words, tilepoints)
import numpy as np
def addword(words,word, pos, dir, dictionary):#adds a word ""robustly"""
    [b1,w1,t1] = gstart()
    if words + w1:
        0
    w1 = words
    if len(word) >15 or word not in dictionary:#is word allowed
        print("incompatable word")
        return (0)
    if dir != "d" and dir != "a":#is direction?
        print("incompatable direction (""d"" or ""a"")")
    for i in range(len(word)):
        if dir == 'd':#down or accross
            if w1[pos[0]+i][pos[1]] == 0 or w1[pos[0]+i][pos[1]] == word[i]:#word overlaps?
                w1[pos[0]+i][pos[1]]=word[i]#adds word
            else:
                print("overlapped word")
                return(words)
        elif dir == 'a':#down or across
            if w1[pos[0]][pos[1]+i] == 0 or w1[pos[0]][pos[1]+i] == word[i]:#||
                w1[pos[0]][pos[1]+i]=word[i]#||
            else:
                print("overlapped word")
                return(words)
    print("done")
    return(w1)
[b2,w2, tilepoints1] = gstart()
def scoreletter(board, letter, tile, tilepoints):
    scoredletter = (board[tile[0]][tile[1]]%1)*10*tilepoints[letter]
    if scoredletter==0:
        scoredletter= tilepoints[letter]
    multiplier = board[tile[0]][tile[1]]
    if multiplier%1 == 0 and multiplier!= 0:
        1
    else:
        multiplier = 1
    return scoredletter, multiplier
def scoreword(words, word, pos, dir, board, tilepoints):#scores given word
    words1 = words #as to not mess with words
    pos2 = []#describes a list of positions for each i in range len word - all letters already defined by words
    score = 0 #return val
    tempscore = 0
    for i in range(len(word)): #creating pos2
        if dir == 'd':#down or accross
            pos2.append([pos[0]+i,pos[1]])
        elif dir == 'a':#||
            pos2.append([pos[0],pos[1]+i])
    popper=0
    for i in range(len(pos2)):
        if words[pos2[i-popper][0]][pos2[i-popper][1]] != 0:
            pos2.pop(i-popper)
            popper += 1 
    #print(pos2)
    #print(len(pos2))
    for i in range(2):#checks score from above and below word
        if i == 0:#going up or left
            if dir == 'd':#down or accross
                temppos = [pos2[0][0]-1,pos2[0][1]]#up one posistion
                if words[temppos[0]][temppos[1]] != 0:#if letter there
                    while words[temppos[0]][temppos[1]] != 0:#calcs letter not associated with word on main line of word
                        tempscore+= tilepoints[words[temppos[0]][temppos[1]]]
                        temppos[0]+= -1
            elif dir == 'a':#||
                temppos = [pos2[0][0],pos2[0][1]-1]
                if words[temppos[0]][temppos[1]] != 0:
                    while words[temppos[0]][temppos[1]] != 0:
                        #print(temppos)
                        #print(words[temppos[0]][temppos[1]])
                        #print(tilepoints["M"])
                        #print(tilepoints[words[temppos[0]][temppos[1]]])
                        tempscore+= tilepoints[words[temppos[0]][temppos[1]]]
                        temppos[1]+= -1
        else:#going down or right
            if dir == 'd':#down or accross
                temppos = [pos2[0][0]+1,pos2[0][1]]
                if words[temppos[0]][temppos[1]] != 0:
                    while words[temppos[0]][temppos[1]] != 0:
                        tempscore+= tilepoints[words[temppos[0]][temppos[1]]]
                        temppos[0]+= +1
            elif dir == 'a':#||
                temppos = [pos2[0][0],pos2[0][1]+1]
                if words[temppos[0]][temppos[1]] != 0:
                    while words[temppos[0]][temppos[1]] != 0:
                        tempscore+= tilepoints[words[temppos[0]][temppos[1]]]
                        temppos[1]+= +1
    mult1 = []
    scoredword = tempscore
    for i in range(len(pos2)):
        temp1,temp2 = scoreletter(board, word[i], pos2[i], tilepoints)
        scoredletter1 = temp1
        #print(scoredletter1)
        mult1.append(temp2)
        scoredword += scoredletter1
        #print(scoredword)
    mult_t = 1
    for i in range(len(mult1)):
        mult_t *= mult1[i]
    score = scoredword*mult_t
    #print()
    #print(score)
    for k in range(len(pos2)):
        tempscore = 0
        if dir == "d":
            for l in range(2):
                if l == 0:
                    temppos = [pos2[k][0],pos2[k][1]-1]
                    while words[temppos[0]][temppos[1]] != 0:
                        tempscore+= tilepoints[words[temppos[0]][temppos[1]]]
                        temppos[1]+= -1
                if l == 1:
                    temppos = [pos2[k][0],pos2[k][1]+1]
                    while words[temppos[0]][temppos[1]] != 0:
                        tempscore+= tilepoints[words[temppos[0]][temppos[1]]]
                        temppos[1]+= +1
        else:
            for l in range(2):
                if l == 0:
                    temppos = [pos2[k][0]-1,pos2[k][1]]
                    #print(temppos)
                    while words[temppos[0]][temppos[1]] != 0:
                        tempscore+= tilepoints[words[temppos[0]][temppos[1]]]
                        temppos[0]+= -1
                if l == 1:
                    temppos = [pos2[k][0]+1,pos2[k][1]]
                    #print(temppos)
                    while words[temppos[0]][temppos[1]] != 0:
                        tempscore+= tilepoints[words[temppos[0]][temppos[1]]]
                        temppos[0]+= +1
        if tempscore != 0:
            scoredletter1, mult1 = scoreletter(board, word[i], pos2[i], tilepoints)
            score += (tempscore+scoredletter1)*mult1
        #print()
        #print(type(tempscore), type(scoredletter1), type(mult1))
        #print()
        #print(score)
    '''
    for i in range(len(pos2)):
        print(board[pos2[i][0]][pos2[i][1]])
        '''
    return score

from fdictsearch import dictwrite
d1 = dictwrite('dictionary.txt')

#w1[0][0] = "s"
#w2 = addword(w2,"SMART",[7,7],"d",d1)

#printwords(w2)
#tilepoints1 = {'E': 1, 'A': 1, 'I': 1, 'O': 1, 'N': 1, 'R': 1, 'T': 1, 'L': 1, 'S': 1, 'U': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10, '*':0}
#

'''if 'M' in tilepoints1:
    print(tilepoints1['M'])
else:'''
    #print("Error: not found in tilepoints")
#a= scoreword(w2,"START",[7,7],"a",b2,tilepoints1)
#print()
#print(a) 
#print(sum(a))
#print(tilepoints["M"])
#w2 = addword(w2,"START",[7,7],"a",d1)
#printwords(w2)
#print(tilepoints1["M"])
#scoreword(w2,"MA",[8,7],"a",b2,tilepoints1)