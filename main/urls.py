from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_sharing.urls')),
    path('profile/', include('accounts.urls')),
    path('', include('home.urls'))    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()