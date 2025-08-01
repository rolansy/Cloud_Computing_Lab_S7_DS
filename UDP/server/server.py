import socket

def start_udp_server():
    host = '127.0.0.1'  
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_socket.bind((host, port))
    print(f"UDP server listening on {host}:{port}...")

    while True:
        data, addr = server_socket.recvfrom(1024)  
        message = data.decode()
        print(f"Received from {addr}: {message}")

        if message.lower() == 'exit':
            print("Server shutting down.")
            break

        reply = input("Reply to client: ")
        server_socket.sendto(reply.encode(), addr)

    server_socket.close()

if __name__ == "__main__":
    start_udp_server()
