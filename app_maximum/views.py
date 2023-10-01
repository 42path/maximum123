from django.http import HttpResponse
from django.shortcuts import render
from .models import Advertisement

# Create your views here.
def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisement': advertisement}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top_sellers.html')