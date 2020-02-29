from django.shortcuts import render
from .models import examsolution,Ask_Qus
from django.db.models import Q
from django.http import HttpResponse
import json
# Create your views here.

def solution(request):
    if request.method == 'POST':
        src = request.POST['search']
        if src:
            result = examsolution.objects.filter(Q(question__icontains = src))
            if result:
                return render(request,'solution_search.html',{'result':result})
            else:
                # uploading the question in Ask model..

                return render(request,'ask.html',{'src':src})
        else:
            return render(request,'solution_search.html')

    return render(request,'solution_search.html')


# Auto-complete view for search
def solution_autocomplete(request):
    if request.is_ajax():
        query = request.GET.get("term", "")
        companies = examsolution.objects.filter(question__icontains=query)
        results = []
        for company in companies:
            place_json = company.question
            results.append(place_json)
        data = json.dumps(results)
    mimetype = "application/json"
    return HttpResponse(data, mimetype)