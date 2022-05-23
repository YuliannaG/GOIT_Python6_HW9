"""Функции обработчики команд -- набор функций, которые ещё называют handler,
они отвечают за непосредственное выполнение команд."""

contacts_dict = {}


def add_contact(name, phone):
    global contacts_dict
    contacts_dict[name] = phone
    return contacts_dict


def change_contact(name, phone):
    global contacts_dict
    contacts_dict[name] = phone
    return contacts_dict


def phone_contact(name):
    global contacts_dict
    return contacts_dict[name]


def show_all():
    return contacts_dict
