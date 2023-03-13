from cryptography.fernet import Fernet

key = Fernet.generate_key()

fernet = Fernet(key)

with open('data.txt', 'rb') as f:
    data = f.read()

encrypt_data = fernet.encrypt(data)

with open('encrypted.txt', 'wb') as f:
    f.write(encrypt_data)

with open('encrypted.txt', 'rb') as f:
    encrypt_data = f.read()

decrypt_data = fernet.decrypt(encrypt_data)

print(decrypt_data.decode())
