""" Admin Privileges Class """
from AdminPrivileges import (RunProgramAsAdmin , ScriptHeaders)

""" Base Libraries """
import os
import sys
import ctypes
import subprocess
from colorama.ansi import Fore
from colorama.initialise import init
from requests.exceptions import ConnectionError

        
        
init(autoreset=False , convert=True , strip=None)



        

""" Main Script """
class MainScript(RunProgramAsAdmin , ScriptHeaders):
    if (RunProgramAsAdmin.IsAdmin()):
        while True:
            ScriptHeaders.ShowHeaders()
            userInput : str = str(input("\n[~] Choose an Operation : "))
            if (userInput == "1"):
                print(f"\n{Fore.GREEN}Starting Scan . . .\n")
                print(f"{Fore.YELLOW}Do Not Turn off Your PC While Running The Application !{Fore.WHITE}")
                try:
                    subprocess.call(args=['DISM' , '/Online' , '/Cleanup-Image' , '/CheckHealth'])
                    print(f"\n{Fore.GREEN}Finished Scanning .{Fore.WHITE}\n")
                    sUserInput : str = str(input("[~] Would You Like To Continue Scanning?(y/n) "))
                    if (sUserInput.startswith('y')):
                        os.system(command='cls')
                        continue
                    elif (sUserInput.startswith('n')):
                        break
                except KeyboardInterrupt as KI:
                    raise f"Operation Canceled {KI}"
                continue
            elif (userInput == "2"):
                print(f"\n{Fore.GREEN}Starting Scan . . .\n")
                print(f"{Fore.YELLOW}Do Not Turn off Your PC While Running The Application !{Fore.WHITE}")
                try:
                    subprocess.call(args=['DISM' , '/Online' , '/Cleanup-Image' , '/ScanHealth'])
                    print(f"\n{Fore.GREEN}Finished Scanning .{Fore.WHITE}\n")
                    sUserInput : str = str(input("[~] Would You Like To Continue Scanning?(y/n) "))
                    if (sUserInput.startswith('y')):
                        os.system(command='cls')
                        continue
                    elif (sUserInput.startswith('n')):
                        break
                except KeyboardInterrupt as KI:
                    raise f"Operation Canceled {KI}"
                continue
            elif (userInput == "3"):
                print(f"\n{Fore.GREEN}Starting Scan . . .\n")
                print(f"{Fore.YELLOW}Do Not Turn off Your PC While Running The Application !{Fore.WHITE}")
                try:
                    subprocess.call(args=['DISM' , '/Online' , '/Cleanup-Image' , '/RestoreHealth' , '/Source:repairSource\install.wim'])
                    print(f"\n{Fore.GREEN}Finished Scanning .{Fore.WHITE}\n")
                    sUserInput : str = str(input("[~] Would You Like To Continue Scanning?(y/n) "))
                    if (sUserInput.startswith('y')):
                        os.system(command='cls')
                        continue
                    elif (sUserInput.startswith('n')):
                        break
                except KeyboardInterrupt as KI:
                    raise f"Operation Canceled {KI}"
                continue
            elif (userInput == "4"):
                print(f"\n{Fore.GREEN}Starting Scan . . .\n")
                print(f"{Fore.YELLOW}Do Not Turn off Your PC While Running The Application !{Fore.WHITE}")
                try:
                    subprocess.call(args=['DISM' , '/Online' , '/Cleanup-Image' , '/RestoreHealth' , '/Source:C:\ESD\Windows\sources\install.esd'])
                    print(f"\n{Fore.GREEN}Finished Scanning .{Fore.WHITE}\n")
                    sUserInput : str = str(input("[~] Would You Like To Continue Scanning?(y/n) "))
                    if (sUserInput.startswith('y')):
                        os.system(command='cls')
                        continue
                    elif (sUserInput.startswith('n')):
                        break
                except KeyboardInterrupt as KI:
                    raise f"Operation Canceled {KI}"
                continue
            elif (userInput == "5"):
                print(f"\n{Fore.GREEN}Starting Scan . . .\n")
                print(f"{Fore.YELLOW}Do Not Turn off Your PC While Running The Application !{Fore.WHITE}")
                try:
                    subprocess.call(args=['SFC' , '/scannow'])
                    print(f"\n{Fore.GREEN}Finished Scanning .{Fore.WHITE}\n")
                    sUserInput : str = str(input("[~] Would You Like To Continue Scanning?(y/n) "))
                    if (sUserInput.startswith('y')):
                        os.system(command='cls')
                        continue
                    elif (sUserInput.startswith('n')):
                        break
                except KeyboardInterrupt as KI:
                    raise f"Operation Canceled {KI}"
                continue
            elif (userInput == "6"):
                print(f"\n{Fore.GREEN}Starting Scan . . .\n")
                print(f"{Fore.YELLOW}Do Not Turn off Your PC While Running The Application !{Fore.WHITE}")
                try:
                    subprocess.call(args=['chkdsk'])
                    print(f"\n{Fore.GREEN}Finished Scanning .{Fore.WHITE}\n")
                    sUserInput : str = str(input("[~] Would You Like To Continue Scanning?(y/n) "))
                    if (sUserInput.startswith('y')):
                        os.system(command='cls')
                        continue
                    elif (sUserInput.startswith('n')):
                        break
                except KeyboardInterrupt as KI:
                    raise f"Operation Canceled {KI}"
                continue
            elif (userInput == "7"):
                print(f"\n{Fore.GREEN}Removing Previouse IP Settings . . .\n")
                print(f"{Fore.YELLOW}Do Not Turn off Your PC While Running The Application !{Fore.WHITE}")
                try:
                    subprocess.call(args=['ipconfig' , '/release'])
                    print(f"\n{Fore.GREEN}Setting New Local IP Settings . . .{Fore.WHITE}\n")
                    subprocess.call(args=['ipconfig' , '/renew'])
                    print(f"{Fore.GREEN}Scan Finished.{Fore.WHITE}")
                    sUserInput : str = str(input("[~] Would You Like To Continue Scanning?(y/n) "))
                    if (sUserInput.startswith('y')):
                        os.system(command='cls')
                        continue
                    elif (sUserInput.startswith('n')):
                        break
                except KeyboardInterrupt as KI:
                    raise f"Operation Canceled {KI}"
                continue
            elif (userInput == "8"):
                print(f"\n{Fore.GREEN}Downloading Requirements . . .\n")
                print(f"{Fore.YELLOW}Do Not Turn off Your PC While Running The Application !{Fore.WHITE}")
                try:
                    subprocess.call(args=['DISM' , '/online' , '/enable-feature' , '/featurename:VirtualMachinePlatform' , '/all' , '/norestart'])
                    subprocess.call(args=['DISM' , '/online' , '/enable-feature' , '/featurename:Microsoft-Windows-Subsystem-Linux' , '/all' , '/norestart'])
                    print(f"{Fore.GREEN}All Linux Features Enabled Successfully")
                    sUserInput : str = str(input("[~] Would You Like To Continue Scanning?(y/n) "))
                    if (sUserInput.startswith('y')):
                        os.system(command='cls')
                        continue
                    elif (sUserInput.startswith('n')):
                        break
                except [ConnectionError , KeyboardInterrupt] as CEKI:
                    raise f"Internet Connection Error Or Operation Canceled By User {CEKI}"
                continue
            elif (userInput == "9"):
                nUserInput : str = str(input("[~] This Option Will Uninstall All of Your Builtins apps , Would You Like to Uninstall All of Your Builtins Apps?(y/n) "))
                if (nUserInput.startswith('y')):
                    print(f"\n{Fore.GREEN}Uninstalling Builtins Applications . . .\n")
                    print(f"{Fore.YELLOW}Do Not Turn off Your PC While Running The Application !{Fore.WHITE}")
                    try:
                        subprocess.call(args=['Get-AppxPackage' , '|' , 'Remove-AppxPackage'])
                        print(f"{Fore.GREEN}All Builtins Applications Uninstalled Successfully.{Fore.WHITE}")
                        sUserInput : str = str(input("[~] Would You Like To Continue Scanning?(y/n) "))
                        if (sUserInput.startswith('y')):
                            os.system(command='cls')
                            continue
                        elif (sUserInput.startswith('n')):
                            break
                    except KeyboardInterrupt as KI:
                        raise f"Operation Canceled By User {KI}"
                    continue
            elif (userInput == "10"):
                nUserInput : str = str(input("[~] This Option Will Reset Factory Your Windows , Would You Like to Continue?(y/n) "))
                if (nUserInput.startswith('y')):
                    print(f"\n{Fore.GREEN}Reseting system . . .\n")
                    print(f"{Fore.YELLOW}Do Not Turn off Your PC While Running The Application !{Fore.WHITE}")
                    subprocess.call(args=['systemreset' , '--resetfactory'])
                    print(f"{Fore.GREEN}All Done.{Fore.WHITE}")
                    continue
            elif (userInput in ["00" , "exit"]):
                break
            else:
                os.system(command='cls')
                print(f"{Fore.RED}[!] Command is not Defined")
                continue
            continue
    else:
        ctypes.windll.shell32.ShellExecuteW(None , 'runas' , sys.executable , " ".join(sys.argv) , None , 1)