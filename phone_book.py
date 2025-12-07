class Phonebook:
    """Телефонная книга."""
    def __init__(self, name, phone_number):
        """Создай атрибуты класса: имя и номер."""
        self.name = name
        self.phone_number = phone_number
        self.Phonebook = {}
    def add_contact(self, name, phone_number):
        """Добавь имя и номер телефона."""
        self.Phonebook[name] = phone_number
        print(f"Контакт {name} добавлен в телефонную книгу")
    def find_contact(self, name):
        """Найди нужный контакт из списка."""
        if name in self.Phonebook:
            print(f"Номер телефона {name}: {self.Phonebook[name]}")
        else:
            print(f"Контакт {name} не найден в телефонной книге")
    def remote_contact(self, name):
        """Удали не нужный контакт."""
        if name in self.Phonebook:
            del self.Phonebook[name]
            print(f"Контакт {name} удален из телефонной книги")
        else:
            print(f"Контакт {name} не найден в телефонной книге")
    def update_contact(self, name, new_phone_number):
        """Обнови номер телефона."""
        if name not in self.Phonebook:
            print(f"Контакт {name} не найден в телефонной книге")
            return
        if name in self.Phonebook:
            self.Phonebook[name] = new_phone_number
            print(f"Номер телефона контакта {name} обновлен")
        else:
            print(f"Контакт {name} не найден в телефонной книге")
    def display_contacts(self):
        """Выведи все контакты."""
        print("Телефонная книга:")
        for name, phone_number in self.Phonebook.items():
            print(f"{name}: {phone_number}")
pb = Phonebook("", "")
while True:
    print("1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Удалить контакт")
    print("4. Обновить контакт")
    print("5. Вывести все контакты")
    print("6. Выйти")
    choice = input("Выберите действие: ")
    if choice == "1":
        name = input("Введите имя контакта: ")
        phone_number = input("Введите номер телефона контакта: ")
        pb.add_contact(name, phone_number)
    elif choice == "2":
        name = input("Введите имя контакта: ")
        pb.find_contact(name)
    elif choice == "3":
        name = input("Введите имя контакта: ")
        pb.remote_contact(name)
    elif choice == "4":
        name = input("Введите имя контакта: ")
        new_phone_number = input("Введите новый номер телефона контакта: ")
        pb.update_contact(name, new_phone_number)
    elif choice == "5":
        pb.display_contacts()
    elif choice == "6":
        print("Выход из программы")
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")