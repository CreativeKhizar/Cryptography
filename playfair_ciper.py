def getPosition(ch,matrix):
    if(ch=='j'):
        ch='i'
    for i in range(5):
        for j in range(5):
            if matrix[i][j]==ch:
                return [i,j]

def encodeText(pt,matrix):
    pairs=[]
    for i in pt:
        if len(pairs)==0:
            pairs.append([i])
        else:
            if len(pairs[-1])==2:
                pairs.append([i])
            else:
                if pairs[-1][0]==i:
                    pairs[-1].append('x')
                    pairs.append([i])
                else:
                    pairs[-1].append(i)
    if len(pairs[-1])==1:
        pairs[-1].append('z')
    en=''
    for i in pairs:
        x1,y1=getPosition(i[0],matrix)
        x2,y2=getPosition(i[1],matrix)

        # Checking for Same Row
        if(x1==x2):
            en+=matrix[x1][(y1+1)%5]+matrix[x2][(y2+1)%5]
        # Checking for Same Column
        elif(y1==y2):
            en+=matrix[(x1+1)%5][y1]+matrix[(x2+1)%5][y2]
        # Not Same Column and Row
        else:
            en+=matrix[x1][y2]+matrix[x2][y1]
    return en

def decodeText(en,matrix):
    de=''
    for i in range(0,len(en),2):
        x1,y1=getPosition(en[i],matrix)
        x2,y2=getPosition(en[i+1],matrix)

        # Checking for Same Row
        if(x1==x2):
            y1=y1-1
            if y1<0:
                y1=y1+5
            y2=y2-1
            if y2<0:
                y2=y2+5
            if matrix[x1][y1] not in 'xz':
                de+=matrix[x1][y1]
            if matrix[x2][y2] not in 'xz':
                de+=matrix[x2][y2]
        # Checking for Same Column
        elif(y1==y2):
            x1=x1-1
            if x1<0:
                x1=x1+5
            x2=x2-1
            if x2<0:
                x2=x2+5
            if matrix[x1][y1] not in 'xz':
                de+=matrix[x1][y1]
            if matrix[x2][y2] not in 'xz':
                de+=matrix[x2][y2]
        # Not Same Column and Row
        else:
            y1,y2=y2,y1
            if matrix[x1][y1] not in 'xz':
                de+=matrix[x1][y1]
            if matrix[x2][y2] not in 'x':
                de+=matrix[x2][y2]
    return de

def createMatrix(key):
    ds=[0 for i in range(26)]
    matrix=[[0 for i in range(5)] for j in range(5)]
    j=0
    for i in key:
        if ds[ord(i)-97]==0:
            matrix[j//5][j%5]=i
            ds[ord(i)-97]=1
            j+=1
    
    for i in range(26):
        if i!=ord('j')-97 and ds[i]==0:
            matrix[j//5][j%5]=chr(i+97)
            j+=1

    return matrix

key=input("Enter the Word for Matrix : ")
matrix=createMatrix(key)

pt=input("Enter the Plain Text : ")
en=encodeText(pt,matrix)

print("Encoded Text is : ",en)
print("Decoded Text is : ",decodeText(en,matrix))
