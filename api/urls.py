
from django.contrib import admin
from django.urls import path, include
from blog.views import index_view

#for static files
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('', index_view),
    path('admin/', admin.site.urls),
    path('api/posts/', include('blog.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('summernote/', include('django_summernote.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

