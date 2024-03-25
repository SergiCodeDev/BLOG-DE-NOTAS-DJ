from django.shortcuts import render, redirect
from .models import Nota
from .forms import NotaForm

# Create your views here.

def inicio(request):
    notas = Nota.objects.all()
    context = {"notas": notas}
    return render(request, "notas/inicio.html", context)

def agregar(request):
    if request.method == "POST":
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = NotaForm()
    
    context = {"form": form}
    return render(request, "notas/agregar.html", context)

def eliminar(request, nota_id):
    nota = Nota.objects.get(id=nota_id)
    nota.delete()
    return redirect("inicio")

def editar(request, nota_id):
    nota = Nota.objects.get(id=nota_id)
    if request.method == "POST":
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = NotaForm(instance=nota)
    
    context = {"form": form}
    return render(request, "notas/editar.html", context)

