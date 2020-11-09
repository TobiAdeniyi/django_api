from django.contrib import admin
from django.urls import path, include
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('cart/', views.cart, name="cart"),
    # path('accounts/', include('allauth.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    # path('auth/', include('rest_framework_social_oauth2.urls')),
]
