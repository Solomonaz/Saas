from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit


def home_view(request, *args, **kwargs):

    # print(request.user.is_authenticated, request.user.first_name)
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path = request.path)
    try:
        percent = (page_qs.count() * 100.0) / qs.count()
    except:
        percent = 0.0
    page_visit_count = page_qs.count()
    my_title = 'My Page'
    my_context = {
        'page_title':my_title,
        'queryset':page_qs,
        'page_visit_count':page_visit_count,
        'percent':percent,
        'total_visit_count':qs.count(),
    }
    PageVisit.objects.create(path = request.path)
    return render(request, 'home.html', my_context)
