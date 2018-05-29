import socket

comms_socket = socket.socket()
comms_socket.bind(('localhost', 5000))  # bind server socket to port
comms_socket.listen(10)  # listen state, 10 as backlog specifies the number of unaccepted connections system allow
connection, address = comms_socket.accept()  # create a new socket stored in connection which used for send() and recv()

while True:
    # data stored in bytes rather than string so that we need charset transformation
    print(connection.recv(4096).decode("UTF-8"))
    send_data = input("Reply:")
    connection.send(bytes(send_data, "UTF-8"))
