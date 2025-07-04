import socket

def start_udp_client():
    server_host = '127.0.0.1'
    server_port = 12345

    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("Enter message for server: ")
        client_socket.sendto(message.encode(), (server_host, server_port))

        if message.lower() == 'exit':
            break

        data, _ = client_socket.recvfrom(1024)
        print(f"Server replied: {data.decode()}")

    client_socket.close()

if __name__ == "__main__":
    start_udp_client()
