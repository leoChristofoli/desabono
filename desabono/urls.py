from django.conf.urls import include, url
from django.contrib import admin
from posto import views as posto_views
from divida import views as divida_views
from usuario import views as usuario_views

urlpatterns = [
    url(r'^$', posto_views.index, name='index'),
    url(r'^cadastro/', posto_views.cadastro, name='cadastro'),
    url(r'^usuarios/', posto_views.credores, name='credores'),
    url(r'^divida/', divida_views.divida, name='divida'),
    url(r'^consulta_divida/', divida_views.consulta_divida, name='consulta_divida'),
    url(r'^login/', usuario_views.login_view, name='login'),
    url(r'^logout/', usuario_views.logout_view, name='logout'),
    url(r'^user/(?P<user_id>)', usuario_views.user_view, name='user'),
    url(r'^admin/', include(admin.site.urls)),
]
