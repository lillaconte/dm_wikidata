#import os
#import dotenv

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#dotenv.load_dotenv(os.path.join(BASE_DIR, '.env'))

#class Config():
    #DEBUG = os.environ.get("DEBUG")

#j'ai dû commenter tout ce fichier et toute la partie config du app.py parce que dotenv ne veut pas se télécharger dans mon environnement virtuel
#j'ai une erreur 'externally managed environment' alors que je suis bien dans mon environemment virtuel env
#j'ai essayé toutes les commandes possibles : pip install python3-dotenv, pip install dotenv, pip install python-dotenv etc
#j'ai essayé de créer un requirements.txt pour tout réinstaller d'un coup dans mon env mais ça n'a pas fonctionné non plus pour dotenv