# Подвиг 8. Пусть в проекте определен следующий список маршрутов:
#
# urlpatterns = [
#     path('', index, name='home'),
#     path('about/', about_view, name='about_name'),
#     path('addpage/', add_page_view, name='add_page'),
#     path('edit/<slug:slug>/', update_page, name='edit_page'),
#     path('contact/', contact_view, name='contact_name'),
#     path('login/', login_view, name='login_name'),
# ]
# Выберите верные варианты вызова и использования функции reverse().
#
#
# Выберите все подходящие ответы из списка
#
# return redirect(reverse('add_page'))                 +
#
# uri = reverse('/about/')
#
# return HttpResponseRedirect(reverse('edit_page', args=['profile']))         +
#
# uri = reverse('login_name')                                +
#
# uri = reverse(update_page, args=['balakirev'])                +
#
# uri = reverse(login_view)                                 +
#
# uri = reverse('/edit/profile/')
#
# uri = reverse('edit_page', args=['balakirev'])                 +