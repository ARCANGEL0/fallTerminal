<div align="center">
<center><p><img src="./fall.png" width='35%' height='35%'></img>
<h1>ROBCO Unified Operating System</h1>
</center>
</div>

<p align="center">
  
<a href="https://github.com/ARCANGEL0/fallTerminal">
    <img src="https://img.shields.io/github/stars/ARCANGEL0/fallTerminal?label=Stars&color=yellow&style=for-the-badge" alt="Stars">
</a>
<a href="https://github.com/ARCANGEL0/fallTerminal">
    <img src="https://img.shields.io/github/watchers/ARCANGEL0/fallTerminal?label=Watchers&color=green&style=for-the-badge" alt="Watchers">
</a>
<a href="https://github.com/ARCANGEL0/fallTerminal">
    <img src="https://img.shields.io/github/forks/ARCANGEL0/fallTerminal?label=Forks&color=orange&style=for-the-badge" alt="Forks">
</a>
</p>

  <table align="center">
 <tr align='center'>
 <td colspan="3">
 ၊၊||၊||၊
 </td>
 </tr>
 <tr><td><a href="README.md"><img 
 src="https://custom-icon-badges.demolab.com/badge/English-%23092e13.svg?logo=fallout&style=for-the-badge" width='140vw' height='45vh' ></a></td>
 <td><a href="README_fr.md"><img src="https://custom-icon-badges.demolab.com/badge/Français-%23092e13.svg?logo=fallout&style=for-the-badge" width='140vw' height='45vh' > </a></td>
 <td><a href="README_pt.md"><img src="https://custom-icon-badges.demolab.com/badge/Português-%23092e13.svg?logo=fallout&style=for-the-badge" width='140vw' height='45vh' > </a></td></tr>
</table>


#      Fallout Terminal Shell
====================================


Script Python inspiré de la franchise de jeux Fallout
qui simule le piratage d'authentification des machines Robco

Il dispose d'un menu post-authentification pour sortir et accéder au terminal tty,
options pour modifier et démarrer les services et les autres, qui peuvent être personnalisés et modifiés.


Projet personnel à utiliser dans mon propre terminal, comme script pour l'initialisation du terminal 

## Utilisation

Il est nécessaire d'installer certains packages s'ils ne sont pas déjà installés

> pip install -r requirements.txt

> python3 init.py

Pour le rendre plus intéressant, vous pouvez ajouter le fichier init.py pour démarrer avec votre shell, en éditant le fichier .zshrc/.bashrc
Et après cela... votre terminal démarrera toujours avec une authentification de style Fallout..

> git clone https://github.com/ARCANGEL0/fallTerminal 

> cd fallTerminal

> echo "python3 $(pwd)/init.py" >> $HOME/.bashrc


## Menu 

Le menu d'options contient certains services de mon propre terminal (comme Apache, MySQL, Snapd)
qui peut être initialisé par le script lui-même, comme un shell interactif
N'hésitez pas à ajouter le votre 


## Mot de passe 


Le mot de passe du terminal est généré à partir d'un fichier texte (pass), qui imprime tous les mots à l'écran et enregistre l'un d'eux de manière aléatoire comme mot de passe système.
Pour visualiser le mot de passe choisi
> /ADMIN.L

sur le terminal de connexion pour afficher le mot de passe actuel.



## Terminal

Pour adhérer davantage au style rétro de Terminal,
Je recommande le terme cool-rétro de Swordfish90

Pour correspondre au style du terminal Fallout, j'ai modifié le terme cool-retro.
J'ai exporté mon style CRT JSON dans le dépôt
comme falout.json

(https://github.com/Swordfish90/cool-retro-term)
