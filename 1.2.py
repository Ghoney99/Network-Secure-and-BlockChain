def vigenere_E(text, key):
    text=text.upper()
    key=key.upper()
    text=text.replace(" ","")
    key=key.replace(" ","")
    key_index=0
    cipher_text=""

    for c in text:
        cipher_text += chr((ord(c) + ord(key[key_index]) - 2*ord("A")) % 26 + ord("A"))
        key_index = (key_index+1)%len(key)
    
    return cipher_text

def vigenere_D(text, key):
    text=text.upper()
    key=key.upper()
    text=text.replace(" ","")
    key=key.replace(" ","")
    key_index=0
    cipher_text=""

    for c in text:
        temp = (ord(c) - ord(key[key_index]) - 2*ord("A")) % 26
        if temp>=0:
            cipher_text +=chr(temp+ord("A"))
        else:
            cipher_text +=chr(temp+2*ord("A"))

        key_index = (key_index+1)%len(key)
    
    return cipher_text

def autokey_E(text, key):
    text=text.upper()
    text=text.replace(" ","")
    cipher_text=""

    for i in range(len(text)):
        temp = chr((ord(text[i])-ord("A")+int(key))%26+ord("A"))
        cipher_text += temp
        key = ord(text[i])-ord("A")

    return cipher_text

def autokey_D(text, key):
    text=text.upper()
    text=text.replace(" ","")
    cipher_text=""

    for i in range(len(text)):
        temp = (ord(text[i]) - int(key) - ord("A")) % 26
    
        if temp>=0:
            cipher_text +=chr(temp+ord("A"))
        else:
            cipher_text +=chr(temp+2*ord("A"))
    
        key = ord(cipher_text[i])-ord("A")
    return cipher_text

plaintext = input("평문 입력: ")
key = input("Vigenere 암호? ")
vigenere_ciphertext = vigenere_E(plaintext, key)
print("암호문:", vigenere_ciphertext)
print("평문:", vigenere_D(vigenere_ciphertext, key))
key = input("자동 키 암호? ")
autokey_ciphertext = autokey_E(plaintext, key)
print("암호문:", autokey_ciphertext)
print("평문:", autokey_D(autokey_ciphertext, key))