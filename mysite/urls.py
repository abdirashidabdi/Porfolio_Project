from django.contrib import admin
from django.urls import path
from mysite import views
from mysite.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mysite/', index, name='index'),
]
