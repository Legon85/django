# Подвиг 3.
# Пусть в списке urlpatterns определены следующие два маршрута:
#
# urlpatterns = [
#     path('post/archive/<int:year>/<slug:post_slug>/', views.post_detail),
#     path('post/archive/<int:year>/<int:post_id>/', views.post_detail_id),
# ]
# Для каких URL - адресов сработает 2 - й маршрут?
#
#
# Выберите все подходящие ответы из списка

# Верно.
#
# http: // 127.0.0.1: 8000 / post / archive / 2023 / 17 /
#
# http: // 127.0.0.1: 8000 / post / archive / 2003 / 2 /
#
# http: // 127.0.0.1: 8000 / post / archive / 2022 / python /
#
# http: // 127.0.0.1: 8000 / post / archive / 2012 / kalman /
#
# не сработает ни для каких                                       +
