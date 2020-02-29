from django.shortcuts import render
from .models import Solution_videos
from django.db.models import Q
from django.http import HttpResponse
import json
# Create your views here.

def tutorial(request):
    if request.method == 'POST':
        src = request.POST['search']
        if src:
            result = Solution_videos.objects.filter(Q(name__icontains = src))
            if result:
                return render(request,'t_search.html',{'result':result})
            else:
                return render(request,'t_error.html')
        else:
            return render(request,'t_search.html')

    return render(request,'t_search.html')


# Auto-complete view for search
def tutorial_autocomplete(request):
    if request.is_ajax():
        query = request.GET.get("term", "")
        companies = Solution_videos.objects.filter(name__icontains=query)
        results = []
        for company in companies:
            place_json = company.name
            results.append(place_json)
        data = json.dumps(results)
    mimetype = "application/json"
    return HttpResponse(data, mimetype)