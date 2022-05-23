"""Цикл запрос-ответ. Эта часть приложения отвечает за получения от пользователя данных
и возврат пользователю ответа от функции-handlerа."""
from parser import normalize
import handler


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("Please enter command, name and phone number")
    return inner


@input_error
def output_func(command_dict_func):
    if command_dict_func['command'] == 'hello':
        return "How can I help you?"
    elif command_dict_func['command'] == 'show all':
        return handler.show_all()
    elif command_dict_func['command'] == 'add':
        handler.add_contact(command_dict_func['name'], command_dict_func['phone'])
        return 'Contact added'
    elif command_dict_func['command'] == 'change':
        handler.change_contact(command_dict_func['name'], command_dict_func['phone'])
        return 'Contact changed'
    elif command_dict_func['command'] == 'phone':
        return handler.phone_contact(command_dict_func['name'])
    elif command_dict_func['command'] == 'good bye' or 'close' or 'exit':
        return 'Good bye!'
    else:
        return "Unexpected error"


user_input = input('>>>')
command_dict = normalize(user_input)
while True:
    result = output_func(command_dict)
    print(result)
    if result == 'Good bye!':
        break
    user_input = input('>>>')
    command_dict = normalize(user_input)
