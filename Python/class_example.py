# Класс LibraryItem представляет любой объект в библиотеке (например, книгу, журнал, и т.д.)
class LibraryItem:
    # __init__ — это конструктор. Он автоматически вызывается, когда создаётся новый объект.
    # Здесь мы задаём начальные свойства объекта: название, автор, ISBN и доступность.
    def __init__(self, title, author, isbn):
        self.title = title  # Название объекта
        self.author = author  # Автор
        self.isbn = isbn  # ISBN — уникальный код книги
        self.available = True  # Книга доступна по умолчанию

    # __str__ — специальный метод. Он определяет, как объект будет отображаться при печати.
    # Когда мы пишем print(book1), на самом деле вызывается book1.__str__()
    def __str__(self):
        # f-строка позволяет вставлять переменные прямо внутрь текста.
        return f"{self.title} автор {self.author}"

    # Метод check_out — используется, чтобы "взять" книгу из библиотеки.
    def check_out(self):
        # Проверяем, доступна ли книга
        if self.available:
            # Если да — печатаем сообщение и делаем её недоступной
            print(f"Выдано: {self}")
            self.available = False
        else:
            # Если уже занята — сообщаем об этом
            print(f"{self} книга недоступна!")

    # Метод check_in — возвращает книгу обратно в библиотеку
    def check_in(self):
        print(f"Возвращено: {self}")
        self.available = True


# Класс Book — это "подкласс" LibraryItem. Это означает, что Book наследует все свойства и методы от LibraryItem.
class Book(LibraryItem):
    # У конструктора Book есть дополнительный аргумент — жанр книги.
    def __init__(self, title, author, isbn, genre):
        # super() вызывает конструктор родительского класса (LibraryItem),
        # чтобы мы не писали заново инициализацию title, author и isbn.
        super().__init__(title, author, isbn)
        self.genre = genre  # Дополнительное свойство: жанр книги

    # Мы переопределяем метод __str__, чтобы он показывал также жанр
    def __str__(self):
        # Сначала вызываем родительский __str__, потом добавляем жанр.
        return f"{super().__str__()} (Жанр: {self.genre})"


# Класс Human представляет пользователя-человека, который может брать книги
class Human:
    def __init__(self, name):
        self.name = name  # Имя человека

    # Метод borrow_item получает объект item (предположительно книгу),
    # и вызывает у него метод check_out()
    def borrow_item(self, item):
        # Здесь неважно, к какому классу относится item, главное, чтобы у него был метод check_out()
        # Это пример "утиной типизации": если выглядит как утка и крякает — значит, утка.
        item.check_out()

    # Метод для возврата книги
    def return_item(self, item):
        item.check_in()


# Класс Robot — другой тип "пользователя". Он может делать то же, что и человек.
# У него тоже есть методы borrow_item и return_item, как и у Human.
class Robot:
    def __init__(self, name):
        self.name = name  # Имя робота

    def borrow_item(self, item):
        item.check_out()

    def return_item(self, item):
        item.check_in()


# Создаём пустой список — наша библиотека будет хранить книги здесь
library = []

# Создаём 2 книги (объекты класса Book) и добавляем их в библиотеку
book1 = Book("Python book", "Andrea Rossi", "632-38563", "Detective")
book2 = Book("Python in 2 hours", "Ivan Ivanov", "632-38564", "Comedy")
library.append(book1)
library.append(book2)

# Выводим список книг, используя __str__ каждого объекта Book
print("Книги в библиотеке:")
for item in library:
    print(item)

# Создаём трёх "клиентов": двух людей и одного робота
customer1 = Human("Sergii")
customer2 = Human("Petr")
customer3 = Robot("Verder")

# Теперь все они могут взаимодействовать с книгами благодаря методам borrow_item и return_item
customer1.borrow_item(book1)  # Sergii берёт первую книгу
customer3.borrow_item(book2)  # Робот берёт вторую книгу

customer2.borrow_item(book2)  # Petr пытается взять вторую книгу, но она уже у робота

customer1.return_item(book1)  # Sergii возвращает первую книгу

customer2.borrow_item(book1)  # Теперь Petr может взять её

customer2.borrow_item(
    book1
)  # Petr снова пытается взять ту же книгу — она уже у него, будет сообщение, что недоступна
