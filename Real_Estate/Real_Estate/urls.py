
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('listings/', include('property_listing.urls')),
    path('account/', include('account.urls')),
    path('contact/', include('contact.urls')),
    path('realtor/', include('realtor.urls')),
    path('', include('core.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)