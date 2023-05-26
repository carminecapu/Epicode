import urllib.parse
import http.client
import requests
import socket
import os
import sys
import urllib.request
import time

from funzioni import *

print("_______________________________________")
print("_______________________________________\n")

text="Benvenuto nel programma di EXPLOIT\n"

for char in text:
	print(char, end='', flush=True)
	time.sleep(0.10)	
	
print("_______________________________________")
print("_______________________________________\n")


print("Operazioni possibili:")
print(" A-Scansione Porte\n","B-Scansione Metodi disponibili\n","C-Brute force PhpMyadmin\n","D-Brute force Dvwa\n","E-Brute force Dvwa esterno\n")
r=input("Cosa vuoi fare ?")
r=r.upper()

match r:
	case "A":
		print ("Facciamo la scansione delle porte \n ")
		portscanner()

	case "B":
		print ("Scansione Metodi disponibili \n ")
		enumerazionehttp()

	case "C":
		print ("Brute force PhpMyadmin \n")
		bruteforcephp()
	
	case "D":
		print ("Brute force Dvwa interno\n")
		bruteforcedvwa()

	case "E":
		print ("Brute force Dvwa esterno\n")
		bruteext()
	case _:
		print ("Nessuna operazione rilevata!")
