#! /usr/bin/env python
import sys
import curses
import time
import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import socket
import signal
from playsound import playsound
from pygame import mixer
import subprocess


def handler(signum, frame):
    pass


signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTSTP, handler)


__location__ = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))



CENTERED_HEADERS = (
    'ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM',
    'COPYRIGHT 2075-2077 ROBCO INDUSTRIES',
    '-SERVER 6-',
    ''
)

OTHER_HEADERS = (
    '"Your Security is Our Security"',
    '>\\ Welcome, '+socket.gethostname(),
    ''
)

SELECTIONS = (
    'Acessar terminal',
    'Logs',
    'Opcoes',
    'Sair'
)

OPCOES = (
    'Modificar zshrc',
    'Modificar bashrc',
    'Iniciar Fusuma',
    'Iniciar apache',
    'Iniciar MySQL',
    'Voltar'


)

def selectOptions(scr):

    inchar = 0
    selection = 0
    selection_count = len(OPCOES)
    selection_start_y = scr.getyx()[0]
    width = scr.getmaxyx()[1]

    while inchar != NEWLINE:
        scr.move(selection_start_y, 0)
        line = 0
        for sel in OPCOES:
            whole_line = '> ' + OPCOES[line]
            space = width - len(whole_line) % width
            whole_line += ' ' * space

            if line == selection:
                scr.addstr(whole_line, curses.A_REVERSE)
            else:
                scr.addstr(whole_line)
            line += 1
            scr.refresh()

        inchar = scr.getch()

        if inchar == curses.KEY_UP and selection > 0:
            selection -= 1
        elif inchar == curses.KEY_DOWN and selection < selection_count - 1:
            selection += 1

        if inchar == ord('\n') and selection == 0:
            playsound(os.path.join(__location__,"audio/keyenter.wav"))
            print("\n\n\nOpening editor...")
            time.sleep(2)
            scr.erase() 
            os.system('ne $HOME/.zshrc')
            exit = scr.getch()

            if exit == ord('\n'):
                scr.erase()
                beginOptions()
            elif exit == ord('\x1A'):
                scr.erase()
                beginOptions()

            beginOptions()

        elif inchar == ord('\n') and selection == 1:
            playsound(os.path.join(__location__,"audio/keyenter.wav"))
            print("\n\n\nOpening editor...")
            time.sleep(2)
            scr.erase() 

            os.system('ne $HOME/.bashrc')
            exit = scr.getch()
            if exit == ord('\n'):
                scr.erase()
                beginOptions()
            elif exit == ord('\x1A'):
                scr.erase()
                beginOptions()

            beginOptions()


        elif inchar == ord('\n') and selection == 2:
            playsound(os.path.join(__location__,"audio/keyenter.wav"))
            print("\n\nStarting fusuma...")
            time.sleep(2)
            os.system('fusuma -d')
            scr.erase()
            beginOptions()
        elif inchar == ord('\n') and selection == 3:
            playsound(os.path.join(__location__,"audio/keyenter.wav"))
            print("\n\nStarting apache2...")
            time.sleep(2)
            os.system('service apache2 start')
            scr.erase() 
            beginOptions()

        elif inchar == ord('\n') and selection == 4:
            playsound(os.path.join(__location__,"audio/keyenter.wav"))
            print("\n\nStarting mysql...")
            time.sleep(2)
            os.system('service mysql start')
            scr.erase() 
            beginOptions()


        elif inchar == ord('\n') and selection == 5:
            playsound(os.path.join(__location__,"audio/keyenter.wav"))
            scr.erase() 
            beginSelection()


def makeSelection(scr):
    """
    ALlow the user to select an option
    Returns the line number of the users selection starting at 0
    """
    inchar = 0
    selection = 0
    selection_count = len(SELECTIONS)
    selection_start_y = scr.getyx()[0]
    width = scr.getmaxyx()[1]

    while inchar != NEWLINE:
        scr.move(selection_start_y, 0)
        line = 0
        for sel in SELECTIONS:
            whole_line = '> ' + SELECTIONS[line]
            space = width - len(whole_line) % width
            whole_line += ' ' * space

            if line == selection:
                scr.addstr(whole_line, curses.A_REVERSE)
            else:
                scr.addstr(whole_line)
            line += 1
            scr.refresh()

        inchar = scr.getch()

        # move up and down
        if inchar == curses.KEY_UP and selection > 0:
            selection -= 1
        elif inchar == curses.KEY_DOWN and selection < selection_count - 1:
            selection += 1

        if inchar == ord('\n') and selection == 0:
            playsound(os.path.join(__location__,"audio/keyenter.wav"))
            print("\n\n\nEntering tty terminal...")
            time.sleep(2)
            os.system('tmux')


        elif inchar == ord('\n') and selection == 1:
            playsound(os.path.join(__location__,"audio/keyenter.wav"))
            
            
            
            print(os.system('journalctl'))
            exit = scr.getch()
            if exit == ord('\n'):
                scr.erase()
                beginSelection()
            scr.erase()
            beginSelection()

            

        elif inchar == ord('\n') and selection == 2:
            playsound(os.path.join(__location__,"audio/keyenter.wav"))
            beginOptions()

        elif inchar == ord('\n') and selection == 3:
            playsound(os.path.join(__location__,"audio/keyenter.wav"))
            time.sleep(3)
            pid = os.getppid()
            os.kill(pid,9)



def runSelection(scr):
    """
    Print the selections and allow the user to select one
    """
    curses.use_default_colors()
    scr.erase()
    scr.move(0, 0)
    curses.curs_set(0)

    width = scr.getmaxyx()[1]

    for header in CENTERED_HEADERS:
        centeredWrite(scr, header + '\n')

    for header in OTHER_HEADERS:
        slowWrite(scr, header + '\n')

    for i in range(width):
        scr.addch(curses.ACS_BSBS)
    scr.refresh()

    return makeSelection(scr)

def runOptions(scr):
    """
    Print the selections and allow the user to select one
    """
    curses.use_default_colors()
    scr.erase()
    scr.move(0, 0)
    curses.curs_set(0)

    width = scr.getmaxyx()[1]

    for header in CENTERED_HEADERS:
        centeredWrite(scr, header + '\n')

    for header in OTHER_HEADERS:
        slowWrite(scr, header + '\n')

    for i in range(width):
        scr.addch(curses.ACS_BSBS)
    scr.refresh()

    return selectOptions(scr)


def beginSelection():
    """
    Initialize curses and start the boot process
    """
    res = curses.wrapper(runSelection)
    return res

def beginOptions():
    res = curses.wrapper(runOptions)
    return res





HEADER_TEXT = 'ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL'


CONST_CHARS = 16

SQUARE_X = 19
SQUARE_Y = 3

LOGIN_ATTEMPTS = 4

HEADER_LINES = 5

LOGIN_PAUSE = 1000

START_HEX = 0xf650

SYMBOLS = '!@#$%^*()_-+={}[]|\\:;\'",<>./?'


def generateHex(n):

    num = START_HEX
    list = []
    for i in range(n):
        list.append(num)
        num += 12
    return list


def getSymbols(n):

    count = len(SYMBOLS)
    result = ""
    for i in range(int(n)):
        result += SYMBOLS[random.randint(0, count - 1)]
    return result


def getPasswords():

    groups = []

    

    with open(os.path.join(__location__, "pass")) as pwfile:
        for line in pwfile:
            if not line.strip():
                groups.append([])
            elif len(groups) > 0:
                groups[len(groups) - 1].append(line[:-1])

    passwords = groups[random.randint(0, len(groups) - 1)]

    random.shuffle(passwords)
    return passwords


def getFiller(length, passwords):

    filler = getSymbols(length)

    pwdLen = len(passwords[0])
    pwdCount = len(passwords)
    i = 0
    for pwd in passwords:
        maxSkip = int(length / pwdCount - pwdLen)
        i += random.randint(maxSkip - 2, maxSkip)
        filler = filler[:i] + pwd + filler[i + pwdLen:]
        i += pwdLen
    return filler


def initScreen(scr):

    size = scr.getmaxyx()
    height = size[0]
    width = size[1]
    fillerHeight = height - HEADER_LINES

    hexes = generateHex(fillerHeight * 2)

    hexCol1 = hexes[:fillerHeight]
    hexCol2 = hexes[fillerHeight:]

    fillerLength = width / 2 * fillerHeight
    passwords = getPasswords()
    filler = getFiller(fillerLength, passwords)
    fillerCol1, fillerCol2 = filler[0:len(filler)//2], filler[len(filler)//2:]


    fillerWidth = int(width / 4)

    slowWrite(scr, HEADER_TEXT)
    slowWrite(scr, '\nENTER PASSWORD NOW\n\n')
    slowWrite(scr, str(LOGIN_ATTEMPTS) + ' ATTEMPT(S) LEFT: ')
    for i in range(LOGIN_ATTEMPTS):
        scr.addch(curses.ACS_BLOCK)
        slowWrite(scr, ' ')
    slowWrite(scr, '\n\n')

    for i in range(fillerHeight):
        slowWrite(scr, "0x%X %s" % (hexCol1[i], fillerCol1[i * fillerWidth: (i + 1) * fillerWidth]), 0)
        if i < fillerHeight - 1:
            scr.addstr('\n')

    for i in range(fillerHeight):
        scr.move(HEADER_LINES + i, int(CONST_CHARS / 2 + fillerWidth))
        slowWrite(scr, '0x%X %s' % (hexCol2[i], fillerCol2[i * fillerWidth: (i + 1) * fillerWidth]), 0)

    scr.refresh()

    return passwords


def moveInput(scr, inputPad):

    size = scr.getmaxyx()
    height = size[0]
    width = size[1]

    inputPad.addstr('\n>')

    cursorPos = inputPad.getyx()

    inputPad.refresh(0, 0,
                     int(height - cursorPos[0] - 1),
                     int(width / 2 + CONST_CHARS),
                     int(height - 1),
                     int(width - 1))


def userInput(scr, passwords):

    size = scr.getmaxyx()
    height = size[0]
    width = size[1]

    inputPad = curses.newpad(height, int(width / 2 + CONST_CHARS))

    attempts = LOGIN_ATTEMPTS
    pwd = 'senha'
    # pwd = passwords[random.randint(0, len(passwords) - 1)]
    curses.noecho()

    while attempts > 0:
        scr.move(int(height - 1), int(width / 2 + CONST_CHARS + 1))

        moveInput(scr, inputPad)

        guess = upperInput(scr, False, False)
        cursorPos = inputPad.getyx()

        inputPad.move(cursorPos[0] - 1, cursorPos[1] - 1)
        inputPad.addstr('>' + guess.upper() + '\n')

        if guess.upper() == pwd.upper():
            playsound(os.path.join(__location__,"audio/keyenter.wav"))

            inputPad.addstr('>Exact match!\n')
            inputPad.addstr('>Please wait\n')
            inputPad.addstr('>while system\n')
            inputPad.addstr('>is accessed.\n')
            moveInput(scr, inputPad)
            playsound(os.path.join(__location__,"audio/correctpass.wav"))
            curses.napms(LOGIN_PAUSE)
            return pwd

        else:
            playsound(os.path.join(__location__,"audio/keyenter.wav"))

            pwdLen = len(pwd)
            matched = 0
            try:
                for i in range(pwdLen):
                    if pwd[i].upper() == guess[i].upper():
                        matched += 1
            except IndexError:
                pass

            inputPad.addstr('>Entry denied\n')
            inputPad.addstr('>' + str(matched) + '/' + str(pwdLen) +
                            ' correct.\n')
            playsound(os.path.join(__location__,"audio/wrongpass.wav"))
        attempts -= 1
        scr.move(SQUARE_Y, 0)
        scr.addstr(str(attempts))
        scr.move(SQUARE_Y, SQUARE_X)
        for i in range(LOGIN_ATTEMPTS):
            if i < attempts:
                scr.addch(curses.ACS_BLOCK)
            else:
                scr.addstr(' ')
            scr.addstr(' ')

    # Out of attempts
    return None

def runLoginHx(scr):

    curses.use_default_colors()
    size = scr.getmaxyx()
    width = size[1]
    height = size[0]
    random.seed()
    scr.erase()
    scr.move(0, 0)
    passwords = initScreen(scr)
    return userInput(scr, passwords)


def beginLogin():

    return curses.wrapper(runLoginHx)



LOCKED_1 = 'TERMINAL LOCKED'
LOCKED_2 = 'PLEASE CONTACT AN ADMINISTRATOR'

LOCKED_3 = '! SECURITY BYPASS ATTEMPT DETECTED !'


LOCKED_OUT_TIME = 1000000


def runLocked(scr):
    """
    Start the locked out portion of the terminal
    """
    curses.use_default_colors()
    size = scr.getmaxyx()
    width = size[1]
    height = size[0]
    scr.erase()
    curses.curs_set(0)
    scr.move(int(height / 2 - 1), 0)
    centeredWrite(scr, LOCKED_1)
    scr.move(int(height / 2 + 1), 0)
    centeredWrite(scr, LOCKED_2)
    scr.refresh()
    curses.napms(LOCKED_OUT_TIME)

def runSecLock(scr):
    """
    Start the locked out portion of the terminal
    """
    curses.use_default_colors()
    size = scr.getmaxyx()
    width = size[1]
    height = size[0]
    scr.erase()
    curses.curs_set(0)
    scr.move(int(height / 2 - 3),0)
    centeredWrite(scr,LOCKED_3)
    scr.move(int(height / 2 - 1), 0)
    centeredWrite(scr, LOCKED_1)
    scr.move(int(height / 2 + 1), 0)
    centeredWrite(scr, LOCKED_2)
    scr.refresh()
    curses.napms(LOCKED_OUT_TIME)

def beginLocked():
    """
    Initialize curses and start the locked out process
    """
    curses.wrapper(runLocked)


def beginSecurityLock():

    curses.wrapper(runSecLock)


ENTRY_1 = 'SET TERMINAL/INQUIRE'

ENTRY_2 = 'SET FILE/PROTECTION=OWNER:RWED ACCOUNTS.F'

ENTRY_3 = 'SET HALT RESTART/MAINT'

ENTRY_4 = 'RUN DEBUG/ACCOUNTS.F'


MESSAGE_1 = 'WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK'

MESSAGE_2 = 'RIT-V300'

MESSAGE_3 = 'Initializing Robco Industries(TM) MF Boot Agent v2.3.0\n' \
            'RETROS BIOS\n' \
            'RBIOS-4.02.08.00 52EE5.E7.E8\n' \
            'Copyright 2201-2203 Robco Ind.\n' \
            'Uppermem: 64 KB\n' \
            'Root (5A8)\n' \
            'Maintenance Mode'



def runBoot(scr, hardMode):
    """
    Start the boot portion of the terminal

    hardMode - boolean indicating whether the user has to enter the ENTRY
               constants, or if they are entered automatically
    """
    curses.use_default_colors()
    scr.erase()
    scr.move(0, 0)

    curses.noecho()
    scr.scrollok(True)
    slowWrite(scr, MESSAGE_1 + '\n\n')




    if hardMode:
        entry = ''
        while entry.upper() != ENTRY_1.upper():
            slowWrite(scr, '>')
            entry = upperInput(scr)
    else:
        slowWrite(scr, '>')
        curses.napms(INPUT_PAUSE)
        slowWrite(scr, ENTRY_1 + '\n', TYPE_DELAY)

    slowWrite(scr, '\n' + MESSAGE_2 + '\n\n')

    if hardMode:
        entry = ''
        while entry.upper() != ENTRY_2.upper():
            slowWrite(scr, '>')
            entry = upperInput(scr)
        while entry.upper() != ENTRY_3.upper():
            slowWrite(scr, '>')
            entry = upperInput(scr)
    else:
        slowWrite(scr, '>')
        curses.napms(INPUT_PAUSE)
        slowWrite(scr, ENTRY_2 + '\n', TYPE_DELAY)
        slowWrite(scr, '>')
        curses.napms(INPUT_PAUSE)
        slowWrite(scr, ENTRY_3 + '\n', TYPE_DELAY)

    slowWrite(scr, '\n' + MESSAGE_3 + '\n\n')

    if hardMode:
        entry = ''
        while entry.upper() != ENTRY_4.upper():
            slowWrite(scr, '>')
            entry = upperInput(scr)
    else:
        slowWrite(scr, '>')
        curses.napms(INPUT_PAUSE)
        slowWrite(scr, ENTRY_4 + '\n', TYPE_DELAY)

    curses.napms(INPUT_PAUSE)
    return True

def beginBoot(hardMode):

    res = curses.wrapper(runBoot, hardMode)
    return res










HEADER_TEXT = 'WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK'

PASSWORD_PROMPT = 'PASSWORD REQUIRED'

PASSWORD_ERROR = 'INCORRECT PASSWORD, PLEASE TRY AGAIN'


ENTRY = 'LOGON '


def runLogin(scr, hardMode, username, password):

    curses.use_default_colors()
    scr.erase()
    scr.move(0, 0)

    curses.noecho()
    scr.scrollok(True)

    slowWrite(scr, HEADER_TEXT + '\n\n')

    if hardMode:
        entry = ''
        while entry.upper() != ENTRY.upper() + username.upper():
            slowWrite(scr, '> ')
            entry = upperInput(scr)
    else:
        slowWrite(scr, '> ')
        curses.napms(INPUT_PAUSE)
        slowWrite(scr, ENTRY + username.upper() + '\n', TYPE_DELAY)

    slowWrite(scr, '\n' + PASSWORD_PROMPT + '\n\n')

    if hardMode:
        entry = ''
        while entry.upper() != password.upper():
            if entry:
                slowWrite(scr, PASSWORD_ERROR + '\n\n')

            slowWrite(scr, '> ')
            entry = upperInput(scr, True)
    else:
        slowWrite(scr, '> ')
        curses.napms(INPUT_PAUSE)
        password_stars = HIDDEN_MASK * len(password)
        slowWrite(scr, password_stars + '\n', TYPE_DELAY)

    curses.napms(500)


def beginLoginMode(hardMode, username, password):

    res = curses.wrapper(runLogin, hardMode, username, password)
    return res



LETTER_PAUSE = 3

INPUT_PAUSE = 50 # ms

TYPE_DELAY = 40

HIDDEN_MASK = '*'

NEWLINE = 10

DELETE = 127

def slowWrite(window, text, pause = LETTER_PAUSE):

    mixer.init()
    mixer.music.load(os.path.join(__location__,"audio/beep.wav"))
    mixer.music.play()



    for i in range(len(text)):

        window.addstr(text[i])
        window.refresh()
        curses.napms(pause)

''


def upperInput(window, hidden = False, can_newline = True):

    inchar = 0
    instr = ''
    curses.noecho()

    while inchar != NEWLINE:
        inchar = window.getch()
        if inchar > 96 and inchar < 123:
            inchar -= 32
        if inchar == curses.KEY_BACKSPACE:
            if len(instr) > 0:
                instr = instr[:-1]
                cur = window.getyx()
                window.move(cur[0], cur[1] - 1)
                window.clrtobot()
            else:
                continue
        elif inchar > 255:
            continue
        elif inchar != NEWLINE:
            instr += chr(inchar)
            if hidden:
                window.addch(HIDDEN_MASK)
            else:
                window.addch(inchar)
        elif can_newline:
            window.addch(NEWLINE)
    return instr

def centeredWrite(window, text, pause = LETTER_PAUSE):

    width = window.getmaxyx()[1]
    window.move(window.getyx()[0], int(width / 2 - len(text) / 2))
    slowWrite(window, text, pause)




try:
        ##### init
    hard = False
    if len(sys.argv) == 2 and sys.argv[1].lower() == 'hard':
         hard = False
    if beginBoot(hard):
         pwd = beginLogin()
         if pwd != None:
             beginLoginMode(hard, 'ADMIN', pwd)
             print(beginSelection())
         else:
             beginLocked()
             print('Login failed')
except KeyboardInterrupt:

    beginSecurityLock()
