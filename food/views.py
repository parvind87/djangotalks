from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'data': 'this is data'}
    return render(request, 'food/index.html', context)

def fake_news_detector(request):
    context = {'data': 'this is fake news detector'}
    return render(request, 'food/index.html', context)