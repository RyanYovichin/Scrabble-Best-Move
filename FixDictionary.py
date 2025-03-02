from fdictsearch import dictwrite
d1 = dictwrite("dictionary.txt")
d2 = []
for i in range(len(d1)):# for over dictionary
    temp = {}
    for j in range(len(d1[i])): # for over letters in word
        c=0
        if d1[i][j] in temp:
            temp[d1[i][j]].append(j+1)
            temp[d1[i][j]].append(len(d1[i])-j-1)
            temp[d1[i][j]].append({})
            c +=1
        else:
            temp[d1[i][j]] = [j+1,len(d1[i])-j-1,{}]
        #print(temp)
        for k in range(len(d1[i])-j):
            if d1[i][j+k] in temp[d1[i][j]][c*3+2]:
                temp[d1[i][j]][c*3+2][d1[i][j+k]].append(k)
            else:
                temp[d1[i][j]][c*3+2][d1[i][j+k]] = []
                temp[d1[i][j]][c*3+2][d1[i][j+k]].append(k)
    d2.append(temp)
    #print(d1[i])
    #print(temp)
print(d1[len(d1)-1])
print(temp)