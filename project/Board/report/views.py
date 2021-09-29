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
        title = request.POST['title']
        content = request.POST['content']
        report = Report(author=author, title=title, content=content)
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