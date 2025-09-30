from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # Blog app routes
    path("", include(("blog.urls", "blog"), namespace="blog")),
    
    # Authentication routes (optional if you create accounts app)
    # path("accounts/", include("django.contrib.auth.urls")),
]

# Serve static & media files only in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
