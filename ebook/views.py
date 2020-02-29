
from django.shortcuts import render
from ebook.models import ebook
from django.db.models import Q
from django.http import HttpResponse
import json
# Create your views here.

def book_search(request):
    if request.method == 'POST':
        src = request.POST['search']
        if src:
            result = ebook.objects.filter(Q(title__icontains = src))
            if result:
                return render(request,'book_search.html',{'result':result})
            else:
                return render(request,'book_error.html')
        else:
            return render(request,'book_search.html')

    return render(request,'book_search.html')

# Auto-complete view for search
def ebook_autocomplete(request):
    if request.is_ajax():
        query = request.GET.get("term", "")
        companies = ebook.objects.filter(title__icontains=query)
        results = []
        for company in companies:
            place_json = company.title
            results.append(place_json)
        data = json.dumps(results)
    mimetype = "application/json"
    return HttpResponse(data, mimetype)
