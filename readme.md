Ce projet est compatible uniquement avec windows et necessite l'installation préalable d'Excel.

## Instruction d'installation du projet 

- Installer python 3.9 ou ultérieur. Durant l'installation, cocher l'option **Add python to PATH**. Si python est déjà installé, s'assurer qu'il est déjà dans le PATH et utiliser la commande depuis le cmd **python -V** pour vérifier la version de python installée

- Se déplacer dans le dossier du projet et taper la commande suivante pour installer les dépendances du projet 
`python -m pip install -r requirements.txt`
**Tooltip:** Une manier assez simple de se déplacer vers le dossier du projet est d'ouvrir le dossier dans l'explorateur de fichier. Puis dans la barre d'adresse, taper **cmd** puis entrer. Ceci ouvrira un invite de commande dans le dossier.

- Copier le fichier excel du simulateur dans le dossier du projet. Le fichier doit être nommer "simulateur.xlsx"

- Toujours dans le dossier du projet, taper la commande `python run.py`. Ceci lancera le serveur du projet. Accessible à l'adresse http://127.0.0.1:5001

