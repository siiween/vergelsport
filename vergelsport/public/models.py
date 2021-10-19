from django.db import models

class Comentario(models.Model):
    # videos de enlaces a youtube
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    nombre = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    comentario = models.CharField(max_length = 1000)
    puntuacion = models.PositiveIntegerField(default = 5)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

