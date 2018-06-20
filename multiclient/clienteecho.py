from socket import*

serverName = 'localhost'
serverPort = int(raw_input("ingrese el puerto:  "))
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

exit=0
while exit==0:
	mensaje = raw_input("ingrese un texto: ")
	if mensaje=="exit":
		exit=1
	clientSocket.send(mensaje)
	
	modifiedMensaje = clientSocket.recv(1024)
	print "respuesta del servidor: ", modifiedMensaje

	
	
