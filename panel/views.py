from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .tasks import task1


def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'panel.html', {'username': request.user.username})
        else:
            return render(request, 'index.html')
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            # 记录会话状态
            login(request, user)
            return render(request, 'panel.html', {'username': request.user.username})
        else:
            return render(request, 'index.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        email = request.POST['email']
        invite_code = request.POST['invite_code']
        if password == repassword and invite_code == "123456":
            User.objects.create_user(username, email, password)
            return redirect('index')
        else:
            return render(request, 'register.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect("index")


@login_required
def xui(request):
    port = '54321'
    # hostname = request.get_host().split(':')[0]
    hostname = 'huanghao.space'
    url = 'http://' + hostname + ':' + port + '/'
    return redirect(url)


@login_required
def user_info(request):
    username = request.user.username
    user = User.objects.get(username=username)
    content = {'username': username,
               'balance': user.friend.balance,
               'longitude': user.friend.longitude,
               'latitude': user.friend.latitude,
               'is_admin': user.is_staff,
               'last_login': "{}年{}月{}日".format(user.last_login.year, user.last_login.month, user.last_login.day)
               }
    task1.delay()

    return render(request, 'user_info_panel.html', content)


def update_location(request):
    try:
        username = request.POST['username']
        longitude = request.POST['longitude']
        latitude = request.POST['latitude']
        user = User.objects.get(username=username)
        user.friend.longitude = longitude
        user.friend.latitude = latitude
        user.save()
        return HttpResponse("succeed")
    except:
        return HttpResponse("failed")
