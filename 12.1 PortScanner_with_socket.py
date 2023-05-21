#!/usr/bin/env python3

import sys
import socket

target_host = sys.argv[1]  # 커맨드라인 인자로 대상 호스트를 받습니다.

for port in range(0, 1024):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP 소켓을 생성합니다.
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 소켓 옵션을 설정합니다.

    try:
        result = s.connect((target_host, port))  # 대상 호스트와 포트에 연결을 시도합니다.
        #connect는 반환값이 없다 -> connect_ex()를 사용해야 함  0:true, 111:false
        
        if result == 0:
            print(f"[*] 포트 {port} 열려 있음!")  # 연결에 성공하면 해당 포트가 열려있음을 출력합니다.

    except:
        pass  # 예외가 발생하면 무시하고 다음 반복으로 넘어갑니다.

    s.close()  # 소켓 연결을 닫습니다.

# 이 코드는 대상 호스트에 대해 0부터 1023까지의 포트를 스캔하는 프로그램입니다.
# 대상 호스트와 각 포트에 소켓 연결을 시도하고, 연결이 성공하면 해당 포트가 열려있음을 출력합니다.
# 소켓을 열고 닫을 때 소켓 옵션을 설정하여 재사용 가능하도록 설정합니다.
# 예외가 발생하면 무시하고 다음 반복으로 넘어가도록 처리합니다.
