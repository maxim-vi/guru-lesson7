from datetime import time



def function_heck_time_day(current_time):
    if time(hour=6) > current_time or current_time >= time(hour=22):
        return True

def function_enable_dark_theme(dark_theme_enabled_by_user, current_time):
    if dark_theme_enabled_by_user is None:
        return function_heck_time_day(current_time)
    elif dark_theme_enabled_by_user:
        return True
    else:
        return False

def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)

    is_dark_theme = function_heck_time_day(current_time)
    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True

    is_dark_theme = function_enable_dark_theme(function_heck_time_day, current_time)
    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    def get_user_name(user_list, name):
        for user in user_list:
            if user["name"] == name:
                return user

    suitable_users = get_user_name(users, "Olga")
    assert suitable_users == {"name": "Olga", "age": 45}

    def function_lowest_age(user_list, age):
        new_users_list = []
        for user in user_list:
            if user["age"] < age:
                new_users_list.append(user)
        return new_users_list

    suitable_users = function_lowest_age(users, 20)
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"
def function_pretty_desc(func, *args):
    name = func.__name__
    desc =f'{name.title().replace("_"," ")} [{", ".join(args)}]'
    print(desc)
    return desc

def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = function_pretty_desc(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = function_pretty_desc(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = function_pretty_desc(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"