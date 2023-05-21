#원시소켓방식
#상위계층 기반의 원시 소켓 생성 기법 : 송신을 구현할떄 주로 사용
import socket
standard_s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

#원시소켓은 일반사용자는 사용불가능, 관리자권한을 가지고 있어야 실행가능
raw_s=socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
raw_s.setsockopts(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
icmp_raw_s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
icmp_raw_s.setsockopts(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)


#하위계층 기반의 원시 소켓 생성 기법 : 이더넷프레임까지 원시 소켓으로 생성
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

##########################################################
from struct import pack
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.IPPROTO_UDP)
s_port = 4321
d_port = 22
length = 0
checksum=0
udp_header = pack('!HHHH', s_port, d_port, length, checksum)
