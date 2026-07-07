import socket

from config import HOST, PORT, ENCODING, BUFFER_SIZE


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
                data = client_socket.recv(BUFFER_SIZE)
                
                if data:
                    message = data.decode(ENCODING)
                    print(f"Received: {message}")

                    response = "ACK"
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