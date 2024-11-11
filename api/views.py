from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .forms import ContentForm
from .models import Content
from bs4 import BeautifulSoup
import json

def render_json(request, id):
    content = get_object_or_404(Content, id=id)
    # return render(request, 'content_detail.html', {'content': content})
    # Renderiza el HTML completo
    full_html = render(request, 'content_detail.html', {'content': content}).content
    
    # Utiliza BeautifulSoup para extraer solo el contenido del div container
    soup = BeautifulSoup(full_html, 'html.parser')
    container_div = soup.find('div', class_='container')
    
    # Retorna el HTML del div container
    # return HttpResponse(container_div)

    # Construye el diccionario con los datos en el formato requerido
    data = {
        "id": content.id,
        "date": content.created_at.isoformat(),
        "date_gmt": content.created_at.isoformat(),
        "guid": {
            "rendered": f"https://tu-dominio.com/?p={content.id}"
        },
        "modified": content.updated_at.isoformat() if hasattr(content, 'updated_at') else content.created_at.isoformat(),
        "modified_gmt": content.updated_at.isoformat() if hasattr(content, 'updated_at') else content.created_at.isoformat(),
        "slug": content.title.lower().replace(' ', '-'),
        "status": "publish",
        "type": "post",
        "link": f"https://tu-dominio.com/{content.title.lower().replace(' ', '-')}/",
        "title": {
            "rendered": content.title
        },
        "content": {
            "rendered": str(container_div),
            "protected": False
        },
        "excerpt": {
            "rendered": content.body[:150],  # Un ejemplo de resumen de 150 caracteres
            "protected": False
        }
    }

    # Retorna la respuesta en JSON
    # return JsonResponse(data)
    return render(request, 'rendered_content.html', {'data': data})
    
def content_detail(request,id):
    # Recupera el contenido específico usando el ID
    content = get_object_or_404(Content, id=id)
    return render(request, 'content_detail.html', {'content': content})


# Create your views here.
def create_content(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)  # Usar request.FILES para manejar imágenes
        if form.is_valid():
            form.save()  # Guarda el contenido en la base de datos
            return redirect('content_list')  # Redirigir a una lista de contenidos o donde prefieras
    else:
        form = ContentForm()
    
    return render(request, 'create_content.html', {'form': form})

def content_list(request):
    contents = Content.objects.all()
    return render(request, 'content_list.html', {'contents': contents})