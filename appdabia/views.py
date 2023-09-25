from django.shortcuts import render, redirect
from .models import Programas, Trilhas, Tabela, Tasks


def home (request):
  programas = Programas.objects.all()
  trilhas = Trilhas.objects.all()
  tabelas = Tabela.objects.all()
  print(programas)
  return render(request,"home.html",context={"programas": programas , "trilhas": trilhas, "tabelas":tabelas})


def list_tasks(request):
  tasks = Tasks.objects.all()
  context = { "tasks": tasks }
  return render(request, "list_tasks.html", context=context)


def create_task(request):
  return render(request, "task_form.html")


def create_programas(request):
  if request.method == 'POST':
    Programas.objects.create(
      title = request.POST['title'],
      duraçao = request.POST['duraçao'],
      genero = request.POST['genero'],
      preço = request.POST['preço'],
      desc = request.POST['desc']
    )
    return redirect('home')
  return render(request, "programas_form.html", context={'type':'Adicionar'})


def update_programas(request, id):
  programa = Programas.objects.get(id = id)
  if request.method == 'POST':
    programa.title = request.POST['title']
    programa.duraçao = request.POST['duraçao']
    programa.genero = request.POST['genero']
    programa.preço = request.POST['preço']
    programa.desc = request.POST['desc']
    programa.save()
    
    return redirect('home')
  return render(request, "programas_form.html", context={'type':'Atualizar', 'programa':programa})


def delete_programas(request, id):
  programa = Programas.objects.get(id = id)
  if request.method == 'POST':
    if 'confirm' in request.POST:
      programa.delete()
    
    return redirect('home')
  return render(request, "are_you_programas.html", context={'programa':programa})


def create_trilhas(request):
  if request.method == 'POST':
    Trilhas.objects.create(
      title = request.POST['title'],
      zona = request.POST['zona'],
      nivel = request.POST['nivel'],
      mais_famosa = request.POST['preço']
    )
    return redirect('home')
  return render(request, "trilhas_form.html", context={'type':'Adicionar'})


def update_trilhas(request, id):
  trilha = Trilhas.objects.get(id = id)
  if request.method == 'POST':
    trilha.title = request.POST['title']
    trilha.zona = request.POST['zona']
    trilha.nivel = request.POST['nivel']
    trilha.mais_famosa = request.POST['preço']
    trilha.save()
    
    return redirect('home')
  return render(request, "trilhas_form.html", context={'type':'Atualizar', 'trilha':trilha})


def delete_trilhas(request, id):
  trilha = Trilhas.objects.get(id = id)
  if request.method == 'POST':
    if 'confirm' in request.POST:
      trilha.delete()
    
    return redirect('home')
  return render(request, "are_you_trilhas.html", context={'trilha':trilha})

