from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'data': 'this is data'}
    return render(request, 'home/home.html', context)