import os
import random
import time
import hashlib


def get_private_key():
    while (True):
        random_str = os.urandom(
            256 // 8) + str(random.random()).encode() + str(time.time()).encode()
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
        w = (3 * point1[0] ** 2 + a) * euclidian((2 * point1[1]), p) % p
    else:
        w = (point2[1] - point1[1]) * euclidian(point2[0] - point1[0], p) % p
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


# ECDSA 알고리즘 파라미터 설정
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
e1 = (0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
      0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)
q = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

# 개인키 d
d = 0x123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
# 공개키 e2
e2 = (0xc8b4f4a1d4a825e12973b8a173f5d92b2c5e71686a5935c6c62a44f736f6b587,
      0xe6ec1e6e0d6fe9c704f119677d237ef57ab270f924b142243a6f97d981c372a6)


def sign(M, d):
    while True:
        # 해싱으로 메세지 다이제스트 생성
        h = hashlib.sha256(M.encode()).hexdigest()
        # 1<r<q-1 범위의 임의의수 r을 생성
        r = random.randint(1, q-1)
        # 스칼라 
        #########################
        #### P = scalar_mult(r, e1) -> P=(x1,y1)
        #########################
        S1 = x1 % q
        if S1 == 0:
            continue
        S2 = ((int(h, 16)+d+S1)*find_inverse(r, q)) % q
        if S2 != 0:
            break
    return S1, S2


def verify(M, S1, S2, e2):
    h = hashlib.sha256(M.encode()).hexdigest()
    S2_inverse = find_inverse(S2, q)
    A = (h*S2_inverse)%q
    B = (S1*S2_inverse)%q
    #########################
    ### T = add(scalar_mult(A, e1),  scalar_mult(B, e2)) T=(x, y)
    #########################

    if x % q == S1 % q:
        return True
    else:
        return False


