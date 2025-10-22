from python_process.server import start_server


def main():
    host = 'localhost'
    port = 22222
    print("starting socket server")    
    server = start_server(host, port)


if __name__ == "__main__":
    main()
