import socket


def receive_all(connection, buffer_size=4096):
    result = b''
    reading = True
    while reading:
        data = connection.recv(buffer_size)
        if data is None or len(data) == 0:
            reading = False
        else:
            result += data
            if result[-1] == 10:
                reading = False

    return result    


def create_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return server


def start_server(host, port):
    running = True
    with create_server(host, port) as server:
        server.bind((host, port))

        # currently only allowing a single connection
        # to account for any statefulness in the simulation
        server.listen(1)

        connection, address = server.accept()
        with connection:
            while running:
                # message = connection.recv(4)
                message = receive_all(connection)
                if message is None or len(message) == 0:
                    running = False
                else:
                    print(message)

