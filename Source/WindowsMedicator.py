""" Admin Privileges Class """
from AdminPrivileges import (RunProgramAsAdmin , ScriptHeaders)

""" Base Libraries """
import sys
import ctypes
import subprocess
from colorama.ansi import Fore
from colorama.initialise import init

        
        
init(autoreset=False , convert=True , strip=None)



        

""" Main Script """
class MainScript(RunProgramAsAdmin , ScriptHeaders):
    if (RunProgramAsAdmin.IsAdmin()):
        while True:
            ScriptHeaders.ShowHeaders()
            userInput : str = str(input("\n[~] Choose an Operation : "))
            if (userInput.startswith("1")):
                print(f"\n{Fore.GREEN}Starting Scan . . .\n")
                print(f"{Fore.YELLOW}Do Not Turn of Your PC While Scanning !{Fore.WHITE}")
                subprocess.call(args=['DISM' , '/Online' , '/Cleanup-Image' , '/CheckHealth'])
                print(f"\n{Fore.GREEN}Finished Scanning .{Fore.WHITE}\n")
                sUserInput : str = str(input("[~] Would You Like To Continue Scanning?(y/n) "))
                if (sUserInput.startswith('y')):
                    continue
                elif (sUserInput.startswith('n')):
                    break
            elif (userInput.startswith("2")):
                print(f"\n{Fore.GREEN}Starting Scan . . .\n")
                print(f"{Fore.YELLOW}Do Not Turn of Your PC While Scanning !{Fore.WHITE}")
                subprocess.call(args=['DISM' , '/Online' , '/Cleanup-Image' , '/ScanHealth'])
                print(f"\n{Fore.GREEN}Finished Scanning .{Fore.WHITE}\n")
                sUserInput : str = str(input("[~] Would You Like To Continue Scanning?(y/n) "))
                if (sUserInput.startswith('y')):
                    continue
                elif (sUserInput.startswith('n')):
                    break
            elif (userInput.startswith("3")):
                print(f"\n{Fore.GREEN}Starting Scan . . .\n")
                print(f"{Fore.YELLOW}Do Not Turn of Your PC While Scanning !{Fore.WHITE}")
                subprocess.call(args=['DISM' , '/Online' , '/Cleanup-Image' , '/RestoreHealth' , '/Source:repairSource\install.wim'])
                print(f"\n{Fore.GREEN}Finished Scanning .{Fore.WHITE}\n")
                sUserInput : str = str(input("[~] Would You Like To Continue Scanning?(y/n) "))
                if (sUserInput.startswith('y')):
                    continue
                elif (sUserInput.startswith('n')):
                    break
            elif (userInput.startswith("4")):
                print(f"\n{Fore.GREEN}Starting Scan . . .\n")
                print(f"{Fore.YELLOW}Do Not Turn of Your PC While Scanning !{Fore.WHITE}")
                subprocess.call(args=['DISM' , '/Online' , '/Cleanup-Image' , '/RestoreHealth' , '/Source:C:\ESD\Windows\sources\install.esd'])
                print(f"\n{Fore.GREEN}Finished Scanning .{Fore.WHITE}\n")
                sUserInput : str = str(input("[~] Would You Like To Continue Scanning?(y/n) "))
                if (sUserInput.startswith('y')):
                    continue
                elif (sUserInput.startswith('n')):
                    break
            elif (userInput.startswith("5")):
                print(f"\n{Fore.GREEN}Starting Scan . . .\n")
                print(f"{Fore.YELLOW}Do Not Turn of Your PC While Scanning !{Fore.WHITE}")
                subprocess.call(args=['SFC' , '/scannow'])
                print(f"\n{Fore.GREEN}Finished Scanning .{Fore.WHITE}\n")
                sUserInput : str = str(input("[~] Would You Like To Continue Scanning?(y/n) "))
                if (sUserInput.startswith('y')):
                    continue
                elif (sUserInput.startswith('n')):
                    break
            elif (userInput.startswith("6")):
                print(f"\n{Fore.GREEN}Starting Scan . . .\n")
                print(f"{Fore.YELLOW}Do Not Turn of Your PC While Scanning !{Fore.WHITE}")
                subprocess.call(args=['chkdsk'])
                print(f"\n{Fore.GREEN}Finished Scanning .{Fore.WHITE}\n")
                sUserInput : str = str(input("[~] Would You Like To Continue Scanning?(y/n) "))
                if (sUserInput.startswith('y')):
                    continue
                elif (sUserInput.startswith('n')):
                    break
            elif (userInput.startswith("7")):
                print(f"\n{Fore.GREEN}Removing Previouse IP Settings . . .\n")
                print(f"{Fore.YELLOW}Do Not Turn of Your PC While Scanning !{Fore.WHITE}")
                subprocess.call(args=['ipconfig' , '/release'])
                print(f"\n{Fore.GREEN}Setting New Local IP Settings . . .{Fore.WHITE}\n")
                subprocess.call(args=['ipconfig' , '/renew'])
                print(f"{Fore.GREEN}Scan Finished.{Fore.WHITE}")
                sUserInput : str = str(input("[~] Would You Like To Continue Scanning?(y/n) "))
                if (sUserInput.startswith('y')):
                    continue
                elif (sUserInput.startswith('n')):
                    break
            elif (userInput in ['exit' , '8']):
                break
            else:
                print(f"{Fore.RED}[!] Command is not Defined")
                continue
            continue
    else:
        ctypes.windll.shell32.ShellExecuteW(None , 'runas' , sys.executable , " ".join(sys.argv) , None , 1)