import socket

def start_server():
    host = '127.0.0.1'  # localhost
    port = 65432        # arbitrary non-privileged port

    # Create socket object with IPv4 and TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket to address
    server_socket.bind((host, port))

    # Enable the server to accept connections (max 1 queued)
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Client says:", data.decode())

        reply = input("Enter reply to client: ")
        conn.sendall(reply.encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
