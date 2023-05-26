import http.client
# Dichiarazione delle varibili target, porta e metodi che rappresentano
# la coppia IPiporta e il relativo metodo da scansionare
target= "192.168.50.101"
porta= 80
metodi= ["GET","OPTIONS", "POST", "HEAD", "TRACE", "DELETE", "PUT"]
# Ciclio for per scansionare ogni metodo della lista sopra
for metodo in metodi:
	try:
		conn=http.client.HTTPConnection (target, porta)
		conn.request (metodo, "/phpMyAdmin")
		response= conn.getresponse()
# Controllo sullo stato della risposta:
# se è ‹ di 400 allora il metodo è attivo altrimenti non è attivo
		if response.status < 400:
			print ("il metodo ",metodo," e' attivo")
		else:
			print ("il metodo ",metodo, " non e' attivo")

# Eccezione nel caso in cui la connessione venisse rifiutata
	except ConnectionRefusedError:
		print( "Connessione rifiutata")
# Eccezione nel caso in cui ci fosse un errore nella richiesta al server
	except http.client.HTTPException:
		print( "Errore durante la richiesta al server")
# Chiusura della connessione
conn.close()
