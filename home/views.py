from django.http import HttpResponseRedirect
from django.shortcuts import render
import pyshorteners
from django.views import View

# Create your views here.
def index(request):
    context = {'data': 'this is data'}
    return render(request, 'home/home.html', context)
def fake_news_detector(request):
    context = {'data': 'this is fake news detector'}
    return render(request, 'home/fake-news.html', context)

class url_shortner(View):
   def post(self, request):
      long_url = 'url' in request.POST and request.POST['url']
      pys = pyshorteners.Shortener()
      short_url = pys.tinyurl.short(long_url)
      return render(request,'home/short-url.html', context={'short_url':short_url,'long_url':long_url})

   def get(self, request):
      return render(request,'home/short-url.html')