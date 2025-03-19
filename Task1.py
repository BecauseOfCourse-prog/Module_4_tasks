import wikipedia
from datetime import datetime

wikipedia.set_lang('ru')

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        t_start = datetime.now()
        result = func(*args, **kwargs)
        t_finish = datetime.now()
        execution_time = t_finish - t_start
        milliseconds = round(execution_time.microseconds / 1000)
        print(f"Функция была выполнена за "
              f"{execution_time.seconds}s {milliseconds}ms")
        return result
    return wrapper

@measure_execution_time
def wiki_query(query):
    return wikipedia.summary(query)

query = input("Введите ваш запрос: ")
print(wiki_query(query))


def requires_admin(func):
    def wrapper(user, *args, **kwargs):
        if user.get("role") == "admin":
            result = func(user, *args, **kwargs)
            return result
        else:
            return PermissionError("У данного пользователя отсутствуют права администратора.")
    return wrapper

@requires_admin
def delete_user(user, username_to_delete):
    return f"Пользователь {username_to_delete} был удалён пользователем {user["username"]}."


admin_user = {"username": "Alice", "role": "admin"}
regular_user = {"username": "Bob", "role": "user"}

print(delete_user(admin_user, "Charlie"))
print(delete_user(regular_user, "Charlie"))