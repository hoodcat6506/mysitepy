from django.http import HttpResponseRedirect
from django.shortcuts import render

from guestbook.models import Guestbook


def gusetbook_index(request):
    return render(request, 'guestbook/list.html', {'guestbook_list': Guestbook.objects.all().order_by('-reg_date')})


def add_guestbook(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['pass']
    guestbook.content = request.POST['content']
    guestbook.save()

    return HttpResponseRedirect('/guestbook')


def guestbook_deleteform(request):
    return render(request, 'guestbook/deleteform.html', {'no': request.GET['no']})


def delete_guestbook(request):
    guestbook = Guestbook.objects \
        .filter(id=request.POST['no']) \
        .filter(password=request.POST['password'])
    if len(guestbook) == 0:
        return HttpResponseRedirect('/guestbook?result=fail')

    guestbook.delete()
    return HttpResponseRedirect('/guestbook')
