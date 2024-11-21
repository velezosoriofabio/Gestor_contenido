from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.index, name='index'),
    path('content/<int:id>/', views.content_detail, name='content_detail'),
    path('render-json/<int:id>/', views.render_json, name='render_json'),
    path('content/<int:id>/json/', views.render_json, name='render_json'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('create/', views.create_content, name='create_content'),
    path('cards/', views.content_list, name='content_list'),
    path('cards/<int:id>/', views.content_detail, name='content_detail'),
    path('contenido/', views.listar_contenido, name='listar_contenido'),
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
