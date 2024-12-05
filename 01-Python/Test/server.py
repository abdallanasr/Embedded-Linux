import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())

server.bind(("127.0.1.2", 4000))

server.listen(1)

while True:
    client, address = server.accept()
    rodate = client.recv(500000)
    print(f"{address} is sending to you this message {rodate.decode('UTF-8')}")
    msg = str(input("Please enter the message that you want to send : "))
    msg_encoded = msg.encode('UTF-8')
    client.send(msg_encoded)
    if msg_encoded == "end":
        client.close()