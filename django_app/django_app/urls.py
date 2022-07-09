from django.contrib import admin
from django.urls import include, path

from .views import HomePageView


urlpatterns = [
    path('admin/', admin.site.urls, name='index'),
    path('', HomePageView.as_view(), name='home'),
    path('todos/', include('todo.urls')),
    path('auth/', include('users.urls')),
    path('languages/', include('languages.urls')),
    path('api/v1/', include('languages.api.urls')),
]
