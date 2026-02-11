import socket
import threading
from detector import analyze_connection
from logger import log_event

HOST = "0.0.0.0"
PORT = 9999

def handle_client(client_socket, address):
    ip = address[0]
    source_port = address[1]

    log_event("INFO", f"Connection from {ip}:{source_port}")
    analyze_connection(ip, PORT)

    client_socket.close()

def start_server():
    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        server.bind(("::", PORT))
        server.listen()
        log_event("INFO", f"Server started on {HOST}:{PORT}")

        while True:
            client_socket, address = server.accept()
            
            thread = threading.Thread(target=handle_client, args=(client_socket, address))
            thread.daemon = True
            thread.start()
