from socket import *
serverPort=12001
serverSocket=socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)

conecccioniniciada = "conectado con el cliente"
coneccionfinalizada = "desconectado con el cliente"
while 1:
	connectionSocket,addr=serverSocket.accept()
	print conecccioniniciada, addr
	try:
		while True:
			msg=connectionSocket.recv(1024)
			if msg != "exit":
				modifiedMsg=msg.upper()
				connectionSocket.sendall(modifiedMsg)
			else:
				
				print coneccionfinalizada,addr
				break
			arch= open("texto.txt", "a+")
			arch.write("\n")	
			arch.write(modifiedMsg)
			arch.close()

	finally:
		connectionSocket.close()

