# <div align="center">Thermostat Domotique</div>

## Contexte

Le but de ce TP est de comprendre comment utiliser des communications réseaux (API REST), ainsi que des communications via bus (I2C, UART, etc...).

Nous allons pour cela prototyper une application domotique de gestion de chauffage.

Nous nous occuperons de la partie réseau, capteur et asservissement moteur. 


On pourrait très bien imaginer rajouter une UI pour communiquer avec notre serveur, ainsi qu'une vanne commandée par le moteur pour régler l'intensité du chauffage.

![img](assets/Schemas_Global.png)


## Capteurs



## Asservissement Moteur



## Réseau

### Serveur

Pour la partie Réseau nous utiliserons une Raspberry Pi. Celle-ci dispose d'une carte réseau et après une configuration nous la connectons sur un réseau local.

Nous allons créer un serveur sur cette carte electronique.
Le serveur va nous permettre de manipuler de la donnée et d'executer des ordres via un protocole de communication sans fil.
Plus précisement une API REST. Nous utiliserons le protocole de communication HTTP pour communiquer avec notre serveur.



### HTTP
Le protocole HTTP normalisé de couche 7 dans le modèle OSI. Il utilise un protocole TCP en couche 4.

HTTP est principalement caractérisé par **_les verbes_** qui permettent d'effectuer des actions spécifiques sur la donnée. On peut par exemple citer: 
- GET pour récuperer de la donnée
- POST pour créer de la donnée
- DELETE pour supprimer de la donnée

### Configuration de la Raspberry

Après avoir installé Raspberry Pi OS Lite 32 Bit: <a>https://www.raspberrypi.org/downloads/raspberry-pi-os/</a>

Nous configurons et connectons notre carte à notre réseau.

La Raspberry communique via **_ssh_**, un protocole de communication permetant de se connecter à distance à un ordinateur et d'obtenir un shell. C'est grâce à ce shell que nous allons pouvoir interagir avec l'os.

On peut chercher notre Raspberry sur le réseau avec la commande  `arp -a`

On se connecte ensuite via la commande  `ssh pi@<ip_adresse>`

### Flask

Comme nous l'avons le serveur appartient à la couche 7, c'est principalement un logiciel.

Nous pouvons donc coder notre serveur en C, Ruby, Java, Dart...

Nous choisissons d'utiliser Python car c'est un langage disposant de très bon framework serveur.

On a maintenant accès à notre OS via le shell. Raspberry Pi OS est en fait une surcouche Linux. Nous pouvons donc installer python via le gestionnaire de paquet apt: `sudo apt install python3-pip`

Flask est un framework python permettant de coder assez simplement des API REST.

Nous devons donc installer donc Flask via le gestionnaire de paquet de Python pip.

Une bonne pratique est de lister toutes les dépendances python dans un fichier. Ainsi quelqu'un récupérant le projet ne devra executer qu'une seule commande pour tout installer : [requirement.txt](API/requirement.txt)

Il ne nous reste plus qu'a executer la commande `python3 -m pip install -r requirement.txt`

### Connection avec la STM32

### [BONUS] Fast API
