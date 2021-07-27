# Fall Terminal
====================================

Script em python inspirado na franquia de Jogos Fallout
que simula um terminal e a autenticaçao do terminal

Conta com um menu pos-autenticaçao para sair e acessar o terminal tty, 
opçoes para modificar arquivos, iniciar serviços e afins, podendo ser customizado
e alterado.

Projeto pessoal para usar no meu proprio terminal, como um script
de inicializaçao no logon

## Uso

E necessario instalar algumas dependencias, caso nao estejam instaladas

> apt-get install ne nano

> pip install -r requirements.txt

> python terminal.py


Para deixar mais interessante, voce pode colocar o arquivo python
para se auto iniciar junto com seu .bashrc ou .zhsrc.


## Menu de opções

O menu de opções consta com alguns serviços do meu terminal próprio
que podem ser inicializados pelo próprio script, como uma shell interativa
Sinta-se a vontade para adicionar seus próprios selects e modificar ao seu gosto

## Geraçao da senha

A senha do terminal e gerada a partir de um arquivo de texto, que printa todas as palavras na tela e salva uma delas
aleatoriamente como senha do sistema
Para visualizar qual a senha escolhida, basta digitar
> [/ADMIN.F PASS] 

no terminal do login para visualizar a senha atual.



## Terminal

Para aderir mais ao estilo retro de Terminal,
recomendo o cool-retro-term de Swordfish90
(https://github.com/Swordfish90/cool-retro-term)
