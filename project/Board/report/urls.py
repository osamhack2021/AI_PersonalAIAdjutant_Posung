from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.report, name='report'),
    path('report_post/', views.report_post, name='report_post'),
    path('<int:id>', views.report_detail, name='report_detail'),

  

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)