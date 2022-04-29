#Created by IsTk0 ;)

import paramiko, time, os
from ping3 import ping, verbose_ping

print("   ____    _  _____     _   _ _____ _____ ")
time.sleep(0.5)
print(" /  ___|  / \|_   _|   | \ | | ____|_   _|")
time.sleep(0.5)
print(" | |     / _ \ | |_____|  \| |  _|   | |  ")
time.sleep(0.5)
print(" | |___ / ___ \| |_____| |\  | |___  | |  ")
time.sleep(0.5)
print(" \_____/_/   \_\_|     |_| \_|_____| |_|  ")
time.sleep(0.5)
print("Benvenuto in CAT-NET V1.1 \nDigita 'help' se hai bisogno di aiuto oppure guarda la mia repository ;)") 
print("Cat Net Source code: https://github.com/IsTk0/Python-project/tree/main/Cat-Net%20project")                      

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
    if comando_ping == "-P":
        risposta = os.system("ping -c 1 " + hostname)
        delay = ping(hostname)
        if risposta == 0:
            print(hostname, " ha risposto in: ", "%.2g" % delay, " S" )
        else:
            print(hostname, " non ha risposto")
    elif comando_ping == "-Ver":
        verbose_ping(hostname)


while True:
    comando = input("CAT-NET-> ")

    if comando == "ssh":
        ssh_code()

    elif comando == "ping":
        ping_code()
    
    elif comando == "help":
        print("---------- TUTTI I COMANDI ----------")
        print("     1) ssh: ")
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

    elif comando == "quit":
        break
