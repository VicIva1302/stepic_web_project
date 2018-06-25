from django.conf.urls import url
from qa.views import test
from . import views

#app_name = 'qa'
urlpatterns = [
    #url(r'^$', test, name='mainpg'),
    # url(r'^question/(?P<pk>\d+)/$', test, name='question'),
    # url(r'^popular/', test, name='popular'),
    # url(r'^ask/', test, name='question_ask'),
    # url(r'^answer/', test, name='question_ans'),
    # url(r'^new/', test, name='test'),
    # url(r'^login/', test, name='login'),
    # url(r'^signup/', test, name='signup'),
    # url(r'^logout/', test, name='logout'),
    # ex: /qa/
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /qa/5/
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /qa/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /qa/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
