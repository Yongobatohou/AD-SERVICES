from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Demandes, Articles
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.


def login(request):
    return render(request, "login.html")
 
def index(request):
   users = User.objects.all()
   user = len(User.objects.all())
   article = len(Articles.objects.all())
   demande = len(Demandes.objects.all())
   return render(request, "dash.html", {'users':users,'user':user, 'article':article, 'demande':demande})



#Articles Start
def new_article(request):
    return render(request, 'add_article.html')

def articles(request):
   articles = Articles.objects.all().order_by('-date')
   return render(request, 'articles.html', {'articles':articles})
   
def add_article(request):
   if request.method == 'POST':
      titre = request.POST['titre']
      extrait = request.POST['extrait']
      article = request.POST['article']
      img = request.FILES['img']
    
      new_article = Articles(titre=titre, extrait=extrait, acticle=article, image=img)
      new_article.save()

   return redirect(request.META['HTTP_REFERER'])
     
def edit_article(request, id):
   article = Articles.objects.get(pk=id)
   return render(request, 'edit-article.html', {'article':article})

def update_article(request, id):
   article = Articles.objects.get(pk=id)
   if request.method == 'POST':
      titre = request.POST['titre']
      extrait = request.POST['extrait']
      article = request.POST['article']
    
      article.titre=titre, 
      article.extrait=extrait, 
      article.article=article,
      article.save()

   return redirect('dashboard/articles/')

def delete_article(request, id):
   article = Articles.objects.get(pk=id)
   article.delete()
   
   return redirect('dashboard/articles/')

#Article end




#Demandes start
def demandes(request):
    demandes = Demandes.objects.all()
    return render(request, "demandes.html", {'demandes':demandes})

   
def do_demande(request):
   if request.method == 'POST':
      nom = request.POST['nom']
      prenom = request.POST['prenom']
      email = request.POST['email']
      contact = request.POST['contact']
      cubage = request.POST['cubage']
      duree = request.POST['duree']
      lieu = request.POST['lieu']
      type_d = request.POST['type']
      details = request.POST['demande']

      new_demande = Demandes(nom=nom, prenom=prenom, email=email, contact=contact, cubage=cubage, duree=duree, lieu=lieu, type_d=type_d, details=details)
      new_demande.save()
      
      subject = 'Demande de Devis pour location de benne'
      from_email = email
      to = 'yongobatohou@gmail.com'
      html_message = render_to_string('mail_template.html', {'nom': nom, 'prenom': prenom, 'email': email, 'contact': contact, 'cubage': cubage, 'duree': duree, 'lieu': lieu, 'type_d': type_d, 'details': details,})
      plain_message = strip_tags(html_message)
      send_mail(subject, plain_message, from_email, [to], html_message=html_message)
      
   return redirect(request.META['HTTP_REFERER'], {'message':'Merçi d\'avoir choisi AD-SERVICES. Votre demande de devis a bienété envoyé. Un retour vous sera fait par mail.' })

def read_demande(request, id):
   demande = Demandes.objects.get(pk=id)
   return render(request, 'demande.html', {'demande':demande})

#Demandes end


def inscription(request):
    if request.method == "POST":
        
        username = request.POST['username']
        email=request.POST['email']
        password = request.POST['password']
        confirm = request.POST['password_confirmation']
        
        if password==confirm:
            
            User.objects.create_user(username=username,email=email,password=password)
            
            return redirect('/dashboard/')
        else:
            error = "Mot de passe non confirmé"
        
    return render(request, 'login.html', {'erreur':error})


def connexion(request):
   if request.method == 'POST':
      email = request.POST['email']
      password = request.POST['password']

      user = authenticate(email=email, password=password)

      if user is not None:
         login(request, user)
         return redirect('dashboard/')
      return render(request, "dash.html")
      
def deconnexion(request):
   logout(request)
   return redirect('/dashboard/')