# backend/urls.py
from django.contrib import admin
from django.urls import path, include  # Use 'include' to reference other URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Include the URLs for each app
    path('users/', include('users.urls')),  # Users API
    path('posts/', include('posts.urls')),  # Posts API
    path('notifications/', include('notifications.urls')),  # Notifications API
]
