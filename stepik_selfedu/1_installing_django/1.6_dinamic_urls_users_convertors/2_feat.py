# Подвиг 2. Пусть имеется следующее определение маршрута:
#
# path('post/archive/<int:year>/<slug:post_slug>/', views.post_detail)
# Укажите правильные определения функции представления для обработки этого маршрута.
#
# Выберите все подходящие ответы из списка

# def post_detail(year, post_slug): ...
#
# функция представления не может быть связана с динамическим URL
#
# def post_detail(request, post_slug, year): ...    +
#
# def post_detail(request, post_slug): ...
#
# def post_detail(request, year, post_slug): ...    +
