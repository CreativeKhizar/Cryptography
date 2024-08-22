# Column Transposition
ns=''
def getMinIndex(ds):
    index=-1
    val=1000000
    for i in range(len(ds)):
        if val>ds[i]:
            val=ds[i]
            index=i
    ds[index]=1000000
    return index

def createMatrix(plain,key):
    global ns
    ds=[0 for i in range(26)]
    n=len(key)
    mat=[]
    i=0
    lst=[]
    while(i<len(plain)):
        ds[ord(plain[i])-97]+=1
        if i!=0 and i%n==0:
            mat.append(lst)
            lst=[]
        lst.append(plain[i])
        i+=1
    
    if len(lst)!=0:
        if len(lst)==n:
            mat.append(lst)
        else:
            i=0
            while len(lst)!=n:
                if ds[i]==0:
                    ns+=chr(97+i)
                    lst.append(chr(97+i))
                i+=1
            mat.append(lst)
    return mat

def getString(mat,key):
    st=''
    ds=[int(i) for i in key]
    i=0
    n=len(key)
    while(i<n):
        j=getMinIndex(ds)
        k=0
        while(k<len(mat)):
            st+=mat[k][j]
            k+=1
        i+=1
    return st

def encode(mat,key):
    return getString(mat,key)

def decode(en,key):
    global ns
    n=len(key)
    m=len(en)//n
    ds=[int(i) for i in key]
    mat=[[0 for i in range(n)] for j in range(m)]
    ind=0
    for i in range(n):
        j=getMinIndex(ds)
        k=0
        while(k<m):
            mat[k][j]=en[ind]
            ind+=1
            k+=1
    de=''
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] not in ns:
                de+=mat[i][j]
    return de
        
    
plain=input('Enter the Plain Text : ')
key=input('Enter the Key : ')
mat=createMatrix(plain,key)
es=encode(mat,key)
print('Encoded Message is : ',es)
ds=decode(es,key)
print('Original Message is : ',ds)
