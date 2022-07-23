from django.contrib import admin
from django.urls import include, path

from .views import HomePageView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls, name='index'),
    path('', HomePageView.as_view(), name='home'),
    path('todos/', include('todo.urls')),
    path('auth/', include('users.urls')),
    path('languages/', include('languages.urls')),
    path('api/v1/languages/', include('languages.api.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
