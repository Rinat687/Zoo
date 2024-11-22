import pickle


class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} издает звук - {self.sound}")

    def eat(self):
        age_word = self.get_age_word(self.age)
        print(f"{self.name}, {self.age} {age_word}.")

    @staticmethod
    def get_age_word(age):
        """Возвращает правильное склонение слова 'год' в зависимости от возраста."""
        if 11 <= age % 100 <= 14:
            return "лет"
        elif age % 10 == 1:
            return "год"
        elif age % 10 in [2, 3, 4]:
            return "года"
        else:
            return "лет"


class Bird(Animal):
    def __init__(self, name, age, sound, wing_span):
        super().__init__(name, age, sound)
        self.wing_span = wing_span  # Размах крыльев

    def fly(self):
        print(f"{self.name} летит с размахом крыльев {self.wing_span} см.")


class Mammal(Animal):
    def __init__(self, name, age, sound, habitat):
        super().__init__(name, age, sound)
        self.habitat = habitat  # Среда обитания

    def run(self):
        print(f"{self.name} обитает в {self.habitat}.")


class Reptile(Animal):
    def __init__(self, name, age, sound, scale_type):
        super().__init__(name, age, sound)
        self.scale_type = scale_type  # Тип чешуи

    def crawl(self):
        print(f"{self.name} ползет по земле: {self.scale_type}.")


def animal_sound(animals):
    """Вызывает метод make_sound() для каждого животного в списке."""
    for animal in animals:
        animal.make_sound()


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        print(f"{self.name}, в должности: {self.position}, выполняет свои обязанности.")


class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "Смотритель зоопарка")

    def feed_animal(self, animal):
        animal_name = AnimalName(animal.name)
        print(f"{self.name} кормит {animal_name.get_accusative()}.")


class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Ветеринар")

    def heal_animal(self, animal):
        animal_name = AnimalName(animal.name)
        print(f"{self.name} лечит {animal_name.get_accusative()}.")


class AnimalName:
    """Класс для склонения имен животных."""

    def __init__(self, name):
        self.name = name

    def get_nominative(self):
        """Возвращает имя в именительном падеже."""
        return self.name

    def get_accusative(self):
        """Возвращает имя в винительном падеже на основе правил склонения."""

        # Определяем окончания для склонения
        if self.name.endswith('а') or self.name.endswith('я'):
            return self.name[:-1] + 'у'  # Например: корова -> корову
        elif self.name == "Лев":
            return "льва"  # Исключение для льва
        elif self.name == "Слон":
            return "слона"  # Исключение для слона
        elif self.name == "Попугай":
            return "попугая"  # Исключение для попугая
        elif self.name == "Змея":
            return "змею"  # Исключение для змеи
        else:
            return self.name + 'а'  # Добавляем 'а' для остальных случаев (например: кот -> кота)


class Zoo:
    def __init__(self):
        self.animals = []  # Список животных
        self.employees = []  # Список сотрудников

    def add_animal(self, animal):
        """Добавляет животное в зоопарк."""
        self.animals.append(animal)
        print(f"{animal.name} добавлен в зоопарк.")

    def add_employee(self, employee):
        """Добавляет сотрудника в зоопарк."""
        self.employees.append(employee)
        print(f"{employee.name} добавлен в зоопарк как {employee.position}.")

    def save_zoo(self, filename='zoo_data.pkl'):
        """Сохраняет состояние зоопарка в файл."""
        with open(filename, 'wb') as f:
            pickle.dump((self.animals, self.employees), f)
            print("Состояние зоопарка сохранено.")

    def load_zoo(self, filename='zoo_data.pkl'):
        """Загружает состояние зоопарка из файла."""
        try:
            with open(filename, 'rb') as f:
                self.animals, self.employees = pickle.load(f)
                print("Состояние зоопарка загружено.")
                for animal in self.animals:
                    print(f"Животное: {animal.name}, Возраст: {animal.age}")
                for employee in self.employees:
                    print(f"Сотрудник: {employee.name}, Должность: {employee.position}")

        except FileNotFoundError:
            print("Файл не найден. Создайте новый зоопарк.")


# Примеры использования
if __name__ == "__main__":
    zoo = Zoo()

    parrot = Bird("Попугай", 1, "Карр", 25)
    lion = Mammal("Лев", 5, "Рррр", "саване")
    snake = Reptile("Змея", 2, "Шшш", "гладкая")
    elephant = Mammal("Слон", 11, "Труба", "джунглях")
    cow = Mammal("Корова", 4, "Му-му", "пастбище")

    # Добавляем животных в зоопарк
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)
    zoo.add_animal(elephant)
    zoo.add_animal(cow)

    # Создаем сотрудников
    zookeeper = ZooKeeper("Иван")
    veterinarian = Veterinarian("Мария")

    # Добавляем сотрудников в зоопарк
    zoo.add_employee(zookeeper)
    zoo.add_employee(veterinarian)

    # Вызов методов для демонстрации
    animal_sound(zoo.animals)  # Звуки животных

    parrot.fly()
    lion.run()
    snake.crawl()

    # Работа сотрудников
    zookeeper.work()  # Смотритель выполняет свои обязанности
    zookeeper.feed_animal(parrot)  # Смотритель кормит попугая

    veterinarian.work()  # Ветеринар выполняет свои обязанности
    veterinarian.heal_animal(lion)  # Ветеринар лечит льва

    # Сохранение состояния зоопарка
zoo.save_zoo()

# Загрузка состояния зоопарка (можно закомментировать этот вызов после первого запуска)
new_zoo = Zoo()
new_zoo.load_zoo()