from django.contrib import admin
from public.models import Comentario
# Register your models here.


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'created')

