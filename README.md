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

Python script inspired by the Fallout game franchise
which simulates authenthication hacking from Robco machines

It has a post-authentication menu to exit and access the tty terminal,
options to modify and start services and the others, which can be customizedand changed.

Personal project to use in my own terminal, as a script for terminal initialization 

## Usage

It is necessary to install certain packages if they are not already installed

> pip install -r requirements.txt

> python3 init.py


To make it more interesting, you can add the init.py file to start along with your shell, by editing .zshrc/.bashrc file
And after this.. your terminal will always start with Fallout-style authentication.

> git clone https://github.com/ARCANGEL0/fallTerminal 

> cd fallTerminal

> echo "python3 $(pwd)/init.py" >> $HOME/.bashrc


## Menu 

The options menu contains some services from my own terminal (such as apache, mysql, snapd)
that can be initialized by the script itself, like an interactive shell
Feel free to add your own 


## Password 

The terminal password is generated from a text file (pass), which prints all the words on the screen and saves one of them randomly as system password
To view the chosen password
> /ADMIN.L

on the login terminal to view the current password.



## Terminal

To adhere more to Terminal's retro style,
I recommend Swordfish90's cool-retro-term

To match the fallout terminal style, I tweaked cool-retro-term.
I exported my CRT styling JSON in the repo
as falout.json

(https://github.com/Swordfish90/cool-retro-term)
