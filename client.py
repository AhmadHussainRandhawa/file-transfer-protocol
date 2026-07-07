import socket
from config import HOST, PORT, BUFFER_SIZE, ENCODING


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")

        message = "Hello Server Jani!"
        client_socket.sendall(message.encode(ENCODING))

        response = client_socket.recv(BUFFER_SIZE)
        print(f"The Server respond with {response.decode(ENCODING)}")

    finally:
        client_socket.close()
        print("Connection closed.")


if __name__ == "__main__":
    main()