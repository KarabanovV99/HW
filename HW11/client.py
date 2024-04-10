import socket
from hash_table_server import ColorEnum

HOST = "127.0.0.1"
PORT = 6548
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    input(f'Нажмине Enter, чтобы инициализировать таблицу')
    s.sendall('init'.encode('utf-8'))
    data = s.recv(1024)
    print(f"{data.decode('utf-8')}")
    while True:
        print(ColorEnum.BLUE + "_" * 27 + ColorEnum.FINISH, "\n")
        print(ColorEnum.GREEN + "1. Add value")
        print("2. Delete value")
        print("3. Get value")
        print("4. Fill factor")
        print("5. Print dictionary")
        print("6. Exit" + ColorEnum.FINISH, "\n")

        choice = input("{0}Enter your choice: {1}".format(ColorEnum.YELLOW, ColorEnum.FINISH))
        print("")

        if choice == '1':
            key = input("{0}Enter key: {1}".format(ColorEnum.YELLOW, ColorEnum.FINISH))
            value = input("{0}Enter value: {1}".format(ColorEnum.YELLOW, ColorEnum.FINISH))
            message = f'set {key} {value}'
            print(message)
        elif choice == '2':
            key = input("{0}Enter key: {1}".format(ColorEnum.YELLOW, ColorEnum.FINISH))
            message = f'del {key}'
        elif choice == '3':
            key = input("{0}Enter key: {1}".format(ColorEnum.YELLOW, ColorEnum.FINISH))
            message = f'get {key}'
        elif choice == '4':
            message = 'siztab'
        elif choice == '5':
            message = 'print'
        elif choice == '6':
            break
        else:
            print("{0}Incorrect choice. Try again{1}".format(ColorEnum.RED, ColorEnum.FINISH))

        s.sendall(message.encode('utf-8'))
        data = s.recv(1024)
        print(f'{data.decode("utf-8")}')
