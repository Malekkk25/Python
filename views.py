from audioop import reverse
import ctypes
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from magasin.models import Article
from magasin.models import Categorie
from django.http import HttpResponseRedirect
from django.urls import reverse
from  django.contrib.auth.models import User 
from .forms import FormUser
from .forms import FormConnexion
from django.contrib.auth import authenticate, login, logout
def index(request):
    art=Article.objects.all().values
    template=loader.get_template('home.html')
    context={
        'art':art,
    }
    return HttpResponse(template.render(context,request))

def del_art(request,id):
    article=Article.objects.get(id=id)
    article.delete()
    return HttpResponseRedirect(reverse('articles'))

def list_cat(request):
    categ=Categorie.objects.all().values
    template=loader.get_template('categ.html')
    context={
        'categ':categ,
    }
    return HttpResponse(template.render(context,request))
def del_categ(request,id):
    categorie=Categorie.objects.get(id=id)
    categorie.delete()
    return HttpResponseRedirect(reverse('index1'))

def update_art(request, id):
    art = Article.objects.get(id=id)
    cat = Categorie.objects.all().values()
    template = loader.get_template('updateArticle.html')
    context = {
    'art': art,
    'cat':cat, }
    return HttpResponse(template.render(context, request))

def update_art_action(request,id):
    lib = request.POST['libelle']
    p = request.POST['prix']
    q = request.POST['qte']
    c = request.POST['categ']
    cat = Categorie.objects.get(id=c)
    article = Article.objects.get(id=id)
    article.libelle = lib
    article.prix = p
    article.qte = q
    article.categ = cat
    article.save()
    return HttpResponseRedirect(reverse('articles'))

def add(request):
    cat = Categorie.objects.all().values()
    template = loader.get_template('addArticle.html')
    context = {
    'cat': cat,
    }
    return HttpResponse(template.render(context, request))
def add_art(request):
    lib = request.POST['libelle']
    p = request.POST['prix']
    q = request.POST['qte']
    da = request.POST['dateAjout']
    c = request.POST['categ']
    cat = Categorie.objects.get(id=c)
    article = Article(libelle=lib, prix=p, qte=q, dateAjout=da, categ=cat)
    article.save()
    return HttpResponseRedirect(reverse('articles'))
def list_users(request):
    users=User.objects.all().values()
    template=loader.get_template('user.html')
    context={
        'users':users,
    }
    return HttpResponse(template.render(context,request))
    
def del_user(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('users'))  

def create_compte(request):
    user_form=FormUser()
    return render(request, 'createUser.html', {'user_form' : user_form})

def create_user_action(request):
    adrEmail = request.POST['email']
    username = request.POST['login']
    password = request.POST['mot2pass']
    confirm = request.POST['confirm']
    prenom = request.POST['prenom']
    nom = request.POST['nom']   
    if(password==confirm):
        user=User.objects.create_user(username,adrEmail,password)
        user.first_name=prenom
        user.last_name=nom
        user.save()
        return HttpResponseRedirect(reverse('users'))
    else:
        print("Mot de passe et confirmation mot de passe ne sont pas identiques")
        return HttpResponseRedirect(reverse('create_compte'))   

def connect (request):
    connect_form = FormConnexion ()
    return render(request, 'connexion.html', {'connect_form' : connect_form }) 

def signIn(request):
    username = request.POST['login']
    password = request.POST['mot2pass']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        request.session['username'] = username 
        return HttpResponseRedirect(reverse('articles'))
    
    else:
        print("Login et/ou mot de passe incorrect")
        return render(request,'connexion.html')
        #return HttpResponseRedirect(reverse('connect'))
def signOut(request):
    logout(request) 
    return HttpResponseRedirect(reverse('connect'))

def update_user(request,id):
    u=User.objects.get(id=id)
    template=loader.get_template('updateUser.html')
    context={
        'u':u
    }    
    return HttpResponse(template.render(context,request))
def update_user_action(request,id):
    prenom = request.POST['prenom']
    nom = request.POST['nom']
    mail = request.POST['mail']
    username=request.POST['login']
    password1 = request.POST['mot2pass']
    ancien=request.POST['ancien']
    admin= request.POST['admin']
    user=User.objects.get(id=id)
    if(not password1 ):
        user.first_name=prenom
        user.last_name=nom
        user.email=mail
        user.is_staff=admin  
        user.save()
        return HttpResponseRedirect(reverse('users'))
    if(password1 is not None):
        a = authenticate(request,password=ancien,username=username)
        if(a is not None):
            user.first_name=prenom
            user.last_name=nom
            user.email=mail
            user.is_staff=admin
            user.set_password(password1)
            user.save()
            return HttpResponseRedirect(reverse('users'))
        else:
            ctypes.windll.user32.MessageBoxW(0, "Mot de passe et confirmation mot de passe ne sont pas identiques", "Erreur", 1)
            return HttpResponseRedirect(reverse('users'))
            