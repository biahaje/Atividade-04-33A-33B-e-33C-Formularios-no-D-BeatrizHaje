from django.db import models

from django.db import models

class Programas(models.Model):
  
  title = models.CharField(max_length=100, null=True)
  duraçao = models.CharField(max_length=50, null=True)
  genero = models.CharField(max_length=30, null=True)
  preço = models.CharField(max_length=30, null=True)
  desc = models.CharField(max_length=500, null=True)

class Trilhas(models.Model):
  ZONAS = [
    ("N", "Norte"),
    ("S", "Sul"),
    ("L", "Leste"),
    ("O", "Oeste"),
  ]
  
  NIVEIS = [
    ("F", "Facil"),
    ("M", "Medio"),
    ("D", "Dificil"),
  ]
  
  title = models.CharField(max_length=100, null=True)
  zona = models.CharField(max_length=50, choices=ZONAS, null=True)
  nivel = models.CharField(max_length=1, choices=NIVEIS, null=True)
  mais_famosa = models.IntegerField(null=True)

class Tabela(models.Model):
  title = models.CharField(max_length=100, null=True)
  zona = models.CharField(max_length=50, null=True)
  insta = models.CharField(max_length=30, null=True)
  tipo = models.CharField(max_length=30, null=True)

class Tasks(models.Model):
  title = models.CharField(max_length = 50)
  description = models.TextField()
  due_date = models.DateField()
  done = models.BooleanField()# Create your models here.
