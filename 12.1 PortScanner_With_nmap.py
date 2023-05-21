#!/usr/bin/env python3

import nmap
nm = nmap.PortScanner()  # 포트스캐너 객체 생성
nm.scan('127.0.0.1', arguments='-sV')  # '127.0.0.1'을 스캔하고, '-sV' 인자로 서비스 버전 탐지 활성화
print(nm.all_hosts())  # 스캔된 모든 호스트의 IP 주소를 출력

# 이 코드는 파이썬에서 Nmap을 사용하여 로컬 호스트(127.0.0.1)를 스캔하는 프로그램입니다.
# Nmap은 네트워크 탐지 및 보안 감사 도구로 널리 알려져 있습니다.
# 해당 코드는 nmap 라이브러리를 사용하여 포트 스캐너 객체를 생성하고, 지정된 IP 주소에 대해 스캔을 실행합니다.
# '-sV' 인자는 서비스 버전 탐지를 활성화하는 옵션입니다.
# 스캔이 완료되면 스캔된 모든 호스트의 IP 주소를 출력합니다.


###############################################
#!/usr/bin/env python3

import nmap
import sys

# 포트스캐너 객체 생성
nm = nmap.PortScanner()

# 기본 대상 호스트와 포트 설정
target_host = '127.0.0.1'
target_port = '22'

# 커맨드라인 인자의 개수 확인
argc = len(sys.argv)

# 대상 호스트가 커맨드라인 인자로 제공되었는지 확인
if argc > 1 and sys.argv[1] != '':
    target_host = sys.argv[1]

# 대상 포트가 커맨드라인 인자로 제공되었는지 확인
if argc > 2 and sys.argv[2] != '':
    target_port = sys.argv[2]

# 대상 호스트와 포트 스캔
nm.scan(target_host, target_port)

# 모든 스캔된 호스트에 대해 반복
for host in nm.all_hosts():
    print(f'호스트: {host} {nm[host].hostname()}')
    print(f'상태: {nm[host].state()}')

    # 현재 호스트에 대한 프로토콜 반복
    for protocol in nm[host].all_protocols():
        print(f'프로토콜: {protocol}')  # 여기에 주석 추가

