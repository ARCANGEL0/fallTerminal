#! /usr/bin/env python
import sys
import curses
import time
import random
import os
import socket
import signal
from playsound import playsound

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

MENU1 = (
    'Acessar terminal',
    'Logs',
    'Opcoes',
    'Sair'
)

MENU2 = (
    'Modificar zshrc',
    'Modificar bashrc',
    'Iniciar Fusuma',
    'Iniciar apache',
    'Iniciar MySQL',
    'Voltar'


)



# pagina de login

LOGIN_TXT = 'ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL'


NUMCHARS = 16

SQUARE_X = 19
SQUARE_Y = 3

TENTATIVAS_MAX = 4

LINHAS_HD = 5

LOGIN_PAUSE = 1000

POINTER = 0xf650

ELEMNT = '!@#$%^*()_-+={}[]|\\:;\'",<>./?'




LOGIN_TXT = 'WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL'

LOGIN_PASS = 'ENTER PASSWORD NOW'

LOGIN_ERROR = 'INCORRECT PASSWORD, PLEASE TRY AGAIN'


LOGIN_USER = 'LOGON '


# tela bloqueada

LOCK_TXT1 = 'TERMINAL LOCKED'
LOCK_TXT2 = 'PLEASE CONTACT AN ADMINISTRATOR'

LOCK_TXT3 = '! SECURITY BYPASS ATTEMPT DETECTED !'


BLOQUEIO = True


# ----------- funcoes --------------------

def menuOpcoes(scr):

    keyInput = 0
    selection = 0
    selection_count = len(MENU2)
    selection_start_y = scr.getyx()[0]
    largura = scr.getmaxyx()[1]

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
            playsound(os.path.join(dir,"audio/keyenter.wav"))
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
            playsound(os.path.join(dir,"audio/keyenter.wav"))
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
            playsound(os.path.join(dir,"audio/keyenter.wav"))
            print("\n\nStarting fusuma...")
            time.sleep(2)
            os.system('fusuma -d')
            scr.erase()
            opcoes()
        elif keyInput == ord('\n') and selection == 3:
            playsound(os.path.join(dir,"audio/keyenter.wav"))
            print("\n\nStarting apache2...")
            time.sleep(2)
            os.system('service apache2 start')
            scr.erase() 
            opcoes()

        elif keyInput == ord('\n') and selection == 4:
            playsound(os.path.join(dir,"audio/keyenter.wav"))
            print("\n\nStarting mysql...")
            time.sleep(2)
            os.system('service mysql start')
            scr.erase() 
            opcoes()


        elif keyInput == ord('\n') and selection == 5:
            playsound(os.path.join(dir,"audio/keyenter.wav"))
            scr.erase() 
            menu()


def criarMenu(scr):


    keyInput = 0
    selection = 0
    selection_count = len(MENU1)
    selection_start_y = scr.getyx()[0]
    largura = scr.getmaxyx()[1]

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
            playsound(os.path.join(dir,"audio/keyenter.wav"))
            print("\n\n\nEntering tty terminal...")
            time.sleep(2)
            os.system('tmux')


        elif keyInput == ord('\n') and selection == 1:
            playsound(os.path.join(dir,"audio/keyenter.wav"))
            
            
            
            print(os.system('journalctl'))
            exit = scr.getch()
            if exit == ord('\n'):
                scr.erase()
                menu()
            scr.erase()
            menu()

            

        elif keyInput == ord('\n') and selection == 2:
            playsound(os.path.join(dir,"audio/keyenter.wav"))
            opcoes()

        elif keyInput == ord('\n') and selection == 3:
            playsound(os.path.join(dir,"audio/keyenter.wav"))
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




def gPointer(n):

    num = POINTER
    point_array = []
    for i in range(n):
        point_array.append(num)
        num += 12
    return point_array


def getELEMNT(n):

    count = len(ELEMNT)
    simbolos = ""
    for i in range(int(n)):
        simbolos += ELEMNT[random.randint(0, count - 1)]
    return simbolos


def f_senhas():

    senha_array = []

    

    with open(os.path.join(dir, "pass")) as senha_ln:
        for line in senha_ln:
            if not line.strip():
                senha_array.append([])
            elif len(senha_array) > 0:
                senha_array[len(senha_array) - 1].append(line[:-1])

    senhas = senha_array[random.randint(0, len(senha_array) - 1)]

    random.shuffle(senhas)
    return senhas


def SCREENF(length, senhas):

    tela = getELEMNT(length)

    senhaLen = len(senhas[0])
    senhaCount = len(senhas)
    i = 0
    for senha in senhas:
        maxSkip = int(length / senhaCount - senhaLen)
        i += random.randint(maxSkip - 2, maxSkip)
        tela = tela[:i] + senha + tela[i + senhaLen:]
        i += senhaLen
    return tela


def sInit(scr):

    tTamanho = scr.getmaxyx()
    altura = tTamanho[0]
    largura = tTamanho[1]
    tAltura = altura - LINHAS_HD

    pCols = gPointer(tAltura * 2)

    coluna1 = pCols[:tAltura]
    coluna2 = pCols[tAltura:]

    tQuant = largura / 2 * tAltura
    senhas = f_senhas()
    tela = SCREENF(tQuant, senhas)
    tCol1, tCol2 = tela[0:len(tela)//2], tela[len(tela)//2:]


    tLargura = int(largura / 4)

    typeT(scr, LOGIN_TXT)
    typeT(scr, '\nENTER PASSWORD NOW\n\n')
    typeT(scr, str(TENTATIVAS_MAX) + ' ATTEMPT(S) LEFT: ')
    for i in range(TENTATIVAS_MAX):
        scr.addch(curses.ACS_BLOCK)
        typeT(scr, ' ')
    typeT(scr, '\n\n')

    for i in range(tAltura):
        typeT(scr, "0x%X %s" % (coluna1[i], tCol1[i * tLargura: (i + 1) * tLargura]), 0)
        if i < tAltura - 1:
            scr.addstr('\n')

    for i in range(tAltura):
        scr.move(LINHAS_HD + i, int(NUMCHARS / 2 + tLargura))
        typeT(scr, '0x%X %s' % (coluna2[i], tCol2[i * tLargura: (i + 1) * tLargura]), 0)

    scr.refresh()

    return senhas


def mvPad(scr, keypad):

    tTamanho = scr.getmaxyx()
    altura = tTamanho[0]
    largura = tTamanho[1]

    keypad.addstr('\n>')

    cursorPos = keypad.getyx()

    keypad.refresh(0, 0,
                     int(altura - cursorPos[0] - 1),
                     int(largura / 2 + NUMCHARS),
                     int(altura - 1),
                     int(largura - 1))


def userPad(scr, senhas):

    tTamanho = scr.getmaxyx()
    altura = tTamanho[0]
    largura = tTamanho[1]

    keypad = curses.newpad(altura, int(largura / 2 + NUMCHARS))

    tentativas = TENTATIVAS_MAX
    
    senha = senhas[random.randint(0, len(senhas) - 1)]
    senhaHack = '[/ADMIN.F PASS]'

    curses.noecho()

    while tentativas > 0:
        scr.move(int(altura - 1), int(largura / 2 + NUMCHARS + 1))

        mvPad(scr, keypad)

        guess = cap_string(scr, False, False)
        cursorPos = keypad.getyx()

        keypad.move(cursorPos[0] - 1, cursorPos[1] - 1)
        keypad.addstr('>' + guess.upper() + '\n')

        if guess.upper() == senha.upper():
            playsound(os.path.join(dir,"audio/keyenter.wav"))

            keypad.addstr('>Exact match!\n')
            keypad.addstr('>Please wait\n')
            keypad.addstr('>while system\n')
            keypad.addstr('>is accessed.\n')
            mvPad(scr, keypad)
            playsound(os.path.join(dir,"audio/correctpass.wav"))
            curses.napms(LOGIN_PAUSE)
            return senha

        elif guess.upper() == senhaHack.upper():
            playsound(os.path.join(dir,"audio/keyenter.wav"))
            keypad.addstr('>'+senha+'\n')
            playsound(os.path.join(dir,"audio/beep.wav"))

        else:
            playsound(os.path.join(dir,"audio/keyenter.wav"))

            senhaLen = len(senha)
            matched = 0
            try:
                for i in range(senhaLen):
                    if senha[i].upper() == guess[i].upper():
                        matched += 1
            except IndexError:
                pass

            keypad.addstr('>Login denied\n')
            keypad.addstr('>' + str(matched) + '/' + str(senhaLen) +
                            ' correct.\n')
            playsound(os.path.join(dir,"audio/wrongpass.wav"))
        tentativas -= 1
        scr.move(SQUARE_Y, 0)
        scr.addstr(str(tentativas))
        scr.move(SQUARE_Y, SQUARE_X)
        for i in range(TENTATIVAS_MAX):
            if i < tentativas:
                scr.addch(curses.ACS_BLOCK)
            else:
                scr.addstr(' ')
            scr.addstr(' ')

    # Out of tentativas
    return None

def login_menu(scr):

    curses.use_default_colors()
    tTamanho = scr.getmaxyx()
    largura = tTamanho[1]
    altura = tTamanho[0]
    random.seed()
    scr.erase()
    scr.move(0, 0)
    senhas = sInit(scr)
    return userPad(scr, senhas)


def login():

    return curses.wrapper(login_menu)




def initLock(scr):
    """
    Start the locked out portion of the terminal
    """
    curses.use_default_colors()
    tTamanho = scr.getmaxyx()
    largura = tTamanho[1]
    altura = tTamanho[0]
    scr.erase()
    curses.curs_set(0)
    scr.move(int(altura / 2 - 1), 0)
    centr(scr, LOCK_TXT1)
    scr.move(int(altura / 2 + 1), 0)
    centr(scr, LOCK_TXT2)
    scr.refresh()
    curses.napms(BLOQUEIO)

def bloquearTela():
    """
    Initialize curses and start the locked out process
    """
    curses.wrapper(initLock)


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
    return True

def iniciar():

    res = curses.wrapper(initBoot)
    return res










def initLogin(scr, username, password):

    curses.use_default_colors()
    scr.erase()
    scr.move(0, 0)

    curses.noecho()
    scr.scrollok(True)

    typeT(scr, LOGIN_TXT + '\n\n')

    
    typeT(scr, '> ')
    curses.napms(Ipausa)
    typeT(scr, LOGIN_USER + username.upper() + '\n', delay)

    typeT(scr, '\n' + LOGIN_PASS + '\n\n')

   
    typeT(scr, '> ')
    curses.napms(Ipausa)
    password_stars = mascara * len(password)
    typeT(scr, password_stars + '\n', delay)

    curses.napms(500)




Lpausa = 3

Ipausa = 50 # ms

delay = 40

mascara = '*'

novaLinha = 10



def typeT(window, text, pause = Lpausa):

    playsound(os.path.join(dir,"audio/beep.wav"))



    for i in range(len(text)):

        window.addstr(text[i])
        window.refresh()
        curses.napms(pause)

''
    

def cap_string(window, hidden = False, can_novaLinha = True):

    keyInput = 0
    def_string = ''
    try:
        while keyInput != novaLinha:
            keyInput = window.getch()
            if keyInput > 96 and keyInput < 123:
                keyInput -= 32
            if keyInput == ord('\b'):
                if len(def_string) > 0:
                    def_string = def_string[:-1]
                    cur = window.getyx()
                    window.move(cur[0], cur[1] - 1)
                    window.clrtobot()
                else:
                    continue
            elif keyInput > 255:
                continue
            elif keyInput != novaLinha:
                def_string += chr(keyInput)
                if hidden:
                    window.addch(mascara)
                else:
                    window.addch(keyInput)
            elif can_novaLinha:
                window.addch(novaLinha)
        return def_string 
        
    except ValueError:
        # We might have Unicode chars in here, let's use unichr instead
        login()

    

def centr(window, text, pause = Lpausa):

    largura = window.getmaxyx()[1]
    window.move(window.getyx()[0], int(largura / 2 - len(text) / 2))
    typeT(window, text, pause)





   
### iniciar 


if iniciar():
    senha = login()
    if senha != None:
        print(menu())
    else:
        bloquearTela()