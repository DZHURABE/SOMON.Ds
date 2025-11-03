from django.contrib import admin
from django.urls import path
from elonlar import views
from django.conf.urls.static import settings 
from django.conf.urls.static import static
urlpatterns =[
    path(admin/',admin.site.urls),
    path('', views.asosiy,name='asosiy'),     
]  + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)