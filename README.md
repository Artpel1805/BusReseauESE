# BusReseauESE

## Contexte

Le but de ce TP est de comprendre comment utiliser des communications réseaux (API REST), ainsi que des communications via bus (I2C, UART, etc...).

Nous allons pour cela prototyper une application domotique de gestion de chauffage.

Nous nous occuperons de la partie réseau, capteur et asservissement moteur. 

On pourrait très bien imaginer rajouter une UI pour communiquer avec notre serveur, ainsi qu'une vanne commandée par le moteur pour régler l'intensité du chauffage.


## Capteurs



## Asservissement Moteur



## Réseau

Pour la partie Réseau nous utiliserons une Raspberry Pi. Celle-ci dispose d'une carte réseau et après une configuration nous la connectons sur un réseau local.

Nous allons créer un serveur sur cette carte electronique. Plus précisement une API REST. Nous utiliserons le protocole de communication HTTP pour communiquer avec notre serveur.

### HTTP
Le protocole HTTP normalisé de couche 7 dans le modèle OSI. Il utilise un protocole TCP en couche 4.
HTTP est principalement caractérisé par **_les verbes__** 

