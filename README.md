# Groupe de courta_f 869974

## Installation du projet

### BDD
Il faut installer un serveur mysql, importer le fichier escape_game.sql dans la base de donnée.

### API
Il faut python3 et python3-pip
lancer les commandes suivantes:

> $> cd api/   

Editer le fichier db_config.py  
> $> pip3 install -r requirements.txt  
> $> python3 api.py  

### Generateur
> $> cd generateur  
> $> php script.php  

control + C pour arreter lorsque vous estimez avoir assez de données

### Dashboard
> $> cd dashboard/  
> $> npm i  
> $> npm start  

Se login:
email: habi_a@etna-alternance.net
mdp: ahabi

la page login fonctionne bien mais vous n'avez juste pas de message d'erreur en cas de mauvais mdp.
