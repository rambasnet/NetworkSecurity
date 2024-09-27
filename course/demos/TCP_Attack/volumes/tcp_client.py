#! /usr/bin/env python3

import socket


def connect(host='10.9.0.5', port=9090):
    # Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        # Send data to the server
        client_socket.sendall(b"Hello, server!")

        # Receive data from the server
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")
        client_socket.sendall(b"Hello, again!")
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")
        client_socket.sendall(b"Goodbye!")
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")
        client_socket.close()


if __name__ == "__main__":
    connect()
