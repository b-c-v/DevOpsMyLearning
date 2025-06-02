# фильтровать лог по ключевым словам, тегам или другим условиям
import logging


# Определяем собственный фильтр логов, наследуя logging.Filter
class CustomFilter(logging.Filter):
    # Метод filter вызывается для каждого лог-сообщения
    def filter(self, record):
        # Пропускаем только те сообщения, которые содержат слово "important"
        return "important" in record.getMessage()


# Создаём логгер с именем "filtered_logger"
logger = logging.getLogger("filtered_logger")
# Устанавливаем минимальный уровень логгирования — DEBUG
logger.setLevel(logging.DEBUG)

# Добавляем пользовательский фильтр к логгеру
logger.addFilter(CustomFilter())

# Создаём обработчик, который будет выводить сообщения в консоль
console_handler = logging.StreamHandler()

# Привязываем обработчик к логгеру
logger.addHandler(console_handler)

# Эти сообщения отправляются в логгер:
# НЕ будет выведено (нет слова "important")
logger.debug("this is a debug message")
# БУДЕТ выведено (содержит "important")
logger.info("this is an important info message")
