from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^friends$', views.dashboard),
    url(r'^user/(?P<id>\d+)$', views.view),
    url(r'^addfriend/(?P<id>\d+)$', views.add),
    url(r'^removefriend/(?P<id>\d+)$', views.remove),
]
