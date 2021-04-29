import json
from datetime import datetime

from django.shortcuts import render
from cal.models import Data
from cal.memcache import MemcacheLocal


# def sample():
#     rep = MemcacheLocal()
#     result = None
#     if not result:
#         result = index()
#         rep.set('my_key', result, 3600)
#     else:
#         result = rep.get('my_key')
#     print(result)

# def index(request):
#     From = request.GET.get('From')
#     To = request.GET.get('To')
#     my_data = Data.objects.filter(date__range=[From, To])
#     context = []
#     context2 = []
#     for e in my_data:
#         arr = {e: e.EC2}
#         arr2 = {e: e.RDS}
#         context.append(arr)
#         context2.append(arr2)
#
#     return render(request, 'index.html', {'context': context, 'context2': context2})

def index(request):
    memcache = MemcacheLocal()
    from_date = request.GET.get('From')
    to_date = request.GET.get('To')
    final_result = []
    # from_date_str = datetime.strptime(from_date, 'YY-MM-DD')
    # to_date_str = datetime.strptime(to_date, 'YY-MM-DD')
    if from_date:
        memcache_key = 'instance_analytics_' + from_date + '_' + to_date
    else:
        return render(request, 'index.html', {'context': final_result})
    result = memcache.get(memcache_key)
    if result:
        final_result = json.loads(result)
    else:
        my_data = Data.objects.filter(date__range=[from_date, to_date])
        if my_data:
            context_ec2 = []
            context_rds = []
            for e in my_data:
                context_ec2.append([str(e.date), e.EC2])
                context_rds.append([str(e.date), e.RDS])
            final_result = [context_ec2, context_rds]
            memcache.set(memcache_key, json.dumps(final_result), 3600)

    return render(request, 'index.html', {'context': final_result})

