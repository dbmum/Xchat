# from email import message
import socket

HOST = "127.0.0.1"  
PORT = 65432  


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print('\n\n\n\nConnecting...')
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        print('You are connected, you may now chat with the other person each time you see ">>"')

        while True:

            data = conn.recv(1024)

            print(data.decode('UTF-8'))
            if data == (b"/exit"):
                break
            

            message = input('>> ')

            if message == '':
                message += '-'

            message = message.encode('UTF-8')
            conn.sendall(message)
            if message == (b"/exit"):
                break

