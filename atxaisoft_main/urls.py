
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('atxaisoft.urls')),
    path('user/', include('user.urls')),
    path('asistan/', include('asistan.urls')),
    path('product_detail/', include('product_packages.urls')),
]
