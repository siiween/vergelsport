from django import forms
from public.models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'apellidos', 'comentario', 'puntuacion')
