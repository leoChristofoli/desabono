from django.conf.urls import include, url
from django.contrib import admin
from posto import views

urlpatterns = [
    # Examples:
    url(r'^$', 'posto.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
