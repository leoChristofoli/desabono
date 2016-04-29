from django.conf.urls import include, url
from django.contrib import admin
from posto import views

urlpatterns = [
    url(r'^$', 'posto.views.index', name='index'),
    url(r'^cadastro/', 'posto.views.cadastro', name='cadastro'),
    url(r'^admin/', include(admin.site.urls)),
]
