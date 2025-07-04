import socket

def start_client():
    host = '127.0.0.1'  # localhost (same as server)
    port = 65432

    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))

    while True:
        msg = input("Enter message for server: ")
        if msg.lower() == "exit":
            break
        client_socket.sendall(msg.encode())
        data = client_socket.recv(1024)
        print("Server replies:", data.decode())

    client_socket.close()

if __name__ == "__main__":
    start_client()
