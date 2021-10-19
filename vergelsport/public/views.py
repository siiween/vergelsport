from django.shortcuts import redirect, render
from django.contrib import messages
from public.models import Comentario
from django.http import HttpResponseRedirect
# forms
from public.forms import ComentarioForm


def home(request):
    return render(request, 'public/home.html')


def contacto(request):
    return render(request, 'public/contacto.html')


def servicios(request):
    return render(request, 'public/servicios.html')


def conoceme(request):
    return render(request, 'public/conoceme.html')


def opiniones(request):
    context = {
        'comentarios': Comentario.objects.order_by('-created'),
    }
    return render(request, 'public/opiniones.html', context)


def crearOpinion(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, ('Opinión añadida correctamente'))
        else:
            form = ComentarioForm()
            messages.error(
                request, ('Ha habido un error añadiendo tu opinión'))
            return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))


