class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    def __del__(self):
        Counter.count -= 1

    # Декоратор @classmethod говорит Python, что метод относится к классу, а не к конкретному объекту.
    # В метод автоматически передаётся cls - это ссылка на сам класс (например, MyClass).
    # Такой метод можно вызывать как через класс, так и через объект.
    @classmethod
    def get_count(cls):
        return cls.count


inst_1 = Counter()
inst_2 = Counter()
inst_3 = Counter()
inst_4 = Counter()

print(f"Number of instances of Counter class: {Counter.get_count()}")

del inst_4

# Counter.get_count() works because use decorator @classmethod
print(f"Number of instances of the Counter class after deletion: {Counter.get_count()}")
