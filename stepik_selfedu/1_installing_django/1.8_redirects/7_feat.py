# Подвиг 7. Выберите верные варианты реализаций перенаправлений, которые могут быть прописаны в функциях
# представлениях. (Все маршруты считать существующими.)
#
# Выберите все подходящие ответы из списка

#
# redirect('/users/', permanent=True)
#
# HttpResponsePermanentRedirect('/women/users/')
#
# return redirect('/users/')                                    +
#
# return HttpResponsePermanentRedirect('/women/users/')         +
#
# return HttpResponseRedirect('/register/')                     +
#
# HttpResponseRedirect('/register/')