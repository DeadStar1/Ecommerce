from django.contrib import admin
from django.urls import path
from adoptions import views
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home'),
    path('adoptions/<int:pet_id>/',views.pet_detail,name= 'pet_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

