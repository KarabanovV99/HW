import socket
from hash_table_server import HashTable

HOST = "127.0.0.1"
PORT = 6548

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Подключено к {addr}")
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                data = data.decode('utf-8')
                data = data.split()
                print(data[0])
                if data[0] == 'init':
                    table = HashTable()
                    conn.sendall(b'tabel is init')
                if data[0] == 'set':
                    key = data[1]
                    value = data[2]
                    table.set_value(key, value)
                    print(f"Дабавлено: {key, value}")
                    conn.sendall('Дабавлено'.encode('utf-8'))
                if data[0] == 'get':
                    key = data[1]
                    value = table.get_value(key)
                    if value:
                        print(f"Значение: {value}")
                        conn.sendall(f'{value}'.encode('utf-8'))
                    else:
                        print(f"Значение не найдено")
                        conn.sendall(f'Значение не найдено'.encode('utf-8'))
                if data[0] == 'siztab':
                    message = f'Table size: {table.size} \n'
                    for i in range(table.size):
                        if table.table[i]:
                            message += "■"
                        else:
                            message += "□"
                    message += f'\n\nFill factor: {table.load()}'
                    conn.sendall(message.encode('utf-8'))
                if data[0] == 'print':
                    message = table.__str__()
                    conn.sendall(message.encode('utf-8'))
                if data[0] == 'del':
                    key = data[1]
                    if table.del_value(key):
                        message = f'\nHappened'
                    else:
                        message = f'\nValue not found'
                    print(message)
                    conn.sendall(message.encode('utf-8'))
            except ConnectionResetError:
                print("Клиент отключился")
                break
