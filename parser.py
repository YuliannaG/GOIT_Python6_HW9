"""Парсер команд. Часть которая отвечает за разбор введенных пользователем строк,
выделение из строки ключевых слов и модификаторов команд."""


def normalize(raw_user_input: str) -> dict[str, str]:
    user_input = raw_user_input.lower().strip()
    command_dict: dict[str, str] = {}

    if user_input in ['hello', 'show all', 'good buy', 'close', 'exit']:
        command_dict['command'] = user_input
    else:
        user_input_list = user_input.split()
        if user_input_list[0] == 'phone' and len(user_input_list) == 2:
            command_dict['command'] = user_input_list[0]
            command_dict['name'] = user_input_list[1]
        elif (user_input_list[0] == 'add' or 'change') and len(user_input_list) == 3:
            command_dict['command'] = user_input_list[0]
            command_dict['name'] = user_input_list[1]
            command_dict['phone'] = user_input_list[2]

    return command_dict
