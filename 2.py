import hashlib
import time

message = input("메시지의 내용? ")
target_bits = input("Target bits? ")

max_nonce = 2 ** 32 - 1
target = int(target_bits, 16)
print("Target: 0x{:064x}".format(target))

extra_nonce = int(time.time())
print("메시지: {}, Extra nonce: {}".format(message, extra_nonce))

start_time = time.time()

for nonce in range(max_nonce + 1):
    data = message.encode() + extra_nonce.to_bytes(4, byteorder='big') + nonce.to_bytes(4, byteorder='big')
    hash_result = hashlib.sha256(hashlib.sha256(data).digest()).digest()
    hash_int = int.from_bytes(hash_result, byteorder='big')

    if hash_int < target:
        print("nonce: {}".format(nonce))
        print("실행 시간: {}초".format(time.time() - start_time))
        print("Hash result: 0x{:064x}".format(hash_int))
        break
else:
    print("POW를 만족하는 nonce가 없습니다.")
