from django.contrib import admin
from django.urls import path, include
# from home.views import home,home2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),


]
