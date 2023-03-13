import random

key = []
for i in range(ord('a'),ord('z')+1):
    key.append(chr(i));

value = key.copy()
random.shuffle(value)

E={}
for i, val in zip(key, value):
    E[i]=val
D={v:k for k,v in E.items()}

def Encryption(text):
    table = text.maketrans(E)
    text=text.translate(table)
    return text

def Decryption(text):
    table = text.maketrans(D)
    text=text.translate(table)
    return text

print("평문입력: ",end='')
text = input().lower()
ciphertext = Encryption(text)
print("암호문: {}".format(ciphertext))
print("복호문: {}".format(Decryption(ciphertext)))
