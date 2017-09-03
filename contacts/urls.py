from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_new, name='post_new'),
    url(r'^contactlist/$', views.Contactlist, name='contactlist'),
    url(r'^contact_edit/(?P<pk>\d+)/$', views.contact_edit, name='contact_edit'),
    url(r'^contact_delete/(?P<pk>\d+)/$', views.contact_delete, name='contact_delete'),

]