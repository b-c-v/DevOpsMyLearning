# Python subprocess module позволяет создавать новые процессы, подключаться к их входным/выходным/потокам ошибок и получать коды возврата.
# Модуль subprocess является предпочтительным способом для запуска внешних программ и команд из Python кода.
# Для использования этих функций в начале программы необходимо подключить модуль, что делается командой import:
import subprocess

# Модуль subprocess предоставляет класс Popen и несколько функций-обертки для удобства работы с внешними процессами.

"""
Основные функции и методы модуля subprocess:

run()                Запускает команду в новом процессе и ждет завершения. Возвращает объект CompletedProcess
Popen()              Создает новый процесс. Позволяет больший контроль над процессом (stdin, stdout, stderr)
check_call()         Запускает команду, возвращает код возврата. Вызывает CalledProcessError если код возврата не 0
check_output()       Запускает команду, возвращает вывод (stdout). Вызывает CalledProcessError если код возврата не 0
call()               Запускает команду в новом процессе и возвращает код возврата (deprecated, используйте run())

CompletedProcess     Объект, возвращаемый функцией run(). Содержит атрибуты: args, returncode, stdout, stderr

Атрибуты Popen объекта:
stdin                Объект, используемый для записи в stdin процесса
stdout               Объект, используемый для чтения из stdout процесса
stderr               Объект, используемый для чтения из stderr процесса
pid                  ID процесса (process ID)
returncode           Код возврата процесса (0 - успех, другое число - ошибка)

Методы Popen:
poll()               Проверить, завершился ли процесс. Возвращает None если процесс еще работает, иначе код возврата
wait()               Ожидать завершения процесса и вернуть код возврата
communicate()        Взаимодействовать с процессом: отправить данные в stdin, получить stdout и stderr
kill()               Завершить процесс немедленно (сигнал SIGKILL)
terminate()          Завершить процесс (сигнал SIGTERM)

Флаги для capture_output и pipes:
capture_output=True  Захватывает stdout и stderr (эквивалентно stdout=PIPE, stderr=PIPE)
stdout=PIPE          Перенаправляет stdout в PIPE для чтения
stderr=PIPE          Перенаправляет stderr в PIPE для чтения
text=True            Декодирует вывод как текст (str вместо bytes). (shell=True или универсальные новые строки)
cwd                  Рабочая директория для процесса
env                  Переменные окружения для процесса
"""

# ***Функция run()***
# Это предпочтительный способ запуска команд. Она запускает команду и ждет её завершения.
# Возвращает объект CompletedProcess, содержащий информацию о выполнении процесса.

# Простой пример: запустить команду "echo Hello"
result = subprocess.run(["echo", "Hello"], capture_output=True, text=True)
print("returncode:", result.returncode)  # returncode: 0 (успех)
print("stdout:", result.stdout)  # stdout: Hello
print("stderr:", result.stderr)  # stderr: (пусто)

# Запустить команду с использованием shell=True (менее безопасно, но удобнее для сложных команд)
result = subprocess.run(
    'echo "Hello World"', shell=True, capture_output=True, text=True
)
print(result.stdout)  # Hello World

# ***Функция Popen()***
# Дает больше контроля над процессом. Позволяет читать и писать в stdin/stdout/stderr в реальном времени.

# Создать процесс без захвата вывода
process = subprocess.Popen(
    ["ping", "google.com"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
)
# Ожидать завершения процесса
returncode = process.wait()
print("Process finished with return code:", returncode)

# Создать процесс и получить вывод
process = subprocess.Popen(
    ["ls", "-la"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
)
stdout, stderr = process.communicate()
print("Output:", stdout)
print("Errors:", stderr)

# ***Функция check_output()***
# Запускает команду и возвращает её вывод (stdout) как строку.
# Если код возврата не 0, вызывает CalledProcessError.

try:
    output = subprocess.check_output(["echo", "Hello"], text=True)
    print("Output:", output)  # Output: Hello
except subprocess.CalledProcessError as e:
    print("Error:", e)

# ***Функция check_call()***
# Запускает команду и возвращает код возврата.
# Если код возврата не 0, вызывает CalledProcessError.

try:
    returncode = subprocess.check_call(["echo", "Hello"])
    print("Return code:", returncode)  # Return code: 0
except subprocess.CalledProcessError as e:
    print("Command failed with return code:", e.returncode)

# ***Работа с входными данными (stdin)***
# Отправить данные в stdin процесса

# Использовать communicate() для отправки данных в stdin и получения вывода
process = subprocess.Popen(
    ["cat"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)
stdout, stderr = process.communicate(input="Hello from stdin\n")
print("Output:", stdout)  # Output: Hello from stdin

# ***Проверка статуса процесса***
# poll() - проверить без ожидания
# wait() - ждать завершения

process = subprocess.Popen(["sleep", "5"])
print("Process started with PID:", process.pid)

# Проверить статус несколько раз
import time

for i in range(3):
    status = process.poll()
    if status is None:
        print(f"Attempt {i+1}: Process still running")
    else:
        print(f"Process finished with return code: {status}")
    time.sleep(1)

# Дождаться завершения
process.wait()
print("Process completed")

# ***Обработка ошибок***
# Перехватывать исключения при работе с процессами

try:
    # Запустить несуществующую команду
    result = subprocess.run(["nonexistent_command"], capture_output=True, text=True)
except FileNotFoundError:
    print("Command not found")
except subprocess.CalledProcessError as e:
    print(f"Process returned error code: {e.returncode}")

# ***Передача переменных окружения***
# Установить переменные окружения для процесса

# Копировать текущие переменные окружения и добавить новую
import os

env = os.environ.copy()
env["MY_VAR"] = "Hello"

# Создать процесс с новой переменной окружения
result = subprocess.run(
    ["python", "-c", 'import os; print(os.environ.get("MY_VAR"))'],
    env=env,
    capture_output=True,
    text=True,
)
print("Output:", result.stdout)  # Output: Hello

# ***Установка рабочей директории***
# Запустить процесс в другой директории

# На Windows используется команда cd, на Unix pwd
# Проверим текущую директорию, создав временный Python скрипт в определенной папке
import tempfile

result = subprocess.run(
    ["python", "-c", "import os; print(os.getcwd())"],
    cwd=tempfile.gettempdir(),
    capture_output=True,
    text=True,
)
print("Current directory:", result.stdout)

# ***Комбинированный пример: запуск скрипта и обработка вывода***

# Запустить Python скрипт и получить результат
script = 'print("Hello from subprocess"); print("Line 2")'
result = subprocess.run(["python", "-c", script], capture_output=True, text=True)
print("Return code:", result.returncode)
print("Output:")
print(result.stdout)
print("Errors:")
print(result.stderr)
