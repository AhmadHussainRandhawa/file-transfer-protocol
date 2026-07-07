import socket

from config import HOST, PORT


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")

    finally:
        client_socket.close()
        print("Connection closed.")


if __name__ == "__main__":
    main()