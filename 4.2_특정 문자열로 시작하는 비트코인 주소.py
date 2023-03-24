from Crypto.Hash import RIPEMD160
import base58check
import os
import random
import time
import hashlib


p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
G = [0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
     0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8]
a = 0
b=7

def get_private_key():
    while (True):
        random_str = os.urandom(256 // 8) + str(random.random()).encode() + str(time.time()).encode()
        random_num = hashlib.sha256(random_str).digest()
        private_key = int.from_bytes(random_num, 'big')
        if private_key < p:
            break
    return private_key

def euclidian(b, n):
    r1 = n
    r2 = b if b > 0 else b+n
    t1 = 0
    t2 = 1
    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        r1 = r2
        r2 = r
        t = t1 - q * t2
        t1 = t2
        t2 = t
    if r1 == 1:
        return t1 if t1 > 0 else t1 + n
    else:
        return None

def euclidean_algorithm(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x, y = euclidean_algorithm(b, a % b)
        return (gcd, y, x - (a // b) * y)

def find_inverse(a, p):
    gcd, x, y = euclidean_algorithm(a, p)
    if gcd == 1:
        return x % p
    else:
        return None

def add(point1: list, point2: list):
    if point1 == point2:
        w = (3 * point1[0] ** 2 + a) * euclidian((2 * point1[1]),p) % p
    else:
        w = (point2[1]- point1[1]) * euclidian( point2[0] - point1[0], p) % p
    if w < 0:
        w += p
    x3 = (w ** 2 - point1[0] - point2[0]) % p
    y3 = (w * (point1[0] - x3) - point1[1]) % p
    if x3 < 0:
        x3 += p
    if y3 < 0:
        y3 += p
    point3 = [x3, y3]
    return point3


def double_and_add(x, G: list):
    binary = bin(x)
    K = G
    for i in range(3, len(binary)):
        if binary[i] == '1':
            K = add(add(K, K), G)
        else:
            K = add(K, K)

    return tuple(K)

def get_bitcoin_addr(hex_public_key : list):
    #1. Take the corresponding public key generated with it (33 bytes, 1 byte 0x02 (y-coord is even), and 32 bytes corresponding to X coordinate)
    if(public_key[1]%2==0):
        x="02"+str(hex_public_key[0])[2:]
    else:
        x="03"+str(hex_public_key[0])[2:]

    #2. SHA-256 hashing
    x=bytes.fromhex(x)
    x=hashlib.sha256(x).digest()

    #3. RIPEMD-160 hashing
    x = RIPEMD160.new(x).hexdigest()

    #4. Add version byte in front of RIPEMD-160 hash (0x00 for Main Network)
    x = "00"+str(x)

    #5. Perform SHA-256 hash on the extended RIPEMD-160 result
    public_key_hash=bytes.fromhex(x)
    public_key_hash=hashlib.sha256(public_key_hash).digest()

    #6. Perform SHA-256 hash on the result of the previous SHA-256 hash
    public_key_hash=hashlib.sha256(public_key_hash).hexdigest()

    #7. Take the first 4 bytes of the second SHA-256 hash. This is the address checksum
    checksum = str(public_key_hash)[:8]

    #8. Add the 4 checksum bytes from stage 7 at the end of extended RIPEMD-160 hash from stage 4. This is the 25-byte binary Bitcoin Address.
    bitcoin_addr = x+checksum

    #9. Convert the result from a byte string into a base58 string using Base58Check encoding. This is the most commonly used Bitcoin Address format
    bitcoin_addr= bytes.fromhex(bitcoin_addr)
    bitcoin_addr = base58check.b58encode(bitcoin_addr)
    return str(bitcoin_addr)[2:-1]

def find_bitcoin_addr(want_str, hex_public_key):
    if "0" in want_str or "O" in want_str or "I" in want_str or "l" in want_str:
        print("0,O,I,l이 들어간 문자열은 사용할수 없습니다")
        want_str = input("희망하는 주소의 문자열")
        find_bitcoin_addr(want_str, hex_public_key)

    addr = get_bitcoin_addr(hex_public_key)

    if want_str == addr[1:len(want_str) + 1]:
        print(addr)
    else:
        find_bitcoin_addr(want_str, hex_public_key)


private_key = get_private_key()
public_key = double_and_add(private_key, G)
hex_public_key = (hex(public_key[0]), hex(public_key[1]))
want_str = input("희망하는 주소의 문자열")
find_bitcoin_addr(want_str, hex_public_key)
