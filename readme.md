Ce projet est compatible uniquement avec windows et necessite l'installation préalable d'Excel.

## Instruction d'installation du projet 

- Installer python 3.9 ou ultérieur. Durant l'installation, cocher l'option **Add python to PATH**. Si python est déjà installé, s'assurer qu'il est déjà dans le PATH et utiliser la commande depuis le cmd **python -V** pour vérifier la version de python installée

- Se déplacer dans le dossier du projet et taper la commande suivante pour installer les dépendances du projet 
`python -m pip install -r requirements.txt`
**Tooltip:** Une manier assez simple de se déplacer vers le dossier du projet est d'ouvrir le dossier dans l'explorateur de fichier. Puis dans la barre d'adresse, taper **cmd** puis entrer. Ceci ouvrira un invite de commande dans le dossier.

- Copier le fichier excel du simulateur dans le dossier du projet. Le fichier doit être nommer "simulateur.xlsx"

- Toujours dans le dossier du projet, taper la commande `python run.py`. Ceci lancera le serveur du projet. Accessible à l'adresse http://localhost:5001

Explication de microsoft relative à l'automatisation de office en server-side
https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2

Le lien ci-dessous décrit le problème rencontré avec les différents packages supportant 
les calculs itératifs qu'on a trouvé. Ce topic est basé sur nodejs mais le problème est très exactement 
le même avec pycel et tout le reste.
https://github.com/exceljs/exceljs/issues/246