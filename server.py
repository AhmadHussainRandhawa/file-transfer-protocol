import socket

from config import HOST, PORT, ENCODING, BUFFER_SIZE
from protocol import process_message
from session import Session
from virtual_fs import VirtualFileSystem


vfs = VirtualFileSystem()


def send_file(client_socket, session, vfs,):
    """
    Stream a file to the client.
    """
    virtual_path = session.pending_download

    real_path = vfs.get_file_path(virtual_path)

    with open(real_path, "rb") as file:

        chunk = file.read(BUFFER_SIZE)
        while chunk:
            client_socket.sendall(chunk)
            chunk = file.read(BUFFER_SIZE)

    session.finish_download()
    

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

            session = Session()

            print(f"Client connected: {client_address}")

            try: 
                while True:
                    data = client_socket.recv(BUFFER_SIZE)
                    
                    if not data:
                        break 

                    message = data.decode(ENCODING)
                    print(f"Received: {message}")

                    response = process_message(message, session)

                    response_text = (f"{response["status"]} {response["message"]}\n")

                    client_socket.sendall(response_text.encode(ENCODING))

                    if session.pending_download:
                        send_file(client_socket, session, vfs,)

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