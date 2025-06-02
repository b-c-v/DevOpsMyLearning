# textwrap используется для форматирования текста — в основном для переноса строк по заданной ширине.
import textwrap

# Исходная длинная строка
long_text = "Python — это мощный язык программирования, идеально подходящий для разработки скриптов, веб-приложений, анализа данных и многого другого."

# Оборачиваем текст в строки не длиннее 40 символов
wrapped_text = textwrap.wrap(long_text, width=40)
print("Результат wrap():")
for line in wrapped_text:
    print(line)  # Каждая строка — не более 40 символов

# Объединяем обёрнутый текст обратно в параграф с переносами строк
formatted_paragraph = textwrap.fill(long_text, width=40)
print("\nРезультат fill():")
print(formatted_paragraph)

# Добавляем отступ слева
indented_text = textwrap.indent(formatted_paragraph, prefix=">> ")
print("\nС отступом:")
print(indented_text)

# Удаляем общий отступ (dedent)
indented_example = """
    Это пример строки
    с одинаковым отступом.
"""
print("\nУдаление отступов с помощью dedent:")
print(textwrap.dedent(indented_example))

# Обрезаем текст до 50 символов, добавляя "..." в конце
shortened = textwrap.shorten(long_text, width=50, placeholder="...")
print("Обрезанный текст:")
print(shortened)
# Вывод: Python — это универсальный язык программирования...