#! /usr/bin/env python
import sys
import curses
import time
import random
import os
import socket
import signal
from playsound import playsound
import psutil

#!/usr/bin/env python
# -*- coding: utf-8 -*- 


# funcao para lidar com interrupcoes do teclado

def handler(signum, frame):
    pass


signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTSTP, handler)





# -------------------- VARIAVEIS GERAIS --------------------------



dir= os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__))) # pega o diretorio do arquivo



# boot

TXT1 = 'SECURITY RESET... '

TXT2 = 'WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK'

TXT3 = 'SET TERMINAL/INQUIRE'

TXT4 = 'RIT-V300'

TXT5 = 'SET FILE/PROTECTION=OWNER:RWED ACCOUNTS.F'

TXT6 = 'SET HALT RESTART/MAIN'




# menu de selecao



MENU_HEAD = (
    'ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM',
    'COPYRIGHT 2075-2077 ROBCO INDUSTRIES',
    '-SERVER 6-',
    ''
)

MENU_HEAD2 = (
    '      SoftLock Solutions, Inc\n'
    '"Your Security is Our Security"',
    '>\\ Welcome, '+ socket.gethostname(),
    ''
)

MENU1 = [
    'Acessar terminal',
    'Iniciar Desktop',
    'Opcoes',
    'Sair'
]

MENU2 = [
    'Modificar zshrc',
    'Modificar bashrc',
    'Iniciar Fusuma',
    'Iniciar apache',
    'Iniciar MySQL',
    'Voltar'
]



# ----------- funcoes --------------------


def checkPS(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;




def menuOpcoes(scr):

    keyInput = 0
    selection = 0
    selection_count = len(MENU2)
    selection_start_y = scr.getyx()[0]
    largura = scr.getmaxyx()[1]


    if checkPS('mysqld'):
        MENU2[4] = "Parar MySQL"
    else:
        MENU2[4] = "Iniciar MySQL"

    if checkPS('apache2'):
        MENU2[3] = "Parar apache"
    else:
        MENU2[3] = "Iniciar apache"



    while keyInput != novaLinha:
        scr.move(selection_start_y, 0)
        line = 0
        for sel in MENU2:
            whole_line = '> ' + MENU2[line]
            space = largura - len(whole_line) % largura
            whole_line += ' ' * space

            if line == selection:
                scr.addstr(whole_line, curses.A_REVERSE)
            else:
                scr.addstr(whole_line)
            line += 1
            scr.refresh()

        keyInput = scr.getch()

        if keyInput == curses.KEY_UP and selection > 0:
            selection -= 1
        elif keyInput == curses.KEY_DOWN and selection < selection_count - 1:
            selection += 1

        if keyInput == ord('\n') and selection == 0:
            os.system("play " +os.path.join(dir,"audio/keyenter.wav -q"))
            print("\n\n\nOpening editor...")
            time.sleep(2)
            scr.erase() 
            os.system('ne $HOME/.zshrc')
            exit = scr.getch()

            if exit == ord('\n'):
                scr.erase()
                opcoes()
            elif exit == ord('\x1A'):
                scr.erase()
                opcoes()

            opcoes()

        elif keyInput == ord('\n') and selection == 1:
            os.system("play " +os.path.join(dir,"audio/keyenter.wav -q"))
            print("\n\n\nOpening editor...")
            time.sleep(2)
            scr.erase() 

            os.system('ne $HOME/.bashrc')
            exit = scr.getch()
            if exit == ord('\n'):
                scr.erase()
                opcoes()
            elif exit == ord('\x1A'):
                scr.erase()
                opcoes()

            opcoes()


        elif keyInput == ord('\n') and selection == 2:
            os.system("play " +os.path.join(dir,"audio/keyenter.wav -q"))
            print("\n\nStarting fusuma...")
            time.sleep(2)
            os.system('fusuma -d')
            scr.erase()
            opcoes()
        elif keyInput == ord('\n') and selection == 3:
            os.system("play " +os.path.join(dir,"audio/keyenter.wav -q"))

            if checkPS('apache2'):
                print("\n\nStopping apache2...")
                time.sleep(2)
                os.system('service apache2 stop')
                scr.erase() 
                opcoes()
            else:
                print("\n\nStarting apache2...")
                time.sleep(2)
                os.system('service apache2 start')
                scr.erase() 
                opcoes()

        elif keyInput == ord('\n') and selection == 4:
            os.system("play " +os.path.join(dir,"audio/keyenter.wav -q"))
    
            if checkPS('mysqld'):
                print("\n\nStopping mysql...")
                time.sleep(2)
                os.system('service mysql stop')
                scr.erase() 
                opcoes()
            else:
                print("\n\nStarting mysql...")
                time.sleep(2)
                os.system('service mysql start')
                scr.erase() 
                opcoes()


        elif keyInput == ord('\n') and selection == 5:
            os.system("play " +os.path.join(dir,"audio/keyenter.wav -q"))
            scr.erase() 
            menu()


def criarMenu(scr):


    keyInput = 0
    selection = 0
    selection_count = len(MENU1)
    selection_start_y = scr.getyx()[0]
    largura = scr.getmaxyx()[1]



    if checkPS('Xvnc'):
      MENU1[1] = 'Encerrar desktop'
    else:
      MENU1[1] = 'Iniciar desktop'
    
  

    while keyInput != novaLinha:
        scr.move(selection_start_y, 0)
        line = 0
        for sel in MENU1:
            whole_line = '> ' + MENU1[line]
            space = largura - len(whole_line) % largura
            whole_line += ' ' * space

            if line == selection:
                scr.addstr(whole_line, curses.A_REVERSE)
            else:
                scr.addstr(whole_line)
            line += 1
            scr.refresh()

        keyInput = scr.getch()

        # move up and down
        if keyInput == curses.KEY_UP and selection > 0:
            selection -= 1
        elif keyInput == curses.KEY_DOWN and selection < selection_count - 1:
            selection += 1

        if keyInput == ord('\n') and selection == 0:
            os.system("play " +os.path.join(dir,"audio/keyenter.wav -q"))
            print("\n\n\nEntering tty terminal...")
            time.sleep(2)
            os.system('tmux')


        elif keyInput == ord('\n') and selection == 1:
            os.system("play " +os.path.join(dir,"audio/keyenter.wav -q"))
            
            if checkPS('Xvnc'):
                print(os.system('stopdesktop'))
            else:
              print(os.system('startdesktop'))
            
          
     
            scr.erase()
            menu()
            

        elif keyInput == ord('\n') and selection == 2:
            os.system("play " +os.path.join(dir,"audio/keyenter.wav -q"))
            opcoes()

        elif keyInput == ord('\n') and selection == 3:
            os.system("play " +os.path.join(dir,"audio/keyenter.wav -q"))
            time.sleep(3)
            pid = os.getppid()
            os.kill(pid,9)



def initMenu(scr):
    """
    Print the MENU1 and allow the user to select one
    """
    curses.use_default_colors()
    scr.erase()
    scr.move(0, 0)
    curses.curs_set(0)

    largura = scr.getmaxyx()[1]

    for header in MENU_HEAD:
        centr(scr, header + '\n')

    for header in MENU_HEAD2:
        typeT(scr, header + '\n')

    for i in range(largura):
        scr.addch(curses.ACS_BSBS)
    scr.refresh()

    return criarMenu(scr)

def initOpcoes(scr):
    """
    Print the MENU1 and allow the user to select one
    """
    curses.use_default_colors()
    scr.erase()
    scr.move(0, 0)
    curses.curs_set(0)

    largura = scr.getmaxyx()[1]

    for header in MENU_HEAD:
        centr(scr, header + '\n')

    for header in MENU_HEAD2:
        typeT(scr, header + '\n')

    for i in range(largura):
        scr.addch(curses.ACS_BSBS)
    scr.refresh()

    return menuOpcoes(scr)


def menu():
    """
    Initialize curses and start the boot process
    """
    res = curses.wrapper(initMenu)
    return res

def opcoes():
    res = curses.wrapper(initOpcoes)
    return res





def initBoot(scr):
 
    curses.use_default_colors()
    scr.erase()
    scr.move(0, 0)

    curses.noecho()
    scr.scrollok(True)
    typeT(scr, TXT1 + '\n\n', delay)
    typeT(scr, TXT2 + '\n\n', delay)

    typeT(scr, '>')
    curses.napms(Ipausa)

    typeT(scr, TXT3 + '\n\n', delay)
    curses.napms(Ipausa)
    typeT(scr, TXT4 + '\n\n', delay)
    typeT(scr, '>')
    curses.napms(Ipausa)
    typeT(scr, TXT5 + '\n', delay)
    typeT(scr, '>')
    curses.napms(Ipausa)
    typeT(scr, TXT6 + '\n\n', delay)
    curses.napms(Ipausa)
    return menu()
def iniciar():

    res = curses.wrapper(initBoot)
    return res











Lpausa = 3

Ipausa = 50 # ms

delay = 40

mascara = '*'

novaLinha = 10



def typeT(window, text, pause = Lpausa):

    os.system("play " +os.path.join(dir,"audio/beep.wav -q"))



    for i in range(len(text)):

        window.addstr(text[i])
        window.refresh()
        curses.napms(pause)

''
    

    

def centr(window, text, pause = Lpausa):

    largura = window.getmaxyx()[1]
    window.move(window.getyx()[0], int(largura / 2 - len(text) / 2))
    typeT(window, text, pause)





   
### iniciar 


iniciar()
  