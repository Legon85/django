# Подвиг 6. Имеется следующий фрагмент программы:
#
# class ABConvertor:
#     regex = "[a-zA-Z]{1,10}"
#
#     def to_python(self, value):
#         return str(value)
#
#     def to_url(self, value):
#         return str(value)
#
#
# register_converter(ABConvertor, "abc10")
#
# urlpatterns = [
#     path('docs/<abc10:slug_doc>/', views.doc_detail, name='docs'),
# ]
# Выберите все верные утверждения для этого фрагмента.
#
#
# Выберите все подходящие ответы из списка
#
# класс ABConvertor определяет пользовательский конвертор для маршрутов с проверкой наличия только символов
# латинского алфавита длиной от 1 до 10   +
#
# функция register_converter() регистрирует класс ABConvertor как конвертор с именем abc10   +
#
# функция register_converter() записана неверно, сначала нужно указывать имя, а затем класс
#
# метод to_python() класса ABConvertor формирует и возвращает значение URL-параметра для функции представления  +
#
# метод to_url() класса ABConvertor формирует и возвращает значение URL-параметра для функции представления
#
# метод to_python() класса ABConvertor формирует и возвращает значение для URL-адреса
#
# метод to_url() класса ABConvertor формирует и возвращает значение для URL-адреса    +