# Подвиг 11. Объявите функцию представления с именем posts_list, которая связана со следующим маршрутом:
#
# urlpatterns = [ ... path('posts/<int:year>', posts_list), ] (Функция должна корректно срабатывать для него.) Внутри
# функции выполните проверку на корректность переданного года. Если он выходит за пределы [1990; 2023], то вызывать
# исключение 404 для отображения страницы с кодом 404. Если же год указан верно, то функция posts_list должна
# возвращать HTTP-ответ со строкой в формате:
#
# "posts: <year>"
#
# Например, для года 2023 должна возвращаться строка (в объекте HTTP-ответа):
#
# "posts: 2023"
#
# P.S. Функцию вызывать не нужно, только объявить.




# from django.http import HttpResponse, HttpRequest, Http404
#
#
# def posts_list(request, year):
#     if year > 2023 or year < 1990:
#         raise Http404()
#     else:
#         return HttpResponse(f"posts: {year}")