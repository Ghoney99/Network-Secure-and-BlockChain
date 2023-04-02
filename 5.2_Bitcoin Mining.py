import time
import hashlib

# 메시지와 target bits 입력
msg = input("메시지의 내용? ")
target_bits = input("Target bits? ")

# target 값 계산
exponent = int(target_bits[:2], 16)
coefficient = int(target_bits[2:], 16)
target = coefficient * 2 ** (8 * (exponent - 3))

# 메시지와 extra nonce 초기화
message = msg.encode()
extra_nonce = int(time.time())

start_time = time.time()

# nonce 값 계산
nonce = 0
while True:
    # 해시 계산
    hash_result = hashlib.sha256(message + extra_nonce.to_bytes(4, 'little') + nonce.to_bytes(4, 'little')).digest()
    
     # 결과 출력
    if int.from_bytes(hash_result, 'big') < target:
        print(f"Target: 0x{target:064x}")
        print(f"메시지: {msg}, Extra nonce: {extra_nonce}, nonce: {nonce}")
        print(f"실행 시간: {time.time() - start_time:.9f}초")
        print(f"Hash result: 0x{hash_result.hex()}")
        break
    
    # nonce 값 변경
    nonce += 1
    if nonce == 2**32:
        extra_nonce = int(time.time())
        nonce = 0