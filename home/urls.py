from django.urls import path
#from django.conf.urls import url
from .views import url_shortner
from . import views
app_name = 'home'

urlpatterns = [
    #path('', views.index, name='index'),
    #path('short-url/', views.short_url, name='short url'),
    path('short-url/', url_shortner.as_view(), name="url-shortner"),
    path('fake-news-detector/', views.fake_news_detector, name='fake_news_detector'),
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]