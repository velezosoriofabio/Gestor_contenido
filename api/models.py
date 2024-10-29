from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Content(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = RichTextField()  # Usar RichTextField para formato enriquecido
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title