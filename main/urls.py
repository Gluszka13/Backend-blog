from . import views
from django.urls import path
from .feeds import LatestPostsFeed
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='home'),
    path('upload/', views.image_upload_view),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)