from django.conf.urls import include, url
from django.contrib import admin
from posto import views as posto_views
from divida import views as divida_views

urlpatterns = [
    url(r'^$', posto_views.index, name='index'),
    url(r'^cadastro/', posto_views.cadastro, name='cadastro'),
    url(r'^usuarios/', posto_views.credores, name='credores'),
    url(r'^divida/', divida_views.divida, name='divida'),
    url(r'^consulta_divida/', divida_views.consulta_divida, name='consulta_divida'),
    url(r'^admin/', include(admin.site.urls)),
]
