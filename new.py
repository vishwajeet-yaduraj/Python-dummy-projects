import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.106.40'
port = 12345

client_socket.connect((host, port))

try:
    while True:
        message = input("Enter message: ")

        client_socket.send(message.encode('utf-8'))

        if message.lower() == 'bye':
            print("Closing connection")
            break

        response = client_socket.recv(1024).decode('utf-8')
        if not response:
            print("Server disconnected")
            break
        print(f"Response from server: {response}")
finally:
    client_socket.close()
