from django.urls import path
from . import views
app_name = 'asistan'  # Uygulama adı tanımlandı
urlpatterns = [
    path("process/", views.process, name="process"),
    path("process2/", views.process2, name="process2"),
    
]
