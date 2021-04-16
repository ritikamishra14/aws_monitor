def read_from_json(request):
    # Use a breakpoint in the code line below to debug your script.
    date_1 = request.get('date_1')
    date_2 = request.get('date_2')
    data = AwsReort.objects.filter(date__range=[date_1, date_2])
    context  = []
    for date in data:
        # create context varible here
        elemnet = {}
        elemnet['date'] = date.ec2
        elemnet['rds'] = date.rds
        context.append(elemnet)
    return render(request, 'articles/article_detail.html', {'context': context})