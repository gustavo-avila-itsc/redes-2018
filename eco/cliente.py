from socket import*

serverName = 'localhost'
serverPort = 12001
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

	
	
