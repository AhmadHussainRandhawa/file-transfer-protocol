import socket

from config import HOST, PORT, ENCODING, BUFFER_SIZE
from protocol import parse_message, handle_command


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}")

    try:
        while True:
            print("Waiting for a client...")

            client_socket, client_address = server_socket.accept()

            print(f"Client connected: {client_address}")

            try: 
                while True:
                    data = client_socket.recv(BUFFER_SIZE)
                    
                    if not data:
                        break 

                    message = data.decode(ENCODING)
                    print(f"Received: {message}")

                    command, arguments = parse_message(message)
                    response = handle_command(command, arguments)

                    client_socket.sendall(response.encode(ENCODING))

            finally: 
                client_socket.close()
                print("Client disconnected.\n")

    except KeyboardInterrupt:
        print("\nShutting down server...")

    finally:
        server_socket.close()
        print("Server socket closed.")

if __name__ == "__main__":
    main()