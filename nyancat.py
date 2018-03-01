#A tool by Shallman and SuperSaiyanNappa, the spiciest meme lords ;)

# importz
import subprocess
import os
import shlex

#Displays the flippin sweet ascii art
def banner():
    print("####################################################################################################")
    print("####################################################################################################")
    print("                                                                                                    ")
    print("                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM~                        ")
    print("                     ???I77777777777777777777777777777777777777777777777777+??                      ")
    print("                  MMM:~~~~~~~~:::::::::::::::::::::::::::::::::::::::~~~~~~~~~MMM                   ")
    print("                  MMM:~~~~~~~~:::::::::::::::::::::::::::::::::::::::~~~~~~~~~MMM                   ")
    print("                  MMM:~~~~~::::::::::::::::::??I::::::I??:::::::::::::::~~~~~~MMM                   ")
    print("                  MMM:~~~~~::::::::::::::::::??I::::::I??:::::::::::::::~~~~~~MMM                   ")
    print("                  MMM:~~::::::???::::::::::::::::::::::::::::::::::::::::::~~~MMM                   ")
    print("                  MMM:~~::::::???::::::::::::::::::::::::::::::::::::::::::~~~MMM                   ")
    print("                  MMM:~~:::::::::::::::::::::::::::::::::8MMMMM:::???::::::~~~MMM      MMMMMM       ")
    print("                  MMM:~~:::::::::::::::::::::::::::::::::8MMMMM:::???::::::~~~MMM      MMMMMM       ")
    print("                  MMM:~~::::::::::::::::::::::::::::::MMMI?????MMM~::::::::~~~MMM   MMM+?????MMM    ")
    print("                  MMM:~~::::::::::::::::::::::::::::::MMMI?????OZZI??::::::~~~MMM===OZZ+?????MMM    ")
    print("                  MMM:~~::::::::::::::::::???:::::::::MMMI????????NMM::::::~~~MMMMMM+????????MMM    ")
    print("                  MMM:~~::::::::::::::::::???:::::::::MMMI????????ZZZI?????IIIMMMZZZ+????????MMM    ")
    print("   MMMMMM         MMM:~~::::::::::::::::::::::::::::::MMMI???????????MMMMMMMMMMMM????????????MMM    ")
    print("   MMMMMM:        MMM:~~::::::::::~~,:::::::::::::::::MMMI???????????MMMMMMMMMMMM????????????MMM    ")
    print("MMM??????MMM      MMM:~~:::::::::=??::::::::::::::::::MMMI???????????????????????????????????MMM    ")
    print("MMM??????MMM      MMM:~~:::::::::=??:::::::::::::::~~~NNNI???????????????????????????????????888:   ")
    print("MMM??????MMMMMMMMMMMM:~~:::::::::::::::::::::???:::MMM??????????????????????????????????????????MMM ")
    print("MMM++????MNNNNNNNNMMM:~~:::::::::::::::::::::???:::MMM+????????...MMM???????????????...MMM??????MMM ")
    print("  :MMM????????????MMM:~~:::???:::::::::::::::::::::MMM?????????...MMM??????????????? ..MMM??????MMM ")
    print("   MMM????????????MMM:~~:::I?I:::::::::::::::::::::MMM?????????NMMMMM?????????MMM???NMMMMM??????MMM ")
    print("     :MMMMMM??????MMM:~~:::::::::::::::::::::::::::MMM+????????MMMMMM?????????MMM???MMMMMM??????MMM ")
    print("      MMMMMM??????MMM:~~:::::::::::::::?II:::::::::MMM+??======???????????????????????????======MMM ")
    print("           :MMMMMMMMM:~~:::::::::::::::???:::::::::MMM???======???????????????????????????======MMM ")
    print("                 :MMM:~~::::::??I~:::::::::::::::::MMM???======???ZMM??????MMM??????MMM???======MMM ")
    print("                  MMM:~~~~~:::???~:::::::::::::::::MMM???======???ZMM??????MMM??????MMM???======MMM ")
    print("                  MMM:~~~~~::::::::::::::::::::::::~~~NMM?????????ZMMMMMMMMMMMMMMMMMMMM??????MMM`   ")
    print("                  MMM~~~~~~~~~::::::::::::::::::::::::MMM?????????ZMMMMMMMMMMMMMMMMMMMM??????MMM    ")
    print("                  MMMMMM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MMM??????????????????????????????MMM`      ")
    print("                 :MMMMMM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MMM??????????????????????????????MMM       ")
    print("               MMM??????MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM          ")
    print("               MMM??????MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM          ")
    print("               MMM??????MMM   MMM??????MMM                  MMZ??????MMM   MMM??????MMM`            ")
    print("               MMM??????MMM   MMM??????MMM                  MMZ??????MMM   MMM??????MMM             ")
    print("               MMMMMMMMM:       ~MMMMMMMMM                    ~MMMMMMMMM     :MMMMMMMMM             ")
    print("               MMMMMMMMM         MMMMMMMMM                     MMMMMMMMM      MMMMMMMMM             ")
    print("                                                                                                    ")
    print("####################################################################################################")
    print("####################################################################################################")
    print("##    _   _       _    __   __                    _               _   _      _    ____      _     ##")
    print("##   | \ | | ___ | |_  \ \ / /__  _   _ _ __     / \__   ____ _  | \ | | ___| |_ / ___|__ _| |_   ##")
    print("##   |  \| |/ _ \| __|  \ V / _ \| | | | '__|   / _ \ \ / / _` | |  \| |/ _ \ __| |   / _` | __|  ##")
    print("##   | |\  | (_) | |_    | | (_) | |_| | |     / ___ \ V / (_| | | |\  |  __/ |_| |__| (_| | |_   ##")
    print("##   |_| \_|\___/ \__|   |_|\___/ \__,_|_|    /_/   \_\_/ \__, | |_| \_|\___|\__|\____\__,_|\__|  ##")
    print("##                                                        |___/                                   ##")
    print("####################################################################################################")
    print("####################################################################################################")
    mainMenu()

'''
def getOs():
    myOs = str(platform.system())
'''

#Raw input for netcat
def raw(paramz):
    #parparz = str(paramz)
    #print(parparz[:-2])
    pop = subprocess.Popen("nc.exe", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print(pop.communicate(paramz[:-2]))
    #FNULL = open(os.devnull, 'w')
    #subprocess.call(paramz, nc.exe)
    mainMenu()

#CONNECT to machine at supplied ip:port
def connect(paramz):
    pop = subprocess.Popen("nc.exe", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print(pop.communicate("-nv " + paramz[:-2]))
    #literally just append -nv ahead of params it takes
    mainMenu()

#LISTEN - establishes a listener on specified port
def listen(paramz):
    pop = subprocess.Popen("nc.exe", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #print(pop.communicate("-nlvp " + paramz[:-2]))
    #literally just append -nlvp ahead of params it takes
    mainMenu()

#The Main Function. Add this fuction to the end of each Command Method to call back the main menu.
def mainMenu():
    while 1:
        try:
            selection = str(input(">"))

            if selection == "BANNER" or selection == "B" or selection == "SHOW ME THAT SICK ART AGAIN":
                banner()
                break
            elif selection == "HELP" or selection == "H":
                helpPlz()
                break
            elif selection == "QUIT" or selection == "EXIT" or selection == "Q":
                break
            elif selection.startswith('RAW'):
                strParams = selection[3:]
                raw(strParams)
                break
            elif selection.startswith('CONNECT'):
                strParams = selection[7:]
                connect(strParams)
                break
            elif selection.startswith('LISTEN'):
                strParams = selection[6:]
                listen(strParams)
                break
            else:
                print("Invalid argument \"" + selection + "\" Type HELP for usage options")
                mainMenu()
        except ValueError:
            print("Invalid argument. Type HELP for usage options")
    exit

#Display the help menu
def helpPlz():
    print("")
    print("Commands List")
    print("=============")
    print("")
    print("BANNER: Display the flippin sweet ascii art")
    print("EXIT: Exit NyanCat")
    print("HELP: display the help menu")
    mainMenu()


#Start the program with the banner and enter the mainMenu loop
banner()


'''
ArgsParseCode
=======

##argparse code##

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("banner", action="store_true", help="display the flippin sweet ascii art")
#parser.add_argument("argName", action="store_true"IFOPTIONAL, help="help text for flag")
args = parser.parse_args()

## DEFINE LOGIC FOR FLAGS BELOW THEIR RESPECTIVE METHOD DECLARATIONS
if args.banner:
    banner()
'''
