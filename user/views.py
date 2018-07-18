from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render

from user.models import User


def joinform(request):
    return render(request, 'user/joinform.html')


def join(request):
    user = User()
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.name = request.POST['name']
    user.gender = request.POST['gender']

    user.save()
    return HttpResponseRedirect('/user/joinsuccess')


def join_success(request):
    return render(request, 'user/joinsuccess.html')


def loginform(request):
    return render(request, 'user/loginform.html')


def login(request):
    result = User.objects \
        .filter(email=request.POST['email']) \
        .filter(password=request.POST['password'])

    # 로그인 실패
    if len(result) == 0:
        return HttpResponseRedirect('/user/loginform?result=fail')

    # 로그인 처리
    auth_user = result[0]
    request.session['authuser'] = model_to_dict(auth_user) # user 객체를 맵으로 전환

    return HttpResponseRedirect('/')


def logout(request):
    del request.session['authuser']

    return HttpResponseRedirect('/')
