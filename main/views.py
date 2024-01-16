from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    host = request.META["HTTP_HOST"] # получаем адрес сервера
    user_agent = request.META["HTTP_USER_AGENT"]    # получаем данные бразера
    path = request.path # получаем запрошенный путь
    user_ip = request.META["REMOTE_ADDR"] # IP пользователя
    
     
    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User IP: {user_ip}</p>
        <p>User-agent: {user_agent}</p>
    """)