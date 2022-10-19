# BusReseauESE
## Capteur BMP280
Les adresses I²C possibles pour ce composant: 1110110 (0X76) ou 1110111 (0x77) ca depend de la connection de SDO

Le registre et la valeur permettant d'identifier ce composant: le registre ID  0xDO et sa valeur est 0x58.

le registre et la valeur permettant de placer le composant en mode normal : control register et la valeur 11

Le registres contenant l'étalonnage du composant: 0xF4

Les registres contenant la température (ainsi que le format): 0xFA 0xFB 0xFC

Les registres contenant la pression (ainsi que le format): 0xF7 0xF8 0xF9

Les fonctions permettant le calcul de la température et de la pression compensées, en
format entier 32 bits: 
-BMP280_S32_t  bmp280_compensate_T_int32(BMP280_S32_t adc_T)
-BMP280_U32_t  bmp280_compensate_P_int64(BMP280_S32_t adc_P)


## Setup du STM32

## Communication I²C 


