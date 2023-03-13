from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import base64

from cryptography.fernet import Fernet


#공개키와 개인키
with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(key_file.read(), backend=default_backend())

with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(key_file.read(), password=None, backend=default_backend())


#평문 입력
plain_text = input("평문 메시지를 입력하시오 : ")

#AES
aes_key_original = Fernet.generate_key()
fernet = Fernet(aes_key_original)

#평문을 AES로 암호화
enc_msg = fernet.encrypt(plain_text.encode())

#AES키를 RAS공개키로 암호화
enc_key=base64.b64encode(public_key.encrypt(aes_key_original, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))).decode()


###Receiver
#AES키를 복호화
aes_key = private_key.decrypt(base64.b64decode(enc_key), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

#AES키로 암호문 복호화
decrypt_msg = fernet.decrypt(enc_msg).decode()

#출력
print("평문   :", plain_text)
print("복호문 :", decrypt_msg)