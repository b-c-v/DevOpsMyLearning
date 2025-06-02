import logging

# Обработчик логов (Handler) — это объект, который отвечает за то, КУДА и КАК отправлять лог-сообщения: в файл, на экран, по сети, в базу данных и т.д.
# Модуль logging построен по архитектуре "логгер ==> обработчик ==> формат ==> вывод". Это позволяет:
# - создавать несколько обработчиков (файл, консоль, почта и т.д.)
# - настраивать разные уровни логирования для каждого (например, в файл — DEBUG, в консоль — только ERROR)
# - указывать разные форматы для разных источников логов

# Сохранять все сообщения в файл, а сообщения об ошибках показывать в консоль
# Создаём отдельный обработчик логов, который будет записывать сообщения всех уровней в файл "example.log"
file_handler = logging.FileHandler("example.log")
# Устанавливаем для этого обработчика минимальный уровень логирования
file_handler.setLevel(logging.DEBUG)

# Создаём отдельный консольный обработчик логов, который будет выводить ERROR и CRITICAL сообщения в консоль
console_handler = logging.StreamHandler()
# Устанавливаем уровень — только сообщения ERROR и CRITICAL будут выведены в консоль
console_handler.setLevel(logging.ERROR)
# Конфигурация логирования - используем два обработчика: файл и консоль
logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, console_handler])


logging.critical("Example of critical log")
logging.error("Example of error log")
logging.warning("Example of warning log")
logging.info("Example of info log")
logging.debug("Example of debug log")
