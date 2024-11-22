from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('scan/', include('scan.urls')),
        path('admin/', admin.site.urls),
]
