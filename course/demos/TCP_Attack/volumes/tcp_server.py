import socket


def start_server(host='0.0.0.0', port=9090):
    # Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the server to the specified host and port
        server_socket.bind((host, port))
        # Start listening for incoming connections (max 5 in the queue)
        server_socket.listen(5)
        print(f"Server started at {host}:{port}. Waiting for connections...")

        # Main server loop to handle incoming connections
        while True:
            # Accept a new connection
            client_socket, client_address = server_socket.accept()
            print(f"Connected by {client_address}")

            # Handle client communication
            with client_socket:
                while True:
                    # Receive data from the client
                    # buffer size of 1024 bytes
                    data = client_socket.recv(1024)
                    if not data:
                        # Break the loop if no data is received (client disconnected)
                        break
                    print(f"Received from {client_address}: {data.decode()}")

                    # Optionally, you can send a response back to the client
                    client_socket.sendall(data)  # Echo the received data back


if __name__ == "__main__":
    start_server()
