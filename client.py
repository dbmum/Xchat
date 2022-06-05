
import socket

HOST = "127.0.0.1"  
PORT = 65432 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('\n\n\n\nYou are connected, you may now chat with the other person each time you see ">>"\n')

    while s:
        message = input('>> ')

        if message == '':
            message = '-'

        message = message.encode('UTF-8')

        s.sendall(message)



        if message == (b"/exit"):
            break

        data = s.recv(1024)

        print(data.decode('UTF-8'))
        if data == (b"/exit"):
                break

