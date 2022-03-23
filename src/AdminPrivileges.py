import os
import ctypes
import platform
from colorama.ansi import Fore





""" This Class Needs Access to System For Scanning Your System's Health """
class RunProgramAsAdmin:
    def IsAdmin():
        if (platform.system()[0].upper() in ["W"]):
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False
            
            


class ScriptHeaders:
    def ShowHeaders():
        os.system(command="mode 72,45")
        ASCII = """{0}
              /////////////.         ,/////////////      
          ///////////////////    .///////////////////   
        /////////////////////// /////////////////////// 
        /////////////////////////////////////////////////
        ///////////////////   ////////////////////////////
        //////////////////     //////. ///////////////////
        /////////////////     ,////    ./////////////////
        ////////////////       ///      ,///////////////.
        ./////////////    ,    /    ,                   
                        ,,,       ,,,                  
            ,,,,,,,,,,,,,,,      ,,,,,,,,,,,,,,,.      
                ,,,,,,,,,,,,,    ,,,,,,,,,,,,,,         
                    ,,,,,,,,,,,  ,,,,,,,,,,,,            
                    ,,,,,,,,,,,,,,,,,,,,,              
                        ,,,,,,,,,,,,,,,                 
                            ,,,,,,,,,,                    
                              ,,,,,
                               ,,, {1} Version : 3.0.0
        
        """.format(Fore.GREEN , Fore.WHITE)
        print(f"{ASCII}\n")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}+{Fore.MAGENTA}] {Fore.WHITE}Windows Medicator Created By shervinbdndev\n\n\n")
        print(f"\t{Fore.GREEN}[ Safe Zone ]")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}1{Fore.MAGENTA}] {Fore.CYAN}(FIX)-(INTERNET_NEEDED) {Fore.WHITE}Check System's Health")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}2{Fore.MAGENTA}] {Fore.CYAN}(FIX)-(INTERNET_NEEDED) {Fore.WHITE}Scan System's Health")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}3{Fore.MAGENTA}] {Fore.CYAN}(FIX)-(INTERNET_NEEDED) {Fore.WHITE}Restore System's Health")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}4{Fore.MAGENTA}] {Fore.CYAN}(FIX)-(INTERNET_NEEDED) {Fore.WHITE}Repair install.esd Image")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}5{Fore.MAGENTA}] {Fore.CYAN}(FIX)-(INTERNET_NEEDED) {Fore.WHITE}Repair windows Installation Image")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}6{Fore.MAGENTA}] {Fore.CYAN}(FIX)-(INTERNET_NEEDED) {Fore.WHITE}Check System's Disks")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}7{Fore.MAGENTA}] {Fore.CYAN}(FIX)-(INTERNET_NEEDED) {Fore.WHITE}Internet Connection Problem")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}8{Fore.MAGENTA}] {Fore.CYAN}(FIX)-(INTERNET_NEEDED) {Fore.WHITE}Enable Linux Features On Windows\n\n")
        print(f"\t{Fore.RED}[ Danger Zone ]")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}9{Fore.MAGENTA}] {Fore.YELLOW}(DANGER) {Fore.WHITE}Uninstall & Delete All Windows Builtins Apps")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}10{Fore.MAGENTA}] {Fore.RED}(DANGER) {Fore.WHITE}Reset Factory PC\n\n")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}00{Fore.MAGENTA}] {Fore.WHITE}Exit")