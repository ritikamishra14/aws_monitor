from django.shortcuts import render
from cal.models import Data
from django.views.decorators.cache import cache_page

from datetime import date
from datetimerange import DateTimeRange


@cache_page(200)
def index(request):
    From = request.GET.get('From')
    To = request.GET.get('To')
    # print(From)
    my_data = Data.objects.filter(date__range=[From, To])
    context = []
    context2 = []
    for e in my_data:
        arr = {e: e.EC2}
        arr2 = {e: e.RDS}
        context.append(arr)
        context2.append(arr2)

    return render(request, 'index.html', {'context': context, 'context2': context2})
