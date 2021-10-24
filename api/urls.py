from django.urls import path, include
from posts import urls

urlpatterns = [
    path('posts/', include(urls)),
]
