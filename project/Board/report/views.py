from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import *


def report(request):
    reports = {'reports': Report.objects.all()}
    return render(request, 'report.html', reports)

def report_post(request):
    if request.method == "POST":
        author = request.POST['author']
        rank = request.POST['rank']
        title = request.POST['title']
        content = request.POST['content']
        content2 = request.POST['content2']
        content3 = request.POST['content3']
        report = Report(author=author, rank=rank title=title, content=content, content2=content2, content3=content3)
        report.save()
        return HttpResponseRedirect(reverse('report'))
    else:
        return render(request, 'report_post.html')

def report_detail(request, id):
    try:
        report = Report.objects.get(pk=id)
    except Report.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'report_detail.html', {'report': report})