#! /usr/bin/env python3
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

TXT1 = '保安がセットし直す。。。'

TXT2 = 'ロブコ産業(TM)端末へようこそ'

TXT3 = '設定端末 / 問い合わせる'

TXT4 = 'RIT-V300'

TXT5 = '設定 ファイル/プロテクション=オーナー:RWED ADMIN.F'

TXT6 = '種類 設定します 再起動/メイン'




# menu de selecao

TITLE_HEAD =   ( 
'ロブコ産業',
'統ーされたオペレ',
'ティングシステム'
)

MENU_HEAD = (
    '版権 2075-2077 ロブコ産業',
    '-サーバー 6-',
    ''
)

MENU_HEAD2 = (
    '      ソフト錠前 ソリューション\n'
    '"あなたのセキュリティは私たちのセキュリティです"',
    '>\\ こんにちは, '+ socket.gethostname(),
    ''
)

MENU1 = [
    '端末がアクセス',
    'ログ',
    '取捨',
    'オフ',
    '電源を切る'
]

MENU2 = [
    '帰る',
    'フスマ を 始める',
    'あぱちぇ を 始める',
    'データベース を 始める',
    'スナップ を 始める',
    'ブルートゥース を 始める',
   
]


# pagina de login

LOGIN_TXT = 'ロブコ産業(TM)端末を手順'


NUMCHARS = 16

SQUARE_X = 19
SQUARE_Y = 3

TENTATIVAS_MAX = 4

LINHAS_HD = 5

LOGIN_PAUSE = 1000

POINTER = 0xf650

ELEMNT = '!@#$%^*()_-+={}[]|\\:;\'",<>./?'




LOGIN_TXT = 'ロブコ産業(TM)端末を手順へようこそ'

LOGIN_PASS = 'パスワードを入力する'

LOGIN_ERROR = 'パスワードが間違っています。 もう一度やり直してください'


LOGIN_USER = 'LOGON '


# tela bloqueada

LOCK_TXT1 = '端末は鍵を掛けた'
LOCK_TXT2 = '管理者に連絡してください'

LOCK_TXT3 = '! ALERT | 検出されたセキュリティバイパスの試み !'


BLOQUEIO = 10000000


# ----------- funcoes --------------------


def checkPS(processName):
    '''
    Funcao para checar se servicos estao em execucao
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

    if checkPS('fusuma'):
        MENU2[1] = "フスマ を 停留"
    else:
        MENU2[1] = "フスマ を 始める"

    if checkPS('apache2'):
        MENU2[2] = "あぱちぇ を 停留"
    else:
        MENU2[2] = "あぱちぇ を 始める"


    if checkPS('mariadb'):
        MENU2[3] = "データベース を 停留"
    else:
        MENU2[3] = "データベース を 始める"


    if checkPS('snapd'):
        MENU2[4] = "スナップ を 停留"
    else:
        MENU2[4] = "スナップ を 始める"

    if checkPS('bluetoothd'):
    	MENU2[5] = "ブルートゥース を 停留"
    else:
    	MENU2[5] = "ブルートゥース を 始める"



    while keyInput != novaLinha:
        scr.move(selection_start_y, 0)
        line = 0
        for sel in MENU2:
            whole_line = '> ' + MENU2[line]
            whole_line += '\n'

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
            scr.erase() 
            menu()



        elif keyInput == ord('\n') and selection == 1:
            playsound(os.path.join(dir,"audio/keyenter.wav"))

            if checkPS('fusuma'):
                playsound(os.path.join(dir,"audio/stopFusuma.wav"))
                print("\n\nフスマ を 停留ている。。。")
                time.sleep(2)
                os.system('killall fusuma')
                scr.erase() 
                opcoes()
            else:
                playsound(os.path.join(dir,"audio/startFusuma.wav"))
                print("\n\nフスマ を 始めるている。。。")
                time.sleep(2)
                os.system('fusuma -d')
                scr.erase() 
                opcoes()



        elif keyInput == ord('\n') and selection == 2:
            playsound(os.path.join(dir,"audio/keyenter.wav"))

            if checkPS('apache2'):
                playsound(os.path.join(dir,"audio/stopApache.wav"))
                print("\n\nあぱちぇ を 停留ている。。。")
                time.sleep(2)
                os.system('echo { ROOT PASSWORD } | sudo -S -k service apache2 stop')
                scr.erase() 
                opcoes()
            else:
                playsound(os.path.join(dir,"audio/startApache.wav"))
                print("\n\nあぱちぇ を 始めるている。。。")
                time.sleep(2)
                os.system('echo { ROOT PASSWORD } | sudo -S -k service apache2 start')
                scr.erase() 
                opcoes()

        elif keyInput == ord('\n') and selection == 3:
            playsound(os.path.join(dir,"audio/keyenter.wav"))
    
            if checkPS('mariadb'):
                playsound(os.path.join(dir,"audio/startBluetooth.wav"))
                print("\n\nデータベース を 停留ている。。。")
                time.sleep(2)
                os.system('echo { ROOT PASSWORD } | sudo -S -k service mysql stop')
                scr.erase() 
                opcoes()
            else:
                playsound(os.path.join(dir,"audio/startSql.wav"))
                print("\n\nデータベース を 始めるている。。。")
                time.sleep(2)
                os.system('echo { ROOT PASSWORD } | sudo -S -k service mysql start')
                scr.erase() 
                opcoes()
        elif keyInput == ord('\n') and selection == 4:
            playsound(os.path.join(dir,"audio/keyenter.wav"))
    
            if checkPS('snapd'):
                playsound(os.path.join(dir,"audio/stopSnap.wav"))
                print("\n\nスナップ を 停留ている。。。")
                time.sleep(2)
                os.system('echo { ROOT PASSWORD } | sudo -S -k service snapd stop')
                scr.erase() 
                opcoes()
            else:
                playsound(os.path.join(dir,"audio/startSnap.wav"))
                print("\n\nスナップ を 始めるている。。。")
                time.sleep(2)
                os.system('echo { ROOT PASSWORD } | sudo -S -k service snapd start && echo { ROOT PASSWORD } |  sudo -S -k service apparmor start')
                scr.erase() 
                opcoes()

        elif keyInput == ord('\n') and selection == 5:
            playsound(os.path.join(dir,"audio/keyenter.wav"))
    
            if checkPS('bluetoothd'):
                playsound(os.path.join(dir,"audio/stopBluetooth.wav"))

                print("\n\nブルートゥース を 停留ている。。。")
                time.sleep(2)
                os.system('echo { ROOT PASSWORD } | sudo -S -k killall bluetoothd')
                scr.erase() 
                opcoes()
            else:
                playsound(os.path.join(dir,"audio/startBluetooth.wav"))
                print("\n\nブルートゥース を 始めるている。。。")
                time.sleep(2)
                os.system('echo { ROOT PASSWORD } | sudo -S -k bluetoothd & disown')
                scr.erase() 
                opcoes()
	    

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
            space = largura - len(whole_line) % largura + 20
            whole_line += '\n'

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
            print("\n\n\n端末を入るている。。。")
            playsound(os.path.join(dir,"audio/EnterTerminal.mp3"))

            time.sleep(2)
            os.system('tmux')


        elif keyInput == ord('\n') and selection == 1:
            playsound(os.path.join(dir,"audio/keyenter.wav"))
            print("\n\n\nログをアクセスている。。。")

            playsound(os.path.join(dir,"audio/sysLogs.mp3"))

            time.sleep(2)

            print(os.system('journalctl'))

            exit = scr.getch()
            if exit == ord('\n'):
                scr.erase()
                menu()
            scr.erase()
            menu()

            

        elif keyInput == ord('\n') and selection == 2:
            playsound(os.path.join(dir,"audio/keyenter.wav"))
            playsound(os.path.join(dir,"audio/options.mp3"))

            opcoes()


        elif keyInput == ord('\n') and selection == 3:
            playsound(os.path.join(dir,"audio/keyenter.wav"))
            playsound(os.path.join(dir,"audio/windowClose.mp3"))

            time.sleep(3)
            pid = os.getppid()
            os.kill(pid,9)

        elif keyInput == ord('\n') and selection == 4:
            playsound(os.path.join(dir,"audio/keyenter.wav"))
            print("\n\n\nShutting down...")
            playsound(os.path.join(dir,"audio/shutDown.mp3"))

            time.sleep(5)
            os.system("systemctl poweroff")


def initMenu(scr):
  
    curses.use_default_colors()
    scr.erase()
    scr.move(0, 0)
    curses.curs_set(0)
  
    largura = scr.getmaxyx()[1]


    for header in TITLE_HEAD:
        centr(scr, header + '\n')

    for header in MENU_HEAD:
        centr(scr, header + '\n')

    for header in MENU_HEAD2:
        typeT(scr, header + '\n')

    for i in range(largura):
        scr.addch(curses.ACS_BSBS)
    scr.refresh()

    return criarMenu(scr)

def initOpcoes(scr):
   
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
    typeT(scr, '\n今すぐパスワードを入力してください\n\n')
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


        if guess.upper() == senhaHack.upper():
            playsound(os.path.join(dir,"audio/keyenter.wav"))
            keypad.addstr('>'+senha+'\n')
            playsound(os.path.join(dir,"audio/beep.wav"))
            continue

        elif guess.upper() == senha.upper():
            playsound(os.path.join(dir,"audio/keyenter.wav"))

            keypad.addstr('>Exact match!\n')
            keypad.addstr('>Please wait\n')
            keypad.addstr('>while system\n')
            keypad.addstr('>is accessed.\n')
            mvPad(scr, keypad)
            playsound(os.path.join(dir,"audio/correctpass.wav"))
            curses.napms(LOGIN_PAUSE)
            playsound(os.path.join(dir,"audio/welcome.wav"))

            return senha


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







if __name__ == '__main__':
    globals()[sys.argv[1]]()
