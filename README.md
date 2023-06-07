<h1 style="color:#00FF00">PROGESTEC / Programme de Gestion de Tournoi d'Echecs</h1>


## <span style="color: #8BC34A">**Description :**</span>
Le Programme de Gestion de Tournois d'Échecs est une application simple et conviviale conçue pour aider les clubs d'échecs locaux à gérer efficacement leurs tournois. Contrairement aux solutions existantes, cette application fonctionne hors ligne, ce qui la rend idéale pour les tournois qui ne disposent pas d'une connexion Internet fiable.

-------------------------------------------------------
## <span style="color: #8BC34A">**Pour commencer :**</span>
Télécharger l’intégralité du repository sur : https://github.com/Thomas-Savelli/association_echecs.git

### <span style="color: #689F38">1/ Pré-requis</span>

Assurez-vous de posséder l’intégralité du repository : 

- app.py
- README.md
- requirements.txt
- .gitignore
- controllers : 
                
                - base.py
- models :

                - joueur.py
                - match.py
                - tour.py
                - tournoi.py
- views :

                - base.py
                - esthetiqueview.py
- reports

### <span style="color: #689F38">2/ Installation</span>

Une fois le repository téléchargé et stocké localement : 

- ouvrez votre terminal et rendez-vous dans le dossier contenant l’intégralité des fichiers du repository.
    `` cd '.\Desktop\OpenClassrooms\Parcours DA PYTHON\Projet_4\association_echecs' ``

- Créer un environnement virtuel afin de récupérer les dépendances et packages du projet.  
    *exemple procedure* : ``python -m venv env``

- Contrôler avec ``ls`` que vous disposez maintenant d’un dossier **env**. Si ce n’est pas le cas, réitérer cette 
    étape en contrôlant la syntaxe de la ligne de commande. Sinon activer votre nouvel environnement virtuel. 

    *exemple procédure (powershell):* ``.\env\Scripts\activate``   
    *exemple procédure (windows):* ``.\env\Scripts\activate.bat``  
    *exemple procédure (autres): ``source env/bin/activate``

    Si vous rencontrez des difficultés vous pouvez vous référer sur le site : 
    *https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows/18713789#18713789*

    Pour contrôler la réussite de cette manœuvre, vous devriez avoir un (env) devant votre ligne de commande :    
    ``(env) PS C:\Users\thoma\Desktop\OpenClassrooms\Parcours DA PYTHON\Projet_4\association_echecs>``  
    
    PS : Taper seulement ``deactivate`` pour fermer ce dernier.  
- Pour finir, télécharger avec **pip** les packages et dépendances requis pour le bon fonctionnement du code avec le requirements.txt en entrant la commande suivante *(dans votre environnement virtuel !)* :   
    ``pip install -r requirements.txt ``  
    Une fois le téléchargement effectué et l'installation terminée, vous êtes prêt à exécuter le code.  

-------------------------------------------------------
## <span style="color: #8BC34A">**Exécuter le programme**</span>
- Dans votre terminal, rendez-vous à l’emplacement  du dossier télécharger et activer votre environnement virtuel.  

- Exécuter le code en tapant la commande : ```python app.py```  

- Bienvenue sur le Menu principal du programme PROGESTEC !

- Lors de la premiere utilisation du programme, seul la création d'un nouveau tournoi sera disponible. Suivez seulement les instructions qui s'affichent à l'écran.

- Une fois votre premier tournoi initialisé, vous pouvez charger ses données avec le choix 2 du menu principal. Les options des sous-menus s'ouvre à vous. laissez vous guider simplement par les noms des choix présents.
  
## <span style="color: #8BC34A">**Les données enregistrées au format JSON**</span>
Dans l'optique où la création des fichiers JSON sont tous enregistrés dans le dossier data_tournois, il est nécéssaire de ne pas deplacer les fichiers de tournois non terminés sous peine de perdre l'accés total à vos données. Toutefois, si ceux ci sont terminés et que vous désirez les archiver, vous pouvez deplacer vos fichiers dans un autre dossier que data_tournois créé au préalable par vous même à l'endroit de votre choix. En effet, un tournoi terminé et archivé ne nécéssitant pas de réutilisation ne fera que surcharger votre dossier data_tournois. De plus, le format JSON permet une lecture et une compréhension facile pour l'homme et ne nécéssite par conséquent aucuns programmes pour être lisible.

-------------------------------------------------------

## <span style="color: #8BC34A">**Fabriqué avec**</span>
* Python - 3.11.1 - [*https://docs.python.org/fr/3/tutorial/index.html*]  
* flake8 - 6.0.0 - [https://pypi.org/project/flake8/]
* flake8-html - 0.4.3 [https://pypi.org/project/flake8-html/]
* IDE - [*https://code.visualstudio.com/*] - Visual Studio Code     
* PowerShell - [*https://learn.microsoft.com/fr-fr/powershell/scripting/overview?view=powershell-7.3*]  
* GitHub - [*https://github.com/*]   


## <span style="color: #8BC34A">**Versions**</span>
**Dernière version stable :** Beta 1.0.0  
**Dernière version :** Beta 1.0.0  

## <span style="color: #8BC34A">**Auteur**</span>
**Thomas Savelli** [https://github.com/Thomas-Savelli] - ``Developpeur d'application PYTHON``   

