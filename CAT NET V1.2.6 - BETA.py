#Created by IsTk0
#this is a pre-release version
#probaly this code have some glitch

import sys, os

#print("Warning: ↓\n")

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
    os.system("""osascript -e 'do shell script "sudo python3 "CAT NET V1.2.5 - BETA.py"" " with administrator privileges'""") #fix

def linux_administrator():
    os.system("""osascript -e 'do shell script "sudo python3 "CAT NET V1.2.5 - BETA.py"" " with administrator privileges'""") #fix

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
print("   ╓▄▄▄▄▄▄▄   ┌▄▄▄▄▄▄▄─   ▄▄▄▄▄▄▄▄▄▄▄▄─   ▄▄▄      ╓▄▄─ ▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄▄─| \033[31;40mCreated by IsTk0\033[0;37;40m")
print(" j█████████┐ ███████████ j████████████▌  j██████   ║██▌ ████████ j████████████▌| \033[32;40mCat Net Source Code:\033[0;37;40m")
print(" j███        ███     ███      ╞██▌       j███▀██,, ║██▌ ███▄,,,,      ╞██▌     | \033[33;40mhttps://github.com/IsTk0/Cat-Net\033[0;37;40m")
print(" j███        ███     ███      ╞██▌ ╔▄▄▄▄ j███ ╞██▌ ║██▌ ████████      ╞██▌     | \033[34;40mVersion: 1.2.5 BETA Version\033[0;37;40m")
print(" j███        ███████████      ╞██▌ ║████ j███ ╞██▌ ║██▌ ███┘''''      ╞██▌     | \033[35;40mApache License\033[0;37;40m")
print(" j███▄▄▄▄▄▄  ███▀▀▀▀▀███      ╞██▌       j███   ██████▌ ███▄▄▄▄▄      ╞██▌     | ")
print("  ╙████████┐ ███     ███      ╞██▌       j███   ╙╙╙███▌ ████████      ╞██▌     | Cat-Net ti da il benvenuto ^.^")
print("Se hai bisogno di un aiuto scrivi help oppure controlla la repository di Cat-Net")


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
printProgressBar(0, l, prefix='Caricamento:', suffix='\033[31;40mIn corso..\033[0;37;40m', length=50)
for i, item in enumerate(items):
    if (i == 56):
        time.sleep(0.1)
        printProgressBar(57, l, prefix='Caricamento:', suffix='\033[1;32;40mCompletato\033[0;37;40m', length=50)
    elif (i <= 56):
        time.sleep(0.1)
        printProgressBar(i + 1, l, prefix='Caricamento:', suffix='\033[31;40mIn corso..\033[0;37;40m', length=50)

def ssh_code():
    print("\n")
    server = input("Hostname macchina: --> ")
    username = input("Username macchina: --> ")
    password = input("Password macchina: --> ")
    porta = input("Porta macchina: --> ")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(server, porta, username, password, allow_agent=False, look_for_keys=False)
    print("Connessione avvenuta con successo")

    while True:
        risposta = []

        comando = input("Comando macchina: --> ")

        if comando == "exit":
            ssh.close()

        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(comando)

        for line in ssh_stdout:
            risposta.append(line.strip('\n'))
        for i in risposta:
            print(i.strip())


def ping_code():
    hostname = input("Indirizzo macchina: --> ")
    comando_ping = input("Opzione: ")
    if comando_ping == "-P" or comando_ping == "-p":
        risposta = os.system("ping -c 1 " + hostname)
        delay = ping(hostname)
        if risposta == 0:
            print(hostname, " ha risposto in: ", "%.2g" % delay, " S")
        else:
            print(hostname, " non ha risposto")
    elif comando_ping == "-Ver" or comando_ping == "-ver":
        verbose_ping(hostname)

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

while True:
    comando = input("CAT-NET-> ")

    if comando == "ssh":
        ssh_code()

    elif comando == "ping":
        ping_code()

    elif comando == "scan":
        scan_network()

    elif comando == "help":
        print("---------- TUTTI I COMANDI ----------")
        print("\033[33;40m     1) ssh: [0;37;40m")
        print("     Parametri: ")
        print("               Hostname: Il nome identificativo di un dispositivo all'interno di una rete")
        print("                        Es: computer@internet-provider.com")
        print("               Username: Il nome utente in informatica definisce il nome con il quale l'utente viene riconosciuto da un computer")
        print("                        Es: nome-utente-computer")
        print("               Password: Una password, in ambito informatico, una sequenza di caratteri alfanumerici e di simboli utilizzata per accedere in modo esclusivo a una risorsa informatica")
        print("                        Es: PasswordComputer")
        print("                  Porta: Nell'ambito delle reti di computer le porte sono lo strumento utilizzato per realizzare la multiplazione delle connessioni a livello di trasporto di dati nella rete")
        print("                        Es: 22 (porta SSH base)")
        print("     2) ping: ")
        print("     Parametri: ")
        print("               Indirizzo macchina: Può essere sia un IP o un indirizzo web")
        print("                        Es: 192.168.1.1 / sito.com")
        print("               -P: Questo valore utilizza la libreria OS per il ping a macchine")
        print("                        Es: esempio-sito.esempio")
        print("               -Ver: Questo valore utilizza la libreria Verbose_Ping per il ping a macchine")
        print("                        Es: esempio-sito.esempio")
        print("     2) scan: ")
        print("     Parametri: Nessuno")
        print("              Lo scanning di rete aiuta a rilevare tutti gli host attivi su una rete e li associa ai loro indirizzi IP")
        print("                        Es: IP                   MAC")
        print("                            --------------------------------------")
        print("                            10.5.5.**            52:54:00:12:**:**")

    elif comando == "quit":
        break

    else:
        print("\033[31;40mWarning! Il comando che hai scritto non è stato riconosciuto dalla macchina o risulta inesistente, riprova.\033[0;37;40m")