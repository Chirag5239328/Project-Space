from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # This line should be present for accessing the admin site
    path('api/', include('my_app.urls')),  # Include the app's URLs
]
