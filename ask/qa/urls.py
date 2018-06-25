from django.conf.urls import url
from .views import test,vquestion,vpopular,vquestion_ask,vsignup,vlogin,vlogout,vmainpg,vquestion_ans

urlpatterns = [
    url(r'^$', vmainpg, name='mainpg'),
    url(r'^question/(?P<pk>\d+)/$', vquestion, name='question'),
    url(r'^popular/', vpopular, name='popular'),
    url(r'^ask/', vquestion_ask, name='question_ask'),
    url(r'^answer/', vquestion_ans, name='question_ans'),
    url(r'^new/', test, name='test'),
    url(r'^login/', vlogin, name='login'),
    url(r'^signup/', vsignup, name='signup'),
    url(r'^logout/', vlogout, name='logout'),
]
