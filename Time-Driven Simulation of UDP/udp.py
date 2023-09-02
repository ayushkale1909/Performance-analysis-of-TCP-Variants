import socket
import time

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 12345

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

SimClock = 0
startTime = time.time()
stopTime = 100
step = 1

packet_statistics = {
    "total_packets": 0,
    "total_bytes": 0
}

def initialize_system():
    print(f"Listening for UDP packets on {UDP_IP_ADDRESS}:{UDP_PORT_NO}")

def handle_event(packet, address):
    print(f"Received packet from {address}")
    print(f"Packet Data: {packet}")
    print(f"Packet Length: {len(packet)} bytes")
    
    packet_statistics["total_packets"] += 1
    packet_statistics["total_bytes"] += len(packet)

def collect_statistics():
    pass

initialize_system()

while SimClock < stopTime:
    serverSock.settimeout(step)
    try:
        data, addr = serverSock.recvfrom(1024)
        handle_event(data, addr)
    except socket.timeout:
        print("Socket timed out, no packet received during this interval.")
    
    collect_statistics()
    SimClock += step

print(f"Simulation completed. Packet statistics collected: {packet_statistics}")
    
