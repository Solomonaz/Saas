from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit


def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path = request.path)
    page_visit_count = page_qs.count()
    my_title = 'My Page'
    my_context = {
        'page_title':my_title,
        'queryset':page_qs,
        'page_visit_count':page_visit_count,
        'percent':(page_qs.count() * 100.0) / qs.count(),
        'total_visit_count':qs.count(),
    }
    path = request.path
    print('path', path)
    PageVisit.objects.create(path = request.path)
    
    return render(request, 'home.html', my_context)
