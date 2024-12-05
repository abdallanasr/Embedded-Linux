import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("127.0.1.2", 4000))

while True:
    msg = str(input("Please enter the message that you want to send :"))
    msg_encoded = msg.encode('UTF-8')
    client.send(msg_encoded)
    print("======================================")
    rodate = client.recv(500000)
    print(f"192.168.15 is sending to you this message {rodate.decode('UTF-8')}")
    if msg_encoded == "end":
        client.close()