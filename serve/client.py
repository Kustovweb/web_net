import socket
import threading

FORMAT = 'utf-8'

# Ввод никнейма
nickname = input("Введите ваш ник: \n")


# Соединение с сервером
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('91.200.148.69', 55555))


# Прослушивание сервера и отправка ника
def receive():
    while True:
        try:
            # Получение сообщения с сервера
            # если 'NICK' отправить ник
            message = client.recv(1024).decode(FORMAT)
            if message == 'NICK':
                client.send(nickname.encode(FORMAT))
            else:
                print(message)
        except ConnectionError as e:
            # Если ошибка, то закрыть соединение
            print(f"Что-то пошло не так!\n Ошибка: {e}")
            client.close()
            break


def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode(FORMAT))


# Создаем поток для отправки сообщений
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Создаем поток для записи сообщений
write_thread = threading.Thread(target=write)
write_thread.start()
