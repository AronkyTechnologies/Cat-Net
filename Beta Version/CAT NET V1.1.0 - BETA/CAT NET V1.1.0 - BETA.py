#Created by IsTk0 ;)

import paramiko, time, os
from ping3 import ping, verbose_ping

print("   ____    _  _____     _   _ _____ _____ ")
time.sleep(0.5)
print("  / ___|  / \|_   _|   | \ | | ____|_   _|")
time.sleep(0.5)
print(" | |     / _ \ | |_____|  \| |  _|   | |  ")
time.sleep(0.5)
print(" | |___ / ___ \| |_____| |\  | |___  | |  ")
time.sleep(0.5)
print("  \____/_/   \_\_|     |_| \_|_____| |_|  ")
time.sleep(0.5)
print("Benvenuto in CAT-NET V1.1 BETA \nDigita 'help' se hai bisogno di aiuto oppure guarda la mia repository ;)")                       

def ssh_code():
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
    hostname = input("Hostname macchina: --> ")
    risposta = os.system("ping -c 1 " + hostname)
    delay = ping(hostname)
    if risposta == 0:
        print(hostname, " ha risposto in: ", delay, "ms")
    else:
        print(hostname, " non ha risposto")

while True:
    comando = input("CAT-NET-> ")

    if comando == "ssh":
        ssh_code()

    elif comando == "ping":
        ping_code()
