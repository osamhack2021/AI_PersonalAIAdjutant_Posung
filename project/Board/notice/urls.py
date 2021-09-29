from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.notice, name='notice'),
    path('notice_post/', views.notice_post, name='notice_post'),
    path('<int:id>', views.notice_detail, name='notice_post_detail'),

  

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)