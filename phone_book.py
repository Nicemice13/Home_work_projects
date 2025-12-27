class Phone_book:
    """Телефонная книга."""

    def __init__(self,phone_book):
        self.phone_book = phone_book

    def add_contact(self, name, phone_number):
        """Добавь имя и номер телефона."""

        self.phone_book[name] = phone_number
        print(f"Контакт {name} добавлен в телефонную книгу")

    def find_contact(self, name):
        """Найди нужный контакт из списка."""

        if name in self.phone_book:
            print(f"Номер телефона {name}: {self.phone_book[name]}")
        else:
            print(f"Контакт {name} не найден в телефонной книге")

    def remove_contact(self, name):
        """Удали не нужный контакт."""

        if name in self.phone_book:
            del self.phone_book[name]
            print(f"Контакт {name} удален из телефонной книги")
        else:
            print(f"Контакт {name} не найден в телефонной книге")

    def update_contact(self, name, new_phone_number):
        """Обнови номер телефона."""

        if name in self.phone_book:
            self.phone_book[name] = new_phone_number
            print(f"Номер телефона контакта {name} обновлен")
        else:
            print(f"Контакт {name} не найден в телефонной книге")

    def display_contacts(self):
        """Выведи все контакты."""

        if self.phone_book != {}
            for name, phone_number in self.phone_book.items():
                if name in self.phone_book:
                    print(f"{name}: {phone_number}")
                else:
                    print("Контакт не найден в телефонной книге")
        else:
            print("Телефонная книга пуста")
            print("Хотите добавить новую запись?")

    def remove_all_contacts(self):
        """Удали все контакты."""

        self.phone_book.clear()
        print("Все контакты удалены из телефонной книги")

pb = Phone_book({})

while True:
    print("1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Удалить контакт")
    print("4. Обновить контакт")
    print("5. Вывести все контакты")
    print("6. Выйти")
    print("7. Удалить все контакты")
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
        pb.remove_contact(name)
    elif choice == "4":
        name = input("Введите имя контакта: ")
        new_phone_number = input("Введите новый номер телефона контакта: ")
        pb.update_contact(name, new_phone_number)
    elif choice == "5":
        pb.display_contacts()
    elif choice == "6":
        print("Выход из программы")
        break
    elif choice == "7":
        pb.remove_all_contacts()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")