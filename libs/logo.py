from colorama import Fore, Back, Style, init
from random import choice


init(convert=True)

logo = f"""
    

{Fore.LIGHTCYAN_EX} ██╗███╗   ███╗██████╗    
{Fore.LIGHTWHITE_EX}██║████╗ ████║██╔══██╗    
{Fore.LIGHTRED_EX}  ██║██╔████╔██║██████╔╝    
{Fore.LIGHTCYAN_EX} ██║██║╚██╔╝██║██╔══██╗   
{Fore.LIGHTWHITE_EX}██║██║ ╚═╝ ██║██║  ██║      
{Fore.LIGHTRED_EX}  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝        
                                                                                           
                                                     
                                                                                                              
                                                                                                                                                                         


      """



def print_logo():
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.LIGHTYELLOW_EX + "                                   Developer: Martizio"+ Style.RESET_ALL + Style.BRIGHT)
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)
