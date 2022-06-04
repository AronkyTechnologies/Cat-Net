#Created by IsTk0
#this is a pre-release version
#probaly this code have some glitch
from xmlrpc import server
import colorama
from colorama import Fore, Back, Style
import sys, os

print(Fore.RED + "Warning: ↓\n" + Fore.WHITE)

def windows_administrator():
    import win32gui, win32con
    import pyuac
    from pyuac import main_requires_admin
    import ctypes, sys, platform

    if not pyuac.isUserAdmin():
        hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hide, win32con.SW_HIDE)
        print("Non chiudere questa finestra!")
        pyuac.runAsAdmin()

def macOS_administrator():
    os.system("""osascript -e 'do shell script "sudo python3 "CAT NET V2.0.0 - BETA.py"" " with administrator privileges'""") #fix

def linux_administrator():
    os.system("""osascript -e 'do shell script "sudo python3 "CAT NET V2.0.0 - BETA.py"" " with administrator privileges'""") #fix

sistema_operativo = sys.platform

if sistema_operativo == "win32":
    windows_administrator()

if sistema_operativo == "darwin":
    macOS_administrator()

if sistema_operativo == "linux":
    linux_administrator()

import paramiko, time, os, sys, subprocess
from ping3 import ping, verbose_ping
import scapy.all as scapy
import argparse
import getpass 
import getpass as getpass
import ftplib
import socket
import platform
import psutil
	
print("\n")
print("              ╘▀,, ╚▀,  ▀▌,")
print("                █▌   █▌  j█┐")
print("              ▐█'  ██'  █▌'           ▐█        █▌")
print("             █▌  j█┐  ╞█             ██▓█▌▄▄▄▄▐█▓╣█▄▄▄▄▄▄▄▄")
print("             ╙▐█  ╙Æ█ └╙█▌         Æ█╬╬▓▓╬╬╬╬╬╬▓▓▓▓╬╬╬╬╬╬╬╬███µ")
print("               ,   ,,           █████▓╬╬▓▓▓╬╬▓▓▓╬╬▓▓▓█████▓╬╬╬▓█")
print("             ▄██████████▄▄      ▄▄▄╢█▓╬█▓╣████╬▓██▓▓▓█████▓▓▓▓▓▓█▌")
print("             ████████████████   └▐█╬▓▓▓▓▓╬╬╬╬╬╬▓▓▓▓▓▓╬╬╬╬╬▓▓▓▓▓▓╬██─ ")
print("             █▌         ,,,  ▀▌, j█╬▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╣█┐")
print("             █▌       ╒╗█▌╙╥▄╗╪█ j█╬▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╣█┐")
print("             █▌       ╞╬█▌ ║█╬╫█ j█╬▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╣█┐")
print("             █▌   ,,,╬╬╬▀▀▀▒╬▄╙▀ ¬▀█╬▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬██▓╬█▀─")
print("             █▌φφφ╬╬╬╬╬╬█████╙`    ╙╙██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╣█╬╬╬╬╬▓╣█╙└")
print("              ╘█████████              ╘███████████████████████Γ")
print("\n")
print(Fore.WHITE + "   ╓▄▄▄▄▄▄▄   ┌▄▄▄▄▄▄▄─   ▄▄▄▄▄▄▄▄▄▄▄▄─   ▄▄▄      ╓▄▄─ ▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄▄─|"+ Fore.RED +" Created by IsTk0")
print(Fore.WHITE + " j█████████┐ ███████████ j████████████▌  j██████   ║██▌ ████████ j████████████▌|"+ Fore.GREEN +" Cat Net Source Code:")
print(Fore.WHITE + " j███        ███     ███      ╞██▌       j███▀██,, ║██▌ ███▄,,,,      ╞██▌     |"+ Fore.YELLOW +" https://github.com/AronkyTechnologies/Cat-Net")
print(Fore.WHITE + " j███        ███     ███      ╞██▌ ╔▄▄▄▄ j███ ╞██▌ ║██▌ ████████      ╞██▌     |"+ Fore.BLUE +" Version: 2.0.0 STABLE Version")
print(Fore.WHITE + " j███        ███████████      ╞██▌ ║████ j███ ╞██▌ ║██▌ ███┘''''      ╞██▌     |"+ Fore.MAGENTA +" Apache License")
print(Fore.WHITE + " j███▄▄▄▄▄▄  ███▀▀▀▀▀███      ╞██▌       j███   ██████▌ ███▄▄▄▄▄      ╞██▌     | ")
print(Fore.WHITE + "  ╙████████┐ ███     ███      ╞██▌       j███   ╙╙╙███▌ ████████      ╞██▌     | Cat-Net ti da il benvenuto ^.^")
print(Fore.WHITE + "Se hai bisogno di un aiuto scrivi help oppure controlla la repository di Cat-Net")


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    if iteration == total:
        print()


items = list(range(0, 57))
l = len(items)

# Qui c'è l'avanzamento ogni 0.1 secondi
printProgressBar(0, l, prefix='Caricamento:', suffix=Fore.RED + 'In corso..' + Fore.WHITE, length=50)
for i, item in enumerate(items):
    if (i == 56):
        time.sleep(0.1)
        printProgressBar(57, l, prefix='Caricamento:', suffix=Fore.GREEN + 'Completato!' + Fore.WHITE, length=50)
    elif (i <= 56):
        time.sleep(0.1)
        printProgressBar(i + 1, l, prefix='Caricamento:', suffix=Fore.RED + 'In corso..' + Fore.WHITE, length=50)

def ssh_code():
    #print("\n")
    server = input(Fore.WHITE + "Hostname macchina: --> "+ Fore.GREEN)
    username = input(Fore.WHITE + "Username macchina: --> " + Fore.GREEN)
    porta = input(Fore.WHITE + "Porta macchina: --> " + Fore.GREEN)
    password = getpass.getpass(Fore.WHITE + "Password macchina: --> ")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(server, porta, username, password, allow_agent=False, look_for_keys=False)
    print(Fore.GREEN + "Connessione avvenuta con successo" + Fore.WHITE)

    while True:
        risposta = []

        comando = input("Comando macchina: --> " + Fore.GREEN)
        print(Fore.WHITE)

        if comando == "exit":
            ssh.close()

        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(comando)

        for line in ssh_stdout:
            risposta.append(line.strip('\n'))
        for i in risposta:
            print(i.strip())


def ping_code():
    hostname = input("Indirizzo macchina: --> "+ Fore.GREEN)
    comando_ping = input(Fore.WHITE + "Opzione: "+ Fore.GREEN)
    print(Fore.WHITE)
    if comando_ping == "-P" or comando_ping == "-p":
        risposta = os.system("ping -c 1 " + hostname)
        delay = ping(hostname)
        if risposta == 0:
            print(hostname, Fore.GREEN + " ha risposto in: " + Fore.WHITE, "%.2g" % delay, " S")
        else:
            print(hostname, Fore.RED + " non ha risposto" + Fore.WHITE)
    elif comando_ping == "-Ver" or comando_ping == "-ver":
        verbose_ping(Fore.BLUE + hostname + Fore.WHITE)

def scan_network():
    def get_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--target", dest="target", help="Specifica l'IP o il range IP")
        options = parser.parse_args()
        return  options

    def scan(ip):
        arp_packet = scapy.ARP(pdst=ip)
        broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_broadcast_packet = broadcast_packet/arp_packet
        answered_list = scapy.srp(arp_broadcast_packet, timeout=1, verbose=False)[0]
        client_list = []

        for element in answered_list:
            client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
            client_list.append(client_dict)

        return client_list

    def print_result(scan_list):
        print("IP\t\t\tMAC\n----------------------------------------")
        for client in scan_list:
            print(client["ip"] + "\t\t" + client["mac"])

    options = get_arguments()
    result_list = scan(options.target)
    print_result(result_list)

def ftp_code():
    server = ftplib.FTP()
    ip_address_input = input(Fore.WHITE + "IP Macchina-> " + Fore.GREEN)
    port_input = input(Fore.WHITE + "Porta Macchina-> " + Fore.GREEN)
    username_machine_input = input(Fore.WHITE + "Username macchina: -> " + Fore.GREEN)
    password_machine_input = getpass.getpass(Fore.WHITE + "Password macchina ->")
    server.connect(ip_address_input, port_input)
    server.login(username_machine_input,password_machine_input)
    server.dir()

def whatip_code():
    server_url_input = input("Url Server-> " + Fore.GREEN)
    ip = socket.gethostbyname(server_url_input)
    print (Fore.BLUE + ip + Fore.WHITE)

def scanport_code():
    hostname = socket. gethostname()
    my_ip_addr_now = socket. gethostbyname(hostname)
    range_port = int(input("Range porte-> "))
    scelta_print = input("Vuoi vedere solo le porte aperte (Y/n)-> ")
    for port in range(1, range_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((my_ip_addr_now, port))
        if result == 0:
            print("Port " + str(port) + Fore.GREEN + " is open" + Fore.WHITE)
        if scelta_print == "n" or scelta_print == "N":
                print("Port " + str(port) + Fore.RED + " is closed" + Fore.WHITE)
        sock.close()

def info_now_code():
    hostname = socket. gethostname()
    my_ip_addr_now = socket. gethostbyname(hostname)
    os_type = platform.system()
    os_info_mor = platform.platform()
    os_version = platform.version()
    type_processor = platform.processor()
    processor_type = platform.machine()
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    ram_disp = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
    ram_disp = "{:.1f}".format(ram_disp)
    cpu_usage = str(cpu_usage)
    ram_usage = str(ram_usage)
    ram_disp = str(ram_disp)
    print(Fore.BLUE + "Hostname macchina" , Fore.GREEN + hostname)
    print(Fore.BLUE + "Indirizzo IP macchina" , Fore.GREEN +  my_ip_addr_now)
    print(Fore.BLUE + "Nome OS/Kernel: " , Fore.GREEN + os_type)
    print(Fore.BLUE + "Maggiori info sul sistema: " , Fore.GREEN +  os_info_mor)
    print(Fore.BLUE + "Versione OS: " ,  Fore.GREEN + os_version)
    print(Fore.BLUE + "Tipo di processore: " ,  Fore.GREEN + type_processor)
    print(Fore.BLUE + "Tipo di Architettura: " ,  Fore.GREEN + processor_type)
    print(Fore.WHITE + "------PC Component Stast------")
    print(Fore.BLUE + "Uso Cpu:" ,  Fore.GREEN + cpu_usage , "%")
    print(Fore.BLUE + "Uso Ram:" ,  Fore.GREEN + ram_usage , "%")
    print(Fore.BLUE + "Ram Disponibile: " , Fore.GREEN + ram_disp , "%")
    print(Fore.WHITE)

while True:
    comando = input("CAT-NET-> "+ Fore.BLUE)
    print(Fore.WHITE)

    if comando == "ssh":
        ssh_code()

    elif comando == "ping":
        ping_code()

    elif comando == "scan":
        scan_network()

    elif comando == "ftp":
        ftp_code()

    elif comando == "wtip":
        whatip_code()

    elif comando == "scanport":
        scanport_code()

    elif comando == "info":
        info_now_code()

    elif comando == "help":
        print(Fore.CYAN + "---------- TUTTI I COMANDI ----------" + Fore.WHITE)
        print(Fore.BLUE + "     1) ssh: " + Fore.WHITE)
        print("     Cosa fa? :")
        print("               Permette di usare dei comandi a riga (CLI) in modo remoto, cioè da un altra macchina diversa da quella che esegue il comando")
        print("     Parametri: ")
        print(Fore.YELLOW + "              Hostname: Il nome identificativo di un dispositivo all'interno di una rete")
        print("                        Es: computer@internet-provider.com")
        print("               Username: Il nome utente in informatica definisce il nome con il quale l'utente viene riconosciuto da un computer")
        print("                        Es: nome-utente-computer")
        print("               Password: Una password, in ambito informatico, una sequenza di caratteri alfanumerici e di simboli utilizzata per accedere in modo esclusivo a una risorsa informatica")
        print("                        Es: PasswordComputer")
        print("               Porta: Nell'ambito delle reti di computer le porte sono lo strumento utilizzato per realizzare la multiplazione delle connessioni a livello di trasporto di dati nella rete")
        print("                        Es: 22 (porta SSH base)" + Fore.WHITE)
        print(Fore.BLUE + "     2) ping: " + Fore.WHITE)
        print("     Cosa fa? :")
        print("               Permette di verificare se un altra macchina connessa in rete risponde a una richiesta tramite un paccetto, in più misura la latenza della risposta")
        print("     Parametri: ")
        print(Fore.YELLOW + "               Indirizzo macchina: Può essere sia un IP o un indirizzo web")
        print("                        Es: 192.168.1.1 / sito.com")
        print("               -P: Questo valore utilizza la libreria OS per il ping a macchine")
        print("                        Es: esempio-sito.esempio")
        print("               -Ver: Questo valore utilizza la libreria Verbose_Ping per il ping a macchine")
        print("                        Es: esempio-sito.esempio" + Fore.WHITE)
        print(Fore.BLUE + "     3) scan: " + Fore.WHITE)
        print("     Cosa fa? :")
        print("               Effetua una scansione della rete locale, e riportando tutti i dispositivi con cui è connesso la macchina che esegue Cat-Net")
        print("     Parametri: Nessuno")
        print(Fore.YELLOW + "              Lo scanning di rete aiuta a rilevare tutti gli host attivi su una rete e li associa ai loro indirizzi IP")
        print("                        Es: IP                   MAC")
        print("                            --------------------------------------")
        print("                            10.5.5.**            52:54:00:12:**:**" + Fore.WHITE)
        print(Fore.BLUE + "     4) ftp: " + Fore.WHITE)
        print("     Cosa fa? :")
        print("               Permette di trasferire file in remoto tra due macchine")
        print("     Parametri: ")
        print(Fore.YELLOW + "               Indirizzo macchina: Può essere sia un IP o un indirizzo web")
        print("                        Es: 192.168.1.1 / sito.com")
        print("               Porta: Porta alla quale cat-net si devve connettere per parlare")
        print("                        Es: 21")
        print("               Username/Password: Username e password dell'account con in quale si vuole condivire un file")
        print("                        Es: un: cat-net | pw: cat-net22" + Fore.WHITE)
        print(Fore.BLUE + "     5) wtip: " + Fore.WHITE)
        print("     Cosa fa? :")
        print("               Permette di scoprire l'indirizzo IP di un server tramite il suo url")
        print("     Parametri: ")
        print(Fore.YELLOW + "               Url Server: è una sequenza di caratteri che identifica univocamente l'indirizzo di una risorsa su una rete")
        print("                        Es: Url Server: aronky.dev oppure aronky.com" + Fore.WHITE)
        print(Fore.BLUE + "     6) scanport: " + Fore.WHITE)
        print("     Cosa fa? :")
        print("               Permette di scoprire quali porte del proprio computer siano aperte e quali no")
        print("     Parametri: ")
        print(Fore.YELLOW + "               Range port: inserendo un numero, Cat-Net scansionera ogni singola porta")
        print("                        Es: Range Port: 50 (scanning da 1 a 49)" + Fore.WHITE)
        print(Fore.BLUE + "     7) info: " + Fore.WHITE)
        print("     Cosa fa? :")
        print("               Mostra alcune statistiche di debug di un istante")
        print("     Parametri: Nessuno")
        print(Fore.YELLOW + "               Mostra: indirizzi ip, hostname, cpu usage etc.." )
        print("                        Es: 132.152.**.** | cat-net-machine | CPU: 32% etc.." + Fore.WHITE)
        

    elif comando == "quit":
        break

    else:
        print(Fore.RED + "Warning! Il comando che hai scritto non è stato riconosciuto dalla macchina o risulta inesistente, riprova." + Fore.WHITE)