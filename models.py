from django.db import models
class Article(models.Model):
    libelle=models.CharField(max_length=100)
    prix=models.FloatField()
    qte=models.IntegerField()
    dateajout=models.DateField()
    fields = ("libelle", "qte","prix")
    categ = models.ForeignKey('Categorie', on_delete=models.CASCADE,)
    def __str__(self) -> str:
        return self.libelle 
    
class Categorie(models.Model):
    nomCat=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self) -> str:
        return self.nomCat


# Create your models here.
