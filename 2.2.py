import os
import random
import time
import hashlib

p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

# 개인키
while True:
    randomness = str(os.urandom(16))+str(random.random())+str(time.time())
    randomness_byte = randomness.encode()
    randomness_hash = hashlib.sha256(randomness_byte).hexdigest()
    private_key = int(randomness_hash, 16)
    if private_key < p:
        break

# 공개키, K = k*G(공개키 = 개인키 * G)

# x * G의 곱하기 연산을 위한 double-and-add 알고리즘
def double_and_add(p, private_key, Gx, Gy):
    key = bin(private_key)[:2]
    temp_x = Gx
    temp_y = Gy

    for i in range(1, len(key)):
        temp_x, temp_y = point_add(p, temp_x, temp_y, temp_x, temp_y)

        if key[i] == "1":
            temp_x, temp_y = point_add(p, temp_x, temp_y, Gx, Gy)

    return temp_x, temp_y

#곱셈의 역원을 계산하기 위한 extended_euclidian 알고리즘
def extended_euclidian(n,b):
    r1, r2 = n, b
    t1, t2 = 0, 1

    while r2 != 0:
        q = r1//r2
        r1 = r2
        r2 = r1 - q * r2
        t1= t2
        t2 = t1- q * t2

    return t1   #t1이 역원

#타원 곡선 상의 덧셈 연산을 위한 함수
def point_add(p, x1, y1, x2, y2):
    #P와 Q가 같은 점
    if x1 == x2 and y1 == y2:
        inverse = extended_euclidian(2*y1, p)   #역원
        slope = ((3*x1**2) * inverse) % p
    #P와 Q가 다른점
    else:
        inverse= extended_euclidian(x2-x1, p)
        slope = ((y2-y1) * inverse) % p

    x3 = (slope**2 - x1 - x2) % p
    y3 = (slope*(x1-x3) - y1) % p
    
    return x3, y3

#공개키
public_key_x, public_key_y = double_and_add(p, private_key, Gx, Gy)

#출력
print("개인키(16진수) =",hex(private_key))
print("개인키(10진수) =",private_key)
print("")
print("공개키(16진수) =({}, {})".format(hex(public_key_x), hex(public_key_y)))
print("공개키(10진수) =({}, {})".format(public_key_x, public_key_y))
