from django.shortcuts import render, redirect

from .models import User


def index(request):
    if request.method == 'GET':
        if request.session.get('username'):
            return render(request, 'panel.html', {'user_name': request.session.get('username')})
        else:
            return render(request, 'index.html')
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return render(request, 'index.html')
        if user.username == username and user.password == password:
            # 记录会话状态
            request.session['username'] = username
            return render(request, 'panel.html', {'user_name': request.session.get('username')})
        else:
            return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def logout(request):
    request.session.flush()
    return redirect("index")

def xui(request):
    port = '54321'
    hostname = request.get_host().split(':')[0]
    url = 'http://' + hostname + ':' + port + '/'
    return redirect(url)
