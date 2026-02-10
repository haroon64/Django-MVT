
import django
from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.urls import include
from django.conf.urls.static import static  
urlpatterns = [
    path('core/', include('core.urls')),
    path('items/', include('item.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
    # Include django_browser_reload URLs only in DEBUG mode
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]