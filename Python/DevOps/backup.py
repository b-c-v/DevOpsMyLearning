# создает резервные копии указанных директорий с помощью rsync, помещая их в папку с временной меткой, и запускает процесс повторно через заданный интервал времени (в часах).

import subprocess  # Импорт модуля для запуска внешних команд в терминале (например, rsync)
import datetime  # Импорт модуля для работы с датой и временем
import time  # Импорт модуля для работы с задержками и временем


def create_backup(source, destination):
    # Получение текущего времени в формате ГГГГММДД_ЧЧММСС
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # Формирование имени папки для резервной копии
    backup_folder = f"backup_{timestamp}"
    try:
        # Запуск команды rsync для копирования данных из source в папку назначения с временной меткой
        subprocess.run(
            ["rsync", "-av", source, f"{destination}/{backup_folder}"], check=True
        )
        # Сообщение об успешном завершении резервного копирования
        print(f"Backup completed successfully for {source}")
    except subprocess.CalledProcessError as e:
        # Вывод ошибки в случае неудачного выполнения rsync
        print(f"Error creating backup for {source}: {e}")


def automated_backup_system(sources, destination, interval_hours):
    try:
        # Бесконечный цикл, в котором периодически выполняется резервное копирование
        while True:
            for source in sources:
                # Создание резервной копии для каждого указанного источника
                create_backup(source, destination)
            # Ожидание заданного интервала времени (в секундах)
            time.sleep(interval_hours * 3600)
    except KeyboardInterrupt:
        print("Backup system stopped by user.")


# Основная точка входа в программу
if __name__ == "__main__":
    # Список директорий, которые нужно копировать
    source_directories = [
        "/mnt/d/Dev/GitHub/DevOpsMyLearning/Python/DevOps",
        "/mnt/d/Dev/GitHub/DevOpsMyLearning/Python/GeneratioPython",
    ]
    # Папка, в которую сохраняются резервные копии
    backup_destination = "/mnt/d/Dev/GitHub/DevOpsMyLearning/Python/"
    # Интервал между резервными копиями в часах
    backup_interval_hours = 24

    # Запуск автоматической системы резервного копирования
    automated_backup_system(
        source_directories, backup_destination, backup_interval_hours
    )
