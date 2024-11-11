from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('content/<int:id>/', views.content_detail, name='content_detail'),
    path('render-json/<int:id>/', views.render_json, name='render_json'),
    path('content/<int:id>/json/', views.render_json, name='render_json'),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # Si deseas subir imágenes
    path('create/', views.create_content, name='create_content'),  # Ruta para crear contenido
    path('cards/', views.content_list, name='content_list'),
    path('cards/<int:id>/', views.content_detail, name='content_detail'),  # Para mostrar una tarjeta en detalle
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
