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
                               ,,, {1} Version : 2.0.0
        
        """.format(Fore.GREEN , Fore.WHITE)
        print(f"{ASCII}\n")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}+{Fore.MAGENTA}] {Fore.WHITE}Windows Medicator Created By shervinbdndev\n\n\n")
        print(f"\t{Fore.GREEN}[ Safe Zone ]")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}1{Fore.MAGENTA}] {Fore.CYAN}(FIX) {Fore.WHITE}Check System's Health")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}2{Fore.MAGENTA}] {Fore.CYAN}(FIX) {Fore.WHITE}Scan System's Health")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}3{Fore.MAGENTA}] {Fore.CYAN}(FIX) {Fore.WHITE}Restore System's Health")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}4{Fore.MAGENTA}] {Fore.CYAN}(FIX) {Fore.WHITE}Repair install.esd Image")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}5{Fore.MAGENTA}] {Fore.CYAN}(FIX) {Fore.WHITE}Repair windows Installation Image")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}6{Fore.MAGENTA}] {Fore.CYAN}(FIX) {Fore.WHITE}Check System's Disks")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}7{Fore.MAGENTA}] {Fore.CYAN}(FIX) {Fore.WHITE}Internet Connection Problem\n\n")
        print(f"\t{Fore.RED}[ Danger Zone ]")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}8{Fore.MAGENTA}] {Fore.YELLOW}(DANGER) {Fore.WHITE}Uninstall & Delete All Windows Builtins Apps")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}9{Fore.MAGENTA}] {Fore.RED}(DANGER) {Fore.WHITE}Reset Factory PC\n\n")
        print(f"{Fore.MAGENTA}[{Fore.GREEN}99{Fore.MAGENTA}] {Fore.WHITE}Exit")