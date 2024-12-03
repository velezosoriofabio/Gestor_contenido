from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .forms import ContentForm
from .models import Content
from bs4 import BeautifulSoup
import json
from django.conf import settings


def render_json(request, id):
    content = get_object_or_404(Content, id=id)
    # Renderiza el HTML completo
    full_html = render(request, 'content_detail.html', {'content': content}).content
    # Utiliza BeautifulSoup para extraer solo el contenido del div container
    soup = BeautifulSoup(full_html, 'html.parser')
    # Construye el diccionario con los datos en el formato requerido
    container_div = soup.find('div', class_='container')
    # Construir la URL dinámica
    link = settings.BASE_URL + f'/content/{content.id}/'
    data = {
        "id": content.id,
        "date": content.created_at.isoformat(),
        "guid": {
            "rendered": link,
        },
        "modified": content.updated_at.isoformat() if hasattr(content, 'updated_at') else content.created_at.isoformat(),
        "slug": content.title.lower().replace(' ', '-'),
        "status": "publish",
        "type": "post",
        "link": link,
        "title": {
            "rendered": content.title
        },
        "content": {
            "rendered": str(container_div),
            "protected": False
        },
        "excerpt": {
            "rendered": content.body[:150],
            "protected": False
        }
    }

    # Retorna la respuesta en JSON
    return JsonResponse(data)
    #return render(request, 'rendered_content.html', {'data': data})
    
def content_detail(request,id):
    # Recupera el contenido específico usando el ID
    content = get_object_or_404(Content, id=id)
    return render(request, 'content_detail.html', {'content': content})


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



def listar_contenido(request):
    contenidos = Content.objects.all()
    return render(request, 'listar_contenido.html', {'contenidos': contenidos})


def home(request):
    contenidos = Content.objects.all()
    return render(request, 'home.html', {'contenidos': contenidos})

def home2(request):
    contenidos = Content.objects.all()
    return render(request, 'home2.html', {'contenidos': contenidos})


def delete_content(request, id):
    content = get_object_or_404(Content, id=id)
    if request.method == 'POST':
        content.delete()
        return redirect('content_list')  # Redirige a la lista de contenidos
    return render(request, 'confirm_delete.html', {'content': content})  # Muestra la vista de confirmación