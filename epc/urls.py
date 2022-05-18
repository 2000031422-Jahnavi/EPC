from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include("hireit.urls")),
   
    path('admin/', admin.site.urls),
]