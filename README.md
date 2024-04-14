<div align="center">
<center><p><img src="./fall.png" width='35%' height='35%'></img>
<h1>ROBCO Unified Operating System</h1>
</center>
</div>

<p align="center">
  
  <a href="https://www.gnu.org/licenses/agpl-3.0">
    <img src="https://img.shields.io/badge/License-AGPL_v3-blue.svg" alt="License: AGPL v3">
</a>
<a href="https://github.com/ARCANGEL0/PortSys">
    <img src="https://views.whatilearened.today/views/github/ARCANGEL0/PortSys.svg" alt="Views">
</a>
<a href="https://github.com/ARCANGEL0/PortSys">
    <img src="https://img.shields.io/github/stars/ARCANGEL0/PortSys?label=Stars&color=yellow&style=flat-square" alt="Stars">
</a>
<a href="https://github.com/ARCANGEL0/PortSys">
    <img src="https://img.shields.io/github/watchers/ARCANGEL0/PortSys?label=Watchers&color=green&style=flat-square" alt="Watchers">
</a>
<a href="https://github.com/ARCANGEL0/PortSys">
    <img src="https://img.shields.io/github/forks/ARCANGEL0/PortSys?label=Forks&color=orange&style=flat-square" alt="Forks">
</a>
</p>

  <table align="center">
 <tr align='center'>
 <td colspan="3">
 ၊၊||၊||၊
 </td>
 </tr>
 <tr><td><a href="README.md"><img 
 src="https://custom-icon-badges.demolab.com/badge/English-%23092e13.svg?logo=fallout" width='40%' height='25%' ></a></td>
 <td><a href="README_fr.md"><img src="https://custom-icon-badges.demolab.com/badge/Français-%23092e13.svg?logo=fallout" width='40%' height='25%' > </a></td>
 <td><a href="README_pt.md"><img src="https://custom-icon-badges.demolab.com/badge/Português-%23092e13.svg?logo=fallout" width='40%' height='25%' > </a></td></tr>
</table>


#      Fallout Terminal Shell
====================================

Script em python inspirado na franquia de Jogos Fallout
que simula um terminal e a autenticaçao do terminal

Conta com um menu pos-autenticaçao para sair e acessar o terminal tty, 
opçoes para modificar e iniciar serviços e afins, podendo ser customizado
e alterado.

Projeto pessoal para usar no meu proprio terminal, como um script
de inicializaçao no boot

## Uso

E necessario instalar certos pacotes, caso nao estejam instalados

> pip install -r requirements.txt

> python3 init.py


Para deixar mais interessante, voce pode colocar o arquivo init.py
para se iniciar juntamente com seu bash no seu arquivo .zshrc/.bashrc
e criar um terminal com autenticação estilo Fallout.

> git clone https://github.com/ARCANGEL0/fallTerminal 

> cd fallTerminal

> echo "python3 $(pwd)/init.py" >> $HOME/.bashrc


## Menu de opções

O menu de opções consta com alguns serviços do meu terminal próprio ( como apache, mysql, snapd )
que podem ser inicializados pelo próprio script, como uma shell interativa
Sinta-se a vontade para adicionar seus próprios selects e modificar ao seu gosto


## Geraçao da senha

A senha do terminal e gerada a partir de um arquivo de texto (pass) , que printa todas as palavras na tela e salva uma delas
aleatoriamente como senha do sistema
Para visualizar qual a senha escolhida, basta digitar
> /ADMIN.L

no terminal do login para visualizar a senha atual.



## Terminal

Para aderir mais ao estilo retro de Terminal,
recomendo o cool-retro-term de Swordfish90

Para ficar mais igual ao estilo do terminal do fallout,
exportei meu JSON de estilização do CRT no repo 
como falout.json

(https://github.com/Swordfish90/cool-retro-term)
