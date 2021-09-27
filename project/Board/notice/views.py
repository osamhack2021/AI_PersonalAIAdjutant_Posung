from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import *


def notice(request):
    notices = {'notices': Notice.objects.all()}
    return render(request, 'notice.html', notices)

def notice_post(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        notice = Notice(author=author, title=title, content=content)
        notice.save()
        return HttpResponseRedirect(reverse('notice'))
    else:
        return render(request, 'notice_post.html')

def notice_detail(request, id):
    try:
        notice = Notice.objects.get(pk=id)
    except Notice.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'notice_detail.html', {'notice': notice})