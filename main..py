# Разработай систему управления учетными записями пользователей для небольшой
# компании. Компания разделяет сотрудников на обычных работников и администраторов. У каждого
# сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы, помимо
# обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или
# удалять пользователя из системы.
#
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень
# доступа ('user' для обычных сотрудников).
#
# 2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный
# атрибут уровня доступа, специфичный для администраторов ('admin'). Класс должен также содержать
# методы add_user и remove_user, которые позволяют добавлять и удалять пользователей из списка
# (представь, что это просто список экземпляров User).
#
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации
# снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User():
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = "user"

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_access_level(self):
        return self._access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'

    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f"User {user.get_name()} добавлен.")
        else:
            print("Неверное имя пользователя")

    def remove_user(self, user_list, user_id):
        for i, user in enumerate(user_list):
            if user.get_user_id() == user_id:
                user_list.pop(i)
                print(f"User ID {user_id} удален.")
                return
        print(f"User ID {user_id} не найден.")


users = []
admin = Admin(user_id=18953, name="Катя")
user1 = User(user_id=16548, name="Петя")
user2 = User(user_id=16789, name="Вася")

admin.add_user(users, user1)
admin.add_user(users, user2)

for user in users:
    print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access: {user.get_access_level()}")

admin.remove_user(users, 16548)

for user in users:
    print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access: {user.get_access_level()}")


