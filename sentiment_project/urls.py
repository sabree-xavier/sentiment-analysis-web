from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from home.views import *

urlpatterns = [
    path('', home_view, name='process_review'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)