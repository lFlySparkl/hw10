from collections import UserDict

class Field:
    # Field: Базовий клас для полів запису. Буде батьківським для всіх полів, у ньому реалізується логіка загальна для всіх полів
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # Name: Клас для зберігання імені контакту. Обов'язкове поле.
    ...


class Phone(Field):
    # Необов'язкове поле з телефоном та таких один запис Record може містити декілька.
    # Клас Phone:
    # Реалізовано валідацію номера телефону (має бути 10 цифр).
    # Реалізовано всі класи із завдання
    def __init__(self, value) -> None:
        if len(value) == 10 and value.isdigit():
            self.value = value
        else:
            raise ValueError


class Record:
    # Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    # Відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name
    # Record:
    # Додавання телефонів.
    # Видалення телефонів.
    # Редагування телефонів.
    # Пошук телефону.
    # Критерії приймання
    # Клас Record:
    # Реалізовано зберігання об'єкта Name в окремому атрибуті.
    # Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.
    # Реалізовано методи для додавання - add_phone/видалення - remove_phone/редагування - edit_phone/пошуку об'єктів Phone - find_phone.

    #  1. Метод find_phone класу Record не знайшов перший номер контакту!
    #  2. Метод find_phone класу Record не знайшов другий номер контакту!
    #  3. Провалена перевірка. Якщо номеру телефона не існує то метод find_phone класу Record повинен повернути None!
    #  4. Метод edit_phone класу Record не відреагував номер телефону, що існує!
    #  5. Провалена перевірка. Якщо номеру телефону не існує то метод edit_phone класу Record повинен викинути виключення ValueError!
    #  6. Провалена перевірка. Метод remove_phone класу Record не видаляє номер телефону!

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, value: Field):
        self.phones.append(value)

    def remove_phone(self, number):
        if number in self.phones:
            self.phones.remove(number)
        else:
            raise ValueError

    def edit_phone(self, old_number, new_number):
        if old_number in self.phones:
            idx = ""
            for number in self.phones:
                if number == old_number:
                    idx = self.phones.index(number)
            self.phones[idx] = new_number
                
        else:
            raise ValueError

    def find_phone(self, number):
        if number in self.phones:
            self.value = number
            return self
        else:
            return None


class AddressBook(UserDict):
    contacts = {}
    # AddressBook: Клас для зберігання та управління записами.
    # Успадковується від UserDict, та містить логіку пошуку за записами до цього класу
    # AddressBook:
    # Додавання записів.
    # Пошук записів за іменем.
    # Видалення записів за іменем.
    # Клас AddressBook:
    # Реалізовано метод add_record, який додає запис до self.data.
    # Реалізовано метод find, який знаходить запис за ім'ям.
    # Реалізовано метод delete, який видаляє запис за ім'ям.
    # Записи Record у AddressBook зберігаються як значення у словнику. В якості ключів використовується значення Record.name.value.

    #  1. Метод add_record класу AddressBook не зберіг запис Record!
    #  2. Метод find класу AddressBook не повернув запис Record який був збережений!
    #  3. Провалена перевірка. Якщо запису не існує то метод find класу AddressBook повинен повернути None!
    #  2. Метод delete класу AddressBook не видалив запис Record який був збережений!
    #  3. Провалена перевірка. Метод delete класу AddressBook не видалив запис!

    def add_record(self, contact:Record):
        self.data[contact.name.value] = contact

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None

    def delete(self, contact):
        if contact in self.data:
            return self.data.pop(contact)
        else:
            return None


if __name__ == "__main__":
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # # Додавання запису John до адресної книги
    book.add_record(john_record)

    # # Створення та додавання нового запису для Jane
    # jane_record = Record("Jane")
    # jane_record.add_phone("9876543210")
    # book.add_record(jane_record)

    # # Виведення всіх записів у книзі
    # for name, record in book.data.items():
    #     print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
