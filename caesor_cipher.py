def encode(pt,key):
    en=""
    for i in pt:
        if i==' ':
            en+=' '
        else:
            nc=chr(97+(ord(i)+key-97)%26)
            en+=nc
    return en

def decode(ct,key):
    de=''
    for i in ct:
        if i==' ':
            de+=' '
        else:
            n=ord(i)-97-key
            if(n<0):
                n+=26
            n+=97
            de+=chr(n)
    return de

pt=input('Enter the Plain Text : ')
key=int(input("Enter the key value : "))

en=encode(pt,key)

print("Encoded String is : "+en)
print("Decoded STring is : "+decode(en,key))
