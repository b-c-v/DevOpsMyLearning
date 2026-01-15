#!/bin/env python
import paramiko  # Импортируем библиотеку для работы с SSH-соединениями

# pip install paramiko
ip_address = "192.168.1.236"  # IP-адрес удалённого сервера
username = "ser"  # Имя пользователя для SSH
password = "changeme"  # Пароль для SSH
ssh_port = 22  # Порт SSH по умолчанию

# Создаём объект клиента SSH
ssh_client = paramiko.SSHClient()
# Устанавливаем политику для автоматического добавления ключей хоста
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Загружаем сохранённые в системе SSH-ключи (необязательно при использовании пароля)
ssh_client.load_system_host_keys()

try:
    ssh_client.connect(
        hostname=ip_address,  # Адрес удалённого хоста
        port=ssh_port,  # Порт SSH
        username=username,  # Имя пользователя
        password=password,  # Пароль
        look_for_keys=False,  # Не искать ключи авторизации
        allow_agent=False,  # Не использовать SSH-агент
    )
    print("Successful connection to", ip_address)

    # Выполняем команду создания директории test1
    stdin, stdout, stderr = ssh_client.exec_command("mkdir test1")

    # Получаем код возврата команды
    exit_status = stdout.channel.recv_exit_status()

    if exit_status == 0:
        print(
            # Если код возврата 0, значит всё прошло успешно
            "Directory created successfully"
        )
    else:
        # Иначе выводим сообщение об ошибке
        print(f"Error creating directory: {stderr.read().decode()}")

except Exception as e:
    print("Error:", str(e))  # Обрабатываем общее исключение и выводим его

finally:
    if (
        ssh_client.get_transport() is not None
    ):  # Проверяем, есть ли активное подключение
        ssh_client.close()  # Закрываем SSH-соединение
