#Blue NRG Snake

Le projet est découpé en trois parties :
* App IOS pour intéragir avec les données de la BlueNRG tile
* Un serveur Python pour récupérer les données de l'accéléromètre
* Une app front HTML pour afficher le Snake.

Sur ce repo, il n'y a que le code du serveur Python et de l'application front

## Serveur Python
> Code dans le dossier `back`
### Installation
1. Se créer un virtual env (par exemple `python2 -m virtualenv venv`)
2. Activer le virtual env `. venv/bin/activate`
3. Installer les dépendances `pip install -r requirements.txt`
4. Lancer le serveur `python2 server.py`

(J'ai run les commandes avec python2 car j'ai rencontré des problèmes avec python3).

## Commentaires
* J'ai repris le code du Serveur Websocket et j'y ai ajouté deux classes pour gérer les données de l'accéléromètre
envoyé par l'app IOS
* Elles se trouvent dans le dossier `core`
* J'ai redirigé les données envoyées par websockets depuis l'app IOS vers un autre client Websocket qui est l'app VueJS

## App front HTML
> Code dans le dossier `front`
### Installation
1. `npm install`
2. `npm run dev`
3. Il y a un fichier `snake.config.js` à la racine du projet dans lequel tu peux renseigner ta config (ex: adresse du server webscoket)

## Commentaires
* Je voulais tester depuis un petit moment les canvas avec VueJS donc j'ai profité de ce projet pour expérimenter :^).
