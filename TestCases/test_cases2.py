import pytest
#Regles a respecter  :
# le nom de fichier dans pytest doit commencer par le mot Test
# le nom de methode doit commencer par le mot Test


def  steup_module (module): # ici module est le scope donc si le scope module l'execution se fait une fois  seulement pcq  module ca veut dire fichier donc ici il se fait au debut de fichier
    print('ouverture de cconnexion BD')

def  teardown_module (module): # ici module est le scope  donc il se fait une seul et avec teardown il sera a la fin de fichier 
    print('cloture  de cconnexion BD')

def  setup_function(function): #cette methode sera executer avant chaque fonction  parceque le scope est function qui est padsser en parametre
    print('ouverture de site login salesforces')
def teardown_function(function): # cette fonction va s'executer a la fdin de chaque finction pcq on a passer le scope qui function
    print('fermeture du navigateur')


def  test_login():

    print ('se connecter au site login salesforce')

def test_creer_utilisateur():

    print('creer un utilisateur')