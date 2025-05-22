from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.staticfiles.views import serve
from django.conf import settings
from django.conf.urls.static import static

from . import views

def return_static(request, path, insecure=True, **kwargs):
    return serve(request, path, insecure, **kwargs)

urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', return_static, name='static'),
    path('', views.permanent_redirect, name='permanent_redirect'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'polls.views.page_not_found'