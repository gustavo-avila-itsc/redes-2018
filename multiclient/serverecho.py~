import select
from socket import *

serverPort=int(raw_input("ingrese el puerto:  "))
serverSocket=socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('localhost',serverPort))
serverSocket.listen(3)
inputs= [serverSocket]
outputs= []
errors=[]

conecccioniniciada = "conectado con el cliente"
coneccionfinalizada = "desconectado con el cliente"
while inputs:
	readable,writable,exceptional= select.select(inputs,outputs,errors)
	for s in readable:
		if s is serverSocket:
			connectionSocket,addr=serverSocket.accept()
			print conecccioniniciada, addr

		else:

			
			msg=connectionSocket.recv(1024)
			if msg != "exit":
				modifiedMsg=msg.upper()
				connectionSocket.sendall(modifiedMsg)
			else:
				
				print coneccionfinalizada,addr
				connectionSocket.close()
				break
			arch= open("texto.txt", "a+")
			arch.write("\n")	
			arch.write(modifiedMsg)
			arch.close()

			
				


