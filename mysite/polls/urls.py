from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^search/', views.search, name='search'),
    url(r'^sort/', views.sort, name='sort'),
    url(r'^basic/', views.BasicView.as_view(), name='basic'),
    # url(r'^questions/', views.QuestionsView.as_view(), name='questions'),
    url(r'^questions/add', views.QuestionsCreateView.as_view(), name='questions'),

    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
]