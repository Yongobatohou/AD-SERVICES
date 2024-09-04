
from django.urls import path
from .views import login, index, demandes, articles, inscription, connexion, deconnexion, do_demande, read_demande, new_article, add_article, edit_article, update_article, delete_article


urlpatterns = [
    # VIEWS URLS
    
    path('', login, name="login"),
    path('dash/', index, name="admin"),
    
    #Demande de devis START
    path('demandes-enregistres/', demandes, name="demandes"),
    path('demande_de_devis/', do_demande, name="do_demande"),
    path('lire_demande/<int:id>/', read_demande, name="read_demande"),
    #Demande de devis END 
    
    #Articles START
    path('articles/', articles, name="articles"),
    path('new_acticle/', new_article, name="new_article"),
    path('add_acticle/', add_article, name="add_article"),
    path('edit_article/<int:id>/', edit_article, name="edit_article"),
    path('update_article/<int:id>/', update_article, name="update_article"),
    path('delete_article/<int:id>/', delete_article, name="delete_article"),
    #Articles END
    
    #Dashboard Authentification
    path('inscription/', inscription, name='inscription'),
    path('connexion/', connexion, name='connexion'),
    path('deconnexion/', deconnexion, name='deconnexion'),
]



