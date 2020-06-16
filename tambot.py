#!/usr/bin/env python3.6

# Variáveis e listas:
info = "uashdua"

# Script

print ("\033[1;34m--------------------------------------------------------------\033[1;34m")
print ("|                                                            |")
print ("|                   Bem vindo ao chatbot                     |")
print ("|                                                            |")
print ("--------------------------------------------------------------")
print ()

print ("\033[1;35mBot" "\033[0m: Olá! Qual é seu nome?")
nome = input("\033[1;32mVocê" "\033[0m: ")
print ("\033[1;35mBot" "\033[0m: Olá", nome+"," " como vai você?")

while(info != "tchau"):

	info = input("\033[1;32mVocê" "\033[0m: ")
	info = info.lower()
	if info == ("tchau"):
		
		print ("\033[1;35mBot" "\033[0m: Ok, até a próxima!")
		exit()
		
	else:

		try:
			responder = open(".cerebro/" + info, "r")
	
		except IOError:
			print ("\033[1;35mBot" "\033[0m: Ainda não sei o que você quis dizer, o que eu deveria responder?")
			resposta = input ("\033[1;32mVocê" "\033[0m: ")
			novo_arquivo = open(".cerebro/" + info, "a") 
			novo_arquivo.write(resposta)
			print ("\033[1;35mBot" "\033[0m: Certo, devo falar " "\033[0;34m[", resposta, "]")
			
		else:
			responder = open(".cerebro/" + info, "r")
			falar = responder.read()
			print ("\033[1;35mBot" "\033[0m: " + falar)
