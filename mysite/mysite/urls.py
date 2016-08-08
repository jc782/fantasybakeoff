from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^fbo/', include('fantasybakeoff.urls', namespace='fbo')),
    url(r'^accounts/', include('allauth.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
