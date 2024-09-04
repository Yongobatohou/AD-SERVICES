from django.db import models

# Create your models here.

class Articles(models.Model):
    titre = models.CharField(max_length=200)
    extrait = models.TextField()
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    acticle = models.TextField()
    image = models.FileField(upload_to='actualité')
    
class Demandes(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    cubage = models.CharField(max_length=20)
    duree = models.CharField(max_length=20)
    lieu = models.CharField(max_length=20)
    type_d = models.CharField(max_length=20)
    details = models.TextField()