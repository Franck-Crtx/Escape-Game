# Escape Game

## Récapitulatif du projet 

Ce projet requiert de vous de concevoir une architecture de base de donnée adaptée au besoin de VDM Escape Game.

Il faut pour cela bien comprendre les besoins et les demandes de chacun des collaborateurs.

Relisez donc bien le sujet dans son intégralité, en prenant en compte, entre autres, ces différents aspects:

- Haute disponnibilité : Comment assurer le bon fonctionnement du service même si une machine tombe en panne ?
- Sécurité : Comment se protéger contre la perte de données ?
- Performance : de quelles données, et sous quelle forme les collaborateurs de VDM Escape Game vont-ils en avoir besoin au quotidien ? Quelle architecture mettre en place pour accéder rapidement à ces données ?
- Scalabilité : Comment anticiper les nouveaux besoins et permettre à votre architecture de pouvoir évoluer sans trop de difficulté ?

## Installation du projet

### BDD
Installer un `serveur mysql`

> $> apt update  
> $> apt install mariadb-server-10.3

Importer le fichier `escape_game.sql` dans la base de donnée.

> $> mysql nom_base_de_donnees < escape_game.sql

### API
Installer `python3` et `python3-pip`

> $> apt install python3-pip

Exectuer les commandes suivantes:

> $> cd api/   

Editer le fichier `db_config.py`.

> $> pip3 install -r requirements.txt  
> $> python3 api.py  

### Générateur

> $> cd generateur  
> $> php script.php  

Control + C pour arreter lorsque vous estimez avoir généré suffisament de données.

### Dashboard
Installer `npm`
> $> apt install nodejs npm

Lancement du dashboard.
> $> cd dashboard/  
> $> npm i  
> $> npm start  

Se login:   
`email`: habi_a@etna-alternance.net   
`mdp`: ahabi

⚠️ La page login fonctionne bien mais il n'y a pas de message d'erreur en cas de mauvais mdp. ⚠️ 


Copyright © 2021 Groupe de COURTAUX Franck | HABI Açal | KERNIN Brandon | VELEZ PEREIRA REAL Francisco De Jesus 
