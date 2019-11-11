from django.contrib import admin
from django.urls import path
from mysite import views
from mysite.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mysite/', index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
