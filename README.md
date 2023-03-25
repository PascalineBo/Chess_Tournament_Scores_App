# App de gestion de scores de tournoi d'échec
Appli pour enregistrer les scores d'un tournoi d'échecs suisse et générer les appariements des joueurs

## Comment installer cette Appli sur votre ordinateur:
Le Code est organisé selon le modèle "Model View Controller", en langage **[Python 3.10](https://www.python.org/downloads/)** (requis)

<ol>
<li> pour importer les fichiers de ce repository, tapez la commande git:

`git clone https://github.com/PascalineBo/Chess_Tournament_Scores_App.git`</li>

 <li> positionnez-vous dans le répertoire Chess_Tournament_Scores_App:
    
- `cd Chess_Tournament_Scores_App` </li>
  
  <li>  créez votre dossier d'environnement virtuel:

- `mkdir .venv`
- `pip install pipenv`
</li>

  <li> puis installez les packages requirements du projet à l'aide des commandes:

- `pipenv install tinydb`
</li>
</ol> 

## Comment utiliser l'Appli:

<ol>

<li> avec votre terminal, positionnez vous dans le dossier dans lequel vous avez installé l'Appli</li>
<li>
 `python main.py`
 </li>

<li> saisissez les données demandées dans le terminal: 
 
- le programme commence par vous demander si vous souhaitez un rapport; si oui, tapez "O", si non, pour saisir le tournoi, tapez "N", puis les informations demandées pour un tournoi, 8 joueurs et 4 tours; les tours s'appellent "Round 1", "Round 2", etc...

Les joueurs sont appariés selon les règles du [tournoi suisse](https://fr.wikipedia.org/wiki/Syst%C3%A8me_suisse#:~:text=Le%20principe%20du%20tournoi%20suisse,leur%20Classement%20Elo%20aux%20%C3%A9checs) .
 </li>

(v) vous pouvez consulter le rapport du tournoi dans le fichier créé: 'databases.json'

(vi) si vous interrompez le programme après avoir saisi les données des joueurs, quand vous le relancerez, il ne vous demandera pas de ressaisie mais ira chercher les données dans le fichier 'databases.json'

(vii) si le programme crashe après la saisie d'une ronde, le programme ira chercher l'information dans le fichier 'databases.json'
et ne la redemandera pas quand vous le relancerez.

(viii) vous pouvez stocker les données de plusieurs tournois dans le fichier 'databases.json'.

Pep8:
Si vous voulez vérifier que le code respecte les règles de la Pep8, tapez dans le terminal, 
(en vous positionnant dans le dossier où vous avez rangé main.py, model.py, view.py, controller.py):

pip install flake8-html

puis:
configurer:

flake8 --max-line-length 119

et lancer:
flake8 --format=html --htmldir=flake-report

Vous aurez alors un dossier flake-report où vous aurez le rapport d'erreurs éventuelles du code concernant le non-respect de la Pep8.

Ci-joint les spécifications techniques demandées pour ce code:

[Centre échecs - spécification technique (11).docx](https://github.com/MargueriteEffren/OC_Projet4/files/8660324/Centre.echecs.-.specification.technique.11.docx)
[Centre échecs - spécification technique.odt](https://github.com/MargueriteEffren/OC_Projet4/files/8660332/Centre.echecs.-.specification.technique.odt)
