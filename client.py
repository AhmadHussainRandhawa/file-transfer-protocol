import socket
from config import HOST, PORT, BUFFER_SIZE, ENCODING, CLIENT_DOWNLOADS


def receive_file(client_socket, filename: str, file_size: int,):
    """
    Receive exactly file_size bytes
    and save them to disk.
    """

    destination = CLIENT_DOWNLOADS / filename

    received = 0

    with open(destination, "wb") as file:
        while received < file_size:

            remaining = file_size - received

            chunk_size = min(BUFFER_SIZE, remaining,)
            chunk = client_socket.recv(chunk_size)

            if not chunk:
                raise ConnectionError("Connection closed during transfer.")
            
            file.write(chunk)
            received += len(chunk)

            print(f"Received {received}/{file_size} bytes")

    print(f"Download complete: {destination}")


def receive_response(client_socket):
    """
    Read exactly one protocol response.
    Responses are terminated by '\n'.
    """
    data = b""

    while b"\n" not in data:
        chunk = client_socket.recv(1)

        if not chunk:
            raise ConnectionError("Server disconnected.")

        data += chunk

    return data.decode(ENCODING).strip()


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")

        while True:
            message = input("> ")

            if message.lower() == 'exit':
                break

            client_socket.sendall(message.encode(ENCODING))

            response = receive_response(client_socket)

            print(f"Server: {response}")

            if message.upper().startswith("GET "):
                parts = response.split(" ", maxsplit=1,)

                if parts[0] == "OK": 
                    file_size = int(parts[1])
                    filename = (message.split()[1])

                    receive_file(client_socket, filename, file_size,)
    finally:
        client_socket.close()
        print("Connection closed.")


if __name__ == "__main__":
    main()