import socket

# Richiesta in input dell'IP target e del range di porte da valutare
# facendo già inserire il valore minimo e massimo delle porte
target= input("Inserire IP target: ")
inizio= int(input("Inserisci valore minimo porta: "))
fine= int(input("Inserisci valore massimo porta: "))

# Controllo se i valori delle porte sono in ordine crescente,
# in caso contrario scambio le variabili senza richiedere un nuovo inserimento
if(fine<inizio):
	temp=inizio
	inizio=fine
	fine=temp

# Ciclo for per scorrere tutte le porte richieste dall'utente e verificarne lo stato
for porta in range(inizio, fine+1):
	s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	stato= s.connect_ex( (target, porta))
# Se lo stato è = a 0 allora la porta è aperta e stampa che quella porta è aperta
	if(stato == 0):
		print("La porta ",porta," e' aperta")
	s.close()
print("\nLe altre porte sono chiuse")
