# Подвиг 4. Объявите функцию представления с именем post_detail и одним параметром request. В этой функции выполните
# проверку наличия параметров в GET-запросе и если они есть, функция должна вернуть их в виде HTTP-ответа со строкой
# в формате:
#
# ключ_1=значение_1|ключ_2=значение_2|...
#
# (все без пробелов, в конце вертикальная черта стоять не должна, только между парами).
#
# Если GET-параметров передано не было, то функция post_detail() должна вернуть HTTP-ответ со строкой "GET is empty".
#
# P.S. Функцию вызывать не нужно, только объявить.

# from django.http import HttpResponse, HttpRequest, QueryDict
#
# def post_detail(request):
#     if request.GET:
#         d = dict(request.GET)
#         return HttpResponse(f"{list(d.keys())[0]}={list(d.values())[0][0]}|{list(d.keys())[1]}={list(d.values())[1][0]}")
#     else:
#         return HttpResponse("GET is empty")
