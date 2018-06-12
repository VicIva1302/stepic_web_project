from django.conf.urls import url
from qa.views import test

urlpatterns = [
    url(r'^$', test, name='mainpg'),
    url(r'^question/(?P<pk>\d+)/$', test, name='question'),
    url(r'^popular/', test, name='popular'),
    url(r'^ask/', test, name='question_ask'),
    url(r'^answer/', test, name='question_ans'),
    url(r'^new/', test, name='test'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', test, name='signup'),
    url(r'^logout/', test, name='logout'),
]
